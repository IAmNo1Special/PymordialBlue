---
type: Vision Specification
title: "PymordialBlue — Unified Vision System & Vendored Tesseract OCR"
description: "Unified perception pipeline integrating OpenCV template matching, pixel checks, and vendored Windows Tesseract OCR binaries."
resource: package:pymordialblue.devices
tags: [pymordialblue, vision, ocr, tesseract, template-matching, perception]
status: stable
generated:
  by: human:IAmNo1Special
  at: 2026-09-16T12:00:00Z
verified:
  - by: human:IAmNo1Special
    at: 2026-09-16T12:00:00Z
sources:
  - id: pymordialblue-vision
    resource: package:pymordialblue.devices
    title: "PymordialBlue Vision & OCR Pipeline"
---

# PymordialBlue — Unified Vision System & Vendored Tesseract OCR

PymordialBlue embeds a zero-external-dependency vision and OCR stack specifically tuned for Windows and BlueStacks execution.

---

## 1. Zero-Config Vendored Binaries

To prevent environment configuration friction:
- **Tesseract OCR**: Pre-packaged under `pymordialblue/bin/tesseract/` complete with `eng.traineddata`, runtime DLLs, and `tesseract.exe`.
- **ADB Tools**: Shipped under `pymordialblue/bin/adb/` for standalone operation without requiring the full Android SDK.

---

## 2. Vision Device Capabilities (`AndroidUiDevice`)

Unifies perceptual modalities into a single interface:
- **Template Matching**: Evaluates image crops using normalized cross-correlation with multi-scale fallback.
- **Pixel Color Checks**: Instantaneous RGB checks against bounding regions.
- **OCR Text Reading**: Invokes the local vendored Tesseract executable directly on NumPy image slices with pre-configured character whitelist dictionaries.

See also: [Architecture](./architecture.md) and [ADB & Streaming](./adb_and_streaming.md).