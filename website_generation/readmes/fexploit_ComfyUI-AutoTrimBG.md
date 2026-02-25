# ComfyUI-AutoCropBgTrim

ComfyUI-AutoCropBgTrim is a powerful tool designed to automatically clean up the background of your images. This tool trims unnecessary spaces and pixels, leaving only the main subject of the image. It generates both a mask and an image output, making it easy to focus on the essential elements. Perfect for enhancing your photos and preparing them for professional use.

![Demo](demo.png)

## Features
- Automatically trims backgrounds.
- Leaves only the main subject.
- Generates a mask and an image output.
- Adjustable padding for cropping.

## Installation

To install ComfyUI-AutoCropBgTrim, clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/ComfyUI-AutoCropBgTrim.git
cd ComfyUI-AutoCropBgTrim
pip install -r requirements.txt
```
## Usage
Here is an example of how to use ComfyUI-AutoCropBgTrim in your project:


```python
import torch
from PIL import Image
from ComfyUI-AutoCropBgTrim import RonLayersTrimBgUltraV2

# Load your image and mask
image = torch.load('path/to/image.pt')
mask = torch.load('path/to/mask.pt')

# Initialize the class
cropper = RonLayersTrimBgUltraV2()

# Set the padding (optional)
padding = 10

# Run the cropping function
cropped_image, cropped_mask, crop_box, box_preview = cropper.run(image, mask, padding)

# Save or process the results
cropped_image.save('path/to/cropped_image.png')
cropped_mask.save('path/to/cropped_mask.png')
box_preview.save('path/to/box_preview.png')
```
## Class and Methods

The main class provided by ComfyUI-AutoCropBgTrim is `RonLayersTrimBgUltraV2`. Below are the main methods and their descriptions:

### `RonLayersTrimBgUltraV2`

- `__init__`: Initializes the class with default values for input and output images, masks, and cropping boxes.
- `INPUT_TYPES`: Defines the input types for the class methods, including the image, mask, and padding.
- `trim_and_crop_by_mask(image, mask, padding)`: Trims and crops the image based on the mask, with optional padding.
- `run(image, mask, padding)`: Runs the `trim_and_crop_by_mask` method and stores the results.

## Contributing

If you want to contribute to ComfyUI-AutoCropBgTrim, please fork the repository and create a pull request with your changes.

## License

ComfyUI-AutoCropBgTrim is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or feedback, please open an issue on GitHub or contact the repository owner.

Enjoy using ComfyUI-AutoCropBgTrim for your image processing needs!
