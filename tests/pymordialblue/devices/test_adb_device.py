"""Tests for PymordialAdbDevice."""

from pymordialblue.devices.adb_device import PymordialAdbDevice


def test_adb_device_init(mock_config):
    """Test initialization of PymordialAdbDevice."""
    device = PymordialAdbDevice(host="127.0.0.1", port=5555)
    assert device.host == "127.0.0.1"
    assert device.port == 5555


def test_adb_device_connect(mock_adb_device):
    """Test connection logic."""
    device = PymordialAdbDevice(host="127.0.0.1", port=5555)
    # Inject the mock directly to avoid redundant patching issues
    device._device = mock_adb_device
    assert device.connect() is True
    assert device.is_connected() is True


def test_adb_device_run_command(mock_adb_device):
    """Test command execution."""
    device = PymordialAdbDevice(host="127.0.0.1", port=5555)
    device._device = mock_adb_device
    mock_adb_device.shell.return_value = "output\n"

    result = device.run_command("echo hello", decode=True)
    assert result == "output"
    mock_adb_device.shell.assert_called_with(
        "echo hello",
        timeout_s=30,
        read_timeout_s=30,
        transport_timeout_s=30,
        decode=True,
    )


def test_adb_device_get_focused_app(mock_adb_device):
    """Test extracting focused app info."""
    device = PymordialAdbDevice(host="127.0.0.1", port=5555)
    device._device = mock_adb_device
    mock_adb_device.shell.return_value = "mCurrentFocus=Window{... u0 com.android.settings/com.android.settings.Settings}\n"

    app_info = device.get_focused_app()
    assert app_info["package"] == "com.android.settings"
    assert app_info["activity"] == "com.android.settings.Settings"


def test_adb_device_is_app_running(mock_adb_device):
    """Test app running check."""
    device = PymordialAdbDevice(host="127.0.0.0", port=5555)
    device._device = mock_adb_device

    # pidof returns a PID if running
    mock_adb_device.shell.return_value = "1234\n"
    assert device.is_app_running(package_name="com.test.app") is True

    # empty output if not running
    mock_adb_device.shell.return_value = ""
    assert device.is_app_running(package_name="com.test.app") is False


def test_adb_device_tap(mock_adb_device):
    """Test tap command."""
    device = PymordialAdbDevice(host="127.0.0.1", port=5555)
    device._device = mock_adb_device
    device.tap(100, 200)
    mock_adb_device.shell.assert_called_with(
        "input tap 100 200",
        timeout_s=30,
        read_timeout_s=30,
        transport_timeout_s=30,
        decode=False,
    )
