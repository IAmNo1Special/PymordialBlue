# Extract Strategies

OCR engines like Tesseract often fail on raw game screenshots due to complex backgrounds, low contrast text, or graphical artifacts. PymordialBlue solves this with "Extract Strategies" (`src/pymordialblue/utils/extract_strategies.py`).

A Strategy is a class that defines:
1.  **Preprocessing**: How to transform the image (crop, grayscale, threshold, upscale) before OCR.
2.  **Configuration**: What Tesseract flags to use (e.g., whitelist specific characters, set Page Segmentation Mode).
3.  **Postprocessing**: How to clean up the resulting text.

## DefaultExtractStrategy

The `DefaultExtractStrategy` provides a robust pipeline suitable for most black-on-white (or inverted) text.

**Pipeline:**
1.  **Upscale**: Increases resolution by `upscale_factor` (default 2x). Tesseract prefers larger characters.
2.  **Grayscale**: Converts to B&W.
3.  **Denoise**: Applies generic denoising to reduce grain.
4.  **Threshold (Otsu)**: Binarizes the image into pure black and white.
5.  **Inversion Check**: Automatically inverts the image if the mean brightness suggests white-on-black text (Tesseract prefers black text on white background).

## Creating a Custom Strategy

To handle specific UI elements (e.g., a resource counter that is always red on a dark background), create a custom strategy.

```python
from pymordial.core.blueprints.extract_strategy import PymordialExtractStrategy
import cv2
import numpy as np

class HpBarStrategy(PymordialExtractStrategy):
    def preprocess(self, image: np.ndarray) -> np.ndarray:
        # Custom logic: Extract only red channel, threshold it
        # ...
        return processed_image

    def tesseract_config(self) -> str:
        # Only look for digits
        return "--psm 7 -c tessedit_char_whitelist=0123456789/"
```

## Configuration

Many parameters of the default strategies (like threshold limits or upscale factors) are exposed in the `extract_strategy` section of `configs.yaml`, allowing tuning without code changes.
