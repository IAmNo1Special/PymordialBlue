from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from pymordial.core.blueprints.emulator_device import EmulatorState


@pytest.fixture
def mock_config():
    """Provides a basic mock configuration."""
    return {
        "adb": {
            "default_host": "127.0.0.1",
            "default_port": 5555,
            "default_max_retries": 1,
            "default_wait_time": 1,
            "default_timeout": 10,
            "process_wait_timeout": 5,
            "app_start_timeout": 10,
            "stream": {
                "resolution": 720,
                "bitrate": "2M",
                "time_limit": 180,
                "queue_size": 2,
                "read_timeout": 0.1,
                "start_timeout_iterations": 50,
                "start_wait": 0.1,
                "stop_timeout": 2,
            },
            "monkey_verbosity": 1,
            "app_check_retries": 1,
            "keyevents": {
                "home": 3,
                "enter": 66,
                "esc": 111,
                "app_switch": "APP_SWITCH",
            },
            "commands": {
                "screenrecord": "screenrecord",
                "dumpsys_focus": "dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'",
                "force_stop": "am force-stop",
                "screencap": "screencap -p",
                "tap": "input tap",
                "text": "input text",
                "keyevent": "input keyevent",
                "monkey": "monkey",
                "timeout": 30,
                "read_timeout": 30,
                "transport_timeout": 30,
            },
        },
        "bluestacks": {
            "default_resolution": [1600, 900],
            "default_open_app_max_retries": 1,
            "default_open_app_wait_time": 1,
            "default_open_app_timeout": 10,
            "default_transport_timeout_s": 0.5,
            "default_load_timeout": 60,
            "default_load_wait_time": 5,
            "default_ui_load_wait_time": 2,
            "hd_player_exe": "C:\\Program Files\\BlueStacks\\HD-Player.exe",
            "window_title": "BlueStacks",
            "ui": {"assets": "assets"},
        },
        "ui": {"default_wait_time": 1, "default_find_ui_retries": 1},
        "extract_strategy": {
            "default": {
                "upscale_factor": 1,
                "denoise_strength": 0,
                "denoise_template_window": 7,
                "denoise_search_window": 21,
                "threshold_binary_max": 255,
                "inversion_threshold_mean": 127,
                "tesseract_config": "--oem 3 --psm 6",
            },
            "revomon": {
                "move": {
                    "upscale_factor": 1,
                    "crop_left_ratio": 0.4,
                    "crop_bottom_ratio": 0.1,
                    "padding": 10,
                    "whitelist_config": "-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                },
                "level": {
                    "crop_left_ratio": 0.5,
                    "whitelist_config": "-c tessedit_char_whitelist=0123456789",
                },
                "padding_value_white": 255,
                "adaptive_thresh_block_size": 11,
                "adaptive_thresh_c": 2,
            },
            "tesseract": {
                "base_config": "",
                "default_config": "",
                "tesseract_cmd": "tesseract",
                "preprocess": {
                    "upscale_factor": 1,
                    "denoise_strength": 0,
                    "denoise_template_window": 7,
                    "denoise_search_window": 21,
                    "threshold_max": 255,
                    "inversion_threshold": 127,
                },
                "psm": {"single_word": "8", "single_line": "7", "block": "6"},
            },
        },
        "setup": {
            "installer_name": "BlueStacksInstaller.exe",
            "download_url": "https://example.com",
            "reg_key": "SOFTWARE\\BlueStacks",
        },
        "controller": {
            "default_click_times": 1,
            "default_max_tries": 1,
            "click_coord_times": 1,
        },
    }


@pytest.fixture
def mock_adb_device():
    """Mocks the adb-shell AdbDeviceTcp."""
    with patch("adb_shell.adb_device.AdbDeviceTcp") as MockAdb:
        mock_instance = MockAdb.return_value
        mock_instance.available = True
        mock_instance.connect.return_value = True
        mock_instance.shell.return_value = "success\n"
        yield mock_instance


@pytest.fixture
def mock_cv2():
    """Mocks OpenCV functions."""
    with (
        patch("cv2.imread") as mock_imread,
        patch("cv2.cvtColor") as mock_cvt,
        patch("cv2.resize") as mock_resize,
        patch("cv2.threshold") as mock_thresh,
        patch("cv2.fastNlMeansDenoising") as mock_denoise,
        patch("cv2.matchTemplate") as mock_match,
        patch("cv2.imdecode") as mock_imdecode,
    ):

        mock_imread.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_imdecode.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_cvt.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_resize.return_value = np.zeros((200, 200), dtype=np.uint8)
        mock_thresh.return_value = (0, np.zeros((100, 100), dtype=np.uint8))
        mock_denoise.return_value = np.zeros((100, 100), dtype=np.uint8)
        mock_match.return_value = np.array([[0.9]])

        yield {
            "imread": mock_imread,
            "imdecode": mock_imdecode,
            "cvtColor": mock_cvt,
            "resize": mock_resize,
            "threshold": mock_thresh,
            "fastNlMeansDenoising": mock_denoise,
            "matchTemplate": mock_match,
        }


@pytest.fixture
def mock_pytesseract():
    """Mocks pytesseract calls."""
    with (
        patch("pytesseract.image_to_string") as mock_i2s,
        patch("pytesseract.image_to_data") as mock_i2d,
    ):
        mock_i2s.return_value = "Mocked Text"
        mock_i2d.return_value = {
            "text": ["", "Target"],
            "conf": ["-1", "95"],
            "left": [0, 50],
            "top": [0, 60],
            "width": [0, 20],
            "height": [0, 10],
        }
        yield {"image_to_string": mock_i2s, "image_to_data": mock_i2d}


@pytest.fixture
def mock_psutil():
    """Mocks psutil for process management."""
    with patch("psutil.process_iter") as mock_iter:
        mock_proc = MagicMock()
        mock_proc.name.return_value = "HD-Player.exe"
        mock_proc.info = {
            "name": "HD-Player.exe",
            "exe": "C:\\path\\to\\Bluestacks.exe",
        }
        mock_iter.return_value = [mock_proc]
        yield mock_iter


@pytest.fixture(autouse=True)
def patch_bluestacks_filepath():
    """Globally patch PymordialBluestacksDevice._autoset_filepath to prevent drive scans."""
    with patch(
        "pymordialblue.devices.bluestacks_device.PymordialBluestacksDevice._autoset_filepath",
        side_effect=lambda self: setattr(self, "_filepath", "C:\\Mock\\HD-Player.exe"),
        autospec=True,
    ):
        yield


@pytest.fixture
def mock_controller(mock_adb_device, mock_config):
    """Provides a mocked PymordialBluestacksController."""
    with patch("pymordialblue.utils.configs.get_config", return_value=mock_config):
        from pymordialblue.bluestacks_controller import PymordialBluestacksController

        controller = PymordialBluestacksController()
        controller.bluestacks.state.current_state = EmulatorState.READY
        yield controller
