# ComfyUI-Ninode-Utils

[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](https://github.com/iGavroche/ComfyUI-Ninode-Utils)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-compatible-orange.svg)](https://github.com/comfyanonymous/ComfyUI)

A collection of utility nodes for ComfyUI, featuring OpenAI Compatible Chat functionality and more.

## 🚀 Features

### OpenAI Compatible Chat Node

A flexible chat node that works with **any OpenAI-compatible API endpoint**, providing complete compatibility with the original ChatGPT node while supporting:

- **Local servers** like [Lemonade Server](https://lemonade-server.ai/docs/server) (`http://127.0.0.1:8000/api/v1/chat/completions`)
- **Ollama** (`http://localhost:11434/v1/chat/completions`)
- **OpenAI API** (`https://api.openai.com/v1/chat/completions`)
- **LM Studio** (`http://localhost:1234/v1/chat/completions`)
- **Any other OpenAI-compatible service**

#### ✨ Key Features

- **🔄 Complete Input Compatibility** - All inputs from the original ChatGPT node are supported
- **💬 Multi-turn Conversations** - Context persistence for ongoing conversations
- **🖼️ Image Support** - Vision model support with image inputs
- **📄 File Support** - Document analysis with file inputs
- **⚙️ Advanced Options** - Fine-tuned control with advanced configuration
- **🌐 Flexible API Configuration** - Custom URLs and API keys
- **🤖 System Message Support** - Set assistant behavior and personality
- **🎛️ Configurable Parameters** - Temperature, top_p, max_tokens, and more
- **🛡️ Robust Error Handling** - Graceful handling of various edge cases

### VibeVoice Voice Design Node

A **drop-in replacement** for Minimax Voice Design node that generates custom voices from text descriptions using VibeVoice TTS. Perfect for the full-loop-Sora2-ComfyUI workflow!

**Features:**
- 🎙️ **Voice Generation from Text Descriptions** - Create custom voices based on detailed prompts
- 🔄 **Drop-in Compatibility** - Same inputs/outputs as Minimax Voice Design node
- 🎵 **Voice Cloning Support** - Optional reference audio for voice cloning
- 🚀 **Local Processing** - No API keys required, runs entirely locally
- ⚡ **High Quality** - Uses VibeVoice's advanced TTS technology

#### ✨ Key Features

- **🔄 Complete Input Compatibility** - Same interface as Minimax Voice Design node
- **🎯 Text-to-Voice Generation** - Generate voices from detailed text descriptions
- **🎵 Reference Audio Support** - Optional voice cloning with reference audio
- **⚙️ Advanced Generation Controls** - CFG scale, inference steps, temperature, top-p
- **🔧 Model Selection** - Choose from available VibeVoice models
- **💾 Audio Output** - Saves generated audio as WAV files
- **🎛️ Memory Management** - Optional model offloading for memory efficiency

## 📦 Installation

### Method 1: Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/iGavroche/ComfyUI-Ninode-Utils.git
cd ComfyUI-Ninode-Utils
pip install -r requirements.txt
```

### Method 2: Manual Installation

1. Download or clone this repository
2. Place the `ComfyUI-Ninode-Utils` folder in your ComfyUI `custom_nodes` directory
3. Install dependencies:
   ```bash
   pip install aiohttp torch Pillow numpy
   ```
4. Restart ComfyUI

## 🎯 Usage

### OpenAI Compatible Chat Node

The node appears in the **"ComfyUI-Ninode-Utils"** category and can be used as a drop-in replacement for the original ChatGPT node.

#### Required Parameters

- **API URL**: Your OpenAI-compatible endpoint (e.g., `http://127.0.0.1:35841/v1/chat/completions`)
- **Model**: Model name (e.g., `gpt-4o-mini`, `llama3.2`, etc.)
- **API Key**: Authentication key (leave empty for local servers)
- **Prompt**: Your text input
- **Persist Context**: Enable multi-turn conversations

#### Optional Parameters

- **Images**: Image inputs for vision models
- **Files**: File inputs for document analysis
- **Advanced Options**: Advanced configuration from OpenAI Chat Advanced Options node
- **Max Tokens**: Response length limit
- **Temperature**: Creativity control (0.0-2.0)
- **Top P**: Diversity control (0.0-1.0)
- **System Message**: Assistant behavior setting

## 🔧 Configuration Examples

### Lemonade Server
```
API URL: http://127.0.0.1:35841/v1/chat/completions
Model: gpt-4o-mini
API Key: (leave empty)
```

### Ollama
```
API URL: http://localhost:11434/v1/chat/completions
Model: llama3.2
API Key: (leave empty)
```

### OpenAI API
```
API URL: https://api.openai.com/v1/chat/completions
Model: gpt-4o
API Key: your-openai-api-key
```

### LM Studio
```
API URL: http://localhost:1234/v1/chat/completions
Model: codellama-7b-instruct
API Key: (leave empty)
```

## 🧪 Testing

The package includes comprehensive tests to ensure reliability:

```bash
cd ComfyUI-Ninode-Utils
python test_node.py                    # Basic functionality tests
python test_new_inputs.py             # Input compatibility tests
python test_advanced_options.py       # Advanced options handling tests
python test_tensor_handling.py        # Image tensor processing tests
```

## 📋 Requirements

- **ComfyUI** (latest version)
- **Python** 3.9+
- **Dependencies**:
  - `aiohttp>=3.8.0`
  - `torch>=2.0.0`
  - `Pillow>=9.0.0`
  - `numpy>=1.25.0`

## 🛠️ Development

### Project Structure

```
ComfyUI-Ninode-Utils/
├── __init__.py                    # Package initialization
├── nodes.py                       # Main node implementations
├── pyproject.toml                 # Project configuration
├── requirements.txt               # Dependencies
├── README.md                      # This file
├── test_node.py                   # Basic tests
├── test_new_inputs.py             # Input compatibility tests
├── test_advanced_options.py       # Advanced options tests
├── test_tensor_handling.py        # Tensor processing tests
└── IMPLEMENTATION_SUMMARY.md      # Technical documentation
```

### Adding New Nodes

1. Add your node class to `nodes.py`
2. Update `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS`
3. Add tests for your node
4. Update documentation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

- **iGavroche** - [GitHub](https://github.com/iGavroche) - nino2k@proton.me

## 🙏 Acknowledgments

- ComfyUI community for the amazing framework
- OpenAI for the API specification
- All contributors and testers

## 📈 Changelog

### v0.9.0 (Current)
- Initial release
- OpenAI Compatible Chat Node with full input compatibility
- Support for multiple API endpoints (Lemonade, Ollama, OpenAI, LM Studio)
- Comprehensive test suite
- Robust error handling and edge case management

## 🐛 Bug Reports

If you encounter any issues, please:

1. Check the [Issues](https://github.com/iGavroche/ComfyUI-Ninode-Utils/issues) page
2. Create a new issue with:
   - ComfyUI version
   - Python version
   - Error message and traceback
   - Steps to reproduce

## 📞 Support

For support, please open an issue on GitHub or contact [iGavroche](mailto:nino2k@proton.me).

---

**Made with ❤️ for the ComfyUI community**