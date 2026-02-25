# ComfyUI DAM Object Extractor

A custom ComfyUI node that uses NVIDIA's Description and Masking (DAM) model to identify and describe objects in masked regions of images. This tool allows you to extract the name or detailed description of any object highlighted by a mask.

## Features

- **Object Name Extraction**: Identify objects within masked regions with a single word
- **Full Description Mode**: Generate detailed descriptions of masked areas
- **Mask Visualization**: Add contours to visualize the detected regions
- **Flexible Mask Handling**: Works with masks from Load Image node, SAM, and other segmentation tools
- **Configurable Parameters**: Adjust temperature, token length, and threshold for optimal results

## Installation

### Prerequisites

- ComfyUI installed and running
- Python environment with the following packages:
  - transformers
  - torch
  - numpy
  - Pillow (PIL)
  - opencv-python (for visualization)

### Installation Steps

1. Clone this repository or download it to your ComfyUI custom nodes directory:
```
cd YOUR_COMFYUI_PATH/custom_nodes/
git clone https://github.com/Irsalistic/comfyui-dam-object-extractor.git
```

2. Restart ComfyUI to load the new nodes

## Nodes Included

### 1. DAM Object Name Extractor

Extracts the name or description of objects in a masked region.

**Inputs**:
- **image**: The input image
- **mask**: The mask highlighting the region to describe
- **temperature**: Controls randomness (0.1 recommended for consistent results)
- **max_tokens**: Maximum number of tokens in the response
- **invert_mask**: Option to invert the mask if needed
- **threshold**: Sensitivity for detecting mask content (default: 0.01)
- **prompt_mode**: Choose between "name_only" or "full_description"

**Output**:
- **STRING**: The extracted name or description

### 2. DAM Mask Visualizer

Adds contour lines to visualize the masked region.

**Inputs**:
- **image**: The input image
- **mask**: The mask to visualize
- **contour_thickness**: Thickness of the contour line
- **contour_color**: Color of the contour (white, red, green, blue, yellow)
- **threshold**: Sensitivity for detecting mask content

**Output**:
- **IMAGE**: The image with contours added

## Example Workflow

1. Add a **Load Image** node to load your image and mask
2. Connect the image and mask outputs to the **DAM Object Name Extractor** node
3. Connect the STRING output to a text display node (like "Show Text" from ComfyUI-Custom-Scripts)
4. Optionally, connect the image and mask to the **DAM Mask Visualizer** node

## Usage Tips

- **First run**: The first time you use the node, it will download the DAM model (about 6GB)
- **Mask detection**: If the mask isn't being detected:
  - Try setting "invert_mask" to "True"
  - Lower the "threshold" value (default is 0.01)
  - Check that your mask has visible white areas
- **Best results**: For best results, use clear masks with well-defined boundaries
- **Processing time**: Initial processing might take 10-15 seconds as the model loads

## Troubleshooting

- **"Mask is empty" error**: Decrease the threshold value or check that your mask has white pixels
- **Dimension errors**: The node should handle various mask formats, but if you encounter issues, check the console for detailed error messages
- **Model loading errors**: Ensure you have enough disk space and a stable internet connection for the initial model download

## How It Works

The node uses NVIDIA's DAM model to understand and describe masked regions in images. The process involves:

1. Loading and preprocessing the input image and mask
2. Converting tensors to the format required by the DAM model
3. Generating a description or name using a specialized prompt
4. Processing the output to extract just the object name if in "name_only" mode

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NVIDIA for the powerful DAM model
- The ComfyUI team for creating an excellent framework
- The Hugging Face Transformers library

## Connect and Contribute

Feel free to open issues or contribute to this project. Any feedback or improvements are welcome!