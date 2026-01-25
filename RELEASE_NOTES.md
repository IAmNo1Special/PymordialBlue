# Release Notes - v0.1.0

We are excited to announce the first release of **PymordialBlue**, an advanced automation framework for BlueStacks built on top of Pymordial!

## 🚀 Highlights

### 🕹️ Native BlueStacks Control
Direct integration with the BlueStacks emulator allowing you to automatically:
- Detect the `HD-Player.exe` process.
- Launch and close the emulator.
- Manage window focus and state.

### ⚡ High-Performance Streaming
Forget slow ADB screenshots. PymordialBlue implements a threaded H.264 video stream decoding pipeline using `screenrecord` and `pyav`.
- **Latency**: <100ms
- **FPS**: Up to 60fps (configurable)
- **Format**: RGB numpy arrays ready for OpenCV

### 🧠 Intelligent UI Controller
A unified controller (`PymordialBluestacksController`) that acts as a single point of entry for your automation scripts.
- **Computer Vision**: Template matching with `opencv-python-headless`.
- **Pixel Checks**: Instant state validation using pixel color checking.
- **OCR**: Integrated Tesseract support with custom extraction strategies for difficult game fonts.

### 📦 Robust Application Model
Structure your automation code using the `PymordialAndroidApp` class. Define your apps, their package names, and their "Ready" states (e.g., waiting for a specific logo) to ensure your scripts never flake on startup.

## 🔧 Installation

```bash
uv add pymordialblue
```

## 📖 Documentation
Check out the fully refactored [User Guide](docs/user_guide/index.md) for detailed setup and usage instructions.
