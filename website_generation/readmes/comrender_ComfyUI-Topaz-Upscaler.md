# ComfyUI Topaz Upscaler (API)

A custom node that integrates the **Topaz Labs Image API**. This allows you to use Topaz's industry-leading AI models directly within your ComfyUI workflows.

<img width="425" height="460" alt="image" src="https://github.com/user-attachments/assets/efd30868-5fae-4854-8e56-f783ca77ad5c" />

## Features

* **Full Suite Support:** Access `Enhance`, `Sharpen`, `Denoise`, `Restore`, and `Lighting` modes.
* **Model Selection:** Choose specific models like *Standard V2*, *CGI*, *Lens Blur*, etc.
* **Batch Support:** Automatically processes image batches sequentially.
* **Auto-Scaling:** Use a simple multiplier (e.g., 2.0x, 4.0x) or define specific output resolutions.
* **Secure:** Supports Environment Variables for API keys.

## Installation

1.  Clone this repository into your ComfyUI `custom_nodes` folder:
    ```bash
    cd ComfyUI/custom_nodes
    git clone [https://github.com/yourusername/comfyui-topaz-upscaler.git](https://github.com/yourusername/comfyui-topaz-upscaler.git)
    ```
2.  Install the required Python package:
    ```bash
    pip install requests
    ```
    *(Note: `torch`, `numpy`, and `Pillow` are likely already installed in your ComfyUI environment).*

## Configuration (API Key)

You need a generic API Key from Topaz Labs. You can configure this in two ways:

### Option A: Environment Variable (Recommended)
Set the `TOPAZ_API_KEY` environment variable on your system.
* **Windows (PowerShell):** `$env:TOPAZ_API_KEY="your_key_here"`
* **Linux/Mac:** `export TOPAZ_API_KEY="your_key_here"`

If this is set, you can leave the `api_key` field in the node **empty**.

### Option B: Node Input
Paste your API key directly into the `api_key` widget on the node itself. This overrides the environment variable.

## Usage

1.  Add the node via `Image` -> `Topaz` -> `Topaz Upscaler (API)`.
2.  Connect an image to the input.
3.  Select your **Mode** (e.g., `enhance` for upscaling, `denoise` for cleaning).
4.  Select the **Model** relevant to that mode (e.g., `Standard V2` for enhance).
5.  **Upscaling:**
    * Set `scale_multiplier` > 1.0 (e.g., 2.0) to automatically upscale.
    * Set `scale_multiplier` to 1.0 to manually control `output_width` and `output_height`.
6.  Adjust strengths (`denoise_strength`, `sharpen_strength`) as needed.

## Parameters

| Parameter | Description |
| :--- | :--- |
| **scale_multiplier** | Multiplies input dimensions. Set to 1.0 to disable auto-scaling. |
| **mode** | Operation type (Enhance, Sharpen, Denoise, Restore, Lighting). |
| **model** | Specific AI model to use. Ensure the model matches the mode. |
| **face_enhancement** | Attempts to restore faces in the image (Enhance mode only). |
| **output_format** | Format sent to Topaz and received back (jpeg/png/tiff). |

## Requirements
* ComfyUI
* Internet connection (images are processed on Topaz servers)
* Topaz Labs API Credits
