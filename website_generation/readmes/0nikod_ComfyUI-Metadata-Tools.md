# ComfyUI Metadata Tools

[English](README.md) | [简体中文](README_ZH.md)

A set of custom nodes for ComfyUI designed to handle image metadata efficiently. This extension allows you to extract, modify, and save metadata directly within your workflows.

## Features

- **Metadata Extraction**: Load images and output their metadata (info dictionary) as a JSON string.
- **Custom Metadata Saving**: Save images with custom metadata or metadata passed from other nodes.
- **Tensor-bound Metadata**: Metadata "travels" with the image tensor throughout the workflow using a hidden attribute.
- **Internationalization**: Support for both English and Chinese UI.

## Node Descriptions

### 1. Load Image (Metadata)
Loads an image and outputs:
- **IMAGE**: The image tensor.
- **MASK**: The alpha channel (if present).
- **metadata**: The metadata found in the image file as a JSON string.

### 2. Save Image (Metadata)
Saves an image and allows adding custom metadata:
- **images**: The image(s) to save.
- **metadata_text**: (Optional) JSON string or plain text to be saved as metadata. If empty, it looks for metadata attached to the image tensor.
- **filename_prefix**: The prefix for the saved file path.

### 3. Set Image Metadata
Attaches a metadata string to an image tensor. This metadata will be used by the "Save Image (Metadata)" node if no explicit text is provided.

### 4. Get Image Metadata
Retrieves the metadata string previously attached to an image tensor.

## Installation

1.  **ComfyUI-Manager (Recommended)**:
    Search for "Metadata Tools" in the ComfyUI-Manager and click install.
2.  **Manual Installation**:
    ```bash
    cd ComfyUI/custom_nodes
    git clone https://github.com/dniko0/ComfyUI-Metadata-Tools
    cd ComfyUI-Metadata-Tools
    pip install -r requirements.txt
    ```

## License

MIT
