"""Main script."""
from __future__ import annotations

from configparser import ConfigParser
from functools import cache
from pathlib import Path, PureWindowsPath
from shlex import quote
from shutil import copyfile
from typing import TYPE_CHECKING
import logging
import re
import subprocess as sp

if TYPE_CHECKING:  # pragma no cover
    from os import PathLike

__all__ = ('copy_kernel_to_win', 'get_automount_root', 'get_cmd_path', 'get_win_var',
           'get_windows_home_path', 'get_windows_home_purewindowspath', 'get_wslconfig_path',
           'is_wsl', 'update_wslconfig', 'wslpath')

BOOT_PATH = Path('/boot')
log = logging.getLogger(__name__)


def is_wsl() -> bool:
    """Check if running under WSL."""
    return Path('/proc/sys/fs/binfmt_misc/WSLInterop').exists()


@cache
def get_kernel_prefix() -> str:
    """Get the kernel prefix for the current WSL distribution."""
    kernel_prefix = re.sub(r'^linux-', 'kernel-', Path('/usr/src/linux').resolve(strict=True).name)
    log.debug('Kernel prefix: %s', kernel_prefix)
    return kernel_prefix


def copy_kernel_to_win(*, fail_immediately: bool = False) -> Path:
    """Copy the kernel update config file to the WSL config directory."""
    kernel_prefix = get_kernel_prefix()
    kernel = min(Path('/boot').glob(f'{kernel_prefix}*-WSL2')).name
    log.debug('Kernel name: %s', kernel)
    win_home_lin = get_windows_home_path()
    target = win_home_lin / kernel
    try:
        copyfile(BOOT_PATH / kernel, target)
    except PermissionError:
        if fail_immediately:
            raise
        log.info('Caught permission error. Usually this means the kernel in use (by Windows) is the'
                 ' same one that is trying to be written to. Using sequential suffix for kernel '
                 'filename.')
        index = 0
        target = win_home_lin / f'{kernel}-00'
        while target.exists():
            index += 1
            target = win_home_lin / f'{kernel}-{index:02d}'
        copyfile(BOOT_PATH / kernel, target)
        kernel = target.name
        log.debug('Adjusted kernel name: %s', kernel)
    return target


def update_wslconfig(kernel_path_lin: PathLike[str] | str) -> None:
    """Update the .wslconfig file with the new kernel path."""
    wslconfig = get_wslconfig_path()
    log.debug('Reading .wslconfig.')
    config = ConfigParser(delimiters=('=',), interpolation=None)
    config.read(wslconfig)
    config.optionxform = str  # type: ignore[assignment,method-assign]
    kernel_path_win = wslpath(kernel_path_lin, windows=True, absolute=True)
    log.debug('Kernel path on Windows: %s', kernel_path_win)
    config['wsl2']['kernel'] = str(kernel_path_win).replace('\\', '\\\\')
    log.debug('Writing .wslconfig.')
    with wslconfig.open('w+', encoding='utf-8') as f:
        config.write(f)
    log.debug('Stripping excess new lines.')
    wslconfig.write_text(wslconfig.read_text(encoding='utf-8').strip() + '\n')


@cache
def get_wslconfig_path() -> Path:
    """Get the path to the .wslconfig file."""
    win_home_lin = get_windows_home_path()
    return win_home_lin / '.wslconfig'


def get_automount_root() -> Path:
    """Get the automount root path."""
    mount_prefix = Path('/mnt')
    if (wsl_conf := Path('/etc/wsl.conf')).exists():
        config = ConfigParser(delimiters=('=',), interpolation=None)
        config.read(wsl_conf)
        mount_prefix = Path(config.get('automount', 'root', fallback='/mnt'))
    log.debug('automount root: %s', mount_prefix)
    return mount_prefix


@cache
def get_cmd_path() -> Path:
    """Get the path to cmd.exe."""
    mount_prefix = get_automount_root()
    # Case-insensitive search for first cmd.exe.
    cmd = min(
        mount_prefix.glob(''.join((f'[{x}{x.upper()}]' if x.isalpha() else x)
                                  for x in '*/windows/system32/cmd.exe'))).resolve(strict=True)
    log.debug('cmd.exe path: %s', cmd)
    return cmd


def get_win_var(var_name: str) -> str:
    """Get a Windows environment variable."""
    cmd = get_cmd_path()
    win_var = sp.run((cmd, '/c', f'<nul set /p=%{var_name}%'),
                     capture_output=True,
                     check=False,
                     text=True).stdout.strip()
    if not win_var:
        msg = f'cmd.exe did not print a value for %{var_name}%.'
        raise ValueError(msg)
    log.debug('%%%s%%=%s', var_name, quote(win_var))
    return win_var


def wslpath(path: str | PathLike[str], *, absolute: bool = False, windows: bool = False) -> str:
    """Convert a Windows path to a WSL path."""
    wsl_path = sp.run(
        (
            'wslpath',
            *(('-a',) if absolute else ()),
            *(('-w',) if windows else ()),
            path,
        ),
        capture_output=True,
        check=True,
        text=True,
    ).stdout.strip()
    if not wsl_path:
        msg = f'wslpath returned an empty string for path `{path}`.'
        raise ValueError(msg)
    log.debug('wslpath result: %s', quote(wsl_path))
    return wsl_path


@cache
def get_windows_home_path() -> Path:
    """Get the Windows home path."""
    win_home_win = get_win_var('USERPROFILE')
    win_home_lin = wslpath(win_home_win, absolute=True)
    log.debug('Linux %%USERPROFILE%% path: %s', win_home_lin)
    return Path(win_home_lin)


@cache
def get_windows_home_purewindowspath() -> PureWindowsPath:
    """Get the Windows home path as a PureWindowsPath."""
    win_home_win = get_win_var('USERPROFILE')
    log.debug('Windows %%USERPROFILE%% path: %s', win_home_win)
    return PureWindowsPath(win_home_win)
