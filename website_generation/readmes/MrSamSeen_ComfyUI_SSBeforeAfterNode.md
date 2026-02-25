# ComfyUI SS Before After Node

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-ComfyUI-blue.svg)]()

> Create stunning before-and-after transition videos directly in ComfyUI.

This repository provides two powerful custom nodes for ComfyUI to create stunning before-and-after transition videos. These nodes are designed for visual comparisons, transformations, and creative effects, supporting both standard and depth map-based transitions.

## ✨ Features

- 🔄 **SSBeforeAndAfterVideo** - Create videos with fade and wipe transitions between two images.
- 🌌 **Depth Map Support** - Create depth-aware transitions (SSBeforeAndAfterVideoWithDepthMap) for immersive effects.
- 🎬 **Customizable Output** - High-quality output with custom resolution, fps, feathering, and looping.
- ⚡ **FFmpeg Integration** - Robust video encoding.
- 📊 **Progress Tracking** - Built-in progress bar for frame generation.

## 🚀 Quick Start

### Prerequisites

- ComfyUI installed
- FFmpeg installed and available in system PATH

### Installation

1.  Go to your ComfyUI custom nodes directory:
    ```bash
    cd ComfyUI/custom_nodes
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/SamSeenX/ComfyUI_SSBeforeAfterNode.git
    ```
3.  Install dependencies:
    ```bash
    pip install -r ComfyUI_SSBeforeAfterNode/requirements.txt
    ```
4.  Restart ComfyUI.

### Basic Usage

1.  Add the node **SSBeforeAndAfterVideo** or **SSBeforeAndAfterVideoWithDepthMap** to your workflow.
2.  Connect your `before_image` and `after_image` inputs.
3.  Configure parameters (transition type, duration, FPS).
4.  Run the workflow.

## 📖 Documentation

### Node 1: SSBeforeAndAfterVideo

Creates before-and-after transition videos using classic fade and wipe effects.

**Parameters:**
- `transition_type`: fade, wipe_from_left, wipe_from_top, etc.
- `transition_duration`: 0.5 - 10.0 seconds.
- `feather`: Softness of the wipe edge (0.0 - 1.0).

### Node 2: SSBeforeAndAfterVideoWithDepthMap

Creates transitions using a depth map, revealing images based on depth (e.g., back-to-front).

**Parameters:**
- `depth_map`: Input depth map image.
- `transition_type`: back_to_front, front_to_back, middle_out.
- `easing_method`: Smoothness of the transition.

## 🏗️ Project Structure

```
ComfyUI_SSBeforeAfterNode/
├── ss_before_after_video.py            # Basic node logic
├── ss_before_after_video_with_depth.py # Depth-aware node logic
├── requirements.txt                    # Python dependencies
└── README.md
```

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ☕ Support

If you find this project useful, please consider supporting me:

- ⭐ Starring this repository
- 🐛 Reporting issues
- ☕ [Buy me a coffee](https://buymeacoffee.com/samseen)

---

Created with ❤️ by [SamSeen](https://buymeacoffee.com/samseen)