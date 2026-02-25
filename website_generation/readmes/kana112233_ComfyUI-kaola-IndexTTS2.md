# ComfyUI-kaola-IndexTTS2

ComfyUI custom nodes for **IndexTTS-2**, a state-of-the-art zero-shot text-to-speech system with advanced emotion control capabilities.

## Features

✨ **Zero-Shot Voice Cloning** - Clone any voice with just a few seconds of reference audio

🎭 **Advanced Emotion Control** - Control emotions through multiple modalities:
- Audio reference (use emotional speech samples)
- 8-dimensional emotion vectors (precise control)
- Natural language descriptions (user-friendly)

🎯 **Speaker-Emotion Disentanglement** - Independent control over timbre and emotion

⚡ **RTX 5090 Optimized** - Support for Blackwell architecture with Blackwell-specific Flash-Attention compilation and cu128 alignment

## Installation

### Method 1: ComfyUI Manager (Recommended)

1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "IndexTTS-2" in the Custom Nodes Manager
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation

Clone this repository into your ComfyUI custom nodes directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ComfyUI-kaola-IndexTTS2.git
cd ComfyUI-kaola-IndexTTS2
```

## Example Workflows

- [example_workflow.json](examples/example_workflow.json) — Basic voice cloning and emotion control
- [05_script_dubbing.json](examples/05_script_dubbing.json) — Multi-character script dubbing with SRT

### Step 1: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

> [!IMPORTANT]
> **External Core Library**: The core IndexTTS-2 library is required. You must install it separately and ensure it's in your Python path.

### Step 2: Download Model Weights

Download the IndexTTS-2 model to your ComfyUI models directory:

```bash
# Using huggingface-cli
uv tool install "huggingface-hub[cli,hf_xet]"
hf download IndexTeam/IndexTTS-2 --local-dir=ComfyUI/models/IndexTTS-2

# Or using modelscope
uv tool install "modelscope"
modelscope download --model IndexTeam/IndexTTS-2 --local_dir ComfyUI/models/IndexTTS-2
```

## Available Nodes

### 1. IndexTTS2 Model Loader

Loads the IndexTTS-2 model with configurable optimization settings.

**Inputs:**
- `model_dir` - Path to model directory (default: `IndexTTS-2`)
- `use_fp16` - Enable FP16 for lower VRAM usage
- `use_cuda_kernel` - Enable compiled CUDA kernels
- `use_deepspeed` - Enable DeepSpeed acceleration

**Outputs:**
- `model` - Loaded IndexTTS2 model instance

### 2. IndexTTS2 Voice Clone

Basic voice cloning using standard ComfyUI `AUDIO` inputs.

**Inputs:**
- `model` - IndexTTS2 model from loader
- `text` - Text to synthesize
- `spk_audio_prompt` - Reference audio (Connect to `LoadAudio` output)
- `temperature` - Randomness control (0.1-2.0, default 1.0)
- `top_k` / `top_p` - Sampling filters for better naturalness
- `use_random` - Enable randomness in generation

**Outputs:**
- `audio` - Generated audio (Standard ComfyUI format)

### 3. IndexTTS2 Emotion (Audio)

Voice synthesis with separate emotion reference audio.

**Inputs:**
- `model` - IndexTTS2 model
- `text` - Text to synthesize
- `spk_audio_prompt` - Speaker reference audio
- `emo_audio_prompt` - Emotion reference audio
- `emo_alpha` - Emotion strength (0.0-1.0)
- `use_random` - Enable randomness

**Outputs:**
- `audio` - Generated audio

### 4. IndexTTS2 Emotion (Vector)

Control emotions via 8-dimensional vector.

**Inputs:**
- `model` - IndexTTS2 model
- `text` - Text to synthesize
- `spk_audio_prompt` - Speaker reference audio
- `happy`, `angry`, `sad`, `afraid`, `disgusted`, `melancholic`, `surprised`, `calm` - Emotion intensities (0.0-1.0)
- `use_random` - Enable randomness

**Outputs:**
- `audio` - Generated audio

**Emotion Vector Format:**
`[happy, angry, sad, afraid, disgusted, melancholic, surprised, calm]`

### 5. IndexTTS2 Emotion (Text)

Control emotions via natural language description.

**Inputs:**
- `model` - IndexTTS2 model
- `text` - Text to synthesize
- `spk_audio_prompt` - Speaker reference audio
- `use_emo_text` - Auto-extract emotion from main text
- `emo_text` - Optional separate emotion description
- `emo_alpha` - Emotion strength (0.0-1.0, recommended: 0.6)
- `use_random` - Enable randomness

**Outputs:**
- `audio` - Generated audio

### 6. IndexTTS2 Script Dubbing (SRT)

Multi-character script dubbing driven by SRT subtitles. Parses an SRT script with character names, matches each line to a voice reference, and assembles the synthesized audio onto the SRT timeline.

**Required Inputs:**
- `model` - IndexTTS2 model
- `script_srt` - SRT format script (multiline, see format below)
- `emo_alpha` - Emotion strength (0.0-2.0, default 1.0)
- `temperature` - Randomness control (0.1-2.0, default 1.0)
- `top_k` - Top-K sampling (0-100, default 0)
- `top_p` - Top-P sampling (0.0-1.0, default 1.0)
- `use_random` - Enable randomness (default False)
- `save_segments` - Save individual emotion clips and synthesized clips as downloadable files (default False)
- `segments_prefix` - Filename prefix for saved segments (default "dubbing")

**Optional Inputs:**
- `emo_audio_prompt` - Emotion reference audio (auto-sliced by SRT timestamps)
- `voice_1` ~ `voice_7` - Up to 7 character voice reference audios
- `voice_1_name` ~ `voice_7_name` - Character names corresponding to each voice (e.g., "唐僧")

**Outputs:**
- `audio` - Full assembled dubbed audio

**SRT Script Format:**

Supports standard multi-line SRT format:

```
1
00:00:01,000 --> 00:00:03,000
唐僧：悟空，你又调皮了。

2
00:00:04,000 --> 00:00:06,500
孙悟空：师父，俺老孙冤枉啊！
```

Also supports compact single-line SRT:

```
1 00:00:01,000 --> 00:00:03,000 唐僧：悟空，你又调皮了。
2 00:00:04,000 --> 00:00:06,500 孙悟空：师父，俺老孙冤枉啊！
```

**Character name** uses Chinese colon `：` or English colon `:` as separator.

**Emotion text in parentheses** — add emotion descriptions after the character name:

```
1
00:00:01,000 --> 00:00:03,000
唐僧(高兴的说)：悟空，快来看。

2
00:00:04,000 --> 00:00:06,000
孙悟空（愤怒）：俺老孙不服！
```

Both half-width `()` and full-width `（）` parentheses are supported.

**Emotion Priority:**

| Priority | Condition | Behavior |
|---|---|---|
| 1 (highest) | Parentheses emotion in script, e.g. `唐僧(高兴的说)：` | Forced `emo_text` mode, ignores audio emotion |
| 2 | `emo_audio_prompt` connected, no parentheses | Slices emotion audio by SRT timestamp |
| 3 (lowest) | Neither | Voice-only synthesis, no emotion control |

**Segment Saving:**

When `save_segments` is enabled, individual files are saved to `{output}/{segments_prefix}_segments/`:
- `{index}_emo_{character}_{time}.wav` — Emotion audio slice for each line
- `{index}_tts_{character}_{time}.wav` — Synthesized audio for each line

These files appear in the ComfyUI output panel for download.

> [!NOTE]
> **Core Node Compatibility**: We have removed the custom Save/Load nodes to ensure 100% compatibility with ComfyUI core. Use standard **LoadAudio** for inputs and **SaveAudio** or **PreviewAudio** for outputs.

## Usage Examples

### Basic Voice Cloning

1. Add **IndexTTS2 Model Loader** node
2. Add **IndexTTS2 Voice Clone** node
3. Connect model output to voice clone input
4. Set speaker audio path and text
5. Add **IndexTTS2 Save Audio** to save output

### Emotion Control with Audio Reference

1. Load model with **IndexTTS2 Model Loader**
2. Add **IndexTTS2 Emotion (Audio)** node
3. Provide speaker audio (for timbre) and emotion audio (for emotion)
4. Adjust `emo_alpha` to control emotion strength
5. Save with **IndexTTS2 Save Audio**

### Precise Emotion Control with Vector

1. Load model
2. Add **IndexTTS2 Emotion (Vector)** node
3. Set individual emotion values (e.g., `surprised: 0.45`, others: 0)
4. Generate and save audio

### User-Friendly Emotion Control with Text

1. Load model
2. Add **IndexTTS2 Emotion (Text)** node
3. Enable `use_emo_text` to extract emotion from text
4. Or provide separate `emo_text` for explicit emotion description
5. Set `emo_alpha` around 0.6 for natural results

### Multi-Character Script Dubbing

1. Load model with **IndexTTS2 Model Loader**
2. Add **IndexTTS2 Script Dubbing (SRT)** node
3. Connect model output to the dubbing node
4. Add **LoadAudio** nodes for each character's voice reference, connect to `voice_1`, `voice_2`, etc.
5. Set `voice_1_name`, `voice_2_name` etc. to match character names in the SRT script (e.g., "唐僧", "孙悟空")
6. (Optional) Add a **LoadAudio** for emotion reference audio, connect to `emo_audio_prompt`
7. Write your SRT script in `script_srt`, using `角色名：台词` format
8. (Optional) Add emotion descriptions in parentheses: `唐僧(高兴的说)：悟空，快来看。`
9. Enable `save_segments` to export individual audio clips for review
10. Connect output to **SaveAudio** or **PreviewAudio**

> [!TIP]
> An example workflow is available at [`examples/05_script_dubbing.json`](examples/05_script_dubbing.json). Import it directly into ComfyUI to get started quickly.

## Tips

💡 **FP16 Mode**: Highly recommended for faster inference and lower VRAM usage with minimal quality loss

💡 **Emotion Alpha**: When using text-based emotion control, use lower `emo_alpha` values (0.6 or less) for more natural speech

💡 **Random Sampling**: Enabling `use_random` adds variety but may reduce voice cloning fidelity

💡 **Audio Format**: Reference audio should be clear, with minimal background noise

💡 **Voice Cloning Accuracy**: For best results, use 5-15 seconds of clean, single-speaker reference audio. Avoid background music or noise. Consistent speaking style in the reference yields more stable cloning.

💡 **Script Dubbing Timeline**: If a synthesized clip is longer than the gap before the next SRT timestamp, the next clip is automatically pushed forward (no truncation). The output may be longer than the original SRT timeline.

## Troubleshooting

### Model Not Found Error

Make sure the model is downloaded to the correct location:
```bash
ComfyUI/models/IndexTTS-2/config.yaml
ComfyUI/models/IndexTTS-2/[model files]
```

### Protobuf `builder` Error

If you see `ImportError: cannot import name 'builder' from 'google.protobuf.internal'`, your environment has a Protobuf version mismatch. Fix it with:
```bash
pip install protobuf==3.20.3
```

### RTX 5090 / CUDA 13.0 Considerations

For the best performance on RTX 5090, ensure your Torch environment is aligned with CUDA 12.8 or higher:
```bash
pip install --force-reinstall torch==2.8.0 torchaudio==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```

### Flash-Attention Compilation

If `flash-attn` fails on your 5090, perform a local source compilation:
```bash
pip install ninja
pip install flash-attn --no-build-isolation --no-cache-dir
```

### Slow HuggingFace Downloads

Set mirror endpoint (for users in China):
```bash
export HF_ENDPOINT="https://hf-mirror.com"
```

## Resources

- 📄 [IndexTTS-2 Paper](https://arxiv.org/abs/2506.21619)
- 🎬 [Demo Page](https://index-tts.github.io/index-tts2.github.io/)
- 💻 [GitHub Repository](https://github.com/index-tts/index-tts)
- 🤗 [HuggingFace Model](https://huggingface.co/IndexTeam/IndexTTS-2)
- 🌐 [ModelScope Model](https://modelscope.cn/models/IndexTeam/IndexTTS-2)

## Citation

If you use IndexTTS-2 in your work, please cite:

```bibtex
@article{zhou2025indextts2,
  title={IndexTTS2: A Breakthrough in Emotionally Expressive and Duration-Controlled Auto-Regressive Zero-Shot Text-to-Speech},
  author={Siyi Zhou, Yiquan Zhou, Yi He, Xun Zhou, Jinchao Wang, Wei Deng, Jingchen Shu},
  journal={arXiv preprint arXiv:2506.21619},
  year={2025}
}
```

## Using Local Models (Advanced)

The official IndexTTS-2 requires internet access to download the `wav2vec2bert` model from HuggingFace. If you want to use a fully **offline setup** with local models, you can use the fork version:

### Install Fork Version

```bash
# Clone the fork instead of the official repo
git clone https://github.com/kana112233/index-tts.git
cd index-tts

# Install dependencies
GIT_LFS_SKIP_SMUDGE=1 git checkout -f
pip install -e .
```

### Download wav2vec2bert Model

```bash
# Download to a local directory
huggingface-cli download facebook/w2v-bert-2.0 \
  --local-dir /path/to/models/w2v-bert-2.0
```

### Set Environment Variable

Before starting ComfyUI, set the local model path:

```bash
export W2V_BERT_PATH="/path/to/models/w2v-bert-2.0"
```

### What's Different in the Fork?

The fork modifies `indextts/utils/maskgct_utils.py` to:
- Check for the `W2V_BERT_PATH` environment variable
- Use local files if the path exists
- Fall back to HuggingFace if not set

This allows completely offline usage without internet access.

## License

This project follows the license of the original IndexTTS-2 project. For commercial usage, please contact: indexspeech@bilibili.com

## Acknowledgements

- [IndexTTS-2](https://github.com/index-tts/index-tts) - The amazing TTS model
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - The powerful node-based UI
