# Getting Started

## Prerequisites

*   **Operating System**: Windows 10/11 (Required for BlueStacks).
*   **BlueStacks**: Version 5 or newer installed.
*   **Python**: 3.11 or newer (3.13 tested).
*   **Packet Manager**: `uv` (Recommended) or `pip`.

### BlueStacks Configuration
To ensure PymordialBlue can connect:
1.  Open BlueStacks Settings.
2.  Go to **Advanced**.
3.  Turn **Android Debug Bridge (ADB)** to **ON**.
4.  Note: You do *not* need to manually install ADB on your system; Pymordial uses the bundled `adb-shell` library.

## Installation

We recommend using `uv` for dependency management.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/IAmNo1Special/PymordialBlue.git
    cd PymordialBlue
    ```

2.  **Sync Environment**
    This command creates the virtual environment and installs all dependencies (including the local Pymordial core).
    ```bash
    uv sync
    ```

3.  **Activate Environment** (Optional)
    ```bash
    # On Windows
    .venv\Scripts\activate
    ```

## Verify Installation

PymordialBlue includes a set of examples to verify functionality. Run the basic connection test:

```bash
uv run examples/01_basic_connection.py
```

**Expected Output:**
```text
INFO:PymordialAdbDevice:Connecting to ADB at 127.0.0.1:5555...
INFO:PymordialAdbDevice:PymordialAdbDevice device connected.
INFO:root:Connected to BlueStacks!
INFO:root:BlueStacks is READY.
```
