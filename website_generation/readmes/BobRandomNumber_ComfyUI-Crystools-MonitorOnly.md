# ComfyUI-Crystools-MonitorOnly

> **Attribution:** This project is a focused, lightweight fork of [ComfyUI-Crystools](https://github.com/crystian/comfyui-crystools) created by **[crystian](https://github.com/crystian)**. All credit for the original architecture, design, and core logic goes to them.

## Overview

This is a, "Monitor Only" version of the Crystools extension for ComfyUI. It provides the real-time system resource monitor (CPU, RAM, GPU, VRAM, HDD) within the ComfyUI interface.

The purpose of this fork is to provide the monitoring functionality for Nvidia only without the additional node suite, or dependencies of the full package.

## Modifications & Refactoring

We have modified the codebase to isolate the monitoring features and improve stability.

### 1. The "Stripping" Process
*   **Removed Nodes:** All functional nodes (Logic Switches, Debuggers, Text utilities, JSON handlers, Metadata editors) were completely removed.
*   **Dependencies:**
    *   Removed most dependencies to reduce installation size and complexity.
    *   Replaced the older `pynvml` dependency with the updated, maintained `nvidia-ml-py` library.
*   **Cleanup:** Deleted icons, assets, and legacy code.

### 2. Code Enhancements & Fixes
*   **Dynamic Pathing:** The extension now dynamically resolves its folder name. This ensures stylesheets and scripts load correctly even if the installation folder is renamed.

*   **Console Hygiene:**
    *   Reduced console log verbosity.
    *   Updated log prefixes to `[Crystools Monitor]` for clarity.
*   **UI & Settings:**
    *   Renamed the Settings category from "Crystools" to **"CrysMonitor"** to differentiate it from the full suite.


## Installation

1.  Navigate to your ComfyUI `custom_nodes` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/BobRandomNumber/ComfyUI-Crystools-MonitorOnly.git
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Start ComfyUI.

## Optional
2.  Open the **Settings** menu (Gear icon).
3.  Scroll down to the **CrysMonitor** category.
4.  Here you can:
    *   Enable/Disable specific monitors (CPU, RAM, GPU, etc.).
    *   Adjust the refresh rate.
    *   Change the size (width/height) of the monitor bar.

---

## Official Attribution

**Original Author:** [Crystian](https://github.com/crystian)
*   **Original Repository:** [ComfyUI-Crystools](https://github.com/crystian/comfyui-crystools)

This project respects and retains the license of the original repository. Please refer to the original project for the full suite of tools.