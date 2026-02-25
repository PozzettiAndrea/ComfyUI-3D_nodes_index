# ComfyUI-Equirect

ComfyUI nodes for conversion between equirectangular panoramas and cubemaps.

## Features

- **EquirectToCubemapNode**: Convert equirectangular panoramas to 6 cubemap faces
- **CubemapToEquirectNode**: Convert 6 cubemap faces back to equirectangular panoramas

## Installation

1. Clone this repository to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/yourusername/ComfyUI-Equirect.git
   ```

2. Install dependencies:
   ```bash
   cd ComfyUI-Equirect
   pip install -r requirements.txt
   ```

## Usage

### EquirectToCubemapNode (Equirectangular to Cubemap)

Inputs:
- `equirect_image`: Equirectangular panorama input (2:1 aspect ratio)
- `face_size`: Size of the output cubemap faces
- `fov`: Field of view angle (default: 90 degrees)

Outputs:
- `front`, `right`, `back`, `left`, `top`, `bottom`: 6 cubemap faces

### CubemapToEquirectNode (Cubemap to Equirectangular)

Inputs:
- `front`, `right`, `back`, `left`, `top`, `bottom`: 6 cubemap faces
- `output_height`: Height of the output equirectangular image (width will be automatically set to twice the height)

Outputs:
- `equirect_image`: Converted equirectangular panorama

## Technical Notes

- Uses `py360convert` library for high-quality conversion when available
- Automatically falls back to custom implementation if the library is not available
- Supports batch processing and maintains correct image formats

## Dependencies

- torch
- numpy
- pillow
- opencv-python
- py360convert

## Parameters

- **Input Image**: Equirectangular panorama image with 2:1 aspect ratio
- **Face Size**: Edge length for each cubemap face (default: 512, range: 64-4096)
- **Field of View**: FOV angle for each face (default: 90, range: 60-120)

## System Requirements

- ComfyUI
- Python 3.7+
- PyTorch
- Pillow (PIL)
- NumPy

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details 