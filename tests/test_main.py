from __future__ import annotations

from typing import TYPE_CHECKING

from installkernel_wsl.main import main

if TYPE_CHECKING:
    from click.testing import CliRunner
    from pytest_mock import MockerFixture


def test_main_not_wsl(runner: CliRunner, mocker: MockerFixture) -> None:
    """Test main function when not running under WSL."""
    mocker.patch('installkernel_wsl.main.is_wsl', return_value=False)
    result = runner.invoke(main, ('add', 'kernel-name', '', '/path/to-kernel'))
    assert result.exit_code == 1
    assert 'Not running under WSL or interop is disabled.' in result.output


def test_main(runner: CliRunner, mocker: MockerFixture) -> None:
    """Test main function."""
    mocker.patch('installkernel_wsl.main.is_wsl', return_value=True)
    update = mocker.patch('installkernel_wsl.main.update_wslconfig')
    copy = mocker.patch('installkernel_wsl.main.copy_kernel_to_win')
    result = runner.invoke(main, ('add', 'kernel-name', '', '/path/to-kernel'))
    assert result.exit_code == 0
    assert update.called
    assert copy.called


def test_main_not_add(runner: CliRunner, mocker: MockerFixture) -> None:
    result = runner.invoke(main, 'add2')
    assert result.exit_code == 0
    assert 'unsupported command' in result.output
