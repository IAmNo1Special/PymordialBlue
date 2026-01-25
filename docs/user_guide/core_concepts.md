# Core Concepts

## PymordialBluestacksController

The `PymordialBluestacksController` (`src/pymordialblue/bluestacks_controller.py`) is the main entry point for using the library. It follows the Facade pattern, orchestrating interactions between the ADB bridge, the Emulator process, and the UI recognition system.

### Initialization

```python
from pymordialblue.bluestacks_controller import PymordialBluestacksController

# Initialize with defaults (loads from config)
controller = PymordialBluestacksController()

# Initialize with overrides
controller = PymordialBluestacksController(adb_host="127.0.0.1", adb_port=5555)
```

The controller initializes three main sub-components, accessible as attributes:
1.  **`controller.adb`** (`PymordialAdbDevice`): For sending shell commands and streaming video.
2.  **`controller.bluestacks`** (`PymordialBluestacksDevice`): For managing the emulator window/process.
3.  **`controller.ui`** (`PymordialUiDevice`): For finding images and text on screen.

### Common Operations

*   **App Management**:
    *   `open_app(app_name)`: Launches an app (via package name or keyword).
    *   `close_app(app_name)`: Force stops an app.
    *   `get_current_app()`: Returns the package name of the focused app.
*   **Input**:
    *   `click_coord((x, y))`: Taps a specific coordinate.
    *   `click_element(element)`: Finds a UI element and taps it.
    *   `type_text("hello")`: Types text via ADB.
    *   `press_enter()`, `press_esc()`: Sends key events.
*   **Screen**:
    *   `capture_screen()`: Returns a screenshot as bytes.
    *   `get_frame()`: Returns the latest frame from the video stream as a numpy array.

---

## PymordialAndroidApp

The `PymordialAndroidApp` class (`src/pymordialblue/android_app.py`) provides a structured way to model the applications you are automating. It maintains a lifecycle state (`CLOSED` -> `LOADING` -> `READY`).

### defining an App

To automate a specific game or app, subclass `PymordialAndroidApp`:

```python
from pymordialblue.android_app import PymordialAndroidApp
from pymordial.ui.image import PymordialImage

# Define a UI element that indicates the app is fully loaded
MAIN_MENU_LOGO = PymordialImage(
    label="main_menu_logo",
    filepath="assets/logo.png"
)

class MyGame(PymordialAndroidApp):
    def __init__(self):
        super().__init__(
            app_name="My Game",
            package_name="com.example.mygame",
            ready_element=MAIN_MENU_LOGO
        )

# Register with controller
game = MyGame()
controller = PymordialBluestacksController(apps=[game])

# Open the app
# The controller will launch 'com.example.mygame' and wait for 'MAIN_MENU_LOGO' to appear.
# Once visible, game.state transitions to READY.
controller.open_app(game)
```

### Lifecycle Methods
*   `check_ready()`: Checks if the `ready_element` is visible. Automatically called during `open_app`.
*   `is_open()`: Returns `True` if state is `READY`.
*   `is_loading()`: Returns `True` if state is `LOADING`.
*   `is_closed()`: Returns `True` if state is `CLOSED`.
