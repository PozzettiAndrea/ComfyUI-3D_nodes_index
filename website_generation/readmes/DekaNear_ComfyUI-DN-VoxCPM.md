# ComfyUI-DN-VoxCPM

VoxCPM custom nodes for ComfyUI - High-quality Text-to-Speech with Audio Reference

**By DekaNear** - [GitHub](https://github.com/DekaNear)

## Features

- 🎙️ **Audio Reference** - Generate speech using reference audio for voice characteristics
- 🗣️ **Text-to-Speech** - Generate natural-sounding speech from text
- 🎯 **ASR Recognition** - Automatic speech recognition for transcription
- 🔄 **Batch Processing** - Process multiple texts at once
- 🎨 **Easy to Use** - Simple ComfyUI nodes with clear inputs/outputs

## Installation

### Option 1: ComfyUI Registry (Recommended)

Install directly from ComfyUI Manager:

1. Open ComfyUI Manager
2. Search for "DN VoxCPM" or "VoxCPM"
3. Click Install
4. Restart ComfyUI

### Option 2: Manual Installation

Clone this repository into your ComfyUI custom_nodes folder:

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/DekaNear/ComfyUI-DN-VoxCPM.git
cd ComfyUI-DN-VoxCPM
pip install -r requirements.txt
```

Restart ComfyUI after installation.

## Available Nodes

### Basic Nodes

#### 1. VoxCPM Model Loader
Load the VoxCPM model for text-to-speech synthesis.

**Inputs:**
- `model_source`: "huggingface" or "local"
- `model_id`: Model ID (default: "openbmb/VoxCPM1.5")
- `enable_denoiser`: Enable audio denoising
- `optimize`: Use torch.compile for faster inference

**Outputs:**
- `model`: Loaded VoxCPM model

**Note:** Models are downloaded automatically from HuggingFace on first use. The download may take a few minutes depending on your internet connection.

#### 2. VoxCPM Text-to-Speech
Generate speech from text without audio reference.

**Inputs:**
- `model`: VoxCPM model
- `text`: Text to synthesize
- `cfg_value`: Classifier-free guidance (1.0-3.0, default: 2.0)
- `inference_timesteps`: Number of diffusion steps (4-30, default: 10)
- `normalize`: Normalize output audio
- `retry_badcase`: Retry if generation fails

**Outputs:**
- `audio`: Generated audio

#### 3. VoxCPM Audio Reference
Generate speech using a reference audio for voice characteristics.

**Inputs:**
- `model`: VoxCPM model
- `text`: Text to synthesize
- `prompt_audio`: Reference audio (AUDIO type)
- `prompt_text`: Transcription of reference audio
- `cfg_value`: Classifier-free guidance (default: 2.0)
- `inference_timesteps`: Diffusion steps (default: 10)
- `normalize`: Normalize output
- `denoise_prompt`: Denoise reference audio

**Outputs:**
- `audio`: Generated audio with reference voice characteristics

#### 4. VoxCPM Streaming TTS
Generate speech in streaming mode for real-time applications.

**Inputs:**
- Same as Audio Reference, but optional prompt audio/text

**Outputs:**
- `audio`: Streamed audio (concatenated)

#### 5. VoxCPM Save Audio
Save generated audio to a WAV file.

**Inputs:**
- `audio`: Audio to save
- `filename`: Output filename (default: "output.wav")
- `output_dir`: Optional custom output directory

**Outputs:**
- None (saves to disk)

#### 6. VoxCPM ASR Recognition
Automatic speech recognition for transcribing audio.

**Inputs:**
- `audio`: Audio to transcribe (AUDIO type)

**Outputs:**
- `transcription`: Recognized text

### Advanced Nodes

#### 7. VoxCPM Batch TTS
Process multiple texts at once with the same settings.

#### 8. VoxCPM Batch Save Audio
Save multiple audio files from batch generation.

#### 9. VoxCPM Concatenate Audio
Combine multiple audio clips with optional silence between them.

#### 10. VoxCPM Text From File
Load text from .txt or .json files.

#### 11. VoxCPM Model Info
Display information about the loaded model.

### Utility Nodes

#### 12. VoxCPM Load Audio
Load audio from file path and convert to ComfyUI AUDIO format.

**Features:**
- Auto-searches in ComfyUI/input/ folder
- Supports WAV, MP3, FLAC, OGG, and more
- Automatic stereo to mono conversion
- Just use filename if file is in ComfyUI/input/

#### 13. VoxCPM Audio Converter
Convert audio from ComfyUI's LoadAudio to proper format for VoxCPM nodes.

**Use case:** Place between LoadAudio and VoxCPM nodes if you get "audio too short" errors.

## Quick Start

### Basic Text-to-Speech

```
[VoxCPM Model Loader] → [VoxCPM Text-to-Speech] → [VoxCPM Save Audio]
```

### Using Audio Reference

**Option 1: Using VoxCPM Load Audio (Recommended)**
```
1. Put your audio file in ComfyUI/input/my_voice.mp3

2. Workflow:
[VoxCPM Model Loader]
        ↓
[VoxCPM Load Audio]
   audio_path: "my_voice.mp3"
        ↓
   ├─→ [VoxCPM ASR Recognition]
   │         ↓
   │   (transcription)
   │         ↓
   └─→ [VoxCPM Audio Reference] ← (model)
             ↓
      [VoxCPM Save Audio]
```

**Option 2: Using ComfyUI LoadAudio**
```
[LoadAudio] → [VoxCPM Audio Converter] → [VoxCPM ASR Recognition]
                                                ↓
                                         [VoxCPM Audio Reference]
```

## Audio Loading Guide

### Where to Put Audio Files

**Recommended:** Put your audio files in `ComfyUI/input/` folder

Then in VoxCPM Load Audio, just write the filename:
```
my_audio.mp3
```

The node will find it automatically!

### Alternative: Full Path

You can also use full paths:
- Windows: `C:/Users/YourName/audio/file.mp3`
- Linux/Mac: `/home/user/audio/file.mp3`

### Supported Formats

- ✅ WAV (recommended)
- ✅ MP3
- ✅ FLAC
- ✅ OGG
- ✅ M4A
- ✅ Most common audio formats

### Audio Requirements

**For Audio Reference:**
- Duration: 3-10 seconds (ideal)
- Quality: Clear voice, minimal background noise
- Format: Any supported format

**For ASR Recognition:**
- Minimum: 0.1 seconds
- Recommended: 3-10 seconds
- Content: Clear speech

## Tips & Best Practices

1. **Audio Quality:** Better quality reference audio = better results
2. **Audio Length:** 3-10 seconds is ideal for audio reference
3. **File Location:** Put files in `ComfyUI/input/` for easy access
4. **Use ASR:** Let ASR transcribe your reference audio automatically
5. **Batch Processing:** Use Batch TTS for multiple texts with same voice
6. **Denoising:** Enable denoiser for cleaner output

## Configuration

Default settings are in `config.py`. You can modify:
- Default CFG values
- Inference timesteps
- Model paths
- Output directories

## Requirements

- Python 3.8+
- PyTorch 2.0+
- ComfyUI updated to latest version
- See `requirements.txt` for full list

## Credits

- **VoxCPM:** [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)
- **ComfyUI:** [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## License

Apache License 2.0

## Support

For issues and questions:
1. Check this README
2. Check error messages in console
3. Open an issue on [GitHub](https://github.com/DekaNear/ComfyUI-VoxCPM-DN/issues)

---

**Made  by DekaNear**  
**Version:** 1.0.0  
**Last Updated:** 2025-12-11