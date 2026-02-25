# ComfyUI Clothing Color Correction Node

A custom node for ComfyUI that performs color correction on clothing in face-swapped images. This node helps maintain the original clothing color when using face swap tools, addressing common color shifts that occur during the face swap process.

## Features

- **Multiple Color Correction Methods**: Choose from statistical, histogram, or LAB color space transfers
- **Fine Control**: Adjust the strength and threshold of the color correction
- **Preserve Luminosity**: Option to maintain the original brightness while correcting colors
- **Masked Processing**: Only applies corrections to specified clothing regions

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ComfyUI_ClothingColorCorrection
   ```

3. Install requirements:
   ```bash
   pip install -r ComfyUI_ClothingColorCorrection/requirements.txt
   ```

4. Restart ComfyUI

## Usage

The node requires the following inputs:

- **Original Image**: The original clothing image 
- **Clothing Mask**: A mask of the clothing area in the original image
- **Output Image**: The face-swapped output image
- **Output Mask**: A mask of the clothing area in the output image
- **Color Threshold**: Determines when color correction is applied (0.01-1.0)
- **Strength**: How strong the color correction should be (0.0-1.0)
- **Preserve Luminosity**: Whether to maintain original brightness
- **Method**: Color transfer technique to use

## Example Workflow

1. Load your original clothing image and face-swapped result
2. Create masks for the clothing areas in both images (using segmentation or manual masking)
3. Connect all inputs to the Color Correction node
4. Adjust parameters as needed

## Advanced Options

### Color Correction Methods

- **Statistical**: Uses mean and standard deviation to transfer color characteristics
- **Histogram**: Matches color distributions using histogram equalization
- **LAB Transfer**: Works in LAB color space for more perceptually accurate corrections

## Acknowledgements

This node was created to solve color shifts that commonly occur during face swapping, particularly when the original and swapped faces have different skin tones or when lighting conditions change.

## License

MIT 