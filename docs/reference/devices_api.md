# Devices API Reference

## AdbDevice
**Class**: `pymordialblue.devices.adb_device.PymordialAdbDevice`

Wrapper for `adb-shell`.

### `run_command`
Executes a raw shell command.

```python
def run_command(self, command: str, decode: bool = False) -> bytes | None
```

### `start_stream`
Starts the background thread that pipes `screenrecord` output to PyAV.

```python
def start_stream(self) -> bool
```

### `get_latest_frame`
Returns the most recent frame from the stream buffer.

```python
def get_latest_frame(self) -> np.ndarray | None
```
*   **Returns**: BGR numpy array (OpenCV format) or None.

---

## UiDevice
**Class**: `pymordialblue.devices.ui_device.PymordialUiDevice`

Wrapper for OpenCV and Tesseract.

### `where_element`
Performs template matching for Image elements.

```python
def where_element(
    self,
    pymordial_element: PymordialElement,
    pymordial_screenshot: bytes | np.ndarray | None = None,
    max_tries: int | None = None
) -> tuple[int, int] | None
```

### `check_pixel_color`
Verifies pixel color at a specific coordinate.

```python
def check_pixel_color(
    self,
    pymordial_pixel: PymordialPixel,
    pymordial_screenshot: bytes | np.ndarray | None = None
) -> bool
```

---

## BluestacksDevice
**Class**: `pymordialblue.devices.bluestacks_device.PymordialBluestacksDevice`

Wrapper for `psutil` process management.

### `open`
Starts the BlueStacks process (`HD-Player.exe`).

```python
def open(self, max_retries: int | None = None) -> None
```

### `close`
Kills the BlueStacks process.

```python
def close(self) -> bool
```
