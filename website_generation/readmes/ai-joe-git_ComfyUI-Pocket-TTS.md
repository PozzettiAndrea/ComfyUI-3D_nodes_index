# ComfyUI-Pocket-TTS 🎙️

**Lightweight CPU-based Text-to-Speech for ComfyUI**

Fast, efficient TTS running at **6x real-time on CPU** without GPU requirements. Perfect for quick voice generation and prototyping!

---

## ✨ Features

- 🚀 **Fast**: ~200ms latency, 6x real-time on CPU
- 💻 **CPU Only**: No GPU needed (works on laptops!)
- 🎯 **Small Model**: Only 100M parameters
- 🎭 **8 Built-in Voices**: Ready to use
- 🔊 **Voice Cloning**: Use any audio file
- 📝 **Long Text**: Handles infinitely long inputs
- ⚡ **Low Memory**: Uses only 2 CPU cores

---

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Simple Pocket TTS"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Install

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ai-joe-git/ComfyUI-Pocket-TTS
cd ComfyUI-Pocket-TTS
pip install -r requirements.txt
```

---

## 🎮 Nodes

### 1. 🎙️ Pocket TTS (Simple)
**All-in-one node for quick TTS**
- Input: Text + Voice
- Output: Audio
- Auto-loads model, no setup needed

### 2. 🎙️ Pocket TTS Model Loader
**Load model with specific settings**
- Precision: float32/float16/bfloat16
- Outputs model for other nodes

### 3. 🎙️ Pocket TTS Generate
**Generate speech with built-in voices**
- 8 voices: alba, marius, javert, jean, fantine, cosette, eponine, azelma
- Fast generation

### 4. 🎙️ Pocket TTS Voice Clone
**Clone voice from audio file**
- Upload reference audio to `ComfyUI/input/`
- Generates speech in that voice

---

## 🎭 Built-in Voices

| Voice | Description |
|-------|-------------|
| **alba** | Alba Mackenna (default) |
| **marius** | Marius Pontmercy |
| **javert** | Inspector Javert |
| **jean** | Jean Valjean |
| **fantine** | Fantine |
| **cosette** | Cosette |
| **eponine** | Eponine |
| **azelma** | Azelma |

---

## 🔧 Usage Examples

### Basic Usage (Simple Node)

```
Text: "Hello world, this is a test."
Voice: alba
→ Audio Output
```

### Voice Cloning

1. Place audio file in `ComfyUI/input/my_voice.wav`
2. Use **Pocket TTS Voice Clone** node
3. Select `my_voice.wav`
4. Enter text
5. Get audio in your voice!

### Advanced (Model Loader)

```
[Model Loader] → [Generate] → [Audio Output]
   precision: float32
   voice: marius
   text: "Your text here"
```

---

## ⚡ Performance

Tested on MacBook Air M4:

| Metric | Value |
|--------|-------|
| **Latency** | ~200ms first chunk |
| **Speed** | 6x real-time |
| **CPU Cores** | 2 cores |
| **Model Size** | 100M params |
| **Memory** | ~400MB RAM |

---

## 🔄 Workflow Integration

Works with:
- ✅ **Video Helper Suite** - Save audio
- ✅ **Audio Processing Nodes** - Effects/mixing
- ✅ **Batch Processing** - Multiple voices
- ✅ **Animation Workflows** - Lip sync

---

## 🐛 Troubleshooting

### ❌ "No module named 'pocket_tts'"

```bash
# In ComfyUI venv:
pip install pocket-tts
```

### ❌ "No audio files found"

Place audio files in:
```
ComfyUI/input/
```

Supported: `.wav`, `.mp3`, `.flac`, `.ogg`

### ⚠️ Slow generation

- Use `float32` precision (fastest on CPU)
- Close other applications
- Check CPU isn't throttling

---

## 🆚 Comparison

| Feature | Pocket TTS | Other TTS |
|---------|-----------|-----------|
| **Device** | CPU only | GPU required |
| **Speed** | 6x RT | 2-4x RT |
| **Latency** | 200ms | 500ms+ |
| **Model Size** | 100M | 1B+ |
| **Setup** | 1-click | Complex |

---

## 📚 Credits

- **Pocket TTS**: [Kyutai Labs](https://github.com/kyutai-labs/pocket-tts)
- **Paper**: [Pocket TTS Research](https://kyutai.org)
- **ComfyUI Node**: ai-joe-git

---

## 📝 License

MIT License

---

## 🚀 Updates

### v1.0.0 (2026-01-25)
- Initial release
- 4 nodes
- 8 built-in voices
- Voice cloning support
- CPU-optimized

---

## 🤝 Contributing

PRs welcome! Areas for improvement:
- [ ] WebAssembly support
- [ ] Quantization (int8)
- [ ] More voices
- [ ] Streaming output

---

## ⚠️ Prohibited Use

Voice cloning requires **explicit consent**. Do not use for:
- ❌ Voice impersonation without consent
- ❌ Misinformation/fake news
- ❌ Harassment or hate speech
- ❌ Privacy violations

See [Pocket TTS license](https://github.com/kyutai-labs/pocket-tts) for full terms.

---

**Made with ❤️ for the ComfyUI community**
