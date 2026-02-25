# ComfyUI-musubi

This repository provides a custom node for ComfyUI to load diffusion models with musubi block-wise scaling.

## 🌟 Features

*   **`MusubiUNETLoader` Node**: A custom UNET loader based on the original `UNETLoader`.
*   **Musubi Support**: Enables the loading of diffusion models that utilize musubi block-wise scaling.
*   **Seamless Integration**: Behaves identically to the native `UNETLoader` for a familiar user experience.

## 👨🏻‍🔧 Installation

1.  Navigate to your ComfyUI `custom_nodes` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/polym/ComfyUI-musubi.git
    ```
3.  Restart ComfyUI.

## 🚀 Usage

1.  **Download the model**: Download the musubi block-wise scaled diffusion model from [huggingface](https://huggingface.co/polym/COMFY_MODELS) and place it in your `ComfyUI/models/diffusion_models` directory.
2.  **Load the model**: After installation, you can find the `MusubiUNETLoader` node in the "musubi" category. Use it in the same way you would use the standard `UNETLoader` to load your musubi block-wise scaled models.

## 🎨 Examples

Drag and drop the image into ComfyUI to reproduce the workflow.

![Musubi LoRA Example](example_workflows/musubi-lora-example-02.png)

## 🙏 Credits

*   The original `UNETLoader` from [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
*   The concept of musubi block-wise scaling.