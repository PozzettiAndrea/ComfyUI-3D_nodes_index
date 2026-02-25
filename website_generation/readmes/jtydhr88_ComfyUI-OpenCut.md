# ComfyUI-OpenCut

**[English](README.md) | [中文](README_CN.md)**

A powerful, privacy-focused video editor integrated directly into ComfyUI. This plugin brings professional video editing capabilities to your ComfyUI workflow without any server-side processing.

![OpenCut Interface](docs/img.png)

## 🌟 Features

### Core Editing Capabilities
- **Multi-track Timeline Editor**: Professional timeline with support for multiple video, audio, and overlay tracks
- **Real-time Preview**: Instant preview of edits without rendering
- **Drag & Drop Interface**: Intuitive drag-and-drop for media files and timeline elements
- **Non-destructive Editing**: All edits are non-destructive, preserving original media files

### Media Support
- **Video Formats**: MP4, WebM, MOV, AVI, and more
- **Audio Formats**: MP3, WAV, OGG, AAC
- **Image Formats**: PNG, JPG, GIF, WebP
- **Resolution Support**: From SD to 4K video editing

### Advanced Features
- **Keyframe Animation**: Animate position, scale, rotation, and opacity
- **Audio Waveform Visualization**: See audio waveforms directly on the timeline
- **Snap-to-Grid**: Precise alignment with magnetic timeline snapping
- **Multiple Export Options**: Export in various formats and resolutions
- **Undo/Redo System**: Full undo/redo support with keyboard shortcuts

### Layout & Workflow
- **Customizable Layouts**: 4 preset layouts optimized for different workflows:
  - Default: Balanced layout for general editing
  - Media Focus: Larger media panel for asset-heavy projects
  - Inspector Focus: Expanded properties panel for detailed adjustments
  - Vertical Preview: Optimized for vertical video editing (TikTok, Reels)
- **Resizable Panels**: Drag to resize any panel to your preference
- **Keyboard Shortcuts**: Comprehensive keyboard shortcuts for efficient editing

### Privacy & Performance
- **100% Client-side Processing**: All video processing happens in your browser using WebAssembly
- **No Upload Required**: Your media files never leave your computer
- **FFmpeg Integration**: Powered by FFmpeg.wasm for professional-grade processing
- **IndexedDB Storage**: Projects saved locally in your browser
- **OPFS Support**: Large files stored efficiently using Origin Private File System

## 📦 Installation

### Prerequisites
- ComfyUI (latest version recommended)
- Modern web browser (Chrome, Firefox, Edge, Safari)
- At least 4GB of available RAM for video processing

### Installation Steps

1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/[your-repo]/ComfyUI-OpenCut.git
   ```

3. Install dependencies (if any):
   ```bash
   cd ComfyUI-OpenCut
   pip install -r requirements.txt  # If Python dependencies exist
   ```

4. Restart ComfyUI

## 🚀 Usage

### Method 1: Direct Browser Access
Open your browser and navigate to:
```
http://127.0.0.1:8188/opencut/
```

### Method 2: ComfyUI Interface (Requires ComfyUI Frontend v1.24.4+)
1. Open ComfyUI in your browser
2. Look for the "OpenCut" button in the interface
3. Click to launch the video editor in a new tab

## 🎬 Getting Started

### Creating Your First Project
1. Launch OpenCut using one of the methods above
2. Click "New Project" or drag media files directly onto the interface
3. Your media will appear in the Media Panel (left side)
4. Drag media from the panel onto the timeline to start editing

### Basic Editing Workflow
1. **Import Media**: Drag files or click "Upload" in the Media Panel
2. **Add to Timeline**: Drag media to the desired track and position
3. **Trim Clips**: Hover over clip edges and drag to trim
4. **Add Transitions**: Overlap clips to create automatic transitions
5. **Adjust Properties**: Select a clip and use the Properties Panel to adjust settings
6. **Preview**: Use the spacebar to play/pause your edit
7. **Export**: Click Export and choose your desired format and quality

### Keyboard Shortcuts
- `Space`: Play/Pause
- `S`: Split clip at playhead
- `Delete`: Delete selected element
- `Ctrl/Cmd + Z`: Undo
- `Ctrl/Cmd + Shift + Z`: Redo
- `Ctrl/Cmd + C/V`: Copy/Paste
- `[` / `]`: Set in/out points
- `Arrow Keys`: Frame-by-frame navigation

## 🎨 Layout Presets

### Switching Layouts
Click the layout button in the header to switch between presets:

- **Default Layout**: Balanced view with all panels visible
- **Media Layout**: Enlarged media panel for browsing many assets
- **Inspector Layout**: Expanded properties panel for detailed editing
- **Vertical Layout**: Optimized for 9:16 vertical videos

### Custom Panel Sizing
- Drag the dividers between panels to customize sizes
- Your custom sizes are saved per layout preset
- Click the reset button to restore default sizes

## 🔧 Advanced Features

### Project Management
- Projects are automatically saved to browser storage
- Export/Import projects as JSON files for backup
- Multiple projects can be managed from the Projects page

### Media Processing
- Automatic thumbnail generation for videos
- Waveform generation for audio tracks
- Smart proxy generation for smooth playback of large files

### Export Options
- **Format**: MP4, WebM, MOV
- **Resolution**: Original, 1080p, 720p, 480p
- **Quality**: High, Medium, Low
- **Frame Rate**: 24, 30, 60 fps
- **Audio**: Stereo/Mono, various bitrates

## 🐛 Troubleshooting

### Common Issues

**Media not loading:**
- Ensure files are in supported formats
- Check browser console for errors
- Try refreshing the page

**Playback stuttering:**
- Lower preview resolution in settings
- Close other browser tabs
- Ensure adequate RAM is available

**Export failing:**
- Check available browser storage
- Try a lower resolution/quality setting
- Ensure no corrupted media files

**Layout not changing:**
- Clear browser cache
- Check localStorage is enabled
- Try resetting to default layout

### Browser Requirements
- Chrome 90+, Firefox 89+, Safari 15+, Edge 90+
- WebAssembly support required
- SharedArrayBuffer support recommended
- At least 4GB RAM recommended

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

### Development Setup
1. Clone the repository
2. Install dependencies: `bun install`
3. Run development mode: `bun dev`
4. Build for production: `bun run build:comfyui`

## 📝 License

This project integrates OpenCut, originally developed by [OpenCut-app](https://github.com/OpenCut-app/OpenCut). Please refer to the original project for licensing information.

## 🙏 Acknowledgments

- Original OpenCut developers for the amazing video editor
- ComfyUI team for the extensible platform
- FFmpeg.wasm for client-side video processing
- All contributors and users of this integration

## 📞 Support

For issues specific to the ComfyUI integration, please open an issue in this repository.
For OpenCut-specific issues, please refer to the [original OpenCut repository](https://github.com/OpenCut-app/OpenCut).

---

**Note**: This integration is under active development. Some features may be experimental or subject to change.