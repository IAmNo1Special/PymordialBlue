# Configuration

PymordialBlue uses a tiered configuration system managed by `src/pymordialblue/utils/configs.py`. This ensures that you can customize settings for your specific environment without modifying the library code.

## 1. The Tiered System

1.  **Package Defaults**: The library comes with built-in default settings located in `src/pymordialblue/configs.yaml`. This file is tracked in git and should **not** be modified directly for local changes.
2.  **User Overrides**: You can override any default setting by creating a `pymordialblue_configs.yaml` file in your project's root directory. This file is loaded last and takes precedence over the defaults.

## 2. Setting Up Your Configuration

To customize PymordialBlue for your environment, you **must** copy the example configuration file provided with the package to your project root.

**Step 1:** Locate `pymordialblue_configs.example.yaml` in the PymordialBlue package root.
**Step 2:** Copy this file to your project's root directory and rename it to `pymordialblue_configs.yaml`.
**Step 3:** Edit `pymordialblue_configs.yaml` to override variables.

```bash
# Example Setup (PowerShell)
cp pymordialblue_configs.example.yaml pymordialblue_configs.yaml
```

## 3. Configuration Sections

The configuration file is divided into several key sections:

### `adb`
Configures the connection to the Android Debug Bridge.
-   `default_host` / `default_port`: The IP/Port of your BlueStacks instance (usually `127.0.0.1:5555`).
-   `commands`: Timeouts for shell commands.
-   `stream`: Settings for the low-latency video stream (`bitrate`, `resolution`, `queue_size`).

### `bluestacks`
Configures the emulator process on Windows.
-   `hd_player_exe`: The name of the BlueStacks executable (e.g., `HD-Player.exe`).
-   `default_resolution`: The expected window size (e.g., `[1920, 1080]`).
-   `window_title`: The window title to look for.

### `ui`
Configures computer vision behavior.
-   `default_find_ui_retries`: How many times to retry finding an image before giving up.
-   `default_wait_time`: Time to sleep between retries.

### `setup`
Contains paths and registry keys for the BlueStacks installer.

### `extract_strategy`
Defines parameters for image preprocessing strategies (used by Tesseract OCR). See [Extract Strategies](extract_strategies.md) for details.
