# App Management

PymordialBlue provides a structured way to manage Android applications using the `PymordialAndroidApp` class. This wrapper handles opening, closing, and tracking the state of your app.

## Defining an App

You define an app by its name and package name. You can also optionally define a "Ready Element" — a UI element that, when visible, confirms the app is fully loaded and ready for interaction.

```python
from pymordialblue import PymordialAndroidApp
from pymordial.ui.text import PymordialText

# Define an element that only appears on the main menu
main_menu_title = PymordialText(
    label="main_menu_title",
    element_text="START GAME"
)

# Create the app instance
my_game = PymordialAndroidApp(
    app_name="Super Game",
    package_name="com.super.game",
    ready_element=main_menu_title  # Optional auto-ready check
)
```

## Lifecycle States

Every app has a state machine attached (`app.app_state`).

1.  **`AppState.CLOSED`**: The app is not running.
2.  **`AppState.LOADING`**: The app process has been started (PID exists), but the `ready_element` is not yet visible.
3.  **`AppState.READY`**: The app is fully loaded and ready for automation.

### Transitioning States

#### Automatic Transition
If you provided a `ready_element`, `open_app()` will automatically:
1.  Launch the app via ADB.
2.  Wait for the PID to verify the process started.
3.  Transition state to `LOADING`.
4.  Continuously scan the screen for `ready_element`.
5.  Transition state to `READY` once found.

#### Manual Transition
If you don't use `ready_element`, the app will stay in `LOADING` indefinitely. You must manually transition it when your script detects it's safe to proceed.

```python
controller.open_app(my_game)
# ... your custom verify logic ...
if custom_check_passed:
    my_game.app_state.transition_to(AppState.READY)
```

## Opening and Closing

The controller interacts with these app objects:

```python
# Open the app (handles BlueStacks startup if needed)
controller.open_app(my_game)

# Check status
if my_game.is_loading():
    print("Game is loading...")

if my_game.is_open():
    print("Game is ready!")

# Force stop the app
controller.close_app(my_game)
```
