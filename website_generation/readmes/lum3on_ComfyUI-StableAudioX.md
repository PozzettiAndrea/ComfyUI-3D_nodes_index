# ComfyUI-AudioX

A powerful audio generation extension for ComfyUI that integrates AudioX models a finetuned version of stable audio tools for high-quality audio synthesis from text and video inputs. Currently only working on min. 16gb Vram - tested on a single 4090.

## 🎵 Features

- **Text to Audio**: Generate high-quality audio from text descriptions with enhanced conditioning
- **Text to Music**: Create musical compositions with style, tempo, and mood controls
- **Video to Audio**: Extract and generate audio from video content with advanced conditioning
- **Enhanced Conditioning**: Separate CFG scales, conditioning weights, negative prompting, and prompt enhancement
- **Professional Audio Processing**: Volume control with LUFS normalization, limiting, and precise gain staging
- **Video Processing**: Mute videos and combine with generated audio

## 🚀 Installation

### 1. System Dependencies (Required)
**Install these system dependencies first:**

**Windows:**
```bash
# Install ffmpeg (required for video processing)
# Download from: https://ffmpeg.org/download.html
# Or use chocolatey: choco install ffmpeg

# Install Microsoft Visual C++ Build Tools (if not already installed)
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

**Linux/Ubuntu:**
```bash
sudo apt update
sudo apt install ffmpeg libsndfile1-dev build-essential
```

**macOS:**
```bash
brew install ffmpeg libsndfile
```

### 2. Clone Repository and Install Python Dependencies
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/lum3on/ComfyUI-StableAudioX.git
cd ComfyUI-StableAudioX

# Install Python dependencies
pip install -r requirements.txt

# Optional: Run dependency checker to verify installation
python install_dependencies.py
```

### Model Setup – AudioX

1. **Model File**: Download from [Hugging Face - model.ckpt](https://huggingface.co/HKUSTAudio/AudioX/resolve/main/model.ckpt)
2. **Config File**: Download from [Hugging Face - config.json](https://huggingface.co/HKUSTAudio/AudioX/resolve/main/config.json)
3. **Place both files** in:
   `ComfyUI/models/diffusion_models/` 

rename model.ckpt file to AudioX.ckpt

#### Alternative Download via Hugging Face CLI

```bash
# Install huggingface-hub if not already installed
pip install huggingface-hub

# Download AudioX model files
huggingface-cli download HKUSTAudio/AudioX model.ckpt --local-dir ComfyUI/models/diffusion_models/
huggingface-cli download HKUSTAudio/AudioX config.json --local-dir ComfyUI/models/diffusion_models/
```

**Model Directory Structure:**
```
ComfyUI/models/diffusion_models/
├── model.safetensors         # AudioX model
└── model_config.json         # Model configuration file
```
### System Requirements
- **VRAM**: 6GB+ recommended for optimal performance
- **RAM**: 16GB+ recommended
- **Storage**: ~5GB for model files
- **GPU**: CUDA-compatible GPU recommended (CPU supported but slower)

## 📋 Available Nodes

### Core Generation Nodes
- **AudioX Model Loader**: Load AudioX models with device configuration and auto-detect config files
- **AudioX Text to Audio**: Basic text-to-audio generation with automatic prompt enhancement
- **AudioX Text to Music**: Basic text-to-music generation with automatic prompt enhancement
- **AudioX Video to Audio**: Basic video-to-audio generation with automatic prompt enhancement
- **AudioX Video to Music**: Generate musical soundtracks for videos

### Enhanced Generation Nodes ⭐
- **AudioX Enhanced Text to Audio**: Advanced text-to-audio with negative prompting, templates, style modifiers, and conditioning modes
- **AudioX Enhanced Text to Music**: Advanced music generation with style, tempo, mood controls, and musical enhancement
- **AudioX Enhanced Video to Audio**: Advanced video-to-audio with separate CFG scales, conditioning weights, and enhanced prompting

### Processing & Utility Nodes
- **AudioX Audio Processor**: Process and enhance audio
- **AudioX Volume Control**: Basic volume control with precise dB control and configurable step size
- **AudioX Advanced Volume Control**: Professional volume control with LUFS normalization, soft limiting, and fade controls
- **AudioX Video Muter**: Remove audio from video files
- **AudioX Video Audio Combiner**: Combine video with generated audio
- **AudioX Multi-Modal Generation**: Advanced multi-modal audio generation
- **AudioX Prompt Helper**: Utility for creating better audio prompts with templates

## 🎯 Quick Start

### Basic Text to Audio
1. Add **AudioX Model Loader** node and select your model from `diffusion_models/`
2. Add **AudioX Text to Audio** node
3. Connect model output to audio generation node
4. Enter your text prompt (automatic enhancement applied)
5. Execute workflow

### Enhanced Text to Audio with Advanced Controls ⭐
1. Add **AudioX Model Loader** node
2. Add **AudioX Enhanced Text to Audio** node
3. Configure advanced options:
   - **Negative Prompt**: Specify what to avoid (e.g., "muffled, distorted")
   - **Prompt Template**: Choose from predefined templates (action, nature, music, etc.)
   - **Style Modifier**: cinematic, realistic, ambient, dramatic, peaceful, energetic
   - **Conditioning Mode**: standard, enhanced, super_enhanced, multi_aspect
   - **Adaptive CFG**: Automatically adjusts CFG based on prompt specificity
4. Execute for enhanced audio generation

### Enhanced Video to Audio with Separate Controls ⭐
1. Add **AudioX Model Loader** node
2. Add **AudioX Enhanced Video to Audio** node
3. Configure separate conditioning:
   - **Text CFG Scale**: Control text conditioning strength (0.1-20.0)
   - **Video CFG Scale**: Control video conditioning strength (0.1-20.0)
   - **Text Weight**: Influence of text conditioning (0.0-2.0)
   - **Video Weight**: Influence of video conditioning (0.0-2.0)
   - **Negative Prompt**: Avoid unwanted audio characteristics
4. Fine-tune balance between text prompts and video content

### Professional Audio Workflow with Volume Control
1. Generate audio using any AudioX generation node
2. Add **AudioX Advanced Volume Control** for professional features:
   - **LUFS Normalization**: Auto-normalize to broadcast standards (-23 LUFS)
   - **Soft Limiting**: Prevent clipping with configurable threshold
   - **Fade In/Out**: Add smooth fades to audio
   - **Precise Step Control**: Ultra-fine volume adjustments (0.001 dB steps)
3. Enable `auto_normalize_lufs` for automatic loudness normalization
4. Set `limiter_threshold_db` to prevent clipping (default: -1.0 dB)
5. Add fade_in_ms/fade_out_ms for smooth transitions

### Enhanced Music Generation ⭐
1. Add **AudioX Enhanced Text to Music** node
2. Configure musical attributes:
   - **Music Style**: classical, jazz, electronic, ambient, rock, folk, cinematic
   - **Tempo**: slow, moderate, fast, very_fast
   - **Mood**: happy, sad, peaceful, energetic, mysterious, dramatic
   - **Negative Prompt**: Avoid discordant, harsh, or atonal characteristics
3. Use automatic music context enhancement for better results

## 📁 Example Workflows

The repository includes example workflows:
- `example_workflow.json` - Basic text to audio
- `audiox_video_to_audio_workflow.json` - Video processing
- `simple_video_to_audio_workflow.json` - Simplified video to audio

## ⚙️ Requirements

- ComfyUI (latest version recommended)
- Python 3.8+
- CUDA-compatible GPU (recommended) or CPU
- Sufficient disk space for model downloads (models can be several GB)
- AudioX model files and config.json (must be downloaded separately)

## 🔧 Configuration

### Model Storage
**Important**: Models must be manually placed in the correct directory:
- **Required Location**: `ComfyUI/models/diffusion_models/`
- **Required Files**:
  - AudioX model file (`.safetensors` or `.ckpt`)
  - `config.json` configuration file
- **Auto-Detection**: The AudioX Model Loader automatically detects config files

### Device Selection
- Automatic device detection (CUDA/MPS/CPU)
- Manual device specification available in Model Loader
- Memory-efficient processing options

### Node Appearance
- AudioX nodes feature a distinctive light purple color (#ddaeff) for easy identification
- All nodes are categorized under "AudioX/" in the node browser

## ✨ Enhanced Features

### Advanced Conditioning Controls
- **Separate CFG Scales**: Independent control over text and video conditioning strength
- **Conditioning Weights**: Fine-tune the balance between text prompts and video content
- **Negative Prompting**: Specify audio characteristics to avoid for better results
- **Prompt Enhancement**: Automatic addition of audio-specific keywords and context

### Professional Audio Processing
- **Volume Control with Step Size**: Configurable precision from coarse (1.0 dB) to ultra-fine (0.001 dB)
- **LUFS Normalization**: Automatic loudness normalization to broadcast standards
- **Soft Limiting**: Intelligent limiting to prevent clipping while preserving dynamics
- **Fade Controls**: Smooth fade-in and fade-out with millisecond precision

### Intelligent Prompt Processing
- **Template System**: Pre-defined templates for common audio scenarios (action, nature, music, urban)
- **Style Modifiers**: Cinematic, realistic, ambient, dramatic, peaceful, energetic
- **Conditioning Modes**: Standard, enhanced, super_enhanced, and multi_aspect processing
- **Adaptive CFG**: Automatically adjusts CFG scale based on prompt specificity

## 🐛 Troubleshooting

### Common Issues

**Installation Problems**:
- **Missing ffmpeg**: Install ffmpeg system dependency (see installation steps above)
- **Build errors on Windows**: Install Microsoft Visual C++ Build Tools
- **Package conflicts**: Use a fresh virtual environment: `python -m venv audiox_env && audiox_env\Scripts\activate`
- **Dependency failures**: Run `python install_dependencies.py` to check and install missing packages

**Model Not Found**: If AudioX Model Loader shows no models:
- Ensure model files are in `ComfyUI/models/diffusion_models/`
- Verify both model file and `model_config.json` are present
- Check file permissions and naming
- Accept the license agreement on Hugging Face before downloading

**Frontend Errors**: If you encounter "beforeQueued" errors:
- Refresh browser (Ctrl+R)
- Clear browser cache
- Restart ComfyUI
- Check ComfyUI console for dependency errors

**Memory Issues**: For VRAM/RAM problems:
- Reduce batch sizes and duration_seconds
- Use CPU mode for large models
- Close other applications
- Try lower CFG scales (3.0-5.0)
- Ensure you have at least 6GB VRAM for optimal performance

**Audio Processing Errors**:
- Verify ffmpeg is properly installed and in PATH
- Check that libsndfile is installed (Linux/macOS)
- For LUFS normalization issues, ensure `pyloudnorm` is installed

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- AudioX team for original models and research
- ComfyUI community for the excellent framework
- All contributors and testers

## 📈 Version History

**Current Version**: v1.1.0
- ✅ **Enhanced Conditioning**: Added separate CFG scales, conditioning weights, and negative prompting
- ✅ **Advanced Volume Control**: LUFS normalization, soft limiting, and configurable step precision
- ✅ **Enhanced Generation Nodes**: Advanced text-to-audio, text-to-music, and video-to-audio nodes
- ✅ **Intelligent Prompting**: Template system, style modifiers, and adaptive CFG
- ✅ **Professional Audio Processing**: Fade controls, precise gain staging, and broadcast-standard normalization
- ✅ **Improved UI**: Distinctive node appearance with light purple color scheme
- ✅ **Better Model Management**: Auto-detection of config files and improved error handling

**Previous Version**: v1.0.9
- ✅ Fixed beforeQueued frontend errors
- ✅ Improved workflow execution stability
- ✅ Enhanced video processing capabilities
- ✅ Better error handling and user experience

## 🎵 Audio Quality Features

### Enhanced Conditioning
- **Better Prompt Adherence**: Enhanced conditioning modes ensure generated audio closely matches your descriptions
- **Negative Prompting**: Avoid unwanted audio characteristics like "muffled", "distorted", or "low quality"
- **Balanced Generation**: Fine-tune the balance between text prompts and video content for optimal results

### Professional Audio Standards
- **LUFS Normalization**: Automatic loudness normalization to -23 LUFS (broadcast standard)
- **Dynamic Range Preservation**: Soft limiting maintains audio dynamics while preventing clipping
- **Precise Control**: Volume adjustments from coarse (1.0 dB) to ultra-fine (0.001 dB) steps

## 🚀 Roadmap

### Upcoming Features
- **🎨 Audio Inpainting**: Fill gaps or replace sections in existing audio with AI-generated content
- **🔧 LoRA Training**: Lightweight fine-tuning for custom audio styles and characteristics
- **🎓 Full Fine-tune Training**: Complete model training pipeline for custom datasets and specialized audio domains
- **� Extended Model Support**: Integration with additional AudioX model variants and architectures

### Development Timeline
- **Phase 1** (Current): Enhanced conditioning and professional audio processing ✅
- **Phase 2** (Next): Audio inpainting capabilities and LoRA training infrastructure
- **Phase 3** (Future): Full fine-tuning pipeline and extended model support

We welcome community feedback and contributions to help prioritize these features!

---

For support and updates, visit the [GitHub repository](https://github.com/lum3on/ComfyUI-StableAudioX).
