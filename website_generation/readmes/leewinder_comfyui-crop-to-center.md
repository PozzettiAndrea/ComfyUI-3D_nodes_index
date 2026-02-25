# Crop To Center

A custom node for ComfyUI that crops images to specified dimensions from a center point with optional offset, removing equal amounts from all sides.

&nbsp;
## Installation

There are two ways to install this custom node:

### ComfyUI Manager (Recommended)

1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) if you don't have it yet.
2. Go to `Manager` > `Install Custom Nodes`.
3. Search for `Crop To Center` and click `Install`.
4. Restart ComfyUI.

### Manual

1. Navigate to your `ComfyUI/custom_nodes/` directory.
2. Clone the repository: `git clone https://github.com/leewinder/comfyui-crop-to-center.git`.
3. Restart ComfyUI.

&nbsp;
## Usage

The `Crop To Center` node takes an input image and crops it to specified dimensions from the center of the image, with the option to offset the center point to move the crop region around the image. 

It removes equal amounts from all sides around the center point, while staying true to the request image dimensions.

<img width="1024" height="1024" alt="Crop Overview" src="https://github.com/user-attachments/assets/0f928ef7-4180-4b3f-a30b-1aecc0408831" />

The center offset can move to the edges of the image, but the crop process will prioritise the image dimensions requested, while staying as close to the center point as possible, ensuring your image is always the correct size.

<img width="2074" height="1024" alt="Crop Edges" src="https://github.com/user-attachments/assets/079c6353-6472-495b-a5b4-721d593d623a" />



### Parameters

<img width="298" height="190" alt="params" src="https://github.com/user-attachments/assets/fbf3091f-f5f2-477c-a1d8-28234e6696c9" />

- **image**: Input image to be cropped
- **target_width**: Target width for the cropped image (must be less than or equal to source width)
- **target_height**: Target height for the cropped image (must be less than or equal to source height)
- **center_offset_x**: Horizontal offset from the true center (positive = right, negative = left)
- **center_offset_y**: Vertical offset from the true center (positive = up, negative = down)

### Outputs

- **cropped_image**: The cropped image with the specified dimensions


&nbsp;
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request of if you have any ideas of bugs, please [raise an issue](https://github.com/leewinder/comfyui-crop-to-center/issues).

### Contribution Workflow
1. Fork this repository
2. Make your changes
3. Test your changes
4. Run quality checks
5. Create a Pull Request

### Development Setup

#### Prerequisites

- python 3.9+
- pytest 8.4+
- pylint 3.0+

#### Setting Up Your Development Environment

1. Install pyenv:
```bash
# macOS
brew install pyenv

# Or follow the official installation guide:
# https://github.com/pyenv/pyenv#installation
```

2. Clone the repository:
```bash
git clone git@github.com:leewinder/comfyui-crop-to-center.git
cd comfyui-crop-to-center
```

3. Set up Python environment:
```bash
# Create the virtual environment
pyenv local 3.11.10
python -m venv venv
source venv/bin/activate
```

4. Install dependencies:
```bash
# Install the project and development dependencies
pip install -e ".[dev]"
```

#### Running Tests
```bash
# Run all tests
pytest test/test_crop.py -v
```

#### Code Quality
```bash
# Run pylint for code quality checks
pylint src/
pylint test/
```

&nbsp;
## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International](LICENSE) license.

&nbsp;
## Contributors

- [@leewinder](https://github.com/leewinder)
