# ComfyUI-SmartImageTools

A collection of smart image processing tools for ComfyUI, focused on advanced image manipulation techniques.

## Nodes

### SmartImagePaletteConvert

Converts an image to use an indexed color palette with optional dithering. Similar to Photoshop's indexed color conversion functionality.

#### Features:
- Generate an optimal color palette from the input image using K-means clustering in LAB color space
- Specify the number of colors in the palette (2-256)
- Apply Floyd-Steinberg dithering with adjustable intensity
- Use a reference image to extract a palette (optional)
- Preserves transparency

#### Inputs:
- **image**: The input image to process
- **num_colors**: Number of colors in the palette (2-256)
- **dithering_amount**: Amount of dithering to apply (0.0-1.0)
- **reference_image** (optional): An image to extract the color palette from

#### Outputs:
- **IMAGE**: The processed image with the indexed color palette applied

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/ComfyUI-SmartImageTools.git
```

2. Install the required dependencies:
```
pip install -r ComfyUI-SmartImageTools/requirements.txt
```

3. Restart ComfyUI

## Requirements

- scikit-learn
- scikit-image
- numpy
- Pillow

## License

MIT 