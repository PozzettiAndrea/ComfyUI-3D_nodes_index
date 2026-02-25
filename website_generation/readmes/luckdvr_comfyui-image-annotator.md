# ComfyUI Luck Annotator

<p align="center">
  <img src="https://img.shields.io/badge/ComfyUI-Custom%20Node-green" alt="ComfyUI">
  <img src="https://img.shields.io/badge/Version-8.3-blue" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

A professional image annotation node for ComfyUI, featuring **Point**, **Rectangle**, and **Polygon** annotations with real-time rendering and WYSIWYG editing.

**Perfect for AI image editing models**: Flux2 Klein, Qwen 2.5 VL, Nano Banana, and other vision-language models that require visual guidance.

[English](README.md) | [中文文档](README.zh-CN.md)

---

## ✨ Features

- 🎯 **3 Annotation Types**: Point ⦿, Rectangle ▢, Polygon ⬡
- 🖱️ **Interactive Canvas**: Zoom, Pan, and Edit directly on the image
- 🎨 **Customizable Style**: Adjustable stroke color, width, fill transparency, and point size
- ⬅️ **Undo**: Support up to 50 undo steps with keyboard shortcuts
- 🛠️ **Selection Tools**: Box select, shift-select, and bulk delete
- 👁️ **Enhanced Visibility**: Dual-color marching ants visible on any background
- 📤 **Dual Output**: Renders annotated image + outputs JSON annotation data
- 🤖 **AI Model Ready**: Optimized for Flux2 Klein, Qwen 2.5 VL, Nano Banana, and other vision models

---

## 🎯 Use Cases

This node is designed for AI-powered image editing workflows:

- **Flux2 Klein**: Mark regions for inpainting and outpainting
- **Qwen 2.5 VL**: Provide visual guidance for vision-language tasks
- **Nano Banana**: Annotate areas for targeted image manipulation
- **General Vision Models**: Create precise visual prompts for any model that accepts annotated images

---

## 🚀 Installation

1. Clone this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/YOUR_USERNAME/comfyui-image-annotator.git
   ```
2. Restart ComfyUI.

---

## 📖 User Guide

### 1. Toolbar & Shortcuts

| Icon | Tool | Hotkey | Description |
|:---:|:---|:---:|:---|
| ↖️ | **Select** | `V` | **Default Tool**. Select/Move marks. Press `V` to cancel any active drawing tool. |
| ✋ | **Hand** | `H` | Pan the view. **Tip**: Hold `Space` bar to temporarily switch to Hand tool. |
| ⦿ | **Point** | `P` | Click to add single points. |
| ▢ | **Rect** | `M` / `R` | Drag to create bounding boxes. |
| ⬡ | **Polygon** | `L` | Click to add vertices. Double-click or Right-click to close shape. Auto-switches to Select tool after closing. |
| ⬅️ | **Undo** | `Ctrl+Z` | Undo last action (up to 50 steps). |

### 2. Selection & Interaction

- **Cancel Drawing**: Press `V` to switch back to Select tool and stop drawing.
- **Zoom Canvas**: Use **Mouse Wheel** to zoom in/out (centered on cursor).
- **Pan Canvas**: Hold `Space` and drag, or use Middle Mouse Button.

### 3. List Management

- **Range Select**: Click one item, hold `Shift`, then click another to select everything in between.
- **Multi-Select**: Hold `Ctrl` (or `Cmd` on Mac) to toggle selection of individual items.
- **Delete**: Press `Delete` or `Backspace`.


### 4. Sidebar Panels

- **Tools**: Quick access to annotation tools.
- **Appearance**: Adjust stroke/fill color, line width, and opacity.
  - *Tip*: Settings apply to **new** selections and **currently selected** items.
- **Annotations**: List of all marks. Toggle visibility 👁️ or delete individually 🗑️.

### 5. Outputs

- **`image_out`**: The input image with all visible annotations rendered on top.
- **`mark_data`** (Hidden): JSON string containing all annotation data.

---

## 📋 Example Workflow

The included `example_workflow.json` demonstrates a basic annotation pipeline:

```
LoadImage → ImageAnnotator → SaveImage
                          ↓
                      ShowText
```

**Workflow Steps:**
1. **LoadImage**: Load your source image
2. **ImageAnnotator**: Add annotations (points, rectangles, polygons)
3. **SaveImage**: Save the annotated image
4. **ShowText**: Display the JSON annotation data

**To use the example:**
1. Load `example_workflow.json` in ComfyUI
2. Replace `example.png` with your image
3. Add annotations using the interactive canvas
4. Run the workflow to generate annotated output

---

## 🔧 Inputs & Outputs

### Inputs
- **`image`** (Required): The source image to annotate.

### Outputs
- **`image_out`**: Annotated image (IMAGE).
- **`mark_data`**: JSON string (STRING).

---

## 📁 Project Structure

```text
comfyui-image-annotator/
├── __init__.py          # Node registration
├── nodes.py             # Backend implementation
├── requirements.txt     # Dependencies
├── web/
│   └── js/
│       └── image_annotator.js  # Frontend UI
├── LICENSE              # MIT License
└── README.md            # Documentation
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
