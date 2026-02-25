# ComfyUI-For-ChatterBox

ComfyUI custom nodes for [Chatterbox TTS](https://github.com/resemble-ai/chatterbox) with **multilingual support (23 languages)**.

This is the only ComfyUI Chatterbox implementation that supports the multilingual model!

## Features

- **Multilingual TTS**: Support for 23 languages with language-specific text processing
- **Standard TTS**: High-quality English text-to-speech
- **Voice Conversion**: Convert voice timbre while preserving speech content
- **Voice Cloning**: Clone voices from reference audio prompts
- **ComfyUI Integration**: Full integration with ComfyUI's model management system

## Supported Languages

| Code | Language | Code | Language | Code | Language |
|------|----------|------|----------|------|----------|
| ar | Arabic | he | Hebrew | pl | Polish |
| da | Danish | hi | Hindi | pt | Portuguese |
| de | German | it | Italian | ru | Russian |
| el | Greek | ja | Japanese | sv | Swedish |
| en | English | ko | Korean | sw | Swahili |
| es | Spanish | ms | Malay | tr | Turkish |
| fi | Finnish | nl | Dutch | zh | Chinese |
| fr | French | no | Norwegian | | |

## Nodes

### Chatterbox Multilingual TTS
Generate speech in 23 languages with voice cloning support.

**Inputs:**
- `text`: Text to synthesize (max 300 characters)
- `language`: Target language selection
- `exaggeration`: Emotional expressiveness (0.25-2.0)
- `temperature`: Sampling randomness (0.05-5.0)
- `cfg_weight`: CFG guidance weight (0.0-1.0, set to 0 for language transfer)
- `audio_prompt`: Optional reference audio for voice cloning

### Chatterbox TTS
Standard English TTS with high quality output.

### Chatterbox Voice Conversion
Convert the voice in an audio file to match a target voice.

## Installation

### Method 1: ComfyUI Manager (Recommended)
Search for "ComfyUI-For-ChatterBox" in ComfyUI Manager and install.

### Method 2: Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-repo/ComfyUI-For-ChatterBox.git
cd ComfyUI-For-ChatterBox
pip install -r requirements.txt
```

## Model Downloads

Models are automatically downloaded from HuggingFace on first use:
- Standard TTS: `models/tts/chatterbox/resembleai_default_voice/`
- Multilingual TTS: `models/tts/chatterbox/resembleai_multilingual/`

## Tips for Best Results

### Language Transfer
When using a reference audio in a different language than the target:
- Set `cfg_weight` to 0 to mitigate accent transfer
- Use a reference audio that matches the target language for best quality

### Japanese
Japanese text is automatically converted to hiragana (kanji → hiragana, katakana preserved).

### Chinese
Chinese characters are converted to Cangjie codes for tokenization.

### Korean
Korean syllables are decomposed into Jamo for proper pronunciation.

## Optional Dependencies

- `resemble-perth`: Audio watermarking support
- `dicta_onnx`: Hebrew diacritization
- `russian_text_stresser`: Russian stress marking

## Credits

- [Chatterbox](https://github.com/resemble-ai/chatterbox) by Resemble AI
- ComfyUI community

## License

MIT License
