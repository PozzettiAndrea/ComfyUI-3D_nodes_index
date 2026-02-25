# ComfyUI-Soprano-TTS

Ultra-lightweight, high-fidelity text-to-speech for ComfyUI using [Soprano TTS](https://github.com/ekwek1/soprano).

![Soprano TTS](https://img.shields.io/badge/Soprano-TTS-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![PyTorch](https://img.shields.io/badge/PyTorch-2.5.1-orange)

<img width="756" height="843" alt="image" src="https://github.com/user-attachments/assets/92aa3758-cef7-4977-86d7-209e12244bcf" />

[soprano_tts_00007.wav](https://github.com/user-attachments/files/24377355/soprano_tts_00007.wav)

## Features

- **Ultra-Fast**: ~100-200x real-time generation
- **High-Fidelity**: 32kHz crystal-clear audio
- **Lightweight**: <1GB VRAM usage, 80M parameters
- **All-in-One**: Integrated saving and playback with autoplay
- **ComfyUI Integration**: Full memory management & interrupt support
- **Easy Installation**: Works with PyTorch 2.5.1 (no ComfyUI breakage!)

## Quick Start

### Installation

```bash
# 1. Navigate to ComfyUI and activate your Python environment
cd /path/to/ComfyUI
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 2. Install soprano-tts WITHOUT dependencies (critical!)
pip install soprano-tts --no-deps

# 3. Install required dependency
pip install unidecode

# 4. Restart ComfyUI
```

**That's it!** The node uses transformers backend (scipy and transformers already in ComfyUI).

### Usage

1. Add **"Soprano TTS"** node (audio/generation category)
2. Enter text to synthesize
3. Run workflow — audio plays automatically!
4. *(Optional)* Connect audio output to other nodes for further processing

**First run**: Downloads model (~500MB) from HuggingFace, takes ~30 seconds, then cached.

## Node Parameters

### Generation Settings

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **text** | STRING | - | Text to convert to speech (2-15 sec sentences work best) |
| **temperature** | FLOAT | 0.3 | Lower = consistent, higher = varied (0.0-2.0) |
| **top_p** | FLOAT | 0.95 | Nucleus sampling threshold (0.0-1.0) |
| **repetition_penalty** | FLOAT | 1.2 | Reduces repetition (1.0-2.0) |
| **seed** | INT | -1 | Change to force regeneration (ComfyUI caching) |
| **keep_model_loaded** | BOOLEAN | False | Keep in VRAM for faster subsequent runs |

### Audio Output Settings

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **filename_prefix** | STRING | audio/soprano_tts | Path/prefix for saved files |
| **format** | ENUM | wav | Output format: wav, mp3, flac, ogg |
| **bitrate** | ENUM | 320k | Bitrate for mp3/ogg: 128k, 192k, 256k, 320k, VBR |
| **save** | BOOLEAN | True | Save to output folder (False = temp/preview only) |
| **autoplay** | BOOLEAN | True | Auto-play audio in the UI when generated |

### Output

- **audio** (AUDIO): 32kHz waveform compatible with ComfyUI audio nodes
- **Built-in player**: Audio plays directly in the node (with autoplay option)
- **Auto-save**: Files saved to `ComfyUI/output/audio/` with counters

## Tips for Best Results

✅ **DO:**
- Use sentences 2-15 seconds long
- Convert numbers to words ("1+1" → "one plus one")
- Use proper grammar and contractions
- Regenerate (change seed) if result isn't perfect

❌ **DON'T:**
- Use very long or very short sentences
- Include special characters (%, #, @, etc.)
- Use all caps or improper grammar
- Expect identical output each time (uses sampling)

## Why --no-deps Installation?

**The Problem**: Soprano TTS officially requires PyTorch 2.8+, but ComfyUI uses PyTorch 2.5.1. Installing normally upgrades PyTorch and **breaks ComfyUI** with errors like:

```
ImportError: undefined symbol: ncclMemFree
```

**The Solution**: Install with `--no-deps` to skip the problematic `lmdeploy` dependency. Soprano automatically falls back to the transformers backend, which works perfectly with PyTorch 2.5.1!

| Backend | Speed | PyTorch | Status |
|---------|-------|---------|--------|
| lmdeploy | ~2000x real-time | 2.8.0+ | ❌ Breaks ComfyUI |
| transformers | ~100-200x real-time | 2.5.1+ | ✅ Works! |

Even at 100-200x, generating 10 seconds of audio takes **less than 1 second**!

## Troubleshooting

### "No module named 'soprano'"

```bash
pip install soprano-tts --no-deps
pip install unidecode
```

### ComfyUI won't start after installing

Your PyTorch got upgraded accidentally. Fix it:

```bash
# Remove conflicting packages
pip uninstall -y lmdeploy torch triton

# Reinstall correct PyTorch for ComfyUI
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 \
  --extra-index-url https://download.pytorch.org/whl/cu121
pip install xformers==0.0.29.post1
```

### Model download fails

- Check internet connection and HuggingFace access
- Need ~500MB free disk space
- Ensure `huggingface-hub` is installed: `pip install huggingface-hub`

### Poor audio quality

- Lower `temperature` (try 0.2)
- Convert numbers/symbols to words
- Ensure sentences are 2-15 seconds
- Regenerate with different seed

### Node not appearing in ComfyUI

- Restart ComfyUI completely
- Check console for loading errors
- Run test: `python test_compat.py`

## Test Your Installation

```bash
cd /path/to/ComfyUI/custom_nodes/ComfyUI-Soprano-TTS
python test_compat.py
```

Should output: `✅ ALL TESTS PASSED! Soprano TTS should work!`

If tests fail, the script provides specific fix commands.

## Technical Details

### Compatibility Layer

The node includes `soprano_compat.py` which:
- Checks PyTorch version (requires 2.5.0+)
- Patches `torch.compiler.disable` if needed (usually not needed for 2.5.1)
- Auto-applies on import

### ComfyUI Integration

- **Memory Management**: Properly loads/unloads models, cleans CUDA cache
- **Interrupt System**: Respects user cancellation during generation
- **Audio Format**: Returns standard ComfyUI AUDIO (waveform + sample_rate)
- **Model Caching**: Downloads once, reuses forever

### Performance

- **Backend**: transformers (HuggingFace)
- **Speed**: ~100-200x real-time
- **Quality**: 32kHz, perceptually indistinguishable from 44.1/48kHz
- **VRAM**: <1GB (80M parameters)
- **Latency**: First token in ~100ms, total generation <1s for 10s audio

### Limitations

- No streaming mode (transformers backend limitation)
- No voice cloning (Soprano limitation)
- No multilingual support yet (Soprano limitation)
- May occasionally mispronounce numbers/special characters

## Example Workflow

See `workflows/example_workflow.json` for a complete example.

## Credits

This node wraps the excellent **Soprano TTS** project:

- **Original Project**: [github.com/ekwek1/soprano](https://github.com/ekwek1/soprano)
- **Model**: [huggingface.co/ekwek/Soprano-80M](https://huggingface.co/ekwek/Soprano-80M)
- **Developer**: [ekwek1](https://github.com/ekwek1) (impressive work from a second-year undergrad!)

### Soprano Acknowledgements

Soprano uses and/or is inspired by:
- [Vocos](https://github.com/gemelo-ai/vocos) - Vocoder architecture
- [XTTS](https://github.com/coqui-ai/TTS) - TTS inspiration
- [LMDeploy](https://github.com/InternLM/lmdeploy) - Acceleration (optional)

## Requirements

- **OS**: Linux or Windows
- **GPU**: CUDA-enabled (CPU support coming to Soprano)
- **PyTorch**: 2.5.0+ (tested with 2.5.1+cu121)
- **VRAM**: <1GB
- **Disk**: ~500MB for model cache
- **pydub**: For integrated audio saving/playback (`pip install pydub`)
- **ffmpeg**: Required by pydub for MP3/FLAC/OGG export

## License

This ComfyUI node wrapper is licensed under **Apache-2.0**, matching the original Soprano project.

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Support

- **Node Issues**: [Open an issue](https://github.com/YOUR_USERNAME/ComfyUI-Soprano-TTS/issues)
- **Soprano TTS Issues**: [Original project](https://github.com/ekwek1/soprano/issues)

## Changelog

### v1.0.0 (Initial Release)
- Full Soprano TTS integration
- PyTorch 2.5.1 compatibility via transformers backend
- ComfyUI memory management & interrupt support
- Automatic model downloading
- Comprehensive error handling and testing

---

**Built with ❤️ for the ComfyUI community**

*Ultra-fast, high-fidelity speech synthesis in your workflows!*
