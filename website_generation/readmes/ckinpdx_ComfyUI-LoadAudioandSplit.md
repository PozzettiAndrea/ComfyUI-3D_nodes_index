[README.md](https://github.com/user-attachments/files/24040568/README.md)
# ComfyUI-LoadAudioandSplit

Splits audio into frame-synced chunks for video generation workflows. Supports overlapping segments for seamless transitions.

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| audio | AUDIO | Source audio |
| fps | FLOAT | Frames per second (default 25) |
| overlap_frames | INT | Frames to overlap between chunks (default 0) |
| frames_1 - frames_8 | INT | Frame count per segment (connect as needed) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| scene_count | INT | Number of detected segments |
| final_timestamp | FLOAT | End time of last chunk in seconds |
| audio_1 - audio_8 | AUDIO | Split audio segments |

## How It Works

**Duration = frames / fps**

Each chunk's start time is offset by `duration - overlap` from the previous chunk:

- 97 frames, 10 overlap, 25fps
- audio_1: 0.0s - 3.88s
- audio_2: 3.48s - 7.36s
- audio_3: 6.96s - 10.84s

## Installation

```
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-LoadAudioandSplit
```

Restart ComfyUI.
