# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2026-01-25
### Fixed
- **PyPI Compatibility**: Updated `README.md` links to absolute GitHub URLs to fix broken documentation on PyPI.
- **CI/CD**: Repaired documentation build failures by adding `pyyaml` dependency and fixing `mkdocstrings` imports.
- **Documentation**: Corrected broken links in `index.md` and fixed missing navigation pages.
- **Code**: Resolved docstring parameter mismatch in `bluestacks_controller.py`.

## [0.1.0] - 2026-01-25

### Added
- **Core Controller**: `PymordialBluestacksController` handling ADB, Emulator, and UI.
- **App Model**: `PymordialAndroidApp` for lifecycle management.
- **Devices**:
    - `PymordialAdbDevice`: ADB shell, input, and H.264 streaming.
    - `PymordialBluestacksDevice`: Process management for BlueStacks.
    - `PymordialUiDevice`: Template matching and pixel verification.
    - `PymordialTesseractDevice`: Tesseract OCR integration.
- **Configuration**: Tiered system with `configs.yaml` and `pymordialblue_configs.yaml` override support.
- **Documentation**: Comprehensive Refactored User Guide in `docs/user_guide/`.

