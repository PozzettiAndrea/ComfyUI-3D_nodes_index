# 🚀 ComfyUI BuimenLabo - Unified Package

[![Author](https://img.shields.io/badge/Author-BuimenLabo-blue.svg)](https://note.com/hirodream44)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)]()
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-orange.svg)]()
[![License](https://img.shields.io/badge/License-MIT-purple.svg)]()

> **📖 Visit the author's blog: [https://note.com/hirodream44](https://note.com/hirodream44)**  
> **🎓 Learn ComfyUI custom node development: [ComfyUI Custom Node Tutorial Series](https://note.com/hirodream44/m/ma40278dc5bf0)**

A comprehensive collection of ComfyUI custom nodes that brings together powerful AI tools in one unified package. This package demonstrates practical custom node development techniques covered in the author's tutorial series, with detailed usage guides and examples available on the blog.

![Overview](images/overview.png)

## ✨ Features

### 🦙 **Advanced LLM Text Generation**
- **Llama-CPP All-In-One**: Complete text generation solution with one-click controls
- **Multiple Models**: Support for CPU/GPU acceleration with llama-cpp-python
- **Smart UI**: Generate, Reset, and Unload buttons with real-time result viewer
- **Memory Management**: Automatic VRAM cleanup and model caching

![Llama AIO](images/llama_aio.png)

### 🌐 **Smart Prompt Translation** 
- **Multi-Provider Support**: Google Translate (free), DeepL, Yandex, Baidu
- **One-Click Translation**: Direct translation buttons with token counting
- **20+ Languages**: Comprehensive language support
- **API Key Management**: Secure local storage of API credentials

![Translator](images/translator.png)

### 🌍 **Multi-Language Interface**
- **20 Language Support**: Switch ComfyUI interface between 20 languages
- **Floating Toggle**: Draggable language switcher in top-right corner
- **Quick Switch**: Left-click for EN ↔ Last Language, Right-click for full menu
- **Persistent Settings**: Remembers your language preference

![Locale Toggle](images/locale_toggle.png)

### 🎛️ **Smart ControlNet Management**
- **Multi-ControlNet Loader**: Load multiple ControlNet models efficiently
- **SD/SDXL Support**: Works with both Stable Diffusion versions
- **Easy Configuration**: Simple dropdown selection interface

![ControlNet](images/comtrolnet.png)

### 📸 **AI-Powered Pose Analysis**
- **Gemini Integration**: Advanced pose analysis using Google's Gemini API
- **22 Language Support**: Descriptions in your preferred language
- **Flexible Analysis**: Full body, face focus, or detailed pose analysis
- **Natural Language Output**: Human-readable pose descriptions

![Gemini Pose](images/gemini_pose.png)

## 🛠️ Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "BuimenLabo"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation
1. Navigate to `ComfyUI/custom_nodes/`
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/comfyui-builmenlabo.git
   ```
3. Run the installation script:
   ```bash
   cd comfyui-builmenlabo
   ./install.bat  # Windows
   ```
4. Restart ComfyUI

## 🔧 Quick Setup

### LLM Text Generation
1. Download GGUF models from [HuggingFace](https://huggingface.co/models?library=gguf)
2. Place models in `ComfyUI/models/llm/` (auto-created)
3. Recommended: `Qwen2.5-7B-Instruct-Q8_0.gguf`

### Gemini Pose Analyzer
1. Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Enter key in the node's API field
3. Upload images for pose analysis

### Prompt Translation
- **Google**: Works without API key (free service)
- **DeepL**: Get key from [DeepL API](https://www.deepl.com/pro-api)
- API keys are stored locally and remembered

## 📋 Available Nodes

| Node | Description | Category |
|------|-------------|----------|
| 🦙 **Llama-CPP All-In-One** | Complete LLM text generation | Text |
| 🦙 **Llama-CPP Loader** | Load LLM models | Model |
| 🦙 **Llama-CPP Generate** | Generate text | Text |
| 🦙 **Llama-CPP Unload** | Unload from VRAM | Memory |
| 🌐 **Prompt Translator** | Multi-language translation | Text |
| 🎛️ **Multi ControlNet Loader** | Load multiple ControlNets | Model |
| 📸 **Gemini Pose Analyzer** | AI pose analysis | Analysis |

## 🎯 Usage Tips

### LLM Generation
- Use **Generate** button for instant text generation
- **Reset** button restores default settings
- **Unload** button frees VRAM when done
- Adjust GPU layers based on your VRAM

### Translation
- Try Google first (no API key needed)
- DeepL provides higher quality for supported languages
- Translation results are cached to avoid repeated API calls

### Language Toggle
- Drag the 🌐 button to reposition
- Left-click for quick EN ↔ Previous language
- Right-click for full language menu

## 🔍 Troubleshooting

### Common Issues
- **Language toggle not showing**: Refresh browser (F5)
- **VRAM issues**: Lower GPU layers or use smaller models
- **API errors**: Check internet connection and API keys
- **Installation issues**: Run as administrator

### GPU Support
- **NVIDIA**: Use CUDA installation option
- **AMD**: Use ROCm installation (experimental)
- **Apple Silicon**: Use Metal installation
- **CPU Only**: Universal but slower

## 📝 Requirements

- ComfyUI (latest version)
- Python 3.8+
- For GPU acceleration: CUDA 11.8+ or ROCm 5.4+

## 🔗 Links

- **Blog**: [https://note.com/hirodream44](https://note.com/hirodream44)
- **Support**: Submit issues via ComfyUI Manager
- **Updates**: Check ComfyUI Manager for latest version

## 📄 License

This project is licensed under the MIT License.

---

**Made with ❤️ by BuimenLabo**

*Bringing AI tools together for creative workflows*
