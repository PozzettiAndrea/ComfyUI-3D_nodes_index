# TK ComfyUI Image to Mask

A dedicated ComfyUI custom node designed to streamline the process of converting transparent images (RGBA) into masks and high-quality mask previews. 

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom--Node-orange.svg)

## 🌟 Overview

Working with transparency in ComfyUI can sometimes be tricky. `TK_Image2Mask` provides a clean, robust way to extract alpha channels and generate mask images that are ready for further processing or visualization. It handles RGBA data natively and offers flexible options for inversion and external mask integration.

## ✨ Features

- **Automatic Alpha Extraction**: Simply plug in an RGBA image, and the node automatically identifies and extracts the transparency layer.
- **Dual Output System**:
  - `MASK`: Standard ComfyUI mask format for use with other nodes.
  - `IMAGE`: A visual RGB image representing the mask (White background with Black mask elements), perfect for inspection or nodes that require IMAGE input.
- **Inversion Support**: Quickly flip your mask logic with a simple `invert_mask` toggle.
- **External Mask Support**: Optionally provide a separate mask to apply the same processing logic.
- **Seamless Integration**: Found under the `TK_Nodes` category.

## 🚀 Installation

1. Open your terminal and navigate to your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/tk_comfyui_img2mask.git
   ```
3. Restart ComfyUI.

## 🛠 Usage

### Node: `Transparent Image to Mask (TK)`

| Input | Type | Description |
|-------|------|-------------|
| `image` | IMAGE | The source image (e.g., from a Load Image node). Supports RGBA. |
| `invert_mask` | BOOLEAN | If `True`, inverts the resulting mask. |
| `mask` (Optional) | MASK | An optional existing mask to be processed. |

| Output | Type | Description |
|--------|------|-------------|
| `mask` | MASK | The processed alpha channel as a mask. |
| `mask_image` | IMAGE | An RGB image representation of the mask (White = Background, Black = Masked Area). |

## 📂 Example Workflows

We have included example workflows to help you get started quickly. You can find them in the `workflow` directory:
- `workflow/i2m_workflow.json`: A standard setup demonstrating how to extract and visualize masks from transparent PNGs.

To use them, simply drag and drop the JSON file into your ComfyUI interface.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
