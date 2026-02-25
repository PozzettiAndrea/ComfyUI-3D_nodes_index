# ComfyUI-kaola-heartMuLa

ComfyUI custom nodes for the **HeartMuLa** project, providing high-quality **Music Generation** and **Lyrics Transcription** (vocal-optimized ASR) pipelines.

HeartMuLa features a Whisper-based ASR model specifically tuned for **lyrics transcription** in music scenes, effectively filtering complex background instrument interference. It also includes a state-of-the-art **Music Generation** model capable of creating high-quality audio from lyrics and tags.

## Features

- 🎤 **Lyrics Transcription**: Accurate lyrics recognition even in complex audio mixes
- 🎵 **Music Generation**: Generate high-quality music from text prompts and lyrics
- 🌍 **Multilingual**: Supports English, Chinese, Japanese, Korean, Spanish and more
- 🔄 **Integrated Pipeline**: Complete suite for music AI workflows in ComfyUI

## Installation

### 1. Clone into ComfyUI custom_nodes

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/kana112233/ComfyUI-kaola-heartMuLa.git
cd ComfyUI-kaola-heartMuLa
pip install -r requirements.txt
```

### 2. Download Models

Place the required models under `ComfyUI/models/checkpoints/`.

#### For Lyrics Transcription (ASR)
```bash
hf download HeartMuLa/HeartTranscriptor-oss --local-dir ./HeartTranscriptor-oss
```

#### For Music Generation
```bash
# 1. HeartCodec
hf download HeartMuLa/HeartCodec-oss-20260123 --local-dir ./HeartCodec-oss

# 2. Tokenizer & Config
hf download HeartMuLa/HeartMuLaGen --local-dir ./HeartMuLaGen

# 3. HeartMuLa Model
hf download base11231/HeartMuLa-RL-oss-3B-20260123 --local-dir ./HeartMuLa-RL-oss-3B-20260123
```

## Nodes

### HeartMuLa Loader 🎵 & HeartTranscriptor Loader 🎤

Loaders for the respective models. They scan `ComfyUI/models/checkpoints/` for compatible directories.

### HeartMuLa Generator 🎵

Generates music from lyrics and style tags.

| Parameter            | Default | Description                                  |
|----------------------|---------|----------------------------------------------|
| `pipeline`           | —       | Pipeline from HeartMuLa Loader               |
| `lyrics`             | —       | Lyrics text (supports multiline)             |
| `tags`               | —       | Style tags (e.g. "piano, pop, happy")        |
| `seed`               | 0       | Random seed for reproducibility              |
| `batch_size`         | 1       | Number of audio variations to generate       |
| `max_audio_length_s` | 30      | Max duration in **seconds**                  |
| `topk`               | 50      | Sampling top-k                               |
| `temperature`        | 1.0     | Sampling temperature                         |
| `cfg_scale`          | 1.5     | Classifier-Free Guidance scale               |

### HeartTranscriptor (Lyrics ASR) 🎤

Transcribes lyrics from audio input.

### Model Download (Music Generation)

To use music generation, download these additional models to `ComfyUI/models/checkpoints/`:

```bash
cd ComfyUI/models/checkpoints

# 1. HeartCodec
hf download HeartMuLa/HeartCodec-oss-20260123 --local-dir ./HeartCodec-oss

# 2. Tokenizer & Config
hf download HeartMuLa/HeartMuLaGen --local-dir ./HeartMuLaGen

# 3. HeartMuLa Model (if you haven't already)
hf download base11231/HeartMuLa-RL-oss-3B-20260123 --local-dir ./HeartMuLa-RL-oss-3B-20260123
```


## Example Workflow

An example workflow is included in the `examples/` folder:

- **[heart_transcriptor_basic.json](examples/heart_transcriptor_basic.json)** — Basic lyrics transcription: LoadAudio → HeartTranscriptor Loader → HeartTranscriptor → ShowText

Drag and drop the JSON file into ComfyUI to load the workflow.

## Tips

- **Best Results**: Use source separation tools (e.g. Demucs) to extract vocal tracks before transcription.
- **Memory**: The model uses ~1.5GB VRAM in float16 mode.

## License

Apache-2.0
