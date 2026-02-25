# ComfyUI-Flux2proReplicate

A set of custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to generate images using the **Flux 2 Pro** model via the [Replicate API](https://replicate.com/).

## Features

- **Flux 2 Pro Generation**: Access the powerful Flux 2 Pro model directly within ComfyUI.
- **Flexible Aspect Ratios**: Choose from standard aspect ratios (16:9, 1:1, 9:16, etc.) or define custom dimensions.
- **Secure API Key Management**: Loads your Replicate API key from a local file to avoid hardcoding it in workflows.
- **Image Input Support**: Supports up to 10 input images for workflows that require image guidance.
- **Debug Output**: Returns the JSON payload sent to Replicate for easy debugging.

## Installation

1.  **Clone the repository**:
    Navigate to your ComfyUI `custom_nodes` directory and clone this repository:
    ```bash
    cd ComfyUI/custom_nodes
    git clone https://github.com/yourusername/ComfyUI-Flux2proReplicate.git
    ```

2.  **Install dependencies**:
    Install the required Python packages:
    ```bash
    cd ComfyUI-Flux2proReplicate
    pip install -r requirements.txt
    ```

## Configuration

To use these nodes, you need a Replicate API token.

1.  Get your API token from [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens).
2.  Create a file named `replicate_api_key.txt` inside the `ComfyUI-Flux2proReplicate` folder.
3.  Paste your API key into that file (just the key, no extra spaces or newlines).

> **Note**: The `replicate_api_key.txt` file is ignored by git to keep your key secure.

## Nodes

### 1. Flux Replicate Auth (File)
*Category: FluxReplicate*

Reads the API key from the `replicate_api_key.txt` file.

- **Outputs**:
    - `api_key`: The loaded API key string.

### 2. Flux 2 Pro Generator
*Category: FluxReplicate*

The main node for generating images.

- **Inputs**:
    - `api_key`: Connect the output from the **Flux Replicate Auth** node.
    - `prompt`: The text prompt for image generation.
    - `aspect_ratio`: Select from presets (e.g., `1:1`, `16:9`) or choose `custom`.
    - `width` / `height`: Active only when `aspect_ratio` is set to `custom`.
    - `resolution`: Target resolution (e.g., `1 MP`, `4 MP`). Ignored if using custom dimensions.
    - `seed`: Seed for reproducibility.
    - `safety_tolerance`: Adjust safety filter strictness (1-5).
    - `output_quality`: JPEG quality of the output (1-100).
    - `image_1` ... `image_10` (Optional): Input images for image-to-image or structural guidance.

- **Outputs**:
    - `IMAGE`: The generated image tensor.
    - `DEBUG_PAYLOAD`: A string containing the JSON payload sent to the API (useful for debugging).

## Usage Example

1.  Add the **Flux Replicate Auth (File)** node.
2.  Add the **Flux 2 Pro Generator** node.
3.  Connect the `api_key` output of the Auth node to the `api_key` input of the Generator node.
4.  Connect your prompt and configure parameters.
5.  (Optional) Connect input images if needed.
6.  Connect the `IMAGE` output to a **Save Image** or **Preview Image** node.

## License

MIT
