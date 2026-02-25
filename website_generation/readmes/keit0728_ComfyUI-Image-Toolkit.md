# ComfyUI-Image-Toolkit

**Custom Node Pack for ComfyUI**

This node pack provides convenient tools for image processing and transformation.

## Features

This pack includes the following nodes:

### BrightnessTransparency

Adjusts transparency based on brightness. Bright areas become transparent, while dark areas remain opaque.

### AlphaToGrayscale

Converts alpha channel (transparency) to grayscale values. Functions as the inverse transformation of BrightnessTransparency, restoring brightness information that was expressed as transparency back to grayscale images.

### AlphaFlatten

Flattens images with alpha channels by compositing them against a white background. Transparent areas are composited with white background and output as RGB images without transparency.

### BinarizeImage

Binarizes images. Areas brighter than the specified threshold become white (1.0), while darker areas become black (0.0).

### BinarizeImageUsingOtsu

Automatically binarizes images using Otsu's binarization algorithm. Automatically calculates the optimal threshold and separates light and dark areas in the image.

### RemoveWhiteBackgroundNoise

Removes noise mixed in white backgrounds. Performs binarization with the specified threshold and replaces white background areas with pure white to remove noise.

### GrayscaleImage

Converts color images to grayscale. Processes RGB values uniformly to generate grayscale images.

### AntialiasingImage

Applies antialiasing effects to images. Smooths edges by first upscaling the image and then returning it to the original size.

## Installation

### Recommended Method

- Install using [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager).

### Manual Installation

1. Navigate to the `ComfyUI/custom_nodes` directory.
2. Clone the repository with the following command:
   ```
   git clone https://github.com/your-username/ComfyUI-Image-Toolkit
   cd ComfyUI-Image-Toolkit
   ```

## Usage

1. Launch ComfyUI.
2. Look for the "ComfyUI-Image-Toolkit" category in the node browser.
3. Add the required nodes to your workflow and use them.

## License

GPL-3.0 license
