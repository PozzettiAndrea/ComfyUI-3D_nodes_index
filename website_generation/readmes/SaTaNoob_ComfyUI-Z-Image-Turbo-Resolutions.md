# Z Image Turbo Resolutions

A ComfyUI custom node that provides quick access to all image resolutions for the Z Image Turbo model, sourced from its official Hugging Face Space.

## Features

- **Three Resolution Presets**: 1024, 1280, and 1536
- **Dynamic Ratio Selection**: Choose from 11 different aspect ratios for each resolution
- **Common Aspect Ratios**: Including 1:1, 16:9, 9:16, 21:9, 4:3, 3:2, and more
- **Three Integer Outputs**: Resolution, Width, and Height

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Z Image Turbo Resolutions"
3. Click Install
4. Restart ComfyUI

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/SaTaNoob/ComfyUI-Z-Image-Turbo-Resolutions.git
   ```

3. Restart ComfyUI


## Available Resolutions

### 1024 Resolution
- 1024x1024 (1:1)
- 1152x896 (9:7)
- 896x1152 (7:9)
- 1152x864 (4:3)
- 864x1152 (3:4)
- 1248x832 (3:2)
- 832x1248 (2:3)
- 1280x720 (16:9)
- 720x1280 (9:16)
- 1344x576 (21:9)
- 576x1344 (9:21)

### 1280 Resolution
- 1280x1280 (1:1)
- 1440x1120 (9:7)
- 1120x1440 (7:9)
- 1472x1104 (4:3)
- 1104x1472 (3:4)
- 1536x1024 (3:2)
- 1024x1536 (2:3)
- 1536x864 (16:9)
- 864x1536 (9:16)
- 1680x720 (21:9)
- 720x1680 (9:21)

### 1536 Resolution
- 1536x1536 (1:1)
- 1728x1344 (9:7)
- 1344x1728 (7:9)
- 1728x1296 (4:3)
- 1296x1728 (3:4)
- 1872x1248 (3:2)
- 1248x1872 (2:3)
- 2048x1152 (16:9)
- 1152x2048 (9:16)
- 2016x864 (21:9)
- 864x2016 (9:21)


## License

MIT License


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Support

If you encounter any issues or have suggestions, please open an issue on GitHub.


## Changelog

### v1.0.0 (Initial Release)
- Basic resolution and ratio selection
- Dynamic dropdown filtering based on selected resolution
- Three integer outputs (resolution, width, height)
