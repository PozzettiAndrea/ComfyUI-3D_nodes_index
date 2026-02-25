# ComfyUI Smart Scaler

A powerful ComfyUI custom node package for intelligent image scaling, aspect ratio adjustments, metadata extraction, resolution customization, and video frame processing. Built to streamline image and video preprocessing workflows, especially for **vid2vid** and **img2vid** tasks using **Wan 2.1** with **Pony** or **SDXL** models where perfect sizes are critical.

## Overview

The `comfyui-smart-scaler` package provides custom nodes to enhance image and video processing in ComfyUI, focusing on perfect frame sizes for workflows like vid2vid and img2vid using Wan 2.1 with Pony or SDXL models:

- **Smart Aspect Scaler**: Scales images to SDXL and Wan resolutions (Small, Medium, Large options for Wan).
- **Size Parser**: Converts size strings (e.g., "1024x1536") into width/height integers.
- **Aspect Ratio Adjuster**: Adjusts image aspect ratio to a target (e.g., 16:9).
- **Image Metadata Extractor**: Extracts metadata like dimensions and aspect ratio.
- **Dynamic Resolution Selector**: Allows custom resolution inputs for SDXL and Wan.
- **Wan Video Frame Scaler**: Optimizes frames for Wan 2.1 vid2vid/img2vid (e.g., 720p, 480p).
- **Batch Frame Processor**: Ensures consistent scaling across video frames for Wan 2.1 vid2vid.

Nodes are under `SmartScaler` and `SmartScaler/Video` in the ComfyUI node menu.

## Installation

### Via ComfyUI Manager (Recommended)

- Open ComfyUI Manager in your ComfyUI interface.
- Search for `comfyui-smart-scaler`.
- Click **Install**.
- Restart ComfyUI.

### Manual Installation

- Navigate to your ComfyUI `custom_nodes` directory: cd path/to/ComfyUI/custom_nodes
- Clone the repository: git clone https://github.com/babydjac/comfyui-smart-scaler.git
- Install dependencies: pip install torch Pillow numpy
- Restart ComfyUI: cd ../.. python main.py

### Requirements

- **Python**: 3.12 (recommended)
- **ComfyUI**: Latest as of May 15, 2025
- **Dependencies**: `torch`, `Pillow`, `numpy`

## Usage

### Node Overview

#### Smart Aspect Scaler
- **Purpose**: Scales images to SDXL/Wan resolutions for vid2vid/img2vid.
- **Inputs**:
- `image`: Input image.
- `target_models`: `SDXL`, `Wan`, or `Both`.
- `wan_size`: `Small` (512x768), `Medium` (768x1152), `Large` (1024x1536).
- `fit_strategy`: `resize` (default), `pad`, or `crop`.
- `force_multiple_64`: Boolean (default: True).
- **Outputs**:
- `sdxl_image`, `wan_image`: Scaled images.
- `original_width`, `original_height`: Original dimensions.
- `scaled_sdxl_size`, `scaled_wan_size`: Scaled dimensions (e.g., "1024x1536").

#### Size Parser
- **Purpose**: Parses size strings into width/height integers.
- **Inputs**:
- `sdxl_size`: Scaled SDXL size string (connection-only).
- `wan_size`: Scaled Wan size string (connection-only).
- **Outputs**:
- `sdxl_width`, `sdxl_height`: SDXL dimensions as integers.
- `wan_width`, `wan_height`: Wan dimensions as integers.

#### Aspect Ratio Adjuster
- **Purpose**: Adjusts image aspect ratio to a target.
- **Inputs**:
- `image`: Input image.
- `target_ratio`: `16:9`, `4:3`, `1:1`, or `Custom`.
- `custom_ratio_width`, `custom_ratio_height`: Custom ratio values (if `Custom` selected).
- `method`: `crop` or `pad`.
- **Outputs**:
- `adjusted_image`: Image with adjusted aspect ratio.
- `new_ratio`: New ratio as a string (e.g., "16:9").

#### Image Metadata Extractor
- **Purpose**: Extracts metadata for debugging or conditional workflows.
- **Inputs**:
- `image`: Input image.
- **Outputs**:
- `width`, `height`: Image dimensions as integers.
- `aspect_ratio`: Width/height ratio as a float.
- `dimensions`: Dimensions as a string (e.g., "1024x1536").

#### Dynamic Resolution Selector
- **Purpose**: Allows custom resolution inputs for SDXL and Wan.
- **Inputs**:
- `sdxl_width`, `sdxl_height`: Custom SDXL resolution (integers, step 64).
- `wan_width`, `wan_height`: Custom Wan resolution (integers, step 64).
- `force_multiple_64`: Boolean to enforce multiples of 64.
- **Outputs**:
- `sdxl_resolution`, `wan_resolution`: Resolution strings (e.g., "1280x720").

#### Wan Video Frame Scaler (For Vid2Vid/Img2Vid with Wan 2.1)
- **Purpose**: Optimizes frame sizes for Wan 2.1 vid2vid and img2vid workflows when using Pony or SDXL models, ensuring perfect sizes (e.g., 720p, 480p).
- **Inputs**:
- `image`: Input image.
- `wan_resolution`: `720p` (1280x720), `480p` (854x480), or `Custom`.
- `custom_width`, `custom_height`: Custom resolution if `Custom` selected.
- `fit_strategy`: `resize` (default), `pad`, or `crop`.
- `force_multiple_64`: Boolean to ensure dimensions are multiples of 64.
- **Outputs**:
- `scaled_image`: Image scaled to Wan 2.1 resolution.
- `scaled_size`: Scaled dimensions as a string (e.g., "1280x720").

#### Batch Frame Processor (For Vid2Vid with Wan 2.1)
- **Purpose**: Ensures consistent scaling across a batch of frames for Wan 2.1 vid2vid workflows.
- **Inputs**:
- `images`: Batch of images (e.g., video frames, ComfyUI `IMAGE` type).
- `target_resolution`: `SDXL`, `Wan-Small`, `Wan-Medium`, `Wan-Large`.
- `fit_strategy`: `resize` (default), `pad`, or `crop`.
- `force_multiple_64`: Boolean to ensure dimensions are multiples of 64.
- **Outputs**:
- `scaled_images`: Batch of scaled images.
- `scaled_size`: Scaled dimensions as a string (e.g., "512x768").

### Example Workflow for Vid2Vid/Img2Vid with Wan 2.1

- **Load Frames**:
Use a `LoadImageBatch` node to load video frames (e.g., 1000x2000 frames, aspect 1:2).
- **Extract Metadata (Optional)**:
Add `Image Metadata Extractor`.
Connect the first frame to `image`.
**Output**: `width` (1000), `height` (2000), `aspect_ratio` (0.5).
- **Scale Frames for Wan 2.1**:
Add `Wan Video Frame Scaler`.
Connect a single frame (for img2vid) to `image`.
Set `wan_resolution` to `720p` (1280x720, optimal for Wan 2.1).
**Output**: `scaled_image` (1280x720), `scaled_size` ("1280x720").
For vid2vid, add `Batch Frame Processor`.
Connect the frame batch to `images`.
Set `target_resolution` to `Wan-Medium` (768x1152).
**Output**: `scaled_images` (all frames at 768x1152), `scaled_size` ("768x1152").
- **Parse Sizes**:
Add `Size Parser`.
Connect `scaled_size` from `Wan Video Frame Scaler` to `wan_size`.
**Output**: `wan_width` (1280), `wan_height` (720).
- **Proceed with Wan 2.1**:
Use the scaled images in your Wan 2.1 vid2vid or img2vid workflow.

## Contributing

Contributions are welcome! To contribute:

- Fork the repository.
- Create a new branch (`git checkout -b feature/your-feature`).
- Make your changes and commit (`git commit -m "Add your feature"`).
- Push to your branch (`git push origin feature/your-feature`).
- Open a Pull Request on GitHub.

Please ensure your code follows Python PEP 8 style guidelines and includes appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For issues, feature requests, or questions:

- Open an issue on the [GitHub repository](https://github.com/babydjac/comfyui-smart-scaler/issues).
- Join the ComfyUI community on Discord (#help or #feedback channels) or Matrix (#comfyui_space:matrix.org).

## Acknowledgments

- Built with inspiration from the ComfyUI community and Suzie’s [ComfyUI_Guide_To_Making_Custom_Nodes](https://github.com/Suzie1/ComfyUI_Guide_To_Making_Custom_Nodes).
- Thanks to the ComfyUI team for creating an amazing platform for visual AI workflows.