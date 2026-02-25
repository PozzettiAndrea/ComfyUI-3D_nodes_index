# BITalino Custom Node for ComfyUI

This module implements a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) to interface with BITalino devices. It provides a convenient way to capture sensor data from a BITalino device, using the PLUX-API-Python library to handle the connection and data acquisition.

## Overview

The module is built around two main components:

- **LRBitalinoReceiver** (in `comfy/bitalino_receiver_node.py`):  
  A custom node for ComfyUI that exposes configurable inputs such as:
  - BITalino MAC address
  - Acquisition duration (in seconds)
  - Sampling frequency (samples per second)
  - Channel code (specifies which sensor channel to use)  

  This node initializes the BITalino connection (if not already done) and fetches the latest sensor value, returning it as a float.

- **BitalinoReceiver** (in `src/bitalino_receiver.py`):  
  Handles the direct interaction with the BITalino device. It uses multi-threading to run the data acquisition process in the background. The class:
  - Sets up the BITalino device for data collection
  - Performs the acquisition based on the specified parameters
  - Uses a callback (`onRawFrame`) to update the last sensor reading, which is later retrieved by the custom node

## Features

- **Custom Node Integration:** Seamlessly integrates with ComfyUI as a custom node, enabling the use of BITalino devices within your ComfyUI workflows.
- **Configurable Parameters:** Easily set the BITalino MAC address, change the duration of data acquisition, adjust the sampling frequency, and select the desired sensor channel.
- **Parallel Data Acquisition:** Uses Python's threading module to run data acquisition in parallel without blocking the main thread.
- **Cross-Platform Support:** Designed to work across different operating systems (macOS, Linux, Windows) with platform-specific adjustments managed internally.

## Requirements

- **Python Version:** Python 3.10 or higher is recommended.
- **PLUX API:** Ensure the PLUX-API-Python library is available and properly configured for your operating system. The module dynamically adjusts paths and settings based on your platform.

## Installation

To install the package in editable mode, run the following command in your terminal:

```bash
pip install -e .
```


