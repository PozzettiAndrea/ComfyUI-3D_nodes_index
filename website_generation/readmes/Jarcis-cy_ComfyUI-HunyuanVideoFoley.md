# ComfyUI-HunyuanVideoFoley

English | [简体中文](README.zh-CN.md)

A ComfyUI custom node integrating the inference pipeline of [HunyuanVideo-Foley](https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley), enabling audio generation from video + text prompts, plus audio-video merging utilities.

## Features

- 🎵 Auto model download on first use (from Hugging Face)
- 🎬 Video-aware audio generation guided by text prompts
- 🔧 Audio-video merging to produce a final video with an audio track

## Nodes

### 1) HunyuanVideo-Foley Generate Audio
Generate an AUDIO tensor from a VIDEO input and a text prompt.

Inputs:
- `video`: VIDEO (LoadVideo / CreateVideo output)
- `prompt`: Text prompt describing the desired audio
- `model`: Model setup (auto-detected under `models/hunyuan_foley`)
- `guidance_scale`: Float, default 4.5
- `num_inference_steps`: Int, default 50
- `device`: auto/cpu/cuda/mps
- `gpu_id`: CUDA device id

Output:
- `audio`: `{ "waveform": [B=1, C=1, T], "sample_rate": int }`

### 2) Video Audio Merger
Merge AUDIO and VIDEO into a single video file with an audio track.

Inputs:
- `video`: VIDEO input
- `audio`: AUDIO input
- `audio_sync_mode`:
  - `stretch` | `loop` | `truncate` | `pad_silence`
- `video_codec`: `copy` | `libx264` | `libx265`
- `audio_codec`: `aac` | `mp3` | `copy`
- `quality`: `high` | `medium` | `low`

Output:
- `merged_video`: VIDEO

## Quick Start

```
LoadVideo → HunyuanVideoFoleyGenerateAudio → VideoAudioMerger → SaveVideo
               ↑                                  ↑
           text prompt                         audio input
```

1. Load a video (LoadVideo)
2. Generate audio via "HunyuanVideo-Foley Generate Audio"
3. Merge audio + video via "Video Audio Merger"
4. Save or preview the final video

## Dependencies

```bash
# Use your ComfyUI Python environment
D:\AI\ComfyUI-aki-v1.3\.ext\python.exe -m pip install ffmpeg-python
```

## Notes

- On first run, models will be downloaded automatically (internet required)
- FFmpeg is required for audio/video processing
- CUDA is recommended for best performance
