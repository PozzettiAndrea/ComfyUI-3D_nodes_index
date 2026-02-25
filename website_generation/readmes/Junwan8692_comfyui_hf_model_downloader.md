# HF Model Downloader for ComfyUI

A simple custom node to download models from Hugging Face URLs directly into your ComfyUI model folders.

## Installation

### Recommended: Using ComfyUI Manager
1.  Open the **ComfyUI Manager**.
2.  Click on **Install Custom Nodes**.
3.  Search for `HF Model Downloader` and click **Install**.
4.  Restart ComfyUI.

### Manual Install
1.  Download this repository as a ZIP file.
2.  Unzip the file.
3.  Copy the `comfyui_hf_model_downloader` folder into your `ComfyUI/custom_nodes/` directory.
4.  Restart ComfyUI.

## Features

* **Direct Download:** Paste a Hugging Face model link to download it right into ComfyUI.
* **Auto-Sorting:** Choose a category (checkpoints, loras, vae, etc.) and the node will save the file in the correct folder.
* **Easy to Use:** No more downloading and moving files manually.

## How to Use

1.  Add the **HF Model Downloader** node to your workflow.
2.  Copy a model's download link from Hugging Face and paste it into the `model_url` box.
3.  Select the correct `model_category` from the dropdown menu.
4.  **Connect the `model_path` output to a `Show Text` node.** This will show you the final path where the file is saved.
5.  **Queue your prompt.** The model will be downloaded and ready for your next workflow!