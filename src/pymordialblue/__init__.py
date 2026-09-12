"""PymordialBlue: Advanced Automation for BlueStacks using Pymordial."""

from pymordialblue.devices import AdbDevice, AndroidUiDevice, BluestacksDevice, TesseractDevice
from pymordialblue.android_app import AndroidApp
from pymordialblue.bluestacks_controller import BluestacksController
from pymordialblue.utils.configs import BlueConfig, get_config
from pymordialblue.utils.extract_strategies import DefaultExtractStrategy, ExtractStrategy, RevomonTextStrategy

__all__ = [
    "AdbDevice",
    "AndroidApp",
    "AndroidUiDevice",
    "BluestacksController",
    "BluestacksDevice",
    "BlueConfig",
    "DefaultExtractStrategy",
    "ExtractStrategy",
    "RevomonTextStrategy",
    "TesseractDevice",
    "get_config",
]

__version__ = "0.1.0"