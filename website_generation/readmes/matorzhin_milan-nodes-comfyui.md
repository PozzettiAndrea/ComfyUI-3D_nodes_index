# Milan Nodes for ComfyUI

This set of custom nodes for ComfyUI enhances image handling capabilities by adding loading with metadata extraction.

## Nodes

### 1. Load Image with Name, Title, Description

This node functions similarly to the standard `Load Image` node in ComfyUI, displaying a preview of the loaded image, but additionally provides the following information:

*   **Outputs:**
    *   `IMAGE`: The loaded image.
    *   `STRING` (File Name): The filename of the image.
    *   `STRING` (Title): The title of the image (if available).
    *   `STRING` (Description): The description of the image (if available).


### 2. Load Multiple Images with Name, Directory, Title, Description

This node sequentially loads images from the specified folder (the quantity is entered by the user to the right of the `▶️ Queue` button).

*   **Inputs:**
    *   `DIRECTORY_PATH`: Path to the folder containing images.

*   **Outputs (for each image):**
    *   `IMAGE`: The currently loaded image.
    *   `STRING` (File Name): The filename of the current image.
    *   `STRING` (Directory): The path to the directory from which the image was loaded.
    *   `STRING` (Title): The title of the current image (if available).
    *   `STRING` (Description): The description of the current image (if available).

*   **Features:**
    *   Images are loaded sequentially with each processing queue run.
    *   *More details about the batch loading mechanism and quantity control can be found [here](https://t.me/milandsgn/194) (in Russian)*


## Installation

1.  **Via ComfyUI Manager:**
    *   Search for "milan-nodes-comfyui" in ComfyUI Manager and install.
2.  **Manually:**
    *   Clone this repository into your `ComfyUI/custom_nodes/` folder:
    *   Restart ComfyUI.


## Feedback and Support

If you have any questions or suggestions, you can contact me [here](https://t.me/milandsgn)


## Acknowledgements

Inspired by and grateful to WASasquatch for [was-node-suite-comfyui](https://github.com/WASasquatch/was-node-suite-comfyui).

---
