# ComfyUI-Qwen3-TTS

<div align="center">

![Version](https://img.shields.io/badge/version-1.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![ComfyUI](https://img.shields.io/badge/ComfyUI-compatible-orange)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

**High-quality Text-to-Speech nodes for ComfyUI using Qwen3-TTS models**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [GPU Support](#-gpu-support) • [Examples](#-examples)

</div>

---

## 📖 Overview

ComfyUI-Qwen3-TTS brings Alibaba's powerful Qwen3-TTS models to ComfyUI, enabling high-quality text-to-speech synthesis with three distinct capabilities:

- **🎭 Voice Cloning**: Clone any voice from a reference audio sample
- **🎨 Voice Design**: Create custom voices from text descriptions
- **🎵 Custom Voice**: Use preset high-quality voices

Based on the open-source [Qwen3-TTS project](https://github.com/QwenLM/Qwen-Audio) by Alibaba Qwen team.

---

## ✨ Features

### Three Powerful Nodes

#### 🎭 Qwen3-TTS VoiceClone
Clone voices from reference audio and synthesize new speech:
- Upload any audio file as voice reference
- Optional: Provide reference text for better accuracy
- Generate speech in the cloned voice
- Supports 11 languages
- X-vector only mode for quick voice embedding extraction

#### 🎨 Qwen3-TTS VoiceDesign
Create custom voices from natural language descriptions:
- Describe the voice you want (e.g., "A deep male voice with a slight accent")
- Model generates speech matching your description
- Highly experimental and creative
- Only available with 1.7B model

#### 🎵 Qwen3-TTS CustomVoice
Use preset high-quality voices:
- 9 preset speakers: Aiden, Dylan, Eric, Ono_anna, Ryan, Serena, Sohee, Uncle_fu, Vivian
- Optional style instructions for voice modulation
- Consistent, reliable quality
- Available in both 0.6B and 1.7B models

### Key Capabilities

✅ **Multi-GPU Support**: CUDA, Apple Silicon (MPS), Intel Arc (XPU), and CPU  
✅ **Automatic Model Download**: Models are downloaded automatically on first run  
✅ **Precision Options**: BFloat16 and Float32 for speed/quality trade-offs  
✅ **11 Languages**: Auto-detect or manually select from Chinese, English, Japanese, Korean, French, German, Spanish, Portuguese, Russian, Italian  
✅ **Flexible Model Sizes**: 0.6B for speed, 1.7B for quality  
✅ **Deterministic Generation**: Seed control for reproducible results  

---

## 📦 Installation

### Method 1: Manual Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/ai-joe-git/ComfyUI-Qwen3-TTS.git
cd ComfyUI-Qwen3-TTS
pip install -r requirements.txt
```

### Method 2: Git Submodule

If your ComfyUI is a git repository:

```bash
cd ComfyUI/custom_nodes/
git submodule add https://github.com/ai-joe-git/ComfyUI-Qwen3-TTS.git
cd ComfyUI-Qwen3-TTS
pip install -r requirements.txt
```

### Important Notes

⚠️ **First Run**: Models (~6GB) will be automatically downloaded to `ComfyUI/models/qwen-tts/`  
⚠️ **Dependencies**: Requires PyTorch 2.0+ and transformers 4.30+  
⚠️ **Qwen TTS Package**: The `qwen_tts` package should be included as a submodule or folder  

---

## 🎮 Usage

### Basic Workflow

1. Add a Qwen3-TTS node from the `Qwen3-TTS` category
2. Configure settings:
   - **Device**: `auto` (recommended), `cuda`, `mps`, `xpu`, or `cpu`
   - **Precision**: `bf16` (faster) or `fp32` (more compatible)
   - **Model**: `0.6B` (faster) or `1.7B` (better quality)
3. Enter your text
4. Run the workflow

### Node-Specific Usage

#### Voice Clone Node

```
Inputs:
- ref_audio: Reference audio (use Load Audio node)
- ref_text: Optional transcription of reference audio
- target_text: Text to synthesize in cloned voice
- device: auto/cuda/mps/xpu/cpu
- precision: bf16/fp32
- model_choice: 0.6B/1.7B
- language: Auto or specific language
- seed: For reproducible results
- x_vector_only: Extract voice embedding only (faster)
```

#### Voice Design Node

```
Inputs:
- text: Text to synthesize
- instruct: Voice description (e.g., "A cheerful female voice")
- device: auto/cuda/mps/xpu/cpu
- precision: bf16/fp32
- model_choice: 1.7B only
- language: Auto or specific language
- seed: For reproducible results
```

#### Custom Voice Node

```
Inputs:
- text: Text to synthesize
- speaker: Choose from 9 preset voices
- device: auto/cuda/mps/xpu/cpu
- precision: bf16/fp32
- model_choice: 0.6B/1.7B
- language: Auto or specific language
- instruct: Optional style instruction
- seed: For reproducible results
```

---

## 🖥️ GPU Support

### CUDA (NVIDIA GPUs)
✅ **Recommended**: Best performance  
✅ **Auto-detected**: Set device to `auto`  
✅ **Precision**: BFloat16 recommended

### Apple Silicon (MPS)
✅ **Supported**: M1/M2/M3 Macs  
✅ **Auto-detected**: Set device to `auto`  
⚠️ **Note**: Automatically uses FP16/BF16 for better performance

### Intel Arc (XPU)
✅ **Supported**: Arc A-series discrete GPUs and iGPUs  
⚠️ **Performance Note**: May be slower than CPU for small models  
💡 **Optimization**: Install Intel Extension for PyTorch:
```bash
pip install intel-extension-for-pytorch
```

**Expected Performance (Intel Arc)**:
- CPU: Often faster for TTS workloads
- XPU without IPEX: 2-5x slower than CPU
- XPU with IPEX: Competitive with CPU

**Recommendation**: Use `device="cpu"` for Intel Arc iGPUs unless you have IPEX installed

### CPU
✅ **Universal fallback**: Works on all systems  
✅ **Good performance**: Especially for smaller models  
✅ **Recommended for**: Intel Arc iGPUs (without IPEX)

---

## 📊 Examples

### Example 1: Voice Cloning

```
1. Load reference audio → Qwen3-TTS VoiceClone
2. Set target_text: "Hello, this is a test of voice cloning"
3. Set device: "auto", precision: "bf16", model: "1.7B"
4. Output → Save Audio
```

### Example 2: Custom Voice with Specific Style

```
1. Qwen3-TTS CustomVoice
2. Set speaker: "Ryan"
3. Set text: "Welcome to the future of AI"
4. Set instruct: "Speak with excitement and energy"
5. Set device: "auto", precision: "bf16"
6. Output → Save Audio
```

### Example 3: Voice Design

```
1. Qwen3-TTS VoiceDesign
2. Set text: "Good morning everyone"
3. Set instruct: "A warm, elderly grandfather voice with a slight rasp"
4. Set device: "cuda", precision: "bf16", model: "1.7B"
5. Output → Save Audio
```

---

## 🔧 Troubleshooting

### Models Not Downloading
```bash
# Manually download models
from huggingface_hub import snapshot_download
snapshot_download(repo_id="Qwen/Qwen3-TTS-12Hz-1.7B-Base", 
                  local_dir="ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-1.7B-Base")
```

### Import Errors
```bash
# Reinstall dependencies
cd ComfyUI/custom_nodes/ComfyUI-Qwen3-TTS
pip install -r requirements.txt --force-reinstall
```

### Slow Performance on Intel Arc GPU
```bash
# Install IPEX for better performance
pip install intel-extension-for-pytorch

# Or use CPU instead
# Set device="cpu" in the node
```

### Out of Memory
- Use 0.6B model instead of 1.7B
- Set device to CPU
- Use BF16 precision
- Reduce max_new_tokens

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Alibaba Qwen Team](https://github.com/QwenLM) for the Qwen3-TTS models
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the amazing UI framework
- All contributors and users of this project

---

## 📮 Support

- **Issues**: [GitHub Issues](https://github.com/ai-joe-git/ComfyUI-Qwen3-TTS/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ai-joe-git/ComfyUI-Qwen3-TTS/discussions)

---

## 🗺️ Roadmap

- [ ] Add streaming audio generation
- [ ] Support for custom fine-tuned models
- [ ] Batch processing support
- [ ] Audio preview in ComfyUI
- [ ] More preset voices

---

<div align="center">

**Star ⭐ this repo if you find it useful!**

Made with ❤️ for the ComfyUI community

</div>
