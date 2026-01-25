"""Tests for pymordialblue.utils.configs."""

from unittest.mock import mock_open, patch

import pytest

from pymordialblue.utils.configs import _deep_merge, get_config


def test_deep_merge():
    """Test recursive dictionary merging."""
    base = {"a": 1, "b": {"c": 2}}
    override = {"b": {"d": 3}, "e": 4}
    _deep_merge(base, override)
    assert base == {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}


@patch("pymordialblue.utils.configs._DEFAULT_CONFIG_PATH")
@patch("pymordialblue.utils.configs._USER_CONFIG_PATH")
@patch("yaml.safe_load")
@patch("builtins.open", new_callable=mock_open, read_data="key: value")
def test_load_config(mock_file, mock_yaml, mock_user_path, mock_default_path):
    """Test configuration loading and merging logic."""
    from pymordialblue.utils import configs

    # Reset cached config
    configs._CONFIG = None

    mock_default_path.exists.return_value = True
    mock_user_path.exists.return_value = False
    mock_yaml.side_effect = [
        {
            "adb": {"commands": {}},
            "bluestacks": {"ui": {"assets": {}}},
            "ui": {},
            "extract_strategy": {},
            "setup": {},
            "key": "default",
        },
    ]

    config = get_config()
    assert config["key"] == "default"
    assert mock_default_path.exists.called
    assert mock_user_path.exists.called  # It is called to check existence


@patch("pymordialblue.utils.configs._DEFAULT_CONFIG_PATH")
@patch("pymordialblue.utils.configs._USER_CONFIG_PATH")
@patch("yaml.safe_load")
@patch("builtins.open", new_callable=mock_open)
def test_load_config_with_override(
    mock_file, mock_yaml, mock_user_path, mock_default_path
):
    """Test configuration loading with user overrides."""
    from pymordialblue.utils import configs

    configs._CONFIG = None

    mock_default_path.exists.return_value = True
    mock_user_path.exists.return_value = True

    # First call for default, second for user
    mock_yaml.side_effect = [
        {
            "adb": {"commands": {}},
            "bluestacks": {"ui": {"assets": {}}},
            "ui": {},
            "extract_strategy": {},
            "setup": {},
            "key": "default",
        },
        {"key": "user"},
    ]

    config = get_config()
    assert config["key"] == "user"


def test_validate_config_error():
    """Test validation errors for missing sections."""
    from pymordialblue.utils.configs import _validate_config

    with pytest.raises(ValueError, match="Missing required config section: adb"):
        _validate_config({})

    with pytest.raises(
        ValueError, match="Missing required config section: bluestacks.ui"
    ):
        _validate_config(
            {"adb": {}, "bluestacks": {}, "ui": {}, "extract_strategy": {}, "setup": {}}
        )
