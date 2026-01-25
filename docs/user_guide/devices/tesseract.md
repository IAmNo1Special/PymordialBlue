# Tesseract Device

The `PymordialTesseractDevice` (`src/pymordialblue/devices/tesseract_device.py`) implements the OCR capability using the local Tesseract binary.

## Setup

The device attempts to resolve the Tesseract executable in two ways:
1.  **System Path**: Uses `tesseract` from the system PATH.
2.  **Configured Path**: Uses the path specified in `extract_strategy.tesseract.tesseract_cmd` in `configs.yaml`.
3.  **Bundled Binary**: Checks for a bundled binary in `bin/tesseract/tesseract.exe` (common for portable distributions).

## Text Extraction

The primary method is `extract_text`. It accepts an image (path, bytes, or numpy array) and an optional "Extract Strategy".

```python
adb_stream_frame = controller.get_frame()
text = controller.ui.read_text(adb_stream_frame)
```

## Text Finding

`find_text(search_text, image)` attempts to return the `(x, y)` center coordinates of the matching text. It uses `pytesseract.image_to_data` to get bounding boxes for all detected words and searches for the keyword.

## Preprocessing Integration

Tesseract accuracy is heavily dependent on image quality. The device integrates deeply with `PymordialExtractStrategy`. When you call `extract_text`, you can pass a strategy:

```python
from pymordialblue.utils.extract_strategies import DefaultExtractStrategy

# Use a specific strategy that denoises and thresholds the image
my_strategy = DefaultExtractStrategy()
text = controller.ui.read_text(frame, strategy=my_strategy)
```

See [Extract Strategies](../extract_strategies.md) for more details.
