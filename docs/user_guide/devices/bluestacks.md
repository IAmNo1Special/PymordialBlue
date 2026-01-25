# BlueStacks Device

The `PymordialBluestacksDevice` class (`src/pymordialblue/devices/bluestacks_device.py`) manages the lifecycle of the actual emulator process running on Windows.

## Filepath Detection

When initialized, the device attempts to automatically locate `HD-Player.exe` (the BlueStacks player executable). It searches:
1.  Standard Program Files directories (`BlueStacks_nxt`, `BlueStacks`).
2.  Common custom paths (e.g., `C:\BlueStacks`).
3.  The current working directory.
4.  A broad search of `C:\` (if configured/fallback).

You can override this by setting the `hd_player_exe` in your configuration or manually setting the `filepath` property.

## Lifecycle Management

The device implements a state machine (`CLOSED` -> `LOADING` -> `READY`).

*   `open(max_retries, wait_time)`: Starts the `HD-Player.exe` process. It polls `psutil` to verify the process exists.
*   `wait_for_load()`: Blocks until the device is responsive via ADB. This is automatically called during the transition from `LOADING` to `READY`.
*   `close()`: Terminates the `HD-Player.exe` process and disconnects ADB.

## Window Management

*   `ref_window_size`: A property `(width, height)` representing the reference resolution. This is initialized from the `bluestacks.default_resolution` config. PymordialBlue uses this to scale coordinates if the actual window size differs (though best practice is to set the emulator to the reference resolution).

```python
bs = PymordialBluestacksDevice(adb_bridge_device=adb)
bs.open()

if bs.is_ready():
    print("BlueStacks is ready for automation.")

bs.close()
```
