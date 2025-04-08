"""Main script."""
from __future__ import annotations

import logging

import click

from .utils import copy_kernel_to_win, is_wsl, update_wslconfig

__all__ = ('main',)

log = logging.getLogger(__name__)


@click.command(context_settings={'help_option_names': ('-h', '--help')})
@click.option('-d', '--debug', help='Enable debug level logging.', is_flag=True)
def main(*, debug: bool = False) -> None:
    logging.basicConfig(format='%(levelname)s:%(module)s:%(lineno)d:%(funcName)s: %(message)s',
                        level=logging.DEBUG if debug else logging.WARNING)
    if not is_wsl():
        click.echo('Not running under WSL or interop is disabled.', err=True)
        raise click.Abort
    update_wslconfig(copy_kernel_to_win())
