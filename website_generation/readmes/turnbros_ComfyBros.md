# ComfyBros - Custom ComfyUI Nodes

A collection of custom nodes for ComfyUI that enhance text and image processing capabilities.

## Installation

1. Clone or download this repository to your ComfyUI custom nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   git clone <your-repo-url> ComfyBros
   ```

2. Install dependencies:
   ```
   cd ComfyBros
   pip install -r requirements.txt
   ```

3. Restart ComfyUI

## Nodes Included

### Text Processing Nodes

#### Text Processor
- **Category**: ComfyBros/Text
- **Function**: Apply various text transformations
- **Inputs**:
  - `text`: Input text (multiline string)
  - `operation`: Transformation type (uppercase, lowercase, title, capitalize, remove_spaces, remove_numbers)
- **Outputs**: Processed text

#### Text Combiner
- **Category**: ComfyBros/Text  
- **Function**: Combine two text inputs with a separator
- **Inputs**:
  - `text1`: First text input
  - `text2`: Second text input
  - `separator`: Text to insert between inputs (default: space)
- **Outputs**: Combined text

### Image Processing Nodes

#### Image Resize
- **Category**: ComfyBros/Image
- **Function**: Resize images with various interpolation methods
- **Inputs**:
  - `image`: Input image
  - `width`: Target width (64-2048, step 8)
  - `height`: Target height (64-2048, step 8)
  - `interpolation`: Method (nearest, linear, bilinear, bicubic)
- **Outputs**: Resized image

#### Image Blend
- **Category**: ComfyBros/Image
- **Function**: Blend two images using different blend modes
- **Inputs**:
  - `image1`: Base image
  - `image2`: Overlay image (auto-resized to match image1)
  - `blend_factor`: Blend strength (0.0-1.0)
  - `blend_mode`: Blending method (normal, multiply, screen, overlay)
- **Outputs**: Blended image

## Usage

After installation, you'll find the ComfyBros nodes in the node menu under their respective categories:
- ComfyBros/Text
- ComfyBros/Image

Simply add them to your workflow like any other ComfyUI node.

## Development

To add new nodes:
1. Create your node class in the appropriate file under `nodes/`
2. Add the node to `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS` in `nodes/__init__.py`
3. Follow ComfyUI node conventions for INPUT_TYPES, RETURN_TYPES, and FUNCTION definitions