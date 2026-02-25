# GLM-4V Image Descriptor

![GLM-4V Logo](https://img.shields.io/badge/GLM--4V-Image%20Descriptor-blue?style=for-the-badge&logo=openai)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-green?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-purple?style=flat-square)](https://github.com/comfyanonymous/ComfyUI)

> 🚀 **Professional AI Image Description Generator**  
> Based on Zhipu AI GLM-4V multimodal model, batch generate accurate and detailed descriptions for images in Chinese and English
> 
> The author's WeChat account is:linyu9418 and linjian257
## ✨ Core Features

- 🎯 **Smart Batch Processing** - Process entire folders of images with one click
- 📝 **Same-name File Output** - Automatically generate txt description files with same names as images
- ⚡ **High Performance Optimization** - Supports 4-bit quantization, GPU acceleration, and memory management optimization
- 🔧 **Flexible Configuration** - Customizable prompts, model selection, and output formats
- 🌐 **Bilingual Support** - Supports Chinese and English interfaces and documentation
- 📊 **Multiple Output Formats** - Supports TXT, JSON, CSV and other output formats
- 🔌 **ComfyUI Integration** - Fully compatible with ComfyUI workflows

## 🖼️ Demo

### Output Example
**Input Image**: `sunset_beach.jpg`  
**Output File**: `sunset_beach.txt`  
**Content**: "A breathtaking sunset scene over a serene beach with golden sand, where gentle waves lap against the shore while vibrant orange and pink hues paint the sky, creating a peaceful and romantic atmosphere."

![单图反推-批量打标](https://github.com/user-attachments/assets/07bfad69-1337-44b4-8773-d9643e3a9db8)


## 🚀 Quick Start

### System Requirements

- **Python**: 3.8 or higher
- **GPU**: Recommended NVIDIA GPU with 8GB+ VRAM
- **System**: Windows / Linux / macOS
- **Memory**: 16GB+ system memory

### Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/ComfyUI_GLM4V_voltspark.git
cd ComfyUI_GLM4V_voltspark
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
or
your_path\python_embeded\python.exe -m pip install -r your_path\custom_nodes\ComfyUI_GLM4V_voltspark\requirements.txt --index-url https://mirrors.aliyun.com/pypi/simple

# Upgrade transformers library to latest version (recommended)
python -m pip install git+https://github.com/huggingface/transformers.git

# Or install specific version
pip install transformers==4.54.0
```

3. **Model Download and Installation**

### Method 1: Domestic Download (Recommended for China)

**glmv4_4bit Model:**
- 📁 Download Link: [Baidu Netdisk](https://pan.baidu.com/s/1x1vWW09YadUdz1EYPWc-Fg?pwd=qbdq)
- 🔑 Extraction Code: `qbdq`
- 📦 File Name: `glmv4_4bit.7z`
- 📂 Extract Path: `ComfyUI/models/glmv4_4bit/`

**GLM-4.1V-9B-Thinking Model:**
- 📁 Download Link: [Baidu Netdisk](https://pan.baidu.com/s/1xXtfKXEJLKg2iJ86OZR6nw?pwd=9n27)
- 🔑 Extraction Code: `9n27`
- 📦 File Name: `GLM-4.1V-9B-Thinking.rar`
- 📂 Extract Path: `ComfyUI/models/GLM-4.1V-9B-Thinking/`

### Method 2: Auto Download
The model will be automatically downloaded from Hugging Face on first run. Ensure stable internet connection.

4. **Plugin Installation**
```bash
# Extract the plugin to ComfyUI's custom_nodes directory
ComfyUI/custom_nodes/ComfyUI_GLM4V_voltspark/
```

### 📂 Complete Installation Directory Structure

After installation, your directory structure should look like this:

```
ComfyUI/
├── models/
│   ├── glmv4_4bit/                    # GLM-4V 4-bit quantized model directory
│   │   ├── config.json
│   │   ├── modeling_chatglm.py
│   │   ├── pytorch_model-*.bin
│   │   └── ...
│   └── GLM-4.1V-9B-Thinking/          # GLM-4.1V full model directory
│       ├── config.json
│       ├── modeling_chatglm.py
│       ├── pytorch_model-*.bin
│       └── ...
└── custom_nodes/
    └── ComfyUI_GLM4V_voltspark/       # This plugin directory
        ├── glm4v.py
        ├── __init__.py
        ├── requirements.txt
        ├── README.md
        └── ...
```

### Usage

#### ComfyUI Nodes

1. **Node Types**
   - `GLM-4V Generate` - Single image processing
   - `GLM-4V Batch Generate` - Batch image processing

2. **Usage Steps**
   - Search for "GLM-4V" in ComfyUI
   - Add nodes to workflow
   - Configure input parameters
   - Execute workflow

## 📋 Detailed Configuration

### Preset Parameters

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
| **Prompt** | `describe this image,Describe in long sentence form, without using Markdown format.` | Optimized preset prompt |
| **Model** | `glmv4_4bit` | 4-bit quantized GLM-4V model |
| **Unload Policy** | `Never` | Keep model loaded |
| **Output Format** | `TXT` | Plain text format output |
| **Max Images** | `100` | Maximum images per batch |

### Supported Image Formats

- 📷 **Common Formats**: JPG, JPEG, PNG, BMP
- 🎨 **Professional Formats**: TIFF, WEBP
- 📐 **Resolution**: Supports various resolutions with automatic optimization

### Model Selection

| Model Name | Size | Features | Recommended Use |
|------------|------|----------|-----------------|
| `glmv4_4bit` | ~6.7GB | 4-bit quantization, fast speed | Daily batch processing |
| `GLM-4.1V-9B-Thinking` | ~12.0GB | Full precision, high quality | High-quality descriptions |

## 🛠️ Advanced Features

### Custom Prompts

You can customize prompts according to your needs:

```python
# Detailed description mode
"Please provide a detailed description of this image, including objects, colors, composition, mood, and artistic style."

# Brief description mode  
"Describe this image briefly and accurately."

# Professional photography mode
"Analyze this image from a photographer's perspective, describing composition, lighting, and technical aspects."
```

### Batch Processing Options

- ✅ **Auto Save** - Generate same-name txt files for each image
- 🔄 **Overwrite Mode** - Choose whether to overwrite existing files
- 📊 **Progress Monitoring** - Real-time progress display and statistics
- 🛑 **Interrupt & Resume** - Support pause and resume processing

### Output Format Options

1. **TXT Format** - Plain text descriptions with same names as images
2. **JSON Format** - Structured data with metadata
3. **CSV Format** - Tabular data for easy analysis

## 📁 Project Structure

```
ComfyUI_GLM4V_voltspark/
├── 📄 glm4v.py                     # ComfyUI node core implementation
├── 🔧 requirements.txt             # Python dependencies list
├── 🔌 __init__.py                  # ComfyUI plugin registration file
├── 📖 使用说明.md                  # Detailed usage documentation
├── 📖 README_CN.md                 # Chinese documentation
├── 📖 README.md                    # English documentation
└── 📁 Example/                     # Example files and workflows
    ├── 单图反推-批量打标.json        # ComfyUI workflow example
    └── 单图反推-批量打标.png         # Workflow screenshot
```

## 🐛 Troubleshooting

### Common Issues & Solutions

#### Q: Application fails to start
**A**: Check Python version and dependency installation
```bash
python --version  # Ensure Python 3.8+
pip install -r requirements.txt --upgrade
```

#### Q: Model download fails
**A**: Check network connection, try using mirror sources
```bash
# Set Hugging Face mirror
export HF_ENDPOINT=https://hf-mirror.com
```

#### Q: GPU memory insufficient
**A**: Use 4-bit quantized model or adjust batch size
- Select `glmv4_4bit` model
- Reduce maximum number of images processed
- Close other GPU applications

#### Q: Slow processing speed
**A**: Optimize settings to improve performance
- Ensure GPU acceleration is used
- Set unload policy to "Never"
- Check CUDA driver version

### Log Analysis

The program displays detailed log information during runtime:
- ✅ **Success**: Green status, normal operation
- ⚠️ **Warning**: Yellow status, needs attention
- ❌ **Error**: Red status, needs handling

## 🤝 Contributing

We welcome community contributions! Ways to participate:

1. 🍴 Fork the repository
2. 🔧 Create feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push branch (`git push origin feature/amazing-feature`)
5. 🔄 Create Pull Request

### Development Environment Setup

```bash
# Install development dependencies
pip install -r requirements.txt
pip install jupyter matplotlib tqdm  # Optional development tools

# Run tests
python -m pytest tests/  # If test files exist

# Code formatting
black . --line-length 88
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Zhipu AI](https://www.zhipuai.cn/) - For providing the GLM-4V multimodal model
- [Hugging Face](https://huggingface.co/) - For model hosting and inference framework
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - For the powerful AI workflow platform
- All developers who contribute to the open source community

## 📞 Contact Us

- 🐛 **Bug Reports**: [Issues Page](https://github.com/your-username/ComfyUI_GLM4V_voltspark/issues)
- 📧 **Email Contact**: linjian257@gmail.com

## 📈 Changelog

### v0.3.42 (Latest Version)
- ✅ Complete GUI interface design
- ✅ Optimized batch processing performance
- ✅ Stable model loading mechanism
- ✅ Complete Chinese and English documentation

### Coming Soon
- 🔄 More model support
- 🎨 Interface theme customization
- 📊 Advanced data analysis features
- 🌐 Extended multilingual support

---

<div align="center">
  <p><strong>⭐ If this project helps you, please give us a star! ⭐</strong></p>
  <p>Made with ❤️ by the Community</p>
</div> 
