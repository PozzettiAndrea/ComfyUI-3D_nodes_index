# ComfyUI LoRA adaLN Patcher Node

A simple but powerful custom node for ComfyUI that patches LoRA models by adding dummy `adaLN_modulation_1` weights. This solves compatibility errors when using LoRAs with newer model architectures that expect these keys to be present in the `final_layer`.

## 🚀 The Problem It Solves

Some modern U-Net architectures and updated ComfyUI workflows require weights for an **Adaptive Layer Normalization** (`adaLN`) module in the final block of the U-Net. However, some LoRAs were trained on architectures that did not have this module.

When you try to load such a LoRA, you might encounter a `KeyError` because the loader cannot find expected keys like:
- `lora_unet_final_layer_adaLN_modulation_1.lora_down.weight`
- `lora_unet_final_layer_adaLN_modulation_1.lora_up.weight`

This node fixes the issue by adding zero-filled "dummy" weights for these missing keys, making the LoRA compatible without altering its artistic output.

## ✨ Features

- **Automated Patching**: Detects and patches LoRAs that have `final_layer.linear` weights but are missing the corresponding `adaLN` weights.
- **Safe & Non-Destructive**: Creates a new, patched file (e.g., `my_lora_patched.safetensors`) and leaves the original file untouched.
- **Smart Detection**: Intelligently skips files that are already patched or do not require patching.
- **Easy Integration**: Works as a standard ComfyUI node, fitting seamlessly into your workflow.

## 📦 Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/Franklyc/comfyui-lora-adain-patcher-node.git
    ```
3.  Restart ComfyUI. The node will be available under the `loaders/patchers` category.

## 🛠️ How to Use

1.  In ComfyUI, add the node by right-clicking and selecting: `Add Node` > `loaders/patchers` > `Patch LoRA (adaLN)`.
2.  From the `lora_name` dropdown, select the LoRA file you want to patch.
3.  Click **Queue Prompt** to run the patching process.

#### **Outputs**

-   **`patched_lora_name`**: The filename of the newly created (or existing) patched LoRA.
-   **`patch_status`**: A message indicating the result (e.g., "Success!", "Skipped", "No patch needed"). You can connect this to a `Show Text` node to see the status.

**Important**: After a LoRA is successfully patched, you must **Refresh** your ComfyUI browser page (or click the Refresh button in the UI) for the new `_patched.safetensors` file to appear in other LoRA loader dropdowns.

## 📜 Technical Details

The node loads the state dictionary of the selected LoRA and checks for the existence of weights under common prefixes for the final layer (`lora_unet_final_layer`, `final_layer`, etc.). If it finds linear projection weights (`...linear.lora_...`) but not the corresponding adaptive layer norm weights (`...adaLN_modulation_1...`), it creates zero-tensors with the correct shapes and adds them to the state dictionary before saving it as a new file.

Because the added weights are all zeros, they have no mathematical effect on the LoRA's output, serving only to satisfy the model loader's key requirements.

## 🙏 Acknowledgements

This tool is an implementation of a hotfix script, adapted for easy use within the ComfyUI ecosystem.
based on: https://github.com/tazztone/patch_comfyui_nunchaku_lora

---

Feel free to open an issue or submit a pull request if you have suggestions for improvement!
