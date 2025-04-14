from __future__ import annotations

from pathlib import Path, PureWindowsPath
from typing import TYPE_CHECKING
from unittest.mock import MagicMock

from installkernel_wsl.utils import (
    copy_kernel_to_win,
    get_automount_root,
    get_cmd_path,
    get_win_var,
    get_windows_home_path,
    get_windows_home_purewindowspath,
    get_wslconfig_path,
    is_wsl,
    update_wslconfig,
    wslpath,
)
import pytest

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def test_is_wsl(mocker: MockerFixture) -> None:
    mock_exists = mocker.patch('installkernel_wsl.utils.Path.exists')
    mock_exists.return_value = True
    assert is_wsl() is True


def test_is_wsl_not_wsl(mocker: MockerFixture) -> None:
    mock_exists = mocker.patch('installkernel_wsl.utils.Path.exists')
    mock_exists.return_value = False
    assert is_wsl() is False


def test_copy_kernel_to_win_success(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.Path.glob',
                 return_value=[Path('/boot/kernel-5.15.0-WSL2')])
    mocker.patch('installkernel_wsl.utils.get_windows_home_path',
                 return_value=Path('/mnt/c/Users/test'))
    mock_copyfile = mocker.patch('installkernel_wsl.utils.copyfile')

    result = copy_kernel_to_win('kernel-5.15.0-WSL2', '/usr/src/linux/arch/x86/boot/bzImage')
    mock_copyfile.assert_called_once_with('/usr/src/linux/arch/x86/boot/bzImage',
                                          Path('/mnt/c/Users/test/kernel-5.15.0-WSL2'))
    assert result == Path('/mnt/c/Users/test/kernel-5.15.0-WSL2')


def test_copy_kernel_to_win_permission_error(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.Path.glob',
                 return_value=[Path('/boot/kernel-5.15.0-WSL2')])
    mocker.patch('installkernel_wsl.utils.get_windows_home_path',
                 return_value=Path('/mnt/c/Users/test'))
    mocker.patch('installkernel_wsl.utils.copyfile', side_effect=[PermissionError, None])
    mocker.patch('installkernel_wsl.utils.Path.exists', side_effect=[True, False])
    result = copy_kernel_to_win('kernel-5.15.0-WSL2', '/usr/src/linux/arch/x86/boot/bzImage')
    assert result == Path('/mnt/c/Users/test/kernel-5.15.0-WSL2-01')


def test_copy_kernel_to_win_permission_error_fail(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.Path.glob',
                 return_value=[Path('/boot/kernel-5.15.0-WSL2')])
    mocker.patch('installkernel_wsl.utils.get_windows_home_path',
                 return_value=Path('/mnt/c/Users/test'))
    mocker.patch('installkernel_wsl.utils.copyfile', side_effect=[PermissionError, None])
    mocker.patch('installkernel_wsl.utils.Path.exists', side_effect=[True, False])
    with pytest.raises(PermissionError):
        copy_kernel_to_win('kernel-5.15.0-WSL2',
                           '/usr/src/linux/arch/x86/boot/bzImage',
                           fail_immediately=True)


def test_update_wslconfig(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.get_wslconfig_path',
                 return_value=Path('/mnt/c/Users/test/.wslconfig'))
    mocker.patch('installkernel_wsl.utils.wslpath',
                 return_value='C:\\Users\\test\\kernel-5.15.0-WSL2')
    mocker.patch('installkernel_wsl.utils.Path.open', mocker.mock_open())
    mocker.patch('installkernel_wsl.utils.Path.write_text')
    mock_config = mocker.patch('installkernel_wsl.utils.ConfigParser')
    mock_config_instance = mock_config.return_value

    update_wslconfig(Path('/mnt/c/Users/test/kernel-5.15.0-WSL2'))
    mock_config_instance.read.assert_called_once_with(Path('/mnt/c/Users/test/.wslconfig'))
    mock_config_instance['wsl2']['kernel'] = 'C:\\Users\\test\\kernel-5.15.0-WSL2'


def test_get_wslconfig_path(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.get_windows_home_path',
                 return_value=Path('/mnt/c/Users/test'))
    assert get_wslconfig_path() == Path('/mnt/c/Users/test/.wslconfig')


def test_get_automount_root_default(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.Path.exists', return_value=False)
    assert get_automount_root() == Path('/mnt')


def test_get_automount_root_custom(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.Path.exists', return_value=True)
    mock_config = mocker.patch('installkernel_wsl.utils.ConfigParser')
    mock_config_instance = mock_config.return_value
    mock_config_instance.get.return_value = '/custom_mnt'
    assert get_automount_root() == Path('/custom_mnt')


def test_get_cmd_path(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.get_automount_root', return_value=Path('/mnt'))
    cmd_path = mocker.MagicMock(spec=Path)
    resolve_ret = cmd_path.resolve.return_value
    mocker.patch('installkernel_wsl.utils.Path.glob', return_value=[cmd_path])
    assert get_cmd_path() == resolve_ret


def test_get_win_var(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.get_cmd_path',
                 return_value=Path('/mnt/c/windows/system32/cmd.exe'))
    run = mocker.patch('installkernel_wsl.utils.sp.run')
    run.return_value.stdout = 'test_value'
    assert get_win_var('TEST_VAR') == 'test_value'


def test_get_win_var_empty(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.get_cmd_path',
                 return_value=Path('/mnt/c/windows/system32/cmd.exe'))
    run = mocker.patch('installkernel_wsl.utils.sp.run')
    run.return_value.stdout = ''
    with pytest.raises(ValueError, match=r'cmd.exe did not print a value for %TEST_VAR%.'):
        get_win_var('TEST_VAR')


def test_wslpath(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.sp.run',
                 return_value=MagicMock(stdout='/mnt/c/Users/test'))
    assert wslpath('C:\\Users\\test') == '/mnt/c/Users/test'


def test_wslpath_empty(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.sp.run', return_value=MagicMock(stdout=''))
    with pytest.raises(ValueError,
                       match=r'wslpath returned an empty string for path `C:\\Users\\test`.'):
        wslpath('C:\\Users\\test')


def test_get_windows_home_path(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.get_win_var', return_value='C:\\Users\\test')
    mocker.patch('installkernel_wsl.utils.wslpath', return_value='/mnt/c/Users/test')
    assert get_windows_home_path() == Path('/mnt/c/Users/test')


def test_get_windows_home_purewindowspath(mocker: MockerFixture) -> None:
    mocker.patch('installkernel_wsl.utils.get_win_var', return_value='C:\\Users\\test')
    assert get_windows_home_purewindowspath() == PureWindowsPath('C:\\Users\\test')
