# ComfyUI-Q_Image_Crop_Calculator

A ComfyUI custom node for intelligent cropping optimization, specifically designed for maximizing texture quality in Hunyuan 3D 2.0 workflows. This node automatically calculates the optimal crop area based on mask data to eliminate wasted space and ensure maximum detail utilization within the 518x518 input constraint.

## Features

- Automatically calculates optimal crop dimensions based on mask data from background removal
- Maximizes space utilization for Hunyuan 3D 2.0's 518x518 input requirement
- Eliminates wasted transparent/empty space around objects
- Ensures better model accuracy and texture detail by using every available pixel
- Configurable padding, step size, and minimum dimensions
- Returns precise crop coordinates for seamless integration with image processing workflows
- Square crop output optimized for 3D model generation

## Installation

1. Clone this repository into your ComfyUI's `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ComfyUI-Q_Image_Crop_Calculator.git
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```
or install manually:
```bash
pip install numpy>=1.24.0 pillow>=10.0.0
```

**Note**: This node requires PyTorch, but since Hunyuan 3D 2.0 workflows require CUDA-enabled PyTorch, you should install PyTorch with CUDA support separately according to your system's CUDA version. Visit [PyTorch's official installation guide](https://pytorch.org/get-started/locally/) for CUDA-specific installation instructions.

3. Restart ComfyUI

## Dependencies

This module requires the following Python libraries:
- **torch**: For tensor operations and ComfyUI compatibility (install CUDA version separately - see installation notes)
- **numpy**: For efficient array processing and mask analysis (>=1.24.0)
- **pillow**: For image processing operations (>=10.0.0)

A `requirements.txt` file is included for easy installation of numpy and pillow dependencies.

## Usage with Hunyuan 3D 2.0

This node is specifically designed to work in Hunyuan 3D 2.0 workflows where input image quality directly impacts model accuracy:

### Q Image Crop Calculator

The node provides intelligent crop calculation with the following parameters:

- **mask**: Input mask from background removal (typically from InstantlyRemoveBackground or similar nodes)
- **step_size**: Alignment step for crop dimensions (default: 32, range: 8-128)
- **padding**: Additional space around detected object (default: 64, range: 0-256)
- **min_size**: Minimum crop dimensions (default: 256, range: 128-1024)

**Returns:**
- **width**: Calculated optimal crop width
- **height**: Calculated optimal crop height  
- **x_offset**: Horizontal position for crop start
- **y_offset**: Vertical position for crop start

## Hunyuan 3D 2.0 Workflow Integration

### Maximizing 518x518 Input Quality

Hunyuan 3D 2.0 (non-mini, non-turbo version) accepts 518x518 pixel images. Every pixel matters for model accuracy:

1. **Background Removal**: Use InstantlyRemoveBackground or similar node to isolate your subject
2. **Mask Analysis**: Connect the mask output to Q Image Crop Calculator
3. **Optimal Cropping**: The node calculates the tightest possible crop that contains your subject
4. **Space Maximization**: Eliminates wasted transparent areas, ensuring maximum detail density
5. **3D Generation**: Feed the optimally cropped image to Hunyuan 3D 2.0 for superior results

### Workflow Connection Pattern

```
[Original Image] → [Background Remover] → [Mask Output] → [Q Image Crop Calculator]
                                      ↓
[Cropped Image] ← [Image Crop] ← [Crop Coordinates]
                        ↓
[Resize to 518x518] → [Hunyuan 3D 2.0]
```

### Benefits for 3D Model Generation

- **Higher Detail Density**: More pixels dedicated to the actual subject
- **Better Texture Resolution**: Fine details are preserved at higher resolution
- **Improved Model Accuracy**: Hunyuan 3D 2.0 has more detail to work with
- **Reduced Artifacts**: Less empty space means fewer generation artifacts
- **Consistent Results**: Automated cropping ensures reproducible workflows

## Technical Details

### Intelligent Crop Calculation

The node analyzes the input mask to:

1. **Detect Object Boundaries**: Finds the minimal bounding box containing all non-transparent pixels
2. **Apply Smart Padding**: Adds configurable padding while respecting image boundaries
3. **Ensure Square Output**: Creates square crops ideal for 3D model generation
4. **Optimize Dimensions**: Rounds to specified step sizes for consistent processing
5. **Handle Edge Cases**: Gracefully handles empty masks or oversized objects

### Performance Optimizations

- Efficient numpy-based mask analysis
- Minimal memory footprint
- Fast coordinate calculation
- Compatible with ComfyUI's tensor format

## Example Use Cases

### Portrait to 3D Model
- Remove background from portrait photo
- Calculate optimal crop to focus on subject
- Maximize facial detail in 518x518 constraint
- Generate high-quality 3D head model

### Product Photography
- Isolate product from background
- Eliminate wasted space around product
- Ensure maximum product detail in final 3D model
- Ideal for e-commerce 3D model generation

### Character Design
- Crop character artwork optimally
- Preserve important design elements
- Maximize character detail for 3D conversion
- Perfect for game asset generation

## License

[MIT License](LICENSE)