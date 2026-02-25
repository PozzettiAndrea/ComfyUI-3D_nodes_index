# ComfyUI AI CustomURL Extension

A comprehensive ComfyUI extension that enables **text, image, video, and speech generation** using any OpenAI-compatible API endpoint with custom URLs.

## 🌟 Features

- **Universal API Support**: Works with any API following the OpenAI format
- **Multiple Modalities**: Text, Image, Video, and Speech generation
- **Advanced Parameters**: Fine-tune generations with advanced parameter nodes
- **Multi-Provider**: Switch between different API providers in one workflow
- **Simple Configuration**: Just enter API URL, key, and model name
- **No Dependencies on Specific APIs**: Works with any compatible endpoint

## 🔌 Supported APIs

- **OpenAI** 
- **Venice.ai** 
- **OpenRouter** 
- **Together.ai** 
- **Ollama** 
- Any other OpenAI-compatible API

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "AI CustomURL"
3. Click Install

### Method 2: Manual Installation

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/bowtiedbluefin/ComfyUI-AI-CustomURL.git
cd ComfyUI-AI-CustomURL
pip install -r requirements.txt
```

### Method 3: Portable Install

```bash
cd /path/to/ComfyUI_windows_portable/ComfyUI/custom_nodes
git clone https://github.com/bowtiedbluefin/ComfyUI-AI-CustomURL.git
cd ComfyUI-AI-CustomURL
../../python_embeded/python.exe -m pip install -r requirements.txt
```

## 🚀 Quick Start

### Basic Text Generation

1. Add "Generate Text (AI CustomURL)" node
2. Enter your API base URL (e.g., `https://api.openai.com/v1`)
3. Enter your API key
4. Enter the model name (e.g., `gpt-4o`)
5. Enter your prompt
6. Execute!

### Image Generation

1. Add "Generate Image (AI CustomURL)" node
2. Configure API settings
3. Enter image description
4. Select size and quality
5. Generate!

### Video Generation (NEW!)

1. Add "Generate Video (AI CustomURL)" node
2. Enter API credentials
3. Provide video prompt
4. Set duration and resolution
5. Create!

### Speech Generation

1. Add "Generate Speech (AI CustomURL)" node
2. Configure API settings
3. Enter text to synthesize
4. Select voice and format
5. Generate!

## 📚 Node Reference

### Core Generation Nodes

#### Text Generation
- **Generate Text (AI CustomURL)**: Basic text generation with chat completions
- **Text Advanced Parameters**: Extended parameters (top_p, frequency_penalty, etc.)

#### Image Generation
- **Generate Image (AI CustomURL)**: Image generation via `/images/generations`
- **Image Advanced Parameters**: Custom dimensions, negative prompts, guidance scale

#### Video Generation
- **Generate Video (AI CustomURL)**: Video generation via `/videos/create`
- **Video Advanced Parameters**: Motion control, camera movement, looping

#### Speech Generation
- **Generate Speech (AI CustomURL)**: Text-to-speech via `/audio/speech`
- **Speech Advanced Parameters**: Voice settings, emotion, pitch

### Utility Nodes

- **Load Image from URL**: Download images from URLs
- **Load Video from URL**: Download and process videos

## 🔧 Configuration

### Environment Variables (Recommended)

```bash
export OPENAI_API_KEY="sk-..."
export VENICE_API_KEY="..."
```

### Config File

Copy `config.example.json` to `config.json` and fill in your API keys:

```json
{
  "profiles": {
    "openai": {
      "base_url": "https://api.openai.com/v1",
      "api_key": "sk-YOUR_API_KEY",
      "enabled": true
    }
  }
}
```

### Per-Node Configuration

You can also enter API credentials directly in each node (not recommended for security).

## 📖 OpenAI API Specification

This extension follows the official OpenAI API specification:

### Text Generation
Endpoint: `POST /v1/chat/completions`

**Required Parameters:**
- `model` (string): Model ID
- `messages` (array): Array of message objects

**Optional Parameters:**
- `temperature` (number): 0-2, default 1
- `max_tokens` (integer): Maximum completion tokens
- `top_p` (number): 0-1
- `frequency_penalty` (number): -2 to 2
- `presence_penalty` (number): -2 to 2
- `stop` (string or array): Stop sequences
- `seed` (integer): For reproducibility
- `response_format` (object): {"type": "json_object"}

### Image Generation
Endpoint: `POST /v1/images/generations`

**Required Parameters:**
- `prompt` (string): Image description

**Optional Parameters:**
- `model` (string): Model ID
- `n` (integer): 1-10, number of images
- `size` (string): Image dimensions
- `quality` (string): "standard" or "hd"
- `style` (string): "vivid" or "natural"
- `response_format` (string): "url" or "b64_json"

### Video Generation
Endpoint: `POST /v1/videos/create`

**Required Parameters:**
- `model` (string): Model ID
- `prompt` (string): Video description

**Optional Parameters:**
- `duration` (integer): Video duration in seconds
- `resolution` (string): Video resolution
- `fps` (integer): Frames per second
- `aspect_ratio` (string): e.g., "16:9", "9:16"

### Speech Generation
Endpoint: `POST /v1/audio/speech`

**Required Parameters:**
- `model` (string): TTS model ID
- `input` (string): Text to synthesize
- `voice` (string): Voice identifier

**Optional Parameters:**
- `response_format` (string): Audio format
- `speed` (number): 0.25-4.0

## 🎯 Advanced Usage

### Combining Nodes

You can chain nodes together for complex workflows:

```
[Text Generation] → prompt
                     ↓
[Image Generation] → images
                     ↓
[Video Generation] → video
```

### Advanced Parameters

Use "Advanced Parameters" nodes to pass extra parameters:

```
[Text Advanced Parameters] → params_json
                              ↓
[Text Generation] ← advanced_params_json
```

### Multi-Provider Workflows

Use different API providers in the same workflow:

```
[OpenAI Text Gen] → description
                     ↓
[Venice Image Gen] → image
                     ↓
[OpenAI Video Gen] → video
```

## 💡 How Model Selection Works

Unlike some extensions, **AI CustomURL doesn't auto-fetch models**. You simply:

1. Look up the model name in your API provider's documentation
2. Enter it manually in the `model` field

**Examples:**
- OpenAI: `gpt-4o`, `dall-e-3`, `sora-1.0`, `tts-1`
- Venice.ai: `llama-3.3-70b`, `flux-dev`, `tts-kokoro`
- Ollama: `llama3:70b`, `mistral`, `codellama`

This keeps the extension simple and compatible with any API!

## 🐛 Troubleshooting

### "API Error 401"
- Check your API key is correct
- Verify the API key has appropriate permissions

### "Connection timeout"
- Check your internet connection
- Verify the API base URL is correct
- Some APIs may be slow, increase timeout in config

### "Model not found"
- The model might not be available in your API
- Use the model discovery feature to see available models
- Check for typos in model name

### "No images/video generated"
- Check the API response in the full_response output
- Some APIs have content filters that may reject prompts
- Verify your account has credits/quota

## 💡 Tips

1. **Cache Models**: Enable model caching to speed up workflows
2. **Use Environment Variables**: More secure than storing keys in nodes
3. **Test Connection**: Use the test connection endpoint before workflows
4. **Start Simple**: Begin with basic nodes, add advanced parameters later
5. **Check Quotas**: Monitor your API usage to avoid rate limits

## 📝 Example Workflows

See the `examples/` directory for sample workflows:

- `text_generation_basic.json` - Simple text generation
- `text_generation_vision.json` - Text generation with image input
- `image_generation.json` - Image generation with parameters
- `video_generation.json` - Video generation from prompt
- `multi_modal_pipeline.json` - Complete text → image → video pipeline

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- ComfyUI team for the excellent framework
- OpenAI for the API specification
- Venice.ai, OpenRouter, Together.ai for compatible APIs

## 📞 Support

- Issues: [GitHub Issues](https://github.com/bowtiedbluefin/ComfyUI-AI-CustomURL/issues)
- Discussions: [GitHub Discussions](https://github.com/bowtiedbluefin/ComfyUI-AI-CustomURL/discussions)

---

**Made with ❤️ for the ComfyUI community**

