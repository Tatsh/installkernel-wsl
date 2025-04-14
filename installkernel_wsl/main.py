"""Main script."""
from __future__ import annotations

import logging

import click

from .utils import copy_kernel_to_win, is_wsl, update_wslconfig

__all__ = ('main',)


@click.command(context_settings={
    'help_option_names': ('-h', '--help'),
    'ignore_unknown_options': True
})
@click.option('-d', '--debug', help='Enable debug level logging.', is_flag=True)
@click.argument('command', nargs=1)
@click.argument('command_args', nargs=-1, type=click.UNPROCESSED)
def main(command: str, command_args: tuple[str, ...], *, debug: bool = False) -> None:
    logging.basicConfig(format='%(levelname)s:%(module)s:%(lineno)d:%(funcName)s: %(message)s',
                        level=logging.DEBUG if debug else logging.WARNING)
    if command != 'add':
        click.echo(f'Ignoring unsupported command `{command}`.')
        return
    if not is_wsl():
        click.echo('Not running under WSL or interop is disabled.', err=True)
        raise click.Abort
    kernel_name, _, kernel_path = command_args
    update_wslconfig(copy_kernel_to_win(f'kernel-{kernel_name}', kernel_path))
