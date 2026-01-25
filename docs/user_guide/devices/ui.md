# UI Device

The `PymordialUiDevice` class (`src/pymordialblue/devices/ui_device.py`) provides the "eyes" of the framework. It handles image recognition, pixel color validation, and text reading.

## Element Finding (Template Matching)

The primary method for finding UI elements is `where_element`. It takes a `PymordialImage` definition and searches for it on the screen using OpenCV template matching (`cv2.matchTemplate`).

```python
from pymordial.ui.image import PymordialImage

# Define an element
logo = PymordialImage(label="logo", filepath="assets/logo.png", confidence=0.8)

# Find it
coords = controller.ui.where_element(logo)
if coords:
    print(f"Found at {coords}")
```

*   **Scaling**: It automatically scales the needle image (the asset) to match the current screen resolution relative to the `og_resolution` defined in the element.
*   **Retries**: It will retry for `default_find_ui_retries` (from config) before returning `None`.

## Pixel Checking

`check_pixel_color` is used for ultra-fast state validation (e.g., checking if a health bar is full or an icon is active) without full image matching.

```python
from pymordial.ui.pixel import PymordialPixel

# Check if pixel at (100, 100) is Red (255, 0, 0)
hp_bar_pixel = PymordialPixel(
    label="hp_full", 
    position=(100, 100), 
    pixel_color=(255, 0, 0), 
    tolerance=10
)

is_full = controller.ui.check_pixel_color(hp_bar_pixel)
```

## Text Recognition

The UI device acts as a gateway to the OCR engine (Tesseract).

*   `read_text(image)`: Returns all text lines found in the image.
*   `find_text(text, image)`: Returns coordinates of the specific text.
*   `check_text(text, image)`: Returns boolean if text exists.

It delegates these calls to the configured `PymordialOCRDevice` (see [Tesseract Device](tesseract.md)).
