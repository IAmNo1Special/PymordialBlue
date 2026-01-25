"""Tests for PymordialBluestacksController."""

from unittest.mock import MagicMock, patch

from pymordial.core.blueprints.emulator_device import EmulatorState

from pymordialblue.android_app import PymordialAndroidApp
from pymordialblue.bluestacks_controller import PymordialBluestacksController


def test_controller_init(mock_config):
    """Test controller initialization and plugin resolution."""
    with patch("pymordialblue.utils.configs.get_config", return_value=mock_config):
        controller = PymordialBluestacksController()
        assert controller.adb is not None
        assert controller.ui is not None
        assert controller.bluestacks is not None


def test_controller_open_app(mock_controller, mock_config):
    """Test open_app delegation."""
    app = PymordialAndroidApp(app_name="TestApp", package_name="com.test.app")
    mock_controller.adb.open_app = MagicMock(return_value=True)

    assert mock_controller.open_app(app) is True

    call_args = mock_controller.adb.open_app.call_args[1]
    assert call_args["app_name"] == "TestApp"
    assert call_args["package_name"] == "com.test.app"


def test_controller_click_element(mock_controller):
    """Test click_element delegation."""
    from pymordial.ui.image import PymordialImage

    with patch("pathlib.Path.exists", return_value=True):
        element = PymordialImage(label="test_el", filepath="fake.png", confidence=0.9)

    mock_controller.bluestacks.state.current_state = EmulatorState.READY
    mock_controller.adb.is_connected = MagicMock(return_value=True)
    mock_controller.adb.run_command = MagicMock()

    # Mock find_element behavior
    with patch.object(mock_controller, "find_element", return_value=(100, 200)):
        assert mock_controller.click_element(element) is True
        # click_element calls click_coord which calls adb.run_command(tap_command)
        assert mock_controller.adb.run_command.called


def test_controller_capture_screen(mock_controller):
    """Test capture_screen delegation."""
    mock_controller.adb.capture_screen = MagicMock(return_value=b"fake_bytes")
    assert mock_controller.capture_screen() == b"fake_bytes"


def test_controller_disconnect(mock_controller):
    """Test disconnect delegation."""
    mock_controller.adb.is_connected = MagicMock(return_value=True)
    mock_controller.adb.disconnect = MagicMock()
    mock_controller.disconnect()
    assert mock_controller.adb.disconnect.called
