# ComfyUI-LikeSpiderAI-SaveMP3

🎧 A custom ComfyUI node that saves input AUDIO as `.mp3` using `ffmpeg`.

## Features

- Saves `.mp3` to `output/audio/`
- Selectable bitrate: 64 / 128 / 192 / 256 / 320 kbps
- Works with any node that outputs `AUDIO`
- No UI hacks or extra files

## Requirements

- Python ≥ 3.10
- ffmpeg (must be installed and available in PATH)

## Installation

Clone this repository into your `ComfyUI/custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Pigidiy/ComfyUI-LikeSpiderAI-SaveMP3.git
