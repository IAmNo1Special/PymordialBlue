# PymordialBlue

**Advanced Android Automation for BlueStacks**

PymordialBlue is the specialized BlueStacks implementation of the **Pymordial** automation framework. It bridges the gap between high-level Python automation and low-level emulator control, offering a unified interface for process management, ADB communication, and high-performance computer vision.

## Why PymordialBlue?

### 🚀 High-Performance Streaming
Traditional automation libraries rely on `adb screencap`, which can take 500ms - 1s per frame. PymordialBlue implements a threaded **H.264 video stream** using `adb screenrecord` and `PyAV`, reducing latency to **<100ms**. This enables real-time reaction to game events and smooth UI interactions.

### 🎮 Native Emulator Control
PymordialBlue doesn't just talk to Android; it talks to **BlueStacks**. It manages the `HD-Player.exe` process directly, allowing you to:
*   Automatically find the BlueStacks installation.
*   Start the emulator if it's closed.
*   Wait for the engine to fully load before attempting ADB connections.
*   Gracefully shut down the emulator.

### 👁️ Unified Vision System
Forget coordinating multiple libraries. The `PymordialUiDevice` unifies:
*   **Template Matching**: Find buttons and icons with multi-scale support.
*   **Pixel Checks**: Ultra-fast color verification for status bars/indicators.
*   **OCR**: Integrated Tesseract support for reading dynamic text.

### 🛡️ Robust Architecture
Built on a foundation of **State Machines**, PymordialBlue prevents common automation flakes.
*   **App States**: `CLOSED` → `LOADING` → `READY`.
*   **Emulator States**: `CLOSED` → `LOADING` → `READY`.
*   **Auto-Reconnect**: Automatically detects and recovers from ADB disconnects.

## Installation

```bash
# Clone the repository
git clone https://github.com/IAmNo1Special/PymordialBlue.git
cd PymordialBlue

# Sync environment
uv sync
```

## Next Steps

*   [**Getting Started**](user_guide/getting_started.md): Installation and first steps.
*   [**Architecture**](user_guide/core_concepts.md): Understand how the Controller, Devices, and Plugins work together.
*   [**Controller API**](reference/controller.md): Full reference for the main `PymordialBluestacksController`.
