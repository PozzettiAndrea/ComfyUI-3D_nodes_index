# 🖼️ Display Image with Mask for ComfyUI

This repository contains a versatile custom node for ComfyUI, `Display Image with Mask`, designed to offer advanced image viewing, masking, and saving capabilities directly within your workflow.

This node acts as a powerful previewer and a utility tool, combining features often found in separate nodes into a single, convenient package.

![image](https://github.com/user-attachments/assets/2681bbab-5bec-44bf-bda2-049151ad9b24)

## Features

- **Flexible Image Sources**: Load the main image and the mask from:
  - Standard ComfyUI `IMAGE` inputs (noodles).
  - Direct URLs (supports `jpg`, `png`, `webp`, `avif`, etc.).
- **Advanced Masking**:
  - **Alpha Channel Masking**: Applies the mask as a transparency channel, not just by blacking out pixels. White in the mask is opaque, black is fully transparent.
  - **Automatic Centering**: If the mask is a different size than the image, it is automatically centered before being applied. No more stretching or distortion!
  - **Color to Grayscale**: Automatically converts color masks to grayscale for correct application.
  - **Invert Mask**: A simple toggle to invert the mask's effect.
- **Enhanced Format Support**:
  - Automatically enables `.avif` support for the entire ComfyUI session, fixing potential loading issues with the native `LoadImage` node.
- **Advanced Saving Options**:
  - **Enable/Disable Saving**: A simple toggle to save the final processed image.
  - **Custom Subdirectory**: Specify a subfolder within your ComfyUI `output` directory.
  - **Custom Filename**: Define a base name for your saved files.
  - **Automatic Timestamping**: Automatically append a `YYYYMMDD-HHMMSS` timestamp to your filename to prevent overwrites and keep your files organized.

## Installation

1.  **Clone the Repository**
    Navigate to your ComfyUI `custom_nodes` directory and clone this repository:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/orion4d/ComfyUI_image-display.git
    ```

2.  **Install Dependencies**
    Navigate into the cloned directory and install the required Python packages using the `requirements.txt` file. Make sure you have activated your ComfyUI's virtual environment (`venv`) first.
    ```bash
    cd YourRepoName/
    pip install -r requirements.txt
    ```

3.  **Restart ComfyUI**
    Start or restart ComfyUI. The `🖼️ Display Image with Mask` node will be available under the `utils/display` category.

## How to Use

1.  Add the `🖼️ Display Image with Mask` node to your workflow.
2.  Provide an input image via the `image` noodle connection or the `image_url` field.
3.  Optionally, provide a mask via the `mask` noodle connection or the `mask_url` field.
4.  Adjust the settings as needed:
    - `invert_mask`: To flip the mask's effect.
    - `save_image`: To enable saving.
    - `save_path`: To set a custom output subfolder (e.g., `my_project/masks`).
    - `filename`: To set a custom base name for the file.
    - `add_datetime`: To toggle the timestamp on the filename.
5.  The node will display a preview of the processed image and pass it along to the next node in your workflow.

<div align="center">

<h3>🌟 <strong>Show Your Support</strong></h3>

<p>If this project helped you, please consider giving it a ⭐ on GitHub!</p>

<p><strong>Made with ❤️ for the ComfyUI community</strong></p>

<p><strong>by Orion4D</strong></p>

<a href="https://ko-fi.com/orion4d">
<img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Buy Me A Coffee" height="41" width="174">
</a>

</div>



