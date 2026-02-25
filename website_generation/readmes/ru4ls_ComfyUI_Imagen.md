# ComfyUI_Imagen

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Built with Gemini](https://img.shields.io/badge/Built_with-Gemini-blue.svg)](https://deepmind.google/technologies/gemini/)

A custom node for ComfyUI that leverages the Google Cloud Vertex AI Imagen API to generate and edit images.

## Installation

1.  Clone this repository into your `custom_nodes` folder.
    ```bash
    cd ComfyUI/custom_nodes
    git clone https://github.com/ru4ls/ComfyUI_Imagen.git
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r ComfyUI_Imagen/requirements.txt
    ```

## Project Setup

To use this node, you need a Google Cloud Project with the Vertex AI API enabled.

1.  **Enable the Vertex AI API:** Follow the instructions in the [Google Cloud documentation](https://cloud.google.com/vertex-ai/docs/start/cloud-environment) to enable the API for your project.

2.  **Authenticate Your Environment:** This node uses Application Default Credentials (ADC) to securely authenticate with Google Cloud. Run the following `gcloud` command in your terminal to log in and set up your credentials. This is a one-time setup.
    ```bash
    gcloud auth application-default login
    ```
    The node authenticates directly through the installed Python libraries and does **not** depend on the `gcloud.cmd` executable being available in your system's PATH at runtime.

3.  **Create a `.env` file:** In the `ComfyUI_Imagen/config/` directory, create a `.env` file by copying the `config/.env.example` file. Replace the placeholder values with your Google Cloud project ID and desired location.
    ```
    # ComfyUI_Imagen/config/.env

    PROJECT_ID="YOUR_PROJECT_ID_HERE"
    LOCATION="YOUR_LOCATION_HERE"
    ```

## Nodes

This package provides a single unified node, **Google Imagen**, which can perform both text-to-image generation and image editing depending on the inputs provided.

### Inputs

*   `prompt` (STRING): The text prompt for image generation or manipulation.
*   `model_name` (STRING): The generation model to use. The list is populated from `data/models.json`.
*   `image` (IMAGE, optional): An optional input for a base image. **Connecting an image switches the node to image-editing mode.**
*   `mask` (MASK, optional): An optional mask for inpainting or outpainting. If no mask is provided in editing mode, the node will perform a mask-free, prompt-based image edit.
*   `aspect_ratio` (STRING, optional): The desired aspect ratio for **text-to-image generation**.
*   `edit_mode` (STRING, optional): The editing mode to use when an image is provided. Options are `inpainting` and `outpainting`.
*   `seed` (INT, optional): A seed for reproducibility. See the **Seed and Watermarking** section below for important usage details.
*   `add_watermark` (BOOLEAN, optional): A toggle to control watermarking and `seed` behavior.

### Outputs

*   `image` (IMAGE): The generated or edited image.

## Features and Limitations

### Seed and Watermarking

The Google Imagen API does not support using a `seed` when the automatic watermark feature is enabled.

*   **For Text-to-Image:** To use a `seed`, you must set the `add_watermark` toggle to **`False`**. When `add_watermark` is `True` (the default), the `seed` value is ignored.
*   **For Image Editing:** The API does not support disabling watermarks. However, to maintain consistent behavior, the `add_watermark` toggle still controls the `seed`. Set it to **`False`** to use a `seed` for your edits.

### Image Editing

The node supports both masked and mask-free image editing.
*   **With a Mask:** Provide an `image` and a `mask` to perform standard inpainting or outpainting.
*   **Without a Mask:** Provide only an `image` and a `prompt`. The node will perform a mask-free, prompt-guided edit of the entire image.

## Example Usage

### Text to Image Generation

1.  Add the `Google Imagen` node to your workflow.
2.  Enter a `prompt`.
3.  Ensure no `image` input is connected.
4.  To use a seed, set `add_watermark` to `False`.
5.  Connect the output `image` to a `PreviewImage` or `SaveImage` node.

![Text to Image Generation Example](media/ComfyUI_Imagen-t2i-new.png)


### Inpainting

1.  Add the `Google Imagen` node.
2.  Connect a `LoadImage` node to the `image` input.
3.  Optional Create a mask and connect it to the `mask` input.
4.  Enter a `prompt` describing the desired changes.
5.  Set `edit_mode` to `inpainting`.
6.  Connect the output `image` to a `PreviewImage` or `SaveImage` node.

![Image Inpainting Generation Example](media/ComfyUI_Imagen-i2i-inpainting-new.png)


### Outpainting

This workflow is identical to inpainting, but with `edit_mode` set to `outpainting` and a mask that defines the area to be extended.


## Changelog

### 2025-09-14: Refactored Authentication and Node Logic

*   **New Authentication:** Replaced insecure `gcloud` subprocess calls with the official `google-auth` Python library, using Application Default Credentials (ADC). This improves security and removes the dependency on the `gcloud` executable being in the system's PATH.
*   **Unified Node:** Consolidated the workflow into a single, powerful `Google Imagen` node that intelligently switches between text-to-image and image-editing modes based on whether an image is provided.
*   **Watermark & Seed Control:** Added an `add_watermark` toggle. Disabling this allows the `seed` parameter to be used for reproducible results.
*   **Enhanced Image Editing:** The node now supports both masked (inpainting/outpainting) and mask-free, prompt-guided image editing.
*   **Centralized Configuration:** The `.env` file is now loaded from the `/config` directory, and credential loading is handled centrally for a cleaner and more robust startup.
*   **Improved Error Handling:** Implemented error handling that prevents the ComfyUI workflow from crashing on API or configuration errors, instead printing clear messages to the console.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
