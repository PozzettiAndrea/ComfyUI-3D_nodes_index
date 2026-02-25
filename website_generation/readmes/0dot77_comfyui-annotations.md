# ComfyUI Annotations

A lightweight annotation overlay for ComfyUI. Draw freehand notes directly on your workflow canvas.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![ComfyUI](https://img.shields.io/badge/ComfyUI-compatible-orange)

![image](comfy-annotations.jpeg)

## Features

- **Freehand Drawing** - Smooth pen strokes with adjustable color, size, and opacity
- **World-Space Annotations** - Strokes stay anchored to nodes during zoom/pan
- **Eraser Tool** - Remove strokes with visual cursor feedback
- **Undo/Redo** - Full history support (Ctrl+Z / Ctrl+Shift+Z)
- **Auto-Save** - Annotations persist with your workflow file
- **Performance Optimized** - Handles thousands of strokes smoothly
- **Non-Destructive** - No workflow data modification

## Installation

### ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Annotations"
3. Click Install
4. Restart ComfyUI

### Git Clone

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/0dot77/comfyui-annotations.git
```

### Manual

1. Download the [latest release](https://github.com/0dot77/comfyui-annotations/releases)
2. Extract to `ComfyUI/custom_nodes/comfyui-annotations/`
3. Restart ComfyUI

## Quick Start

1. Press **`A`** to toggle annotation mode
2. Draw with your mouse, trackpad, or pen tablet
3. Press **`A`** again to exit and resume normal editing
4. Save your workflow - annotations are included automatically

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `A` | Toggle annotation mode |
| `P` | Pen tool |
| `E` | Eraser tool |
| `T` | Collapse/expand toolbar |
| `Ctrl+Z` | Undo |
| `Ctrl+Shift+Z` | Redo |
| `Escape` | Exit annotation mode |

## Toolbar

Located in the top-right corner:

- **Mode Toggle** - ON/OFF button
- **Tools** - Pen and Eraser
- **Pen Settings** - Size, opacity, color presets
- **Actions** - Undo, Redo, Clear All

## Browser Support

| Browser | Status |
|---------|--------|
| Chrome 90+ | ✅ Full support |
| Edge 90+ | ✅ Full support |
| Firefox 88+ | ✅ Full support |
| Safari 14+ | ✅ Full support |

## Uninstall

Remove the `comfyui-annotations` folder from `custom_nodes/` and restart ComfyUI.

Your workflows remain intact - annotations are simply ignored when the extension isn't installed.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

[MIT License](LICENSE)
