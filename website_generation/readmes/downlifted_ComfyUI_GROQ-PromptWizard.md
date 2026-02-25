# ComfyUI_ComfyGroq

A streamlined ComfyUI custom node package for interacting with GROQ's AI models, including both text and vision capabilities.

## Features

- **GROQ LLM Node**: Generate text using GROQ's language models
- **GROQ Vision Node**: Analyze images with GROQ's vision-language models
- **API Key Management**: Set API key per-node or via environment variable
- **Simple Interface**: Easy-to-use nodes with sensible defaults

## Installation

1. Clone or download this repository into your ComfyUI `custom_nodes` directory:
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/yourusername/ComfyUI_ComfyGroq.git
   ```

2. Install the required dependencies:
   ```
   pip install groq
   ```

## Usage

### Setting Up Your API Key

You can provide your GROQ API key in one of two ways:
1. **Per-node**: Enter your API key directly in the node's input field
2. **Environment Variable**: Set `GROQ_API_KEY` in your environment variables

### Available Nodes

#### GROQ LLM
Generates text using GROQ's language models.

**Inputs:**
- `api_key`: Your GROQ API key (or leave empty to use environment variable)
- `model`: The language model to use
- `prompt`: Your input prompt
- `system_message`: System message to guide the model's behavior
- `temperature`: Controls randomness (0.0 to 2.0)
- `max_tokens`: Maximum number of tokens to generate
- `top_p`: Nucleus sampling parameter
- `seed`: Random seed for reproducibility

#### GROQ Vision
Analyzes images using GROQ's vision-language models.

**Inputs:**
- `api_key`: Your GROQ API key (or leave empty to use environment variable)
- `model`: The vision model to use
- `image`: Input image to analyze
- `prompt`: Your question or instruction about the image
- `temperature`: Controls randomness (0.0 to 2.0)
- `max_tokens`: Maximum number of tokens to generate

## Examples

### Text Generation
1. Add a "GROQ LLM" node to your workflow
2. Enter your API key or set the `GROQ_API_KEY` environment variable
3. Type your prompt and adjust parameters as needed
4. Run the workflow to generate text

### Image Analysis
1. Add an image loader node and a "GROQ Vision" node
2. Connect the image to the Vision node
3. Enter your question about the image
4. Run the workflow to get the model's analysis

## License

This project is licensed under the MIT License.
