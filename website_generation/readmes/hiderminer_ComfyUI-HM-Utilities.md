# ComfyUI-HM-Utilities

A collection of custom nodes for ComfyUI that provides useful image processing tools.

## Nodes

### AutoCropImage

The AutoCropImage node automatically crops images to remove transparent areas by finding the minimum bounding box around non-transparent pixels.

#### Functionality

- **Input**: IMAGE (supports batch processing)
- **Output**: IMAGE (batch of cropped images)

#### Specifications

The node performs the following operations on input images:

1. **Alpha Channel Analysis**: For each image in the batch, analyzes the alpha channel (transparency) values
   - For RGBA images: Uses the alpha channel (4th channel) to detect transparent pixels
   - For RGB images: Treats all pixels as fully opaque (alpha = 1.0)

2. **Bounding Box Calculation**: Finds the minimum bounding box that contains all non-transparent pixels (alpha > 0)
   - Calculates the minimum and maximum X and Y coordinates of non-transparent pixels
   - Each image in the batch gets its own individual bounding box

3. **Image Cropping**: Crops each image to its calculated bounding box dimensions
   - Creates a new image with the same dimensions as the bounding box
   - Preserves the original image data within the cropped area

4. **Output**: Returns a batch tensor of cropped images, where all images are padded to the same dimensions (the maximum dimensions among all cropped images)

#### Usage

1. Connect an image source to the `image` input pin
2. The node will automatically process all images in the batch
3. Connect the `image` output pin to any node that accepts IMAGE input (e.g., PreviewImage, SaveImage)

#### Features

- **Batch Processing**: Handles multiple images simultaneously with individual processing for each image
- **Alpha Channel Support**: Works with both RGBA and RGB images
- **Automatic Sizing**: Each output image is automatically sized to its optimal dimensions
- **Transparency Handling**: Properly handles transparent and semi-transparent pixels

#### Category

`image/processing`

### NormalizeImageWithRectangle ⚠️ **Development Status**

**This node is currently under development and testing. Features and behavior may change in future versions.**

The NormalizeImageWithRectangle node resizes images to fit within a specified rectangular area while preserving aspect ratio and adding transparent padding when necessary.

#### Functionality

- **Input**: IMAGE (supports batch processing)
- **Parameters**: 
  - `width`: Target width (1-8192, default: 512)
  - `height`: Target height (1-8192, default: 512)
- **Output**: IMAGE (normalized images with exact target dimensions)

#### Specifications

The node performs the following operations on input images:

1. **Aspect Ratio Preservation**: Calculates the optimal scaling factor to fit the image within the target rectangle while maintaining the original aspect ratio

2. **Resize Operation**: Resizes the image using bilinear interpolation to the calculated dimensions

3. **Padding with Transparency**: Adds transparent padding around the resized image to achieve the exact target dimensions
   - For RGB input images: Converts to RGBA and adds transparent padding (alpha = 0)
   - For RGBA input images: Preserves existing alpha channel and uses transparent padding

4. **Centering**: Centers the resized image within the target rectangle

#### Usage

1. Connect an image source to the `image` input pin
2. Set the desired `width` and `height` parameters
3. Connect the `image` output pin to any node that accepts IMAGE input

#### Features

- **Letterboxing/Pillarboxing**: Automatically adds transparent bars when aspect ratios don't match
- **Batch Processing**: Handles multiple images simultaneously
- **Alpha Channel Handling**: Properly manages transparency for both RGB and RGBA inputs
- **Precise Dimensions**: Output images always match the specified width and height exactly

#### Category

`image/processing`

(c) hiderminer, 2025.

