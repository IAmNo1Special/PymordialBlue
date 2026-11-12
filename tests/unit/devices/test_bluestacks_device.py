"""Tests for BluestacksDevice.wait_for_load() timeout behaviour."""

from unittest.mock import MagicMock

import pytest
from pymordial.core.blueprints.emulator_device import EmulatorState

from pymordialblue.devices.bluestacks_device import BluestacksDevice


def _make_device(mock_config, adb):
    """Build a device with fast load timings so timeout tests stay quick."""
    config = dict(mock_config["bluestacks"])
    config["default_load_wait_time"] = 0
    config["default_ui_load_wait_time"] = 0
    return BluestacksDevice(adb_bridge_device=adb, config=config)


def test_wait_for_load_timeout_raises_and_does_not_report_ready(mock_config):
    """A timed-out load must raise, not mark the device READY."""
    adb = MagicMock()
    adb.connect.return_value = False
    device = _make_device(mock_config, adb)
    device.state.current_state = EmulatorState.LOADING

    with pytest.raises(TimeoutError):
        device.wait_for_load(timeout_s=1)

    assert device.state.current_state == EmulatorState.LOADING
    assert device.is_ready() is False


def test_wait_for_load_timeout_via_loading_transition(mock_config):
    """The LOADING handler path must also leave the device unready.

    transition_to() sets LOADING before running wait_for_load(), so a
    raise from the handler leaves the state in LOADING, not READY.
    """
    adb = MagicMock()
    adb.connect.return_value = False
    device = _make_device(mock_config, adb)
    assert device.state.current_state == EmulatorState.CLOSED

    with pytest.raises(TimeoutError):
        device.state.transition_to(EmulatorState.LOADING)

    assert device.state.current_state == EmulatorState.LOADING
    assert device.is_ready() is False


def test_wait_for_load_success_still_reports_ready(mock_config):
    """A responsive emulator must still reach READY (no regression)."""
    adb = MagicMock()
    adb.connect.return_value = True
    device = _make_device(mock_config, adb)
    device.state.current_state = EmulatorState.LOADING

    device.wait_for_load(timeout_s=10)

    assert device.state.current_state == EmulatorState.READY
    assert device.is_ready() is True
