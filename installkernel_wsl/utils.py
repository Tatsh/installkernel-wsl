"""Main script."""
from __future__ import annotations

from configparser import ConfigParser
from pathlib import Path, PureWindowsPath
import logging
import subprocess as sp

__all__ = ('get_home_paths',)

log = logging.getLogger(__name__)


def get_home_paths() -> tuple[Path, PureWindowsPath]:
    mount_prefix = Path('/mnt')
    if (wsl_conf := Path('/etc/wsl.conf')).exists():
        config = ConfigParser(delimiters=('=',), interpolation=None)
        config.read(wsl_conf)
        mount_prefix = Path(config.get('automount', 'root', fallback='/mnt')).resolve(strict=True)
    # Case-insensitive search for first cmd.exe.
    cmd = min(mount_prefix.glob('*/windows/system32/cmd.exe',
                                case_sensitive=False)).resolve(strict=True)
    log.debug('cmd.exe path: %s', cmd)
    if not (win_home_win := sp.run(
        (cmd, '/c', '<nul set /p=%USERPROFILE%'), capture_output=True, check=False,
            text=True).stdout.strip()):
        msg = 'cmd.exe did not print a value for %USERPROFILE%.'
        raise ValueError(msg)
    if not (win_home_lin := sp.run(
        ('wslpath', '-a', win_home_win), capture_output=True, check=True,
            text=True).stdout.strip()):
        msg = f'wslpath returned an empty string for path `{win_home_win}`.'
        raise ValueError(msg)
    log.debug('Linux %%USERPROFILE%% path: %s', win_home_lin)
    log.debug('Windows %%USERPROFILE%% path: %s', win_home_win)
    return Path(win_home_lin), PureWindowsPath(win_home_win)
