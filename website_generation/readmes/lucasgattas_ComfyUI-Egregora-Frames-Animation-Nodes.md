# Egregora Frames Animation Nodes for ComfyUI

Advanced image list animation toolkit for ComfyUI with batch processing, AI-powered frame interpolation, and multi-format video encoding.

## 🎨 Features

### 5 Powerful Nodes

1. **Advanced Batch Loader (Dir/ZIP/URL)** - Load images from directories, ZIP files, or URLs
2. **Batch Multi-Folder Processor** - Process multiple folders/ZIPs automatically
3. **Video Frame Extractor (File/URL)** - Extract and resample frames from any video
4. **Batch Animation Processor** - Order, interpolate, and process frame sequences
5. **Multi-Format Animation Encoder** - Export to GIF, MP4, WebM, AVI, MOV, MKV

### Key Capabilities

- 📁 **Flexible Loading**: Local directories, ZIP files, or direct URL downloads
- 🔄 **Batch Processing**: Process multiple folders/ZIPs in one go
- 🎬 **Video Integration**: Extract frames from videos, process them, and re-encode
- 🌟 **AI Interpolation**: Smooth frame transitions with optical flow, RIFE, or FILM
- 💾 **Multi-Format Export**: Save to 6 different formats simultaneously
- ⚡ **Production Ready**: Loop control, FPS adjustment, quality settings

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Egregora Frames Animation"
3. Click Install

### Method 2: Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/lucasgattas/ComfyUI-Egregora-Frames-Animation-Nodes.git
```

3. Install dependencies:
```bash
cd ComfyUI-Egregora-Frames-Animation-Nodes
pip install -r requirements.txt
```

4. Restart ComfyUI

### Method 3: Automatic Installation

```bash
cd ComfyUI/custom_nodes/ComfyUI-Egregora-Frames-Animation-Nodes
python install.py
```

## 🚀 Quick Start

### Basic Animation Workflow

```
Load Image Batch → Batch Animation Processor → Multi-Format Encoder
```

### Video Processing Workflow

```
Video Frame Extractor → KSampler (process frames) → Batch Animation Processor → Multi-Format Encoder
```

### Batch Processing Workflow

```
Batch Multi-Folder Loader → Batch Animation Processor → Multi-Format Encoder
```

## 📚 Node Documentation

### 1. Advanced Batch Loader

Load images from various sources.

**Inputs:**
- `source_type`: directory / zip_file / zip_url
- `path`: Path to directory, ZIP file, or URL
- `file_filter`: Comma-separated extensions (default: png,jpg,jpeg,webp)
- `sort_method`: alphabetical / random / modified_date
- `max_frames`: Maximum frames to load (0 = unlimited)
- `frame_step`: Load every Nth frame
- `random_seed`: Seed for random sorting

**Outputs:**
- `images`: Loaded image batch
- `frame_count`: Number of frames loaded

### 2. Batch Multi-Folder/ZIP Loader

Automatically process multiple folders or ZIP files.

**Inputs:**
- `parent_directory`: Parent folder containing subfolders/ZIPs
- `source_type`: subfolders / zip_files / both
- `file_filter`: File extensions to load
- `sort_method`: How to sort frames within each batch
- `max_frames_per_batch`: Limit frames per folder/ZIP
- `frame_step`: Sample every Nth frame

**Outputs:**
- `all_batches`: Combined image batches
- `batch_info`: JSON metadata about each batch
- `total_batches`: Number of sources processed

**Use Case:** Perfect for processing multiple animation sequences in one workflow. Point it at a parent folder, and it processes all subfolders or ZIP files automatically.

### 3. Video Frame Extractor

Extract frames from video files with FPS control.

**Inputs:**
- `video_path`: Path to video file (MP4, AVI, MOV, WebM, MKV)
- `output_fps`: Target FPS (0 = keep original)
- `start_frame`: First frame to extract
- `end_frame`: Last frame to extract (0 = all)
- `frame_step`: Extract every Nth frame

**Outputs:**
- `frames`: Extracted image sequence
- `frame_count`: Number of frames extracted
- `original_fps`: Original video FPS

**Use Case:** Extract frames from a video, modify them in ComfyUI (e.g., with KSampler), then re-encode to a new video.

### 4. Batch Animation Processor

Process and interpolate frame sequences.

**Inputs:**
- `images`: Input image batch
- `frame_order`: sequential / random / ping-pong / reverse
- `fps`: Target frames per second
- `interpolation`: none / crossfade / optical_flow / rife / film
- `interpolation_frames`: Number of frames to generate between each pair
- `random_seed`: Seed for random ordering

**Outputs:**
- `processed_frames`: Processed image sequence
- `fps`: Output FPS

**Interpolation Methods:**
- **none**: No interpolation, use original frames
- **crossfade**: Simple alpha blending between frames
- **optical_flow**: Motion-based interpolation using OpenCV (smooth, natural motion)
- **rife**: AI-powered interpolation (requires RIFE model)
- **film**: Google's FILM interpolation (requires FILM model)

### 5. Multi-Format Animation Encoder

Export animations to multiple formats simultaneously.

**Inputs:**
- `frames`: Processed frame sequence
- `fps`: Playback speed
- `loop_mode`: no_loop / loop_duration / loop_count
- `loop_duration_seconds`: Target duration for looping (when using loop_duration)
- `loop_count`: Number of loops (when using loop_count)
- `filename_prefix`: Base filename
- `output_directory`: Custom save location (empty = ComfyUI default)
- `save_gif`: Enable/disable GIF export
- `save_mp4`: Enable/disable MP4 export
- `save_webm`: Enable/disable WebM export
- `save_avi`: Enable/disable AVI export
- `save_mov`: Enable/disable MOV export
- `save_mkv`: Enable/disable MKV export
- `quality`: Output quality (1-100)
- `auto_open_folder`: Open output folder after saving

**No Outputs** - Terminal node that saves files directly.

## 🎯 Use Cases

### 1. Create Looping GIFs from Image Sequences
Perfect for sprite animations, logo animations, or art collections.

### 2. Process Video with AI
Extract video frames → Apply AI effects (img2img, controlnet) → Re-encode to new video

### 3. Batch Process Multiple Projects
Organize sequences in folders, process all at once with Batch Multi-Folder Loader

### 4. Smooth Frame Interpolation
Create fluid slow-motion or smooth transitions with optical flow or AI interpolation

### 5. Multi-Format Distribution
Export to GIF for web, MP4 for social media, and MOV for professional use - all at once

## ⚙️ Advanced Features

### Loop Control

- **No Loop**: Single playthrough
- **Loop Duration**: Specify exact duration (e.g., 10 seconds) - automatically repeats sequence
- **Loop Count**: Repeat sequence N times

### Frame Ordering

- **Sequential**: Use original order
- **Random**: Shuffle frames (with seed for reproducibility)
- **Ping-pong**: Forward then backward for seamless loops
- **Reverse**: Play sequence backwards

### FPS Control

- Extract video at different framerates
- Speed up or slow down animations
- Match specific platform requirements (e.g., 24fps for film, 60fps for smooth playback)

## 🤖 AI Interpolation (Optional)

For the best interpolation results, install AI models:

### RIFE (Real-Time Intermediate Flow Estimation)
```bash
pip install torch-rife
```

### FILM (Frame Interpolation for Large Motion)
```bash
pip install film-net
```

**Note:** These are optional. The nodes work great with optical flow interpolation without AI models.

## 📋 Requirements

- Python 3.8+
- PyTorch 2.0+
- ComfyUI (latest version)

### Dependencies (auto-installed)
- numpy
- Pillow
- opencv-python
- imageio
- imageio-ffmpeg
- requests

## 🛠️ Troubleshooting

### "No images found" error
- Check file extensions match your `file_filter` setting
- Ensure directory path is correct
- Verify ZIP file isn't corrupted

### Video extraction fails
- Install ffmpeg: `pip install imageio-ffmpeg`
- Try different video format
- Check video file isn't corrupted

### MP4/WebM export not working
- Install: `pip install imageio imageio-ffmpeg`
- For opencv fallback: `pip install opencv-python`

### Interpolation options missing
- Optical flow requires opencv-python
- RIFE requires torch-rife package
- FILM requires film-net package

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- ComfyUI community
- OpenCV project
- RIFE authors
- Google FILM team

## 🔄 Changelog

### v1.0.0 (Initial Release)
- Advanced Batch Loader with ZIP and URL support
- Batch Multi-Folder/ZIP Loader for automatic processing
- Video Frame Extractor with FPS control
- Batch Animation Processor with multiple interpolation methods
- Multi-Format Animation Encoder (GIF/MP4/WebM/AVI/MOV/MKV)
- Optical flow interpolation
- Loop control and frame ordering
- Auto-open output folder

---

Made with ❤️ for the ComfyUI community
