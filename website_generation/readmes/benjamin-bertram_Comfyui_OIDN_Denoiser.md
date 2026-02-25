# ComfyUI OIDN Denoiser

This custom node for ComfyUI provides a wrapper for Intel's Open Image Denoise (OIDN) library, allowing you to denoise images directly within your ComfyUI workflow.

## Installation

1.  Navigate to your `ComfyUI/custom_nodes/` directory.
2.  Clone this repository:
    ```
    git clone https://github.com/your-repo/ComfyUI_OIDN_Denoiser.git
    ```
3.  Install the required dependencies:
    ```
    pip install -r ComfyUI/custom_nodes/ComfyUI_OIDN_Denoiser/requirements.txt
    ```
4.  Restart ComfyUI.

## Node Functionality

The OIDN Denoiser node takes an image as input and outputs a fully denoised image.

### Inputs

*   **image**: The input image (or batch of images) to be denoised.

### Outputs

*   **denoised_image**: The denoised image, with the same shape and type as the input.

## Example Usage

1.  Add the **OIDN Denoiser** node to your workflow (you can find it in the "Image Denoising" category).
2.  Connect an image output from another node to the `image` input of the OIDN Denoiser.
3.  Connect the `denoised_image` output to another node, such as a "Save Image" node.

## Known Issues or Limitations

*   The node currently processes images on the CPU, as the `oidn-python` library primarily supports CPU-based denoising. Performance may vary depending on your system's CPU.
*   Large images may consume a significant amount of memory.