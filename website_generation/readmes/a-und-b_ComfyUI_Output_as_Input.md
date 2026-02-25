> [!NOTE]
> There is now a native ComfyUI node called **"Load Image (from Outputs)"** available.  
> I recommend using it instead. As a result, this repository is no longer under development.

---

# ComfyUI_Output_as_Input

This is a simple custom ComfyUI node that allows you to easily use recent output images as input in your workflows. It does not allow image uploads on purpose and does not require any additional dependencies.

## Manual Installation

1. Download the `output_as_input_node.py` file.
2. Move the file to the `custom_nodes` folder in your ComfyUI directory.
3. Restart ComfyUI.

As soon as this node is published in the official ComfyUI registry, it will be available for installation via the ComfyUI extension manager.

## Usage

1. Add the `OutputAsInput` node to your ComfyUI workflow.
2. Connect the `OutputAsInput` node to the node that generates the image you want to use as input.
3. Connect the `OutputAsInput` node to the node that will use the image as input.
