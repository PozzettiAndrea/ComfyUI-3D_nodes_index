## ComfyUI-S4Tool-Text · v1.0.0

Text rendering and styling nodes for ComfyUI. This extension provides a basic text renderer, multiple font loaders, and a style node that adds stroke, shadow, gradient fill, and opacity control. All nodes are grouped under the category "💀S4Tool" inside ComfyUI.

### Highlights
- Horizontal and vertical typesetting, alignment, character spacing, and line spacing
- Multiple font sources: bundled file selector, Base64 string, and remote URL
- Style processing: scalable stroke (OpenCV SDF when available), drop shadow, gradient fill, and global alpha
- Outputs standard ComfyUI image tensors and masks

## Requirements
- ComfyUI installed and running
- Python 3.10+ (match your ComfyUI environment)
- Dependencies:

```powershell
# Required
pip install pillow numpy requests

# Optional (recommended for best stroke quality in the Style node)
pip install opencv-python
```

Notes:
- PyTorch is provided by ComfyUI; you typically do not need to install it manually for this extension.

## Installation
1. Place this folder at `ComfyUI/custom_nodes/ComfyUI-S4Tool-Text`.
2. Start or restart ComfyUI.
3. Nodes appear under the "💀S4Tool" category.

## Nodes Overview

### S4Tools Text Basic (`py/textBasic.py`)
Renders text into an RGBA image, and also exposes the rendered RGBA as "style" plus a grayscale mask.

- Inputs:
  - **font** (`FONT_DATA`): Font bytes (from one of the font loader nodes)
  - **text** (`STRING`, multiline): Text content
  - **font_size** (`INT`, 1–512, default 32)
  - **color** (`STRING`, hex, default `#000000`)
  - **text_direction** (`horizontal` | `vertical`, default `horizontal`)
  - **align** (`left` | `center` | `right`, default `left`)
  - **char_spacing** (`INT`, -50–200, default 0)
  - **line_spacing** (`FLOAT`, -10.0–10.0, step 0.1, default 1.0)
- Outputs:
  - **image** (`IMAGE`): Tensor of the colored RGBA text on transparent background
  - **style** (`STYLE_DATA`): The same RGBA image, convenient for downstream styling
  - **mask** (`MASK`): Grayscale alpha mask of the text

Behavior notes:
- Horizontal mode: `line_spacing` controls the gap between lines (as a multiple of font size).
- Vertical mode: columns flow left-to-right; `line_spacing` controls the horizontal gap between columns.

### S4Tools Text Style (`py/textStyle.py`)
Applies stroke, outer shadow, gradient fill, and global alpha to an incoming style image.

- Inputs:
  - **style** (`STYLE_DATA`): RGBA style image (e.g., from Basic node output `style`)
  - **stroke_size** (`INT`, 0–100, default 0)
  - **stroke_color** (`STRING`, hex, default `#000000`)
  - **outer_shadow_x** (`INT`, -100–100, default 0)
  - **outer_shadow_y** (`INT`, -100–100, default 0)
  - **outer_shadow_color** (`STRING`, hex, default `#000000`)
  - **outer_shadow_blur** (`FLOAT`, 0.0–20.0, step 0.1, default 2.0)
  - **gradient_start** (`STRING`, hex, default `#FFFFFF`)
  - **gradient_end** (`STRING`, hex, default `#00FF00`)
  - **gradient_angle** (`FLOAT`, 0.0–360.0, default 0.0)
  - **alpha** (`FLOAT`, 0.0–1.0, step 0.01, default 1.0)
- Outputs:
  - **IMAGE**: Styled RGBA image tensor
  - **MASK**: Final alpha mask

Quality notes:
- If `opencv-python` is available, the node uses an SDF-like approach for smoother, scalable strokes. Otherwise, it falls back to a PIL-based stroke.

### S4Tools Text Font file (`py/textFontFile.py`)
Loads font bytes from the bundled `font/` directory.

- Inputs:
  - **font_name** (enum): Populated from filenames in `font/` (extension hidden). Supports `.ttf` and `.otf`.
- Outputs:
  - **font** (`FONT_DATA`): Font bytes for downstream nodes

Notes:
- To add more fonts, copy `.ttf` or `.otf` files into the `font/` folder. The selector lists names without extensions.

### S4Tools Text Font Base64 (`py/textFontBase64.py`)
Decodes Base64-encoded font data (optionally accepts a `data:*;base64,` prefix).

- Inputs:
  - **font_base64** (`STRING`, multiline)
- Outputs:
  - **font** (`FONT_DATA`)

Errors:
- Invalid input raises "Invalid base64 font data".

### S4Tools Text Font URL (`py/textFontURL.py`)
Downloads a font file from a URL.

- Inputs:
  - **font_url** (`STRING`)
- Outputs:
  - **font** (`FONT_DATA`)

Dependencies:
- Requires `requests` at runtime.

Errors:
- Empty or failing downloads raise messages like "Unable to download font: ...".

## Typical Workflow
1. Choose a font source:
   - `S4Tools Text Font file` for bundled fonts in `font/`
   - `S4Tools Text Font Base64` to paste Base64 font data
   - `S4Tools Text Font URL` to fetch a remote font
2. Connect the `font` output to `S4Tools Text Basic` → configure text, sizing, spacing, and direction.
3. Optionally connect the `style` output into `S4Tools Text Style` for stroke, shadow, and gradient.
4. View or save the resulting `IMAGE` in ComfyUI.

## Bundled Fonts
This repository ships multiple English and Simplified Chinese fonts inside the `font/` directory. You can add or remove fonts by placing `.ttf`/`.otf` files there. The `S4Tools Text Font file` node will list them automatically by filename (without extension).

## Error Handling Summary
- Base64 loader: raises on invalid Base64 content
- File loader: raises if the selected font file cannot be found
- URL loader: raises on network or HTTP errors

## Changelog
- 1.0.0: Initial public release of the text nodes (Basic, Style, Font file, Font Base64, Font URL)


