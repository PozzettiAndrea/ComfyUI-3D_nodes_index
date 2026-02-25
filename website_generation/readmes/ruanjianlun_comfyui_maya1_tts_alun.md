# 🎙️ Maya1 TTS ComfyUI Custom Node

[中文文档](README.zh-CN.md) | English

A high-quality text-to-speech (TTS) ComfyUI custom node powered by the Maya1 model, featuring multiple voice styles and flexible parameter configuration.

## ✨ Features

- 🎵 **High-Quality Speech Synthesis**: Based on the advanced Maya1 voice generation model
- 🎨 **Multiple Voice Styles**: 5 built-in voice presets (male, female, different ages)
- 🔧 **Flexible Parameters**: Adjustable temperature, chunk length, and more
- 💾 **Automatic Model Management**: Models auto-download and cache to ComfyUI models directory
- ⚡ **Smart Caching**: Models load once for improved generation efficiency
- 🌐 **International Support**: English UI and logging

## 📦 Installation

### Method 1: Clone directly to ComfyUI custom nodes directory

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/ruanjianlun/comfyui_maya1_tts_alun.git
cd comfyui_alun_maya1
pip install -r requirements.txt
```

### Method 2: Manual Installation

1. Copy the entire project folder to `ComfyUI/custom_nodes/` directory
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Dependencies

Main dependencies include:

- `transformers` - Hugging Face model library
- `torch` - PyTorch deep learning framework
- `snac` - SNAC audio codec
- `soundfile` - Audio file processing
- `numpy` - Numerical computing

## 🚀 Usage

### 1. Add Node in ComfyUI

1. Launch ComfyUI
2. Right-click on canvas, select `Add Node` -> `audio` -> `maya1` -> `Maya1 Text to Speech`
3. The node will appear on the canvas

### 2. Configure Node Parameters

The node provides the following parameters:

| Parameter                    | Type              | Description                                            | Default                    |
| ---------------------------- | ----------------- | ------------------------------------------------------ | -------------------------- |
| **text**               | String            | Text to convert to speech                              | "Hello, this is a test..." |
| **voice_preset**       | Dropdown          | Voice style preset                                     | Male-Mature                |
| **chunk_length**       | Integer           | Text chunk length (characters)                         | 50                         |
| **temperature**        | Float             | Generation temperature (0.1-1.0, higher = more random) | 0.4                        |
| **custom_description** | String (Optional) | Custom voice description                               | Empty                      |

### 3. Voice Style Presets

5 built-in voice style presets:

- **Male-Mature**: Male voice around 30 years old, American accent, normal pitch, warm timbre
- **Female-Gentle**: Female voice around 20 years old, American accent, slightly high pitch, soft timbre
- **Male-Energetic**: Male voice around 20 years old, American accent, high energy, bright timbre
- **Female-Professional**: Female voice around 30 years old, British accent, professional tone, clear timbre
- **Neutral-Broadcast**: Neutral voice, standard accent, clear articulation, balanced timbre

### 4. Custom Voice Description

If presets don't meet your needs, use the `custom_description` parameter for custom voice characteristics:

```
Realistic male voice in the 40s age with british accent. 
Deep pitch, authoritative tone, slow pacing.
```

Description template:

- **Age**: in the 20s/30s/40s age
- **Accent**: american/british/australian accent
- **Pitch**: high/normal/low/deep pitch
- **Timbre**: warm/bright/soft/clear timbre
- **Pacing**: fast/moderate/slow/conversational pacing
- **Style**: energetic/professional/gentle/authoritative tone

## 📁 Project Structure

```
comfyui_alun_maya1/
├── __init__.py              # Node registration entry file
├── maya_tts_node.py         # Main node implementation
├── config.py                # Configuration file (model paths, constants, etc.)
├── requirements.txt         # Python dependencies list
├── workflow_example.json    # ComfyUI workflow example
├── README.md               # Project documentation (English)
└── README.zh-CN.md         # Project documentation (Chinese)
```

## 🔧 Configuration

### Model Storage Location

Models will auto-download to:

```
ComfyUI/models/maya1_tts_alun/
```

Includes the following model files:

- Maya1 main model (~4GB)
- Maya1 tokenizer
- SNAC audio decoder (~200MB)

### Output File Location

Generated audio files are saved to:

```
ComfyUI/output/maya_tts_XXXXXX.wav
```

File naming format: `maya_tts_{timestamp}.wav`

### Audio Specifications

- **Sample Rate**: 24000 Hz
- **Format**: WAV (16-bit PCM)
- **Channels**: Mono

## 📊 Workflow Example

The project includes a basic workflow example `workflow_example.json`, demonstrating how to:

1. Use the Maya1 TTS node to generate speech
2. Save the generated audio file
3. Preview and play the audio

### Import Workflow

1. Open ComfyUI
2. Click the `Load` button
3. Select the `workflow_example.json` file
4. Click `Queue Prompt` to start generation

## ⚙️ Advanced Configuration

### Modify Default Model Path

Edit the `get_maya_model_path()` function in `config.py`:

```python
def get_maya_model_path():
    # Custom model path
    return "/your/custom/path/to/models"
```

### Add New Voice Presets

Add to the `VOICE_PRESETS` dictionary in `config.py`:

```python
VOICE_PRESETS = {
    # ... existing presets
    "Custom-Preset-Name": "Your custom voice description here",
}
```

### Clear Model Cache

To free up VRAM, call:

```python
from config import clear_model_cache
clear_model_cache()
```

## 🐛 Common Issues

### Q1: First run is very slow?

**A**: First run requires downloading models (~4GB), please be patient. Models cache locally, subsequent usage will be much faster.

### Q2: Out of memory errors?

**A**:

- Reduce the `chunk_length` parameter (e.g., change to 30)
- Close other VRAM-consuming programs
- Use CPU mode (auto-detects, no configuration needed)

### Q3: Generated speech quality is not ideal?

**A**:

- Adjust the `temperature` parameter (0.3-0.5 usually works well)
- Try different voice presets
- Use custom descriptions for more precise voice characteristics
- Ensure input text has correct grammar and punctuation

### Q4: Does it support Chinese?

**A**: Current version primarily supports English text-to-speech, Chinese support is limited. Recommended to use English text for best results.

### Q5: How to speed up generation?

**A**:

- Ensure using GPU (CUDA)
- Reduce `chunk_length` (but may affect speech continuity)
- Lower `temperature` value
- Process long text in segments

## 🔄 Changelog

### v1.0.0 (2025-01-09)

- ✨ Initial release
- 🎵 Support for Maya1 text-to-speech
- 🎨 5 built-in voice presets
- 🔧 Flexible parameter configuration
- 📁 Automatic model management
- 🌐 Complete English support

## 📄 License

This project is open source under the MIT License.

## 🙏 Acknowledgments

- [Maya Research](https://github.com/maya-research) - Maya1 model
- [Hugging Face](https://huggingface.co/) - Model hosting
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Workflow platform

## 📮 Contact

- Author: Alun
- Issues: Please submit on GitHub Issues

## 🌟 Support the Project

If this project helps you, please:

- ⭐ Star the project
- 🐛 Report bugs
- 💡 Suggest new features
- 🤝 Contribute code

---

**Enjoy high-quality speech synthesis!** 🎉
