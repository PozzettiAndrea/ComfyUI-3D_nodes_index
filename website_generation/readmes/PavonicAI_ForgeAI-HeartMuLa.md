# ForgeAI HeartMuLa — ComfyUI Custom Nodes

All-in-one music generation node for ComfyUI, powered by [HeartMuLa](https://heartmula.github.io/).

**Works on 16 GB VRAM GPUs** (RTX 4060 Ti, RTX 5070 Ti, etc.) with built-in 4-bit quantization.

## Nodes

### ForgeAI Music Generator
Generate music from lyrics and genre tags in a single node.

- **Inputs**: Lyrics, Tags (genre/style), Duration, Quantization, Temperature, Top-K, CFG Scale, Output Format
- **Outputs**: Audio (ComfyUI AUDIO type) + File Path (saved WAV/MP3)
- **Quantization**: none / 4-bit NF4 / 8-bit (select in node)

### ForgeAI Lyrics Transcriber
Transcribe lyrics from audio using Whisper.

- **Input**: Audio (ComfyUI AUDIO type)
- **Output**: Transcribed lyrics text

## Tag Guide

HeartMuLa uses comma-separated tags to control the style of generated music. **Genre is the most important tag** — always put it first.

### Tag Format
```
genre:pop, emotional, synth, warm, female voice
```

### Available Tag Categories

| Category | Examples | Priority |
|---|---|---|
| **Genre** | `pop`, `rock`, `electronic`, `jazz`, `reggae`, `j-pop` | Highest |
| **Timbre** | `synth`, `acoustic`, `warm`, `bright`, `deep` | High |
| **Gender** | `male voice`, `female voice` | High |
| **Mood** | `emotional`, `energetic`, `chill`, `dark`, `happy` | Medium |
| **Instrument** | `piano`, `guitar`, `bass`, `drums`, `strings` | Medium |
| **Scene** | `dance`, `ballad`, `anthem`, `lullaby` | Low |
| **Region** | `latin`, `french`, `japanese`, `korean` | Low |
| **Tempo** | `fast tempo`, `slow tempo`, `moderate tempo` | Low |

### Structure Tags (in Lyrics field)
Use structure tags in your lyrics to control song sections:
```
[intro]
[verse]
Your verse lyrics here...
[chorus]
Your chorus lyrics here...
[bridge]
Bridge lyrics...
[outro]
```

### Multi-Language Lyrics
HeartMuLa supports lyrics in multiple languages including English, Spanish, French, Japanese, and more. Simply write your lyrics in the desired language.

## CFG Scale Guide

CFG (Classifier-Free Guidance) controls how strictly the model follows your tags. Range: **1.0 — 10.0**

| CFG | Best For | Notes |
|---|---|---|
| **2.0** | Pop, Ballads, Emotional | Sweet spot for clean vocals |
| **3.0** | Rock, Latin, Uptempo | More energy, stronger instrumentation |
| **4.0+** | Electronic, Dance, EDM | Bold sound, may introduce artifacts |
| **5.0+** | Experimental | Use with caution |

**Recommendation:** Start with **CFG 2.0** and increase if you need more energy or harder genres.

## Installation

### 1. Clone into ComfyUI custom_nodes
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/PavonicAI/ForgeAI-HeartMuLa.git
```

### 2. Install dependencies
```bash
pip install -r ForgeAI-HeartMuLa/requirements.txt
```

### 3. Download models

**Recommended: Use our pre-quantized 4-bit checkpoint (fits on 16 GB GPUs):**

Download [**ForgeAI/HeartMuLa-3B-4bit**](https://huggingface.co/PavonicAI/HeartMuLa-3B-4bit) and place in `ComfyUI/models/HeartMuLa/HeartMuLa-oss-3B/`

You also need HeartCodec + tokenizer from the [original repo](https://huggingface.co/HeartMuLa/HeartMuLa-oss-3B):

```
ComfyUI/models/HeartMuLa/
  ├── HeartMuLa-oss-3B/    ← our 4-bit checkpoint OR original weights
  ├── HeartCodec-oss/       ← from original repo
  ├── tokenizer.json        ← from original repo
  └── gen_config.json       ← from original repo
```

## Compatibility Fixes Included

All fixes are applied automatically — no manual patching needed:

| Issue | Status |
|---|---|
| `ignore_mismatched_sizes` (transformers 5.x) | Fixed |
| `RoPE cache not built` (torchtune >= 0.5) | Fixed |
| OOM on 16 GB GPUs | Fixed (model CPU offload) |
| `torchcodec` missing (torchaudio >= 2.10) | Fixed (uses soundfile) |
| CFG 1.0 crash (batch_size mismatch) | Fixed (auto-clamp to 1.1) |

## Hardware Tested

- NVIDIA RTX 5070 Ti (16 GB) with 4-bit quantization
- Stable for hours of continuous generation
- ~13 GB VRAM during generation, ~8 GB during encoding

## License

Apache-2.0

## Credits

- Original HeartMuLa model by [HeartMuLa Team](https://heartmula.github.io/)
- ComfyUI nodes & compatibility fixes by [ForgeAI](https://huggingface.co/PavonicAI)
