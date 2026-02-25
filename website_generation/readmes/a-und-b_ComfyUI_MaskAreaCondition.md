# ComfyUI Mask Area Condition

A simple custom node for ComfyUI that analyzes the size (area) of a mask relative to the total image area. Its primary purpose is to enable **conditional workflows**, allowing you to run  face detailing only when needed based on the size of the detected face.

## Why Measure Mask Size?

Image generation models often struggle with rendering small details, especially faces. While nodes like [Face Detailer](https://github.com/ltdrdata/ComfyUI-Impact-Pack) (part of the popular Impact Pack) or [ADetailer (After Detailer)](https://github.com/Bing-su/adetailer) can fix this using inpainting, running them unconditionally adds significant processing time, even if the face is already large and well-rendered.

While it's possible to achieve similar conditional logic by combining existing nodes (e.g., getting mask properties and using math/comparison nodes), this dedicated `MaskAreaCondition` node provides a streamlined, single-node solution specifically for this common optimization task, keeping your workflow cleaner and easier to manage.

This node helps **optimize** such workflows by checking the mask size first.

## Features

*   **`Mask Area Condition` node:**
    *   Calculates the percentage of the mask area compared to the total tensor area.
    *   Outputs a boolean (`is_below_threshold`) indicating if the mask percentage is less than the provided threshold.
    *   Outputs the calculated mask size percentage (`mask_area_percent`).
    *   Passes the original mask through (`mask_passthrough`) for easy chaining.
    *   Special handling for empty masks: automatically returns `False` for `is_below_threshold` to skip processing when nothing is detected.

*   **`Select Data based on Condition`**
    *   Helper Node for Conditional Workflows.
    *   Takes two data inputs (`data_if_true`, `data_if_false`) of any type and a boolean `condition`. 
    *   Outputs either `data_if_true` or `data_if_false` based on the condition. This is useful for dynamically selecting workflow parameters or routing data based on the mask area condition.

## Installation

### Via ComfyUI Manager (Recommended)

1. Ensure you have [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) installed
2. Open ComfyUI and click the "Manager" button
3. Navigate to "Install Custom Nodes" tab
4. Search for "Mask Area Condition"
5. Click "Install"
6. Restart ComfyUI and reload the browser tab

### Manual Installation

1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/a-und-b/ComfyUI_MaskAreaCondition.git
   ```
3. Restart ComfyUI

## Nodes Included

This package includes two nodes that work together to create conditional workflows:

### Mask Area Condition

Analyzes a mask to determine its relative size and provides outputs to control conditional logic.

### Select Data

A general-purpose node that selects between two inputs based on a boolean condition. This works with any data type (images, latents, masks, etc.).

## Basic Usage

1. Add the "Mask Area Condition" node to your workflow
   * Find it under "mask" → "conditional"
2. Connect a `MASK` output from another node (e.g., SAM detector, mask primitive, etc.) to the `mask` input
   * Common sources include face/object detection nodes or segmentation models
3. Set the desired `threshold_percent` value (0-100)
   * This defines the cutoff: if mask area percentage is *less than* this threshold, `is_below_threshold` will be `True`
   * Note: For empty masks (nothing detected), `is_below_threshold` will always be `False`
4. Add the "Select Data based on Condition" node to your workflow
5. Connect:
   * `is_below_threshold` from Mask Area Condition to `condition` on Select Data
   * Two processing paths to `data_if_true` and `data_if_false` on Select Data

## Example Use Cases

* **Optimize Face Detailing**: Automatically skip computationally expensive face detailing (like Face Detailer or After Detailer) if the detected face mask is already large enough.
* **Conditional Image Processing**: Apply different effects or processing steps based on the size of a masked object.
* **Workflow Routing**: Direct the workflow down different paths depending on whether a detected object meets a size criterion.
* **Quality Control**: Filter out or handle masks differently if they are too small or too large for subsequent reliable processing.

## Changelog

### v1.1.1
- Added console logging for easier debugging and workflow monitoring
- Console logs show threshold values, mask area calculations, and decision outcomes

### v1.1.0
- Removed Gate nodes (GateImageForConditional and GateMaskForConditional) in favor of using the more versatile SelectData node
- Changed empty mask behavior to return False for is_below_threshold (skips processing when nothing is detected)
- Improved documentation and code comments

### v1.0.0
- Initial release with MaskAreaCondition and supporting nodes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

* [Georg Neumann](https://www.linkedin.com/in/georg-neumann) from [KI Marketing Bootcamp](https://marketing-ki.de) for the initial code and concept
* The [ComfyUI](https://github.com/comfyanonymous/ComfyUI) team and contributors for creating an amazing platform
* The vibrant [ComfyUI community](https://registry.comfy.org) and all the custom node creators who continue to push the boundaries of what's possible
* [Claude by Anthropic](https://www.anthropic.com/claude) for assistance in code refactoring, optimization, and documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created with ❤️ for the ComfyUI community.