---
type: Pipeline Specification
title: "PymordialBlue — Dynamic ADB Port Discovery & H.264 Video Streaming"
description: "Automated BlueStacks ADB port scanning, localhost loopback connection, and threaded H.264 video decoding via PyAV and adb screenrecord."
resource: package:pymordialblue.devices
tags: [pymordialblue, adb, streaming, h264, pyav, screenrecord, low-latency]
status: stable
generated:
  by: human:IAmNo1Special
  at: 2026-09-16T12:00:00Z
verified:
  - by: human:IAmNo1Special
    at: 2026-09-16T12:00:00Z
sources:
  - id: pymordialblue-devices
    resource: package:pymordialblue.devices
    title: "PymordialBlue Devices Module"
---

# PymordialBlue — Dynamic ADB Port Discovery & H.264 Video Streaming

Traditional mobile automation via standard `adb screencap` incurs $500\text{--}1000\text{ ms}$ overhead per frame, making reactive gameplay impossible. PymordialBlue implements continuous in-memory video stream decoding.

---

## 1. Dynamic Port Discovery & ADB Bridge

BlueStacks dynamically assigns local loopback ports on each reboot:
1. PymordialBlue queries running instances or parses active ports from `bluestacks.conf`.
2. Connects via loopback address: `127.0.0.1:<discovered_port>`.
3. Validates connection health using ADB daemon ping before initiating streaming.

---

## 2. Low-Latency H.264 Streaming Pipeline

```mermaid
flowchart LR
    BS["BlueStacks Android Container"] -->|"adb exec-out screenrecord"| RawStream["Raw H.264 Byte Stream"]
    RawStream --> Thread["Background Reader Thread"]
    Thread --> PyAV["PyAV Hardware Decoder"]
    PyAV --> FrameBuffer["Latest Frame Buffer (NumPy BGR)"]
    FrameBuffer --> Vision["Perception / Vision Pipeline (<100ms)"]
```

### Key Performance Attributes
- **Throughput**: $30\text{--}60\text{ FPS}$ sustained capture.
- **Latency**: Drops perception pipeline latency from $\sim 800\text{ ms}$ down to $<100\text{ ms}$.
- **Thread Safety**: The frame buffer is protected by a fast lock; perception workers read the latest decoded frame without blocking frame acquisition.

See also: [Architecture](./architecture.md) and [Vision & OCR](./vision_and_ocr.md).