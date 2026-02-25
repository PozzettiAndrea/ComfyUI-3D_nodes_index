# Segment Any Bedroom Interior

## Description
**Segment Any Bedroom Interior** is a Python-based project designed to segment furniture and objects within a bedroom image. The segmentation process uses RGB codes to accurately differentiate between various pieces of furniture, providing a precise mask output for each segmented object. This project is integrated with **ComfyUI** to allow easy and intuitive usage.

## Installation

To install and use this project:

1. Clone the repository into your ComfyUI project directory:
   ```bash
   git clone https://github.com/your-repository-link
   ```
2. Ensure that you have all the necessary dependencies for **ComfyUI** and any other relevant tools.

## Usage

Once the project is installed, follow these steps to segment bedroom interiors:

1. Upload an image of a bedroom via the ComfyUI interface.
2. The node will process the image and generate segmentation masks for every piece of furniture detected in the image.
3. The output will be a mask indicating the segmented areas of the furniture.

### Example
1. Upload an image of a bedroom.
2. The system processes and segments the image based on RGB codes.
3. Output: A mask file with clearly delineated furniture areas.

## Input

- **Image**: Any image format supported by ComfyUI (JPEG, PNG, etc.)

## Output

- **Mask**: A segmentation mask indicating each segmented piece of furniture.

## Technologies and Tools Used

- **ComfyUI**: For user interface integration.
- **Python**: For backend processing and segmentation logic.

