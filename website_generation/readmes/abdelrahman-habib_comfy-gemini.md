# ComfyUI Gemini Nodes

This repository provides custom nodes for ComfyUI that leverage the Google Gemini API for prompt generation and enhancement.

## Installation

1.  Clone this repository into your `ComfyUI/custom_nodes/` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/your-username/comfy-gemini.git # Replace with the actual repo URL if different
    ```
2.  Install the required dependencies:
    ```bash
    cd comfy-gemini
    pip install -r requirements.txt
    ```
3.  Restart ComfyUI.

## Nodes

### 1. Gemini Image To Prompt (`Gemini/Image`)

This node analyzes an input image using a Gemini model and generates a descriptive text prompt based on its content and a provided system prompt template.

**Inputs:**

- `image` (IMAGE): The input image to analyze.
- `model` (STRING): The Gemini vision model to use (e.g., `gemini-2.0-pro-latest`).
- `api_key` (STRING): Your Google AI API key.
- `prompt_template` (STRING, Optional): The system prompt guiding the model on how to describe the image. Defaults to a detailed template focused on illustration regeneration.

**Outputs:**

- `prompt` (STRING): The generated text prompt describing the image.

**Example Usage:** Connect an image output (e.g., from a LoadImage node) to the `image` input. Provide your API key and select a model. The node will output a text prompt suitable for use in text-to-image generation nodes.

### 2. Gemini Enhance Prompt (`Gemini/Text`)

This node takes an existing text prompt and enhances it using a Gemini text model, making it more detailed and descriptive based on a system prompt.

**Inputs:**

- `prompt` (STRING): The initial text prompt to enhance.
- `api_key` (STRING): Your Google AI API key.
- `model` (STRING): The Gemini text model to use (e.g., `gemini-2.5-pro-latest`).
- `system_prompt` (STRING, Optional): The system prompt guiding the model on how to enhance the input prompt. Defaults to a template focused on adding scene, subject, style, and technical details.

**Outputs:**

- `enhanced_prompt` (STRING): The enhanced, more detailed text prompt.

**Example Usage:** Connect a text prompt (e.g., from a Primitive node or another generation node) to the `prompt` input. Provide your API key and select a model. The node will output an enhanced prompt, potentially leading to more detailed image generations.

## Configuration

- **API Key:** You can provide the Gemini API key directly in the node inputs or set the `GEMINI_API_KEY` environment variable. Using the environment variable is generally more secure.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

[Specify License, e.g., MIT License]
