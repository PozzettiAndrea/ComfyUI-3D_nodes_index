# ComfyUI OpenAI Compatible LLM Node

A ComfyUI custom node that provides integration with OpenAI-compatible Large Language Model APIs, including OpenAI, local models, and other compatible endpoints. Supports both text-only and multimodal (text + image) interactions.

## Features

- **Multi-line prompt input**: Large text area for complex prompts
- **Image input support**: Optional image input for multimodal LLMs (GPT-4 Vision, etc.)
- **Configurable endpoint**: Support for OpenAI API and other compatible services
- **Secure token input**: API key/token field for authentication
- **Model selection**: Specify which model to use (defaults to vision-capable model)
- **Generation parameters**: Control max tokens, temperature, and image detail level
- **Automatic image encoding**: Converts ComfyUI images to base64 for API compatibility
- **Error handling**: Comprehensive error reporting and fallback responses

## Installation

### Method 1: ComfyUI Manager (Recommended)

1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) if you haven't already
2. Open ComfyUI Manager in your ComfyUI interface
3. Search for "OpenAI Compatible LLM Node"
4. Click Install

### Method 2: Manual Installation

1. Navigate to your ComfyUI installation directory:
   ```bash
   cd /path/to/your/ComfyUI
   ```

2. Clone this repository into the custom_nodes directory:
   ```bash
   cd custom_nodes
   git clone https://github.com/yourusername/ComfyUI-OpenAI-Compat-LLM-Node.git
   ```

3. Install the required dependencies:
   ```bash
   cd ComfyUI-OpenAI-Compat-LLM-Node
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

### Method 3: Direct Download

1. Download the latest release from the [releases page](https://github.com/yourusername/ComfyUI-OpenAI-Compat-LLM-Node/releases)
2. Extract the archive to your `ComfyUI/custom_nodes/` directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Restart ComfyUI

## Usage

1. After installation, restart ComfyUI
2. In the ComfyUI interface, right-click to add a new node
3. Navigate to `LLM` → `OpenAI Compatible LLM`
4. Configure the node with your settings:
   - **Prompt**: Enter your text prompt (supports multi-line input)
   - **Endpoint**: API endpoint URL (default: OpenAI's endpoint)
   - **API Token**: Your API key/token
   - **Image** (optional): Connect an image from another node for multimodal analysis
   - **Model**: Model name (default: gpt-4-vision-preview for multimodal support)
   - **Max Tokens**: Maximum response length (default: 150)
   - **Temperature**: Creativity/randomness (0.0-2.0, default: 0.7)
   - **Image Detail**: Quality level for image processing (low/high/auto, default: auto)

## Supported Endpoints

This node works with any OpenAI-compatible API endpoint, including:

- **OpenAI API**: `https://api.openai.com/v1/chat/completions`
- **Local models** (via tools like ollama, text-generation-webui, etc.)
- **Cloud providers** with OpenAI-compatible APIs
- **Self-hosted solutions**

## Configuration Examples

### OpenAI API (Text + Vision)
- **Endpoint**: `https://api.openai.com/v1/chat/completions`
- **Models**: 
  - Text-only: `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo`
  - Vision: `gpt-4-vision-preview`, `gpt-4-turbo` (with vision)
- **API Token**: Your OpenAI API key

### Local Ollama (Vision Models)
- **Endpoint**: `http://localhost:11434/v1/chat/completions`
- **Models**: 
  - Text-only: `llama2`, `mistral`, `codellama`
  - Vision: `llava`, `bakllava`, `llava-llama3`
- **API Token**: Leave empty for local usage

### Text Generation WebUI (with MultiModal)
- **Endpoint**: `http://localhost:5000/v1/chat/completions`
- **Model**: Your loaded vision-capable model
- **API Token**: Set if authentication is enabled

## Usage Examples

### Text-Only Generation
1. Add the node to your workflow
2. Set your prompt: "Explain the concept of machine learning"
3. Leave the image input disconnected
4. Use a text model like `gpt-3.5-turbo`

### Image Analysis
1. Connect an image output from another node to the image input
2. Set your prompt: "Describe what you see in this image"
3. Use a vision model like `gpt-4-vision-preview`
4. Adjust image detail level as needed

### Image + Text Prompt
1. Connect an image and set a specific prompt
2. Example: "What colors are prominent in this image and how do they affect the mood?"
3. The model will analyze both the text and image together

## Requirements

- ComfyUI
- Python 3.8+
- requests >= 2.32.3
- Pillow >= 10.0.0
- numpy >= 1.24.0

## Node Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| prompt | STRING | Yes | "You are a helpful assistant." | The text prompt to send to the LLM |
| endpoint | STRING | Yes | "https://api.openai.com/v1/chat/completions" | API endpoint URL |
| api_token | STRING | Yes | "" | API authentication token |
| image | IMAGE | No | None | Optional image input for multimodal analysis |
| model | STRING | No | "gpt-4-vision-preview" | Model name to use (vision-capable by default) |
| max_tokens | INT | No | 150 | Maximum tokens in response |
| temperature | FLOAT | No | 0.7 | Sampling temperature (0.0-2.0) |
| image_detail | STRING | No | "auto" | Image processing detail level (low/high/auto) |

## Node Outputs

| Output | Type | Description |
|--------|------|-------------|
| response | STRING | The generated text response from the LLM |

## Error Handling

The node includes comprehensive error handling:
- Network connection errors
- API authentication failures
- Invalid JSON responses
- Rate limiting and timeout issues
- Missing response content

Errors are returned as descriptive text strings for debugging.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- For issues and feature requests: [GitHub Issues](https://github.com/yourusername/ComfyUI-OpenAI-Compat-LLM-Node/issues)
- For discussions: [GitHub Discussions](https://github.com/yourusername/ComfyUI-OpenAI-Compat-LLM-Node/discussions)

## Changelog

### v1.1.0
- Added image input support for multimodal LLMs
- Automatic base64 image encoding
- Support for GPT-4 Vision and other vision models
- Image detail level control
- Updated dependencies (Pillow, numpy)

### v1.0.0
- Initial release
- Basic OpenAI-compatible API integration
- Multi-line prompt support
- Configurable endpoints and models
- Comprehensive error handling