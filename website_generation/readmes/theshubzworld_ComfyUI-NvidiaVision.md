# ComfyUI-NvidiaVision Nodes

✨ **Enhance your ComfyUI workflow with powerful NVIDIA AI models for text and vision tasks!** ✨

## 🌟 Features

### 📝 ✨ NVIDIA Prompt Generator (Text) ✨
- Generate high-quality, creative prompts for AI image generation
- Supports multiple state-of-the-art language models from NVIDIA's API
- Customize generation with temperature, top-p sampling, and more
- Built-in rate limiting and request retries for reliable operation
- Response caching to save on API costs

### 🖼️ 👁️‍🗨️ NVIDIA Vision Node 👁️‍🗨️
- Powerful image analysis and description generation
- Supports various vision-language models from NVIDIA
- Process images with detailed visual understanding
- Stream responses for real-time interaction
- Robust error handling and retry mechanisms

## 🚀 Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:
   ```bash
   git clone https://github.com/theshubzworld/ComfyUI-NvidiaVision.git
   ```

2. Install the required dependencies:
   ```bash
   python_embeded\python.exe -m pip install openai requests pillow numpy torch
   ```

3. Restart ComfyUI

## 🔑 API Key Setup

You'll need an NVIDIA API key to use these nodes:

1. Get your API key from [NVIDIA API Catalog](https://developer.nvidia.com/)
2. Add the key in the node's settings panel in ComfyUI

## 🎨 Usage

### ✨ Prompt Generator Node
1. Add the "✨ NVIDIA Prompt Generator (Text) ✨" node to your workflow
2. Enter your NVIDIA API key
3. Select your preferred model (e.g., "meta/llama-3.3-70b-instruct")
4. Input your prompt or instruction
5. Adjust generation parameters as needed
6. Run the workflow to generate text

### 👁️‍🗨️ Vision Node
1. Add the "👁️‍🗨️ NVIDIA Vision Node 👁️‍🗨️" to your workflow
2. Connect an image input
3. Enter your NVIDIA API key
4. Choose a vision model (e.g., "meta/llama-3.2-11b-vision-instruct")
5. Configure your analysis parameters
6. Run the workflow to process the image

## ⚙️ Configuration

### Common Parameters
- **API Key**: Your NVIDIA API key
- **Model**: Select from available models
- **Max Tokens**: Maximum length of the generated response
- **Temperature**: Controls randomness (lower = more focused, higher = more creative)
- **Top-p**: Controls diversity of the output
- **Stream**: Enable for real-time streaming of responses

## 📦 Available Models

### Text Generation Models
- Meta LLAMA 3 (3.3B to 70B parameters)
- Mistral models (7B to Mixtral 8x22B)
- Google Gemma (2B to 27B)
- NVIDIA's own models (Nemotron, Llama 3.1 variants)

### Vision Models
- Meta LLAMA Vision Instruct models
- Other vision-language models from NVIDIA's catalog

## ⚠️ Notes
- API usage may be subject to rate limits
- Some models may have specific requirements or limitations
- Monitor your API usage through NVIDIA's developer portal

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- NVIDIA for their powerful AI models and API
- The ComfyUI community for their support and inspiration
