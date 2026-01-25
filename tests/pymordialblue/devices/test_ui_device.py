"""Tests for PymordialUiDevice."""

from unittest.mock import patch

import numpy as np
from PIL import Image
from pymordial.ui.pixel import PymordialPixel

from pymordialblue.devices.ui_device import PymordialUiDevice


def test_ui_device_init(mock_config):
    """Test initialization of PymordialUiDevice."""
    device = PymordialUiDevice()
    assert device is not None


def test_ui_device_check_pixel_color(mock_cv2):
    """Test pixel color matching."""
    device = PymordialUiDevice()
    # Set og_resolution to (100, 100) to match the mock image size and avoid scaling issues
    pixel = PymordialPixel(
        label="test_pixel",
        position=(10, 20),
        pixel_color=(255, 0, 0),
        tolerance=10,
        og_resolution=(100, 100),
    )

    # Mock image (RGB for PIL consistency in tests)
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[20, 10] = [255, 0, 0]  # Red in RGB

    assert device.check_pixel_color(pixel, pymordial_screenshot=img) is True


def test_ui_device_where_element(mock_cv2):
    """Test element finding via template matching."""
    device = PymordialUiDevice()
    from pymordial.ui.image import PymordialImage

    # Create a real small PIL image instead of a MagicMock to avoid __array_interface__ errors
    real_needle = Image.new("RGB", (10, 10))

    with patch("PIL.Image.open") as mock_open:
        mock_open.return_value = real_needle

        # Need to satisfy PymordialImage initialization (checks path existence)
        with patch("pathlib.Path.exists", return_value=True):
            element = PymordialImage(
                label="test_el",
                filepath="fake.png",
                confidence=0.9,
                og_resolution=(100, 100),
            )

        # Mock match result at (10, 10)
        with patch("cv2.minMaxLoc", return_value=(0, 0.99, (0, 0), (10, 10))):
            coords = device.where_element(
                element, pymordial_screenshot=np.zeros((100, 100, 3), dtype=np.uint8)
            )
            # Center of 10x10 at (10,10) is (15, 15)
            assert coords == (15, 15)


def test_ui_device_read_text(mock_pytesseract, mock_cv2):
    """Test OCR text reading."""
    device = PymordialUiDevice()
    text = device.read_text(
        pymordial_screenshot=np.zeros((100, 100, 3), dtype=np.uint8)
    )
    assert text == ["mocked text"]
    assert mock_pytesseract["image_to_string"].called


def test_ui_device_find_text(mock_pytesseract, mock_cv2):
    """Test finding text coordinates."""
    device = PymordialUiDevice()

    # Center of (50, 60, 20, 10) is (60, 65)
    coords = device.find_text(
        "Target", pymordial_screenshot=np.zeros((100, 100, 3), dtype=np.uint8)
    )
    assert coords == (60, 65)
    # Center of (50, 60, 20, 10) is (60, 65)
    coords = device.find_text(
        "Target", pymordial_screenshot=np.zeros((100, 100, 3), dtype=np.uint8)
    )
    assert coords == (60, 65)
