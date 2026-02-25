# AMD GPU Monitor for ComfyUI

A simple, lightweight AMD GPU monitoring tool for ComfyUI that displays real-time information about your AMD GPU directly in the UI.

![AMD GPU Monitor Screenshot](https://github.com/iDAPPA/ComfyUI-AMDGPUMonitor/raw/main/screenshot.png)

## Features

- Real-time GPU utilization monitoring (%)
- VRAM usage tracking (both in MB/GB and percentage)
- GPU temperature monitoring (°C)
- Color-coded indicators (blue for low, orange for medium, red for high usage)
- Draggable, collapsible, and closable UI
- Position persistence between sessions
- Works with ROCm-enabled GPUs
- Specifically tested with AMD Radeon RX 7900 XTX

## Installation

1. Clone the repository into your ComfyUI custom nodes directory:

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/iDAPPA/ComfyUI-AMDGPUMonitor.git
```

2. Restart ComfyUI

## Requirements

- An AMD GPU with ROCm support
- `rocm-smi` or `amd-smi` command-line tools installed and accessible in your PATH
- ComfyUI running on a Linux system with ROCm drivers

## Usage

No setup is required. Once installed, the monitor will automatically appear in the top-right corner of ComfyUI's interface.

### Monitor Features:

- **Drag**: Click and hold the title bar to move the monitor anywhere on the screen
- **Collapse/Expand**: Click the "−" button to collapse the monitor to just the title bar
- **Close**: Click the "×" button to close the monitor (a "Show AMD GPU Monitor" button will appear to bring it back)

## How It Works

This extension uses the `rocm-smi` command-line tool to collect GPU information and displays it in a floating UI element in the ComfyUI interface. It does not affect the performance of ComfyUI or your GPU.

## Troubleshooting

If the monitor doesn't appear or doesn't show any data:

1. Check if `rocm-smi` is installed and working by running it in a terminal
2. Make sure your AMD GPU is properly detected by the system
3. Verify that you're running ComfyUI with ROCm support
4. Check the browser console for any JavaScript errors

## Credits

- Inspired by the GPU monitoring in [ComfyUI-Crystools](https://github.com/crystian/ComfyUI-Crystools)
- Created with the help of Claude AI

## License

MIT License
