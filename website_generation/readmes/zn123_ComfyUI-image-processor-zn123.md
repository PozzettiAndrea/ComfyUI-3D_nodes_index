# ComfyUI Image Processor Nodes

A comprehensive image processing plugin for ComfyUI that provides various image manipulation and enhancement capabilities.

## 🚀 Features

### Basic Operations
- **Image Upscale**: Scale images with multiple interpolation methods
- **Image Resize**: Resize images to exact dimensions
- **Image Rotate**: Rotate images by specified angles
- **Image Flip**: Horizontal and vertical image flipping
- **Image Crop**: Crop images to specific regions

### Image Enhancement
- **Adjust Brightness**: Modify image brightness levels
- **Adjust Contrast**: Adjust image contrast
- **Image Blur**: Apply Gaussian blur
- **Image Sharpen**: Sharpen image details
- **Image Grayscale**: Convert images to grayscale

### Smart Scaling
- **Scale By Short Side**: Maintain aspect ratio while scaling based on short edge
- **Scale By Long Side**: Maintain aspect ratio while scaling based on long edge

## 📦 Installation

1. Navigate to your ComfyUI `custom_nodes` directory
2. Clone or copy this repository:
   ```bash
   git clone https://github.com/zn123/ComfyUI-image-processor-zn123
   ```
3. Restart ComfyUI
4. The nodes will appear in the `image/processor` category

## 🔧 Usage

### Basic Image Operations

#### Image Upscale
Scales images using various interpolation methods:
- **Methods**: Nearest, Bilinear, Bicubic, Area, Lanczos
- **Scale Factor**: Multiplier for image dimensions
- **Crop**: Optional cropping to maintain aspect ratio

#### Image Resize
Resizes images to exact dimensions:
- **Width**: Target width in pixels
- **Height**: Target height in pixels
- **Method**: Interpolation method for resizing

#### Image Flip
Flips images horizontally and/or vertically:
- **Horizontal**: Flip left-right (default: True)
- **Vertical**: Flip top-bottom

### Smart Scaling

#### Scale By Short Side
Maintains aspect ratio while scaling based on the shorter edge:
- **Short Side Target**: Target length for the shorter edge
- **Upscale Method**: Interpolation method
- **Only Upscale**: Skip processing if image is already large enough

#### Scale By Long Side
Maintains aspect ratio while scaling based on the longer edge:
- **Long Side Target**: Target length for the longer edge
- **Upscale Method**: Interpolation method
- **Only Upscale**: Skip processing if image is already large enough

### Image Enhancement

#### Brightness & Contrast
Adjust image brightness and contrast levels:
- **Brightness**: Range (-1.0 to 1.0, 0 = no change)
- **Contrast**: Range (-1.0 to 1.0, 0 = no change)

#### Blur & Sharpen
Apply blur or sharpen effects:
- **Blur Radius**: Gaussian blur radius (0.1 to 10.0)
- **Sharpen Amount**: Sharpening intensity (0.0 to 2.0)

## 🎯 Workflows

### Basic Image Preprocessing
1. Load image with `LoadImage` node
2. Use `Scale By Short Side` to normalize image size
3. Apply `Adjust Brightness` and `Adjust Contrast` for exposure correction
4. Use `Image Sharpen` to enhance details
5. Output to other processing nodes

### Smart Resizing Workflow
1. Input image from any source
2. Use `Scale By Short Side` with `only_upscale=True` to ensure minimum size
3. Use `Image Crop` to remove unwanted areas
4. Apply enhancement nodes as needed

## 📊 Node Reference

| Node Name | Input | Output | Description |
|-----------|-------|--------|-------------|
| ImageUpscale | IMAGE, scale_by, method, crop | IMAGE | Scale image by factor |
| ImageResize | IMAGE, width, height, method | IMAGE | Resize to exact dimensions |
| ImageRotate | IMAGE, angle, method | IMAGE | Rotate by degrees |
| ImageFlip | IMAGE, flip_horizontal, flip_vertical | IMAGE | Flip image |
| ImageCrop | IMAGE, x, y, width, height | IMAGE | Crop to region |
| ImageAdjustBrightness | IMAGE, brightness | IMAGE | Adjust brightness |
| ImageAdjustContrast | IMAGE, contrast | IMAGE | Adjust contrast |
| ImageBlur | IMAGE, radius | IMAGE | Apply Gaussian blur |
| ImageSharpen | IMAGE, amount | IMAGE | Sharpen image |
| ImageGrayscale | IMAGE | IMAGE | Convert to grayscale |
| Scale By Short Side | IMAGE, target, method, only_upscale | IMAGE, width, height | Scale by short edge |
| Scale By Long Side | IMAGE, target, method, only_upscale | IMAGE, width, height | Scale by long edge |

## 🛠️ Technical Details

### Data Types
- **Input**: ComfyUI `IMAGE` tensor format (BHWC)
- **Output**: Same format with processed data
- **Batch Processing**: All nodes support batch processing

### Interpolation Methods
- **Nearest**: Fastest, lowest quality
- **Bilinear**: Good balance of speed and quality
- **Bicubic**: Higher quality, moderate speed
- **Area**: Best for downscaling
- **Lanczos**: Highest quality, slowest

### Performance Notes
- Smart scaling nodes skip processing when dimensions match target
- Batch processing is optimized for multiple images
- Memory usage scales with image dimensions

## 🐛 Troubleshooting

### Common Issues
1. **Node not appearing**: Check that ComfyUI was restarted after installation
2. **Memory errors**: Reduce image dimensions or batch size
3. **Quality issues**: Try different interpolation methods

### Performance Tips
- Use `only_upscale=True` to skip unnecessary processing
- Choose interpolation methods based on your quality/speed needs
- Batch process multiple images when possible

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- ComfyUI community for the framework
- Contributors and testers
- Open source image processing libraries

## 📞 Support

- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Use GitHub Discussions for questions
- **Community**: Join the ComfyUI Discord server

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Compatibility**: ComfyUI v0.3.15+