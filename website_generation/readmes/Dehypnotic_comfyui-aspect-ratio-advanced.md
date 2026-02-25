# AspectRatioAdvanced - ComfyUI Node

An advanced aspect ratio calculator and image scaler for ComfyUI with flexible scaling modes and intelligent image handling.

<img width="430" height="567" alt="image" src="https://github.com/user-attachments/assets/d9da9e45-93a8-424f-8cb3-4a290b08fa90" />

## Features

📐 **Flexible Scaling**
- **Aspect Ratio**: Choose an aspect ratio to be calculated from target megapixels, min/max side, or input image.
- **Custom dimensions**: Scale to custom width and height
- **Target Megapixels**: Scale to achieve a specific resolution
- **Min Side**: Set shortest dimension, maintain aspect ratio  
- **Max Side**: Set longest dimension, maintain aspect ratio
- **12 preset aspect ratios**: square, portrait, landscape, and social media formats

🖼️ **Intelligent Image Processing**
- Optional image input automatically detects aspect ratio when `use_image_ratio` is set to `Yes`.
- Real-time image scaling to calculated dimensions

⚡ **Advanced Controls**
- Dimension flipping (portrait ↔ landscape)
- Batch processing support
- 8-divisible dimensions (latent space compatible)

## Installation

### 1. Via ComfyUI Manager

1. Open ComfyUI Manager → Custom Nodes
2. Search for **Aspect Ratio Advanced**.
3. Press **Install** and restart ComfyUI.

### 2. Manually by clone or copy.

1. Navigate to your ComfyUI custom nodes directory:
   ```bashcd
   cd ComfyUI/custom_nodes/
   ```
2. Clone or copy this repository:
   ```bashcd
   git clone https://github.com/Dehypnotic/comfyui-aspect-ratio-advanced.git
   ```
3. Restart ComfyUI

## Usage

### Basic Aspect Ratio Calculation

1. Select desired `aspect_ratio` preset
2. Choose `scaling_mode` (target megapixels, min or max side)
3. Adjust the corresponding value

### With Image Input

1. Connect an image node to the optional `image` input
2. Set `use_image_ratio` to **Yes** to use the image's aspect ratio
3. Set `use_image_ratio` to **No** to scale image to selected preset as describe above
4. Optional image outputs will be scaled

### Custom Dimensions

1. Select `scaling_mode: custom dimensions`
2. Set `custom_width` and `custom_height` to desired values
3. Connected image outputs will be scaled to these exact dimensions

<img width="694" height="649" alt="image" src="https://github.com/user-attachments/assets/45ba58cd-6b4e-4a9c-ab32-6783c86e211b" />

## Node Inputs

| Input | Type | Description |
|-------|------|-------------|
| `custom_width` | INT | Width when using custom aspect ratio |
| `custom_height` | INT | Height when using custom aspect ratio |
| `scaling` | COMBO | How to scale dimensions (megapixels/min/max side/aspect ratios) |
| `use_image_ratio` | COMBO | Use connected image's ratio (Yes/No) |
| `target_megapixels` | FLOAT | Target resolution in megapixels |
| `min_side` | INT | Shortest dimension in pixels |
| `max_side` | INT | Longest dimension in pixels |
| `flip_dimensions` | COMBO | Swap width/height (No/Yes) |
| `batch_count` | INT | Number of latent batches to generate |
| `image` | IMAGE | Optional: Image to analyze/scale |

## Node Outputs

| Output | Type | Description |
|--------|------|-------------|
| `width` | INT | Calculated width |
| `height` | INT | Calculated height |  
| `batch_count` | INT | Batch count passthrough |
| `empty_latent` | LATENT | Empty latent tensor |
| `scaled_image` | IMAGE | Scaled input image (if provided) |
| `resolution_info` | STRING | Human-readable resolution summary |

## Supported Aspect Ratios

- **1:1 square** - Perfect square format
- **4:3 standard** - Classic monitor/photo ratio
- **3:2 classic** - 35mm film ratio
- **16:9 widescreen** - Modern video/monitor standard
- **21:9 ultrawide** - Cinematic widescreen
- **3:4 portrait** - Vertical standard format
- **2:3 photo** - Vertical photo ratio
- **9:16 mobile** - Vertical video (TikTok, Instagram Stories)
- **9:21 vertical** - Extended vertical format
- **4:5 social** - Instagram post format
- **5:7 print** - Standard print ratio

## Technical Notes

- All output dimensions are automatically rounded to multiples of 8 (required for latent space)
- Minimum dimension is 64 pixels
- Uses bilinear interpolation for high-quality image scaling
- Compatible with all ComfyUI image processing workflows

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Changelog

### v0.2.0
- Scaling methods added

### v0.1.0
- Initial release
- Support for 12 aspect ratio presets
- Three scaling modes (megapixels, min/max side)
- Optional image input with intelligent ratio detection
- Real-time image scaling output

---

**Created for the ComfyUI community** 💙





