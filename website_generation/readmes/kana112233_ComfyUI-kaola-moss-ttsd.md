# ComfyUI-kaola-moss-tts

A ComfyUI custom node pack for the [MOSS-TTS Family](https://github.com/OpenMOSS/MOSS-TTS) — a suite of open-source speech and audio generation models. This pack provides nodes for **dialogue synthesis**, **narration**, **voice design**, and **sound effects**.

## Features

- 🎙️ **Multi-Speaker Dialogue (MOSS-TTSD)**: Generate expressive multi-party conversations with up to 5 speakers using `[S1]`~`[S5]` tags. Supports long-form (up to 60 min) coherent audio.
- 🗣️ **Narration & TTS (MOSS-TTS)**: High-fidelity single-speaker speech synthesis with zero-shot voice cloning. Available in 8B and 1.7B variants.
- 🎨 **Voice Design (MOSS-VoiceGenerator)**: Create speaker timbres from text descriptions — no reference audio needed.
- 🔊 **Sound Effects (MOSS-SoundEffect)**: Generate sound effects from text prompts with controllable duration.
- 🔄 **Zero-Shot Voice Cloning**: Clone any voice with just a short reference audio clip.
- 🌍 **Multilingual**: Supports 20+ languages including Chinese, English, Japanese, and more.

## Installation

> [!TIP]
> We strongly recommend creating a fresh **Python 3.12** environment to avoid dependency conflicts:
> ```bash
> conda create -n moss_ttsd python=3.12 -y && conda activate moss_ttsd
> pip install flash-attn --no-build-isolation
> ```

1.  Clone this repository into your `ComfyUI/custom_nodes` directory:
    ```bash
    cd custom_nodes
    git clone https://github.com/kana112233/ComfyUI-kaola-moss-tts.git
    ```

2.  Install dependencies:
    ```bash
    cd ComfyUI-kaola-moss-tts
    pip install -r requirements.txt
    ```

    *Note: For GPU acceleration, ensure you have a CUDA-compatible PyTorch installed.*

> [!WARNING]
> This node requires `transformers >= 5.0.0`. Please make sure your environment meets this requirement:
> ```bash
> pip install "transformers>=5.0.0"
> ```

## Nodes Overview

| Node | Category | Description |
|------|----------|-------------|
| `Load MOSS-TTSD Model` | Dialogue | Loads the MOSS-TTSD model for multi-speaker dialogue |
| `Load MOSS-Audio Codec` | Shared | Loads the audio tokenizer (shared by multiple models) |
| `MOSS-TTSD Generate` | Dialogue | Generates multi-speaker dialogue audio |
| `Load MOSS Voice Generator Model` | Voice Design | Loads the voice design model |
| `MOSS Voice Generator Generate` | Voice Design | Creates speech from text + voice description |
| `Load MOSS Sound Effect Model` | Sound Effect | Loads the sound effect model |
| `MOSS Sound Effect Generate` | Sound Effect | Generates sound effects from text prompts |
| `Load MOSS-TTS Foundation Model` | Narration | Loads MOSS-TTS (8B or 1.7B) for narration/TTS |
| `MOSS-TTS Generate` | Narration | Generates narration speech with optional voice cloning |

## Models

| Model | HuggingFace ID | Size | Use Case |
|-------|----------------|------|----------|
| MOSS-TTSD v1.0 | [OpenMOSS-Team/MOSS-TTSD-v1.0](https://huggingface.co/OpenMOSS-Team/MOSS-TTSD-v1.0) | ~7GB | Multi-speaker dialogue |
| MOSS-TTS (8B) | [OpenMOSS-Team/MOSS-TTS](https://huggingface.co/OpenMOSS-Team/MOSS-TTS) | ~7GB | Narration, dubbing |
| MOSS-TTS-Local (1.7B) | [OpenMOSS-Team/MOSS-TTS-Local-Transformer](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Local-Transformer) | ~1.7GB | Lightweight narration |
| MOSS-VoiceGenerator | [OpenMOSS-Team/MOSS-VoiceGenerator](https://huggingface.co/OpenMOSS-Team/MOSS-VoiceGenerator) | ~3GB | Voice design from text |
| MOSS-SoundEffect | [OpenMOSS-Team/MOSS-SoundEffect](https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect) | ~3GB | Sound effects |
| MOSS-Audio-Tokenizer | [OpenMOSS-Team/MOSS-Audio-Tokenizer](https://huggingface.co/OpenMOSS-Team/MOSS-Audio-Tokenizer) | ~1GB | Audio codec (shared) |

### Auto Download
If models are not found locally, they will be **automatically downloaded** from HuggingFace on first run.

### Manual Download
Place models in the `ComfyUI/models/moss_ttsd/` directory:
```
ComfyUI/
└── models/
    └── moss_ttsd/
        ├── MOSS-TTSD-v1.0/
        ├── MOSS-TTS/
        ├── MOSS-VoiceGenerator/
        ├── MOSS-SoundEffect/
        └── MOSS-Audio-Tokenizer/
```

You can use `huggingface-cli` to download:
```bash
huggingface-cli download OpenMOSS-Team/MOSS-TTSD-v1.0 --local-dir ComfyUI/models/moss_ttsd/MOSS-TTSD-v1.0
huggingface-cli download OpenMOSS-Team/MOSS-TTS --local-dir ComfyUI/models/moss_ttsd/MOSS-TTS
huggingface-cli download OpenMOSS-Team/MOSS-TTS-Local-Transformer --local-dir ComfyUI/models/moss_ttsd/MOSS-TTS-Local-Transformer
huggingface-cli download OpenMOSS-Team/MOSS-VoiceGenerator --local-dir ComfyUI/models/moss_ttsd/MOSS-VoiceGenerator
huggingface-cli download OpenMOSS-Team/MOSS-SoundEffect --local-dir ComfyUI/models/moss_ttsd/MOSS-SoundEffect
huggingface-cli download OpenMOSS-Team/MOSS-Audio-Tokenizer --local-dir ComfyUI/models/moss_ttsd/MOSS-Audio-Tokenizer
```

## Usage

### 1. MOSS-TTSD — Multi-Speaker Dialogue
Best for podcasts, audiobooks, and conversational content.

- **Load Model**: `Load MOSS-TTSD Model` node
- **Load Codec**: `Load MOSS-Audio Codec` node
- **Generate**: `MOSS-TTSD Generate` node
- **Text format**: Use `[S1]`, `[S2]`...`[S5]` to switch speakers
  ```
  [S1] Hello there! [S2] Hi! How are you doing today?
  ```

#### Generation Modes

| Mode | Reference Audio | Reference Text | Description |
|------|:-:|:-:|-------------|
| `generation` | ❌ | ❌ | Pure generation with random voices |
| `voice_clone` | ✅ | ❌ | Clone voice timbre from reference audio |
| `continuation` | ✅ | ✅ | Continue speaking after reference audio |
| `voice_clone_and_continuation` | ✅ | ✅ | Clone + continue (best for single speaker) |

### 2. MOSS-TTS — Narration & Single-Speaker TTS
Best for voiceovers, dubbing, and long-form narration.

- **Load Model**: `Load MOSS-TTS Foundation Model` node (choose 8B or 1.7B)
- **Generate**: `MOSS-TTS Generate` node
  - **Text**: Narration content
  - **Reference Audio**: (Optional) Connect for zero-shot voice cloning
  - **Instruction**: (Optional) Describe the desired voice style

### 3. MOSS-VoiceGenerator — Voice Design
Design speaker timbres from text descriptions — no reference audio needed!

- **Load Model**: `Load MOSS Voice Generator Model` node
- **Generate**: `MOSS Voice Generator Generate` node
  - **Instruction**: Describe the voice (e.g., `"A warm, deep male voice"`, `"年轻女性，温柔的声音"`)
  - **Text**: Content to speak with this designed voice
  - **Output**: Can be used as *reference audio* for MOSS-TTSD `voice_clone` mode!

### 4. MOSS-SoundEffect — Sound Effect Generation
Generate environmental sounds, ambient audio, and sound effects from text prompts.

- **Load Model**: `Load MOSS Sound Effect Model` node
- **Generate**: `MOSS Sound Effect Generate` node
  - **Text**: Description (e.g., `"birds chirping in a forest"`, `"rain on a tin roof"`)
  - **Duration**: Target duration in seconds (~12.5 tokens/sec)

## Example Workflows

Example workflow files are provided in the `examples/` directory:

| Workflow | File |
|----------|------|
| MOSS-TTSD (3-node split) | `examples/workflow_split_full.json` |
| MOSS-VoiceGenerator | `examples/workflow_voice_generator.json` |
| MOSS-SoundEffect | `examples/workflow_sound_effect.json` |
| MOSS-TTS Foundation | `examples/workflow_moss_tts.json` |

## License
Apache 2.0 (Inherited from MOSS-TTS)
