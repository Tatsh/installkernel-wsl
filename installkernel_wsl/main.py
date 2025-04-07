"""Main script."""
from __future__ import annotations

from pathlib import Path
from shutil import copyfile
import configparser
import logging
import re

import click

from .utils import get_home_paths

__all__ = ('main',)

BOOT_PATH = Path('/boot')
log = logging.getLogger(__name__)


@click.command(context_settings={'help_option_names': ('-h', '--help')})
@click.option('-d', '--debug', help='Enable debug level logging.', is_flag=True)
def main(*, debug: bool = False) -> None:
    logging.basicConfig(format='%(levelname)s:%(module)s:%(lineno)d:%(funcName)s: %(message)s',
                        level=logging.DEBUG if debug else logging.WARNING)
    if not Path('/proc/sys/fs/binfmt_misc/WSLInterop').exists():
        click.echo('Not running under WSL or interop is disabled.', err=True)
        raise click.Abort
    win_home_lin, win_home_win = get_home_paths()
    if not (wslconfig := win_home_lin / '.wslconfig').exists():
        wslconfig.write_text('[wsl2]\nkernel=')
    prefix = re.sub(r'^linux-', 'kernel-', Path('/usr/src/linux').resolve(strict=True).name)
    log.debug('Kernel prefix: %s', prefix)
    kernel = min(BOOT_PATH.glob(f'{prefix}*-WSL2')).name
    log.debug('Kernel name: %s', kernel)
    try:
        copyfile(BOOT_PATH / kernel, win_home_lin / kernel)
    except PermissionError:
        log.info('Caught permission error. Usually this means the kernel in use (by Windows) is the'
                 ' same one that is trying to be written to. Using sequential suffix for kernel '
                 'filename.')
        index = 0
        new_path = win_home_lin / f'{kernel}-00'
        while new_path.exists():
            index += 1
            new_path = win_home_lin / f'{kernel}-{index:02d}'
        copyfile(BOOT_PATH / kernel, new_path)
        kernel = new_path.name
        log.debug('Adjusted kernel name: %s', kernel)
    win_kernel_path = win_home_win / kernel
    log.debug('Kernel path on Windows: %s', win_kernel_path)
    log.debug('Reading .wslconfig.')
    config = configparser.ConfigParser(delimiters=('=',), interpolation=None)
    config.read(wslconfig)
    config.optionxform = str  # type: ignore[assignment,method-assign]
    config['wsl2']['kernel'] = str(win_kernel_path).replace('\\', '\\\\')
    log.debug('Writing .wslconfig.')
    with wslconfig.open('w+', encoding='utf-8') as f:
        config.write(f)
    log.debug('Stripping excess new lines.')
    wslconfig.write_text(wslconfig.read_text(encoding='utf-8').strip() + '\n')
