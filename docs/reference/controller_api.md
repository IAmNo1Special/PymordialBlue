# Controller API Reference

**Class**: `pymordialblue.bluestacks_controller.PymordialBluestacksController`

The main interface for global operations, input, and vision.

## Initialization

```python
def __init__(
    self,
    adb_host: str | None = None,
    adb_port: int | None = None,
    apps: list[PymordialAndroidApp] | None = None
)
```

## App Methods

### `open_app`
Opens an app on the device.

```python
def open_app(
    self,
    app_name: str | PymordialAndroidApp,
    package_name: str | None = None,
    timeout: int | None = None,
    wait_time: int | None = None
) -> bool
```
*   **app_name**: Display name or App object.
*   **package_name**: Optional package name (if not in App object).
*   **timeout**: Max seconds to wait for launch.
*   **Returns**: `True` if launch verification passed.

### `close_app`
Force closes an app.

```python
def close_app(
    self,
    app_name: str | PymordialAndroidApp,
    package_name: str | None = None
) -> bool
```

## Input Methods

### `click_element`
Finds a UI element and clicks it.

```python
def click_element(
    self,
    pymordial_element: PymordialElement,
    times: int = 1,
    screenshot_img_bytes: bytes | None = None,
    max_tries: int = 10
) -> bool
```
*   **pymordial_element**: The Image, Pixel, or Text element to find.
*   **times**: Number of clicks (default 1).
*   **max_tries**: Retries if element is not immediately visible.

### `click_coord`
Clicks specific (x, y) coordinates.

```python
def click_coord(self, coords: tuple[int, int], times: int = 1) -> bool
```

### `type_text`
Types text into the device.

```python
def type_text(self, text: str, enter: bool = False) -> None
```

## Vision Methods

### `find_element`
Returns the coordinates of an element.

```python
def find_element(
    self,
    pymordial_element: PymordialElement,
    max_tries: int = 10
) -> tuple[int, int] | None
```
*   **Returns**: `(x, y)` tuple of the center point, or `None` if not found.

### `is_element_visible`
Checks if an element is currently visible.

```python
def is_element_visible(
    self,
    pymordial_element: PymordialElement,
    max_tries: int | None = None
) -> bool
```

### `start_streaming` / `stop_streaming`
Controls the background video stream for high-performance capture.

```python
def start_streaming(self) -> bool
def stop_streaming() -> None
```
