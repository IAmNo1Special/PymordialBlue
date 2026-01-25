"""Tests for PymordialAndroidApp."""

from pymordial.core.state_machine import AppState
from pymordial.ui.element import PymordialElement

from pymordialblue.android_app import PymordialAndroidApp


def test_android_app_init():
    """Test initialization of PymordialAndroidApp."""
    app = PymordialAndroidApp(app_name="TestApp", package_name="com.test.app")
    assert app.app_name == "TestApp"
    assert app.package_name == "com.test.app"


def test_android_app_check_ready(mock_controller):
    """Test check_ready logic."""
    ready_element = PymordialElement(label="ready_btn")
    app = PymordialAndroidApp(
        app_name="TestApp", package_name="com.test.app", ready_element=ready_element
    )

    # Setup state and controller
    app.pymordial_controller = mock_controller
    app.app_state.transition_to(AppState.LOADING)

    # Mock controller's element detection
    mock_controller.is_element_visible = lambda el, **kwargs: True

    assert app.check_ready() is True
    assert app.is_open() is True
