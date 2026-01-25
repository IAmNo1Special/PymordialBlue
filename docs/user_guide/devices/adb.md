# ADB Device

The `PymordialAdbDevice` class (`src/pymordialblue/devices/adb_device.py`) is responsible for all low-level communication with the Android instance. It wraps `adb-shell` to provide a pythonic interface for commands, input, and video streaming.

## Connection

The device connects to the host and port specified in the configuration (default `127.0.0.1:5555`).

```python
adb = PymordialAdbDevice()
adb.connect()
if adb.is_connected():
    print("Connected!")
adb.disconnect()
```

## Shell Commands

You can run any ADB shell command using `run_command`.

```python
# Returns bytes or None
output = adb.run_command("ls /sdcard/")
print(output.decode("utf-8"))
```

## Input Injection

Convenience methods are provided for common inputs:
*   `tap(x, y)`: Taps a coordinate.
*   `type_text(text, enter=False)`: Types text (automatically escapes specific characters).
*   `press_enter()`: Sends Keycode 66.
*   `press_esc()`: Sends Keycode 4 (Back).
*   `go_home()`: Sends Keycode 3.

## App Management

*   `open_app(name)`: Attempts to launch an app. It first tries to find a package matching the `name` keyword, checks for a launchable activity, and starts it. If activity resolution fails, it falls back to `monkey`.
*   `close_app(name)`: Force stops the package matching the name.
*   `get_focused_app()`: Returns a dictionary `{'package': str, 'activity': str}` of the current foreground app.

## Video Streaming

Unique to PymordialBlue is its high-performance streaming capability. Instead of taking repeated screenshots (which is slow), it uses `screenrecord` on the device piped to a background thread that decodes H.264 frames using PyAV.

```python
# Start the background stream
if adb.start_stream():
    # Access the latest frame (numpy array) at any time
    frame = adb.get_latest_frame()
    
    # ... process frame ...
    
    # Stop the stream when done
    adb.stop_stream()
```

### Configuration
Stream settings (bitrate, resolution limit) are controlled via the `adb.stream` section in `configs.yaml`.
