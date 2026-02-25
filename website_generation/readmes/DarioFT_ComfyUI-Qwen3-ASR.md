# ComfyUI-Qwen3-ASR

ComfyUI custom nodes for **Qwen3-ASR** (Automatic Speech Recognition) - audio-to-text transcription supporting 52 languages and dialects.

> 🔗 Compatible with [ComfyUI-Qwen3-TTS](https://github.com/DarioFT/ComfyUI-Qwen3-TTS) for complete speech workflows

<p align="center">
    <img src="https://raw.githubusercontent.com/DarioFT/ComfyUI-Qwen3-ASR/refs/heads/main/assets/intro.png"/>
<p>

## Features

- **Multi-language**: 30 languages + 22 Chinese dialects
- **Two model sizes**: 1.7B (best quality) and 0.6B (faster)
- **Auto language detection**: No need to specify language
- **Timestamps**: Optional word/character-level timing via Forced Aligner
- **Batch processing**: Transcribe multiple audio files
- **Auto-download**: Models download automatically on first use

## Installation

### Via ComfyUI Manager (Recommended)
Search for "Qwen3-ASR" in ComfyUI Manager

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DarioFT/ComfyUI-Qwen3-ASR.git
cd ComfyUI-Qwen3-ASR
pip install -r requirements.txt
```

## Nodes

### Qwen3-ASR Loader
Loads the ASR model with auto-download support.

| Input | Type | Description |
|-------|------|-------------|
| repo_id | dropdown | Model: 1.7B or 0.6B |
| source | dropdown | HuggingFace or ModelScope |
| precision | dropdown | fp16, bf16, fp32 |
| attention | dropdown | auto, flash_attention_2, sdpa, eager |
| forced_aligner | dropdown | Optional aligner for timestamps |
| local_model_path | string | Optional custom model path |

### Qwen3-ASR Transcribe
Transcribes a single audio input to text.

| Input | Type | Description |
|-------|------|-------------|
| model | QWEN3_ASR_MODEL | Loaded model |
| audio | AUDIO | Audio input (ComfyUI format) |
| language | dropdown | Force language or "auto" |
| context | string | Optional context hints |
| return_timestamps | boolean | Enable timestamp output |

| Output | Type | Description |
|--------|------|-------------|
| text | STRING | Transcribed text |
| language | STRING | Detected language |
| timestamps | STRING | Word-level timestamps (if enabled) |

### Qwen3-ASR Batch Transcribe
Batch transcription for multiple audio files.

## Supported Languages

Chinese, English, Cantonese, Arabic, German, French, Spanish, Portuguese, Indonesian, Italian, Korean, Russian, Thai, Vietnamese, Japanese, Turkish, Hindi, Malay, Dutch, Swedish, Danish, Finnish, Polish, Czech, Filipino, Persian, Greek, Hungarian, Macedonian, Romanian

Plus 22 Chinese dialects including Sichuan, Cantonese (HK/Guangdong), Wu, Minnan, and regional accents.

## Workflow Examples

### Basic Transcription
```
LoadAudio → Qwen3-ASR Loader → Qwen3-ASR Transcribe → ShowText
```

### With TTS (Speech-to-Speech)
```
LoadAudio → Qwen3-ASR Transcribe → [process text] → Qwen3-TTS → SaveAudio
```

## Model Storage

Models are stored in: `ComfyUI/models/Qwen3-ASR/`

## Credits

- [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) by Alibaba Qwen Team
- [qwen-asr](https://pypi.org/project/qwen-asr/) Python package

## License

Apache-2.0
