<div align="center">

# 🎤 Qwen-TTS Nodes for ComfyUI

![Qwen-TTS Banner](https://img.shields.io/badge/Qwen3--TTS-Advanced%20TTS%20System-blue)
![ComfyUI Compatible](https://img.shields.io/badge/ComfyUI-Custom%20Nodes-green)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
  
  **Nodes to integrate Qwen3-TTS into ComfyUI with emotion support and voice cloning**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Models-yellow)](https://huggingface.co/Qwen)

</div>

---

## 📋 Summary

- [✨ Features](#-Features)
- [🚀 Install](#-install)
- [🎯 Nodes](#-nodes)
- [🎨 Example Workflow](#-example-workflow)
- [🔧 Model parameters](#-model-parameters)
- [📁 Project structure](#-project-structure)
- [❓ Frequently asked questions](#-frequently-asked-questions)
- [📄 License](#-license)

---

## ✨ Features

<div align="center">
  <img src="https://raw.githubusercontent.com/SLVGITHUB/QWEN3_TTS_DVA/main/images/features.png" alt="Qwen-TTS" width="800"/>
</div>

- 🎭 **Support of emotions** - synthesis of speech with different emotional colors
- 🎤 **Voice cloning** - creation of voice duets from reference audio
- 🌍 **Multilingual** - support for Russian, English and other languages
- ⚡ **High performance** - optimization for CUDA and CPU
- 🎨 **Flexible setting** - fine adjustment of synthesis parameters
- 🔄 **Batch processing** - mass audio file generation

---

## 🚀 Installation

### Method 1: Through ComfyUI Manager (recommended)

1. Open **ComfyUI Manager**
2. Go to **Custom Nodes Install**   **Install via Git URL**
3. Enter the URL: https://github.com/SLVGITHUB/QWEN3_TTS_DVA
4. Press **Install**
5. Restart the ComfyUI

### Method 2: Manual Installation

`bash
# Clone repository to custom_nodes directory
cd ComfyUI/custom_nodes
git clone https://github.com/SLVGITHUB/QWEN3_TTS_DVA.git

# Set dependencies
pip install -r requirements.txt
# Or set manually
pip install qwen-tts soundfile openai-whisper faster_whisper
`

### Requirements

- Python 3.8+
- ComfyUI latest version
- PyTorch 2.0+
- Video card with CUDA support (recommended) or CPU

---

## 🎯 Nodes

### 📦 Qwen TTS Loader
**Downloads Qwen-TTS speech model to memory**

<div align="center">
  <img src="https://raw.githubusercontent.com/SLVGITHUB/QWEN3_TTS_DVA/main/images/model_loader.png" alt="Model Loader" width="400"/>
</div>

**Supported models:**
- «Qwen3-TTS-Base`- for voice cloning
- «Qwen3-TTS-CustomVoice» - a synthesis called speaker
- «Qwen3-TTS-VoiceDesign» - text description synthesis

**Parameters:**
- **Calculation accuracy**: fp16, bf16, fp32
- **Device**: CUDA, CPU
-**Type of attention**: standard, optimized

---

### 🎤 Qwen TTS Generate
**Generates speech from text without reference audio**

<div align="center">
  <img src="https://raw.githubusercontent.com/SLVGITHUB/QWEN3_TTS_DVA/main/images/text_to_speech.png" alt="Speech Generation" width="400"/>
</div>

**Features:**
- Support languages: Russian, English, Chinese, Japanese and others
- Emotional presets: neutral, cheerful, sad, angry, scared
- Extended parameters: temperature, top-p, sample length
- For CustomVoice: specifying the speaker’s name (e.g., "Vivian", "Alex", "Maya")

---

### 🎭 Qwen TTS Voice Clone
**Clones voice from reference audio file**

<div align="center">
  <img src="https://raw.githubusercontent.com/SLVGITHUB/QWEN3_TTS_DVA/main/images/voice_cloning.png" alt="Voice cloning" width="400"/>
</div>

**Requirements:**
- Input audio (reference) - WAV, MP3, FLAC
- Audio text (ref_text)
- New text for synthesis

**Perfect for:**
- Voice doubling
- Voice-overs of content with a unique voice
- Remaking of historical speeches

**Attention!!! Reference audio must be in the following format: mono, 44.1kHz, PCM, 16bit**


---

### 📚 Qwen TTS Batch Generate
**Generates multiple audio files per run**

<div align="center">
  <img src="https://raw.githubusercontent.com/SLVGITHUB/QWEN3_TTS_DVA/main/images/batch_generation.png" alt="Batch generation" width="400"/>
</div>

**Functional:**
- Split text by specified separator (default is "|")
- Parallel or sequential processing
- Automatic file numbering
- Support of different parameters for each segment

---

### 💾 Qwen TTS Audio Saver
**Saves generated audio to disk**

<div align="center">
  <img src="https://raw.githubusercontent.com/SLVGITHUB/QWEN3_TTS_DVA/main/images/audio_saver.png" alt="Save audio" width="400"/>
</div>

**Save settings:**
- Format: WAV (16-bit, 24kHz)
- Destination folder: «ComfyUI/output/tts/
- Automatic file deletion
- Metadata in JSON format
- Overwrite or incremental save

---

### 🔀 Qwen TTS Emotion Mixer
**Mixes options with different emotions**

<div align="center">
  <img src="https://raw.githubusercontent.com/SLVGITHUB/QWEN3_TTS_DVA/main/images/emotion_mixer.png" alt="Mixing emotions" width="400"/>
</div>

**Application:**
- Creating complex emotional transitions
- Mixing 70% "calm" + 30% "energetic"
- Real-time adjustment of weights
- Normalization of the sum of weights up to 1.0

---

## 🎨 Example Workflow

<div align="center">
  <img src="https://raw.githubusercontent.com/SLVGITHUB/QWEN3_TTS_DVA/main/images/workflow.png" alt="workflow" width="400"/>
</div>


**Typical use case:**
1. Upload the model via **Qwen TTS Loader**
2. Generate speech via **Qwen TTS Generate**
3. Set the save settings to **Qwen TTS Audio Saver**
4. Start workflow

---

## 🔧 Model Parameters

### Recommended settings

| Parameter | Qwen3-TTS-Base | Qwen3-TTS-CustomVoice | Qwen3-TTS-VoiceDesign |
|--------|_____________|_______|
| Temperature | 0.6-0.8 | 0.7-0.9 | 0.7-0.9 |
| Top-P | 0.8-0.95 | 0.85-0.98 | 0.85-0.98 |
| Sample length | 2048 | 1024 | 1024 |

### Supported languages

- 🇷🇺 Russian (ru)
- 🇺🇸 English (en)
- 🇨🇳 Chinese (zh)
- 🇯🇵 Japanese (ja)
- 🇰🇷 Korean (ko)
- 🇫🇷 French (fr)
- 🇩🇪 German (de)
- 🇪🇸 Spanish (es)

---

## 📁 Project structure

`
QWEN3_TTS_DVA/
qwen_tts_comfy/
nodes.py   # Basic ComfyUI Nodes
__init__.py
requirements.txt   # Python dependencies
README.md
examples/
workflows/
audio_samples/
images/   # Images for documentation
License
`

---

## ❓ Frequently asked questions

### ❓ Which model to choose?
- For voice cloning: **Qwen3-TTS-Base**
- For ready voices: **Qwen3-TTS-CustomVoice**
- To create unique voices: **Qwen3-TTS-VoiceDesign**

### ❓ Why does it work slowly on the CPU?
TTS models require significant computing resources. It is recommended to use a GPU with CUDA support.

### ❓ How to improve synthesis quality?
- Use longer reference audio for cloning
- Experiment with temperature parameters and top-p
- Use emotional presets for expressiveness

### ❓ Are other audio formats supported?
Input audio: WAV, MP3, FLAC, OGG
Audio output: WAV (standard), can be converted through additional nodes

---

## 📄 License

This project is distributed under the Apache 2.0. license.

---

## 🔗 Useful links

<div align="center">

[🌐 Official Qwen3-TTS Repository](https://github.com/QwenLM/Qwen3-TTS) |
[🤗 Models on Hugging Face](https://huggingface.co/collections/Qwen/qwen3-tts) |
[💬 Problem Discussion](https://github.com/SLVGITHUB/QWEN3_TTS_DVA/issues)

</div>

---

## 🤝 Contribution to the project

Welcome:
- Error messages
- Proposals for improvement
- Pull requests
- Sample workflows

---

<div align="center">

**Created with ❤️ for ComfyUI community**

⭐ If you like this project, put a star on GitHub!

</div>













