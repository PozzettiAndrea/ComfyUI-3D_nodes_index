# ComfyUI Video Crop

A ComfyUI custom node for cropping videos using FFmpeg with pixel-precise control.

## Features

- **Pixel-precise cropping**: Specify exact x, y coordinates and dimensions
- **Multiple output formats**: MP4, WebM, AVI, MOV
- **Codec options**: H.264, H.265, VP9, ProRes
- **Quality control**: Adjustable quality/compression settings  
- **Custom FFmpeg arguments**: Add your own FFmpeg parameters
- **Frame rate control**: Set output frame rate

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/snomiao/ComfyUI-Video-Crop.git
```

2. Install FFmpeg if not already installed:
   - **Ubuntu/Debian**: `sudo apt install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Windows**: Download from https://ffmpeg.org/download.html

3. Restart ComfyUI

## Usage

1. Add the "Video Crop (FFmpeg)" node to your workflow
2. Connect your video input (IMAGE tensor from video loader)
3. Set crop parameters:
   - **X, Y**: Top-left corner coordinates in pixels
   - **Width, Height**: Crop dimensions in pixels
   - **Output Format**: Video container format
   - **Codec**: Video compression codec
   - **Quality**: Compression quality (lower = better quality)
   - **FPS**: Output frame rate
   - **Extra FFmpeg Args**: Additional FFmpeg parameters (optional)

## Node Parameters

### Required
- **video**: Input video as IMAGE tensor
- **x**: Crop X coordinate (pixels)
- **y**: Crop Y coordinate (pixels) 
- **width**: Crop width (pixels)
- **height**: Crop height (pixels)
- **output_format**: Video format (mp4, webm, avi, mov)
- **codec**: Video codec (libx264, libx265, libvpx-vp9, prores)
- **quality**: Quality/CRF value (0-51, lower is better)

### Optional
- **fps**: Output frame rate (default: 30.0)
- **extra_ffmpeg_args**: Additional FFmpeg arguments

## Examples

### Basic crop
- X: 100, Y: 50
- Width: 640, Height: 480
- Format: mp4, Codec: libx264, Quality: 23

### High quality crop with custom settings
- Extra FFmpeg Args: `-preset slow -tune film`
- Quality: 18 (higher quality)

## Requirements

- ComfyUI
- FFmpeg (system dependency)
- Python packages: PIL, numpy, torch, ffmpeg-python

## Installation Notes

This node uses the `ffmpeg-python` library instead of direct subprocess calls for better integration and error handling. The library still requires FFmpeg to be installed on your system.

## License

MIT License

## Contributing

Issues and pull requests welcome!