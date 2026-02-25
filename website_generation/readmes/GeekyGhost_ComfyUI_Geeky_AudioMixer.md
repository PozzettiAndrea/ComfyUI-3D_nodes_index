# 🎵 ComfyUI Geeky AudioMixer

<img width="1088" height="538" alt="Screenshot 2025-08-03 200408" src="https://github.com/user-attachments/assets/ddaa88db-fb30-4335-b99c-a10d8350f332" />

https://github.com/user-attachments/assets/71881db4-22b9-4545-8647-4a51518bbefe

A professional-grade audio mixing node for ComfyUI that allows you to combine up to 4 audio tracks with **precise volume control** and full timing flexibility. Perfect for creating polished audio tracks for lip-sync videos, tutorials, podcasts, or any multimedia content.

## ✨ Features

### 🎤 **Multi-Track Audio Mixing**
- **1 Required Track**: Primary audio (voice, narration, main content)
- **3 Optional Tracks**: Background music, sound effects, additional audio
- **Native ComfyUI Integration**: Uses ComfyUI's audio input system directly

### 🎛️ **Professional Controls**
- **🔥 ACCURATE Volume Control**: Individual track volumes are now **precisely preserved** - no more unexpected level changes!
- **Individual Volume Control**: 0-500% range for each track with slider + number display
- **Precise Timing**: Start time offset control (0-60 seconds) for each track
- **Fade Effects**: Customizable fade in/out (0-5 seconds) for smooth transitions
- **Master Volume**: Overall output level control (0-500%)
- **Pre-Gain Boost**: Extra amplification (0.1x-10x) for very quiet audio sources

### 🔊 **Advanced Audio Processing**
- **🆕 Smart Normalization Modes**: Choose how (or if) to normalize your audio
  - **"prevent_clipping"** *(default)*: Only reduces levels if clipping would occur
  - **"off"**: No normalization - preserves exact volume relationships
  - **"full_normalize"**: Traditional normalization to maximum level
  - **"smart_normalize"**: Only boosts very quiet signals
- **High-Quality Resampling**: Automatic sample rate conversion with sinc interpolation
- **Dynamic Range Compression**: Optional compression (1.0-10.0 ratio)
- **Soft Limiting**: Prevents harsh clipping (-1dB default threshold)
- **Detailed Level Metering**: Real-time RMS and peak level monitoring with debug output

### 📊 **Output Options**
- **Multiple Formats**: WAV, MP3, FLAC support
- **Sample Rates**: 8kHz to 96kHz configurable
- **Stereo Processing**: Automatic mono-to-stereo conversion
- **Timeline Mixing**: Precise audio placement on timeline

## 🚀 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Geeky AudioMixer"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation
1. **Clone this repository** into your ComfyUI custom_nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/GeekyGhost/ComfyUI_Geeky_AudioMixer.git
   ```

2. **Install Dependencies**:
   ```bash
   cd ComfyUI_Geeky_AudioMixer
   pip install -r requirements.txt
   ```

3. **Restart ComfyUI** and the node will appear in the `audio/mixing` category.

### Requirements
- `torch` (included with ComfyUI)
- `torchaudio>=0.13.0`
- `soundfile>=0.12.1`
- `numpy>=1.21.0`
- `scipy>=1.9.0` (optional, for enhanced audio processing)

## 📖 Usage Guide

### Basic Workflow Setup

```
[TTS/Audio Generator] ──→ [🎵 Geeky AudioMixer] ──→ [Video Combine Node]
[Music Loader] ──→ [audio_2 input]           │
[SFX Loader] ──→ [audio_3 input]             │
[SFX Loader] ──→ [audio_4 input]             ▼
                                    [Mixed Audio Output]
```

### Node Inputs

#### **Required Inputs**
- **`audio_1`**: Main audio track (voice, narration, primary content)
- **`output_duration`**: Length of final mixed audio in seconds
- **`output_format`**: Export format (WAV, MP3, FLAC)
- **`sample_rate`**: Target sample rate (44100Hz recommended)

#### **Optional Audio Inputs**
- **`audio_2`**: Secondary audio (background music, ambient sounds)
- **`audio_3`**: Additional audio (sound effects, notifications)
- **`audio_4`**: Extra audio (more sound effects, voice-overs)

### Control Groups

#### **🎵 AUDIO 1 CONTROLS** (Main Track)
- **Volume**: 150% default (0-500% range)
- **Start Time**: When track begins (0-60 seconds)
- **Fade In/Out**: Smooth transitions (0-5 seconds)

#### **🎵 AUDIO 2 CONTROLS** (Background)
- **Volume**: 120% default (perfect for background music)
- **Start Time**: Sync with main track
- **Fade In/Out**: 1 second defaults for smooth music entry

#### **🎵 AUDIO 3/4 CONTROLS** (Sound Effects)
- **Volume**: 100% default (adjust as needed)
- **Start Time**: Precise timing for sound effects
- **Fade In/Out**: Quick or no fades for impact sounds

#### **🎛️ MASTER CONTROLS**
- **Master Volume**: **100% default** *(changed from 200% for better control)*
- **🆕 Normalization Mode**: **"prevent_clipping" default** - Choose your normalization strategy
- **Pre-Gain Boost**: 100% default (extra amplification if needed)
- **Compression**: 1.0 default (no compression)
- **Limiter Threshold**: -1dB default (soft limiting)

## 🔥 Volume Control Fix

### **The Problem (FIXED!)**
Previous versions applied normalization to the **entire mixed output**, which destroyed your carefully set volume relationships. If you set Audio 1 to 150% and Audio 2 to 15% (1/10th volume), they would end up at similar levels after normalization.

### **The Solution**
✅ **Volume relationships are now preserved!** The mixer processes each track with its individual volume setting, mixes them together additively, then applies master processing that respects your intended balance.

### **New Normalization Modes**
- **"prevent_clipping"** *(recommended)*: Only reduces levels if they would clip - preserves your volume ratios
- **"off"**: No normalization whatsoever - exact volume control
- **"full_normalize"**: Old behavior - normalizes to maximum level
- **"smart_normalize"**: Only boosts very quiet overall mixes

## 🎯 Real-World Examples

### Example 1: Tutorial Video with Precise Volume Control
```yaml
# Voice narration (clear and prominent)
audio_1_volume: 1.5        # 150% - main voice
audio_1_start_time: 0.0    # Start immediately
audio_1_fade_in: 0.2       # Quick fade in
audio_1_fade_out: 0.5      # Gentle fade out

# Background music (exactly 1/4 the volume of voice)
audio_2_volume: 0.375      # 37.5% - exactly 1/4 of voice volume
audio_2_start_time: 0.0    # Start with voice
audio_2_fade_in: 2.0       # Slow fade in
audio_2_fade_out: 3.0      # Slow fade out

# Notification sound (1/2 the volume of voice)
audio_3_volume: 0.75       # 75% - exactly 1/2 of voice volume
audio_3_start_time: 5.2    # Play at 5.2 seconds
audio_3_fade_in: 0.0       # Instant
audio_3_fade_out: 0.1      # Quick fade

# Master settings
master_volume: 2.0         # 200% overall boost
normalization_mode: "prevent_clipping"  # Preserve ratios
output_duration: 30.0      # 30-second video
```

### Example 2: Podcast with Perfect Voice/Music Balance
```yaml
# Intro music (full volume initially)
audio_1_volume: 2.0        # 200% - prominent intro
audio_1_start_time: 0.0
audio_1_fade_out: 2.0      # Fade as voice comes in

# Voice narration (louder than music)
audio_2_volume: 2.5        # 250% - 25% louder than music
audio_2_start_time: 3.0    # Start at 3 seconds
audio_2_fade_in: 1.0

# Transition sound (moderate level)
audio_3_volume: 1.0        # 100% - audible but not overwhelming
audio_3_start_time: 10.0

# Master settings - no normalization for exact control
master_volume: 1.8         # 180% boost
normalization_mode: "off"  # Preserve exact relationships
```

### Example 3: Gaming Content with SFX Hierarchy
```yaml
# Game audio/commentary
audio_1_volume: 1.8        # 180% - main content
audio_1_start_time: 0.0

# Background music (much quieter)
audio_2_volume: 0.36       # 36% - exactly 1/5 of main audio
audio_2_start_time: 0.0

# Achievement sound (prominent but not overwhelming)
audio_3_volume: 1.35       # 135% - 3/4 of main audio level
audio_3_start_time: 15.5

# Victory sound (loudest effect)
audio_4_volume: 2.25       # 225% - 25% louder than main
audio_4_start_time: 28.0

# Master settings
master_volume: 1.5         # 150% overall
normalization_mode: "smart_normalize"  # Boost if too quiet
pre_gain_boost: 1.2        # 120% - slight extra boost
```

## 🔧 Output Information

### `mixed_audio`
The final mixed audio in ComfyUI's native audio format, ready to connect to video nodes or audio export nodes.

### `mix_info` (JSON)
Detailed information about the mixing process:
```json
{
  "tracks_loaded": 3,
  "processing_steps": [
    "Processed Audio 1 (main track)",
    "Processed Audio 2",
    "Mixed 3 tracks with preserved volume relationships",
    "Applied master volume: 1.5",
    "Normalization: prevent_clipping - no scaling needed"
  ],
  "sample_rate": 44100,
  "duration": 10.0,
  "channels": 2,
  "master_volume": 1.5,
  "normalization_mode": "prevent_clipping",
  "final_levels": {
    "rms": 0.234567,
    "peak": 0.890000,
    "rms_db": -12.6,
    "peak_db": -1.0
  }
}
```

### `total_duration`
Actual duration of the mixed audio in seconds.

### `level_meters` (JSON)
Real-time audio level information:
```json
{
  "rms_left_db": -12.3,
  "rms_right_db": -12.1,
  "peak_left_db": -1.0,
  "peak_right_db": -0.9,
  "stereo_balance": "centered"
}
```

## 🎵 Pro Tips for Best Results

### Volume Balancing (Now Actually Works!)
- **Voice/Main Content**: 120-200% for clarity
- **Background Music**: 30-60% of main content volume for proper background level
- **Sound Effects**: 80-150% depending on impact needed
- **Master Volume**: 100-200% for final output level
- **Use ratios**: If voice is 150%, set music to 37.5% for exactly 1/4 volume

### Normalization Mode Selection
- **"prevent_clipping"**: Best for most use cases - preserves your ratios
- **"off"**: Use when you need exact volume control for professional mixing
- **"full_normalize"**: Use when you want maximum loudness regardless of ratios
- **"smart_normalize"**: Good for content with very quiet overall levels

### Timing and Fades
- **Voice**: Short fades (0.1-0.5s) for natural speech
- **Music**: Longer fades (1-3s) for smooth transitions
- **Sound Effects**: Quick or no fades for maximum impact
- **Staggered Timing**: Offset tracks by 0.1-0.5s for natural feel

### Audio Quality Settings
- **Sample Rate**: 44.1kHz for most content, 48kHz for professional video
- **Format**: WAV for editing workflows, MP3 for final delivery
- **Normalization**: Use "prevent_clipping" for best balance
- **Pre-Gain Boost**: Use 1.2-2.0x for slightly quiet sources, 3.0+ for very quiet sources

### Common Workflow Patterns
1. **Voice + Music**: Voice at 150%, music at 37.5% (1/4 ratio), master at 150%
2. **Podcast**: Voice at 200%, intro music at 120%, master at 130%
3. **Gaming**: Game audio at 180%, background music at 36% (1/5 ratio), effects at 135%
4. **Tutorial**: Voice at 150%, music at 30%, notification SFX at 75%

## 🐛 Troubleshooting

### Volume Relationships Not Working
**Check these settings:**
- Use `normalization_mode: "prevent_clipping"` or `"off"` 
- Avoid `"full_normalize"` if you need precise ratios
- Check console output for actual applied volumes and levels
- Verify master_volume isn't set too high causing clipping

### Audio Too Quiet
**Solutions:**
- Increase `master_volume` to 1.5-3.0
- Use `pre_gain_boost` of 1.5-3.0 for quiet sources
- Raise individual track volumes proportionally
- Try `normalization_mode: "smart_normalize"` for very quiet mixes

### Audio Distorted/Clipping
**Solutions:**
- Use `normalization_mode: "prevent_clipping"` (default)
- Reduce `master_volume` below 1.5
- Lower individual track volumes proportionally
- Increase `limiter_threshold` to -3dB or lower
- Enable compression with ratio 2.0-4.0

### Volume Ratios Still Wrong
**Debug steps:**
1. Check ComfyUI console for detailed level information
2. Look for lines like "Applied volume: 1.5x" and "Final RMS: 0.123456"
3. Verify normalization mode is not "full_normalize"
4. Test with `normalization_mode: "off"` and `master_volume: 1.0` for pure testing

### Tracks Not Audible
**Solutions:**
- Check audio connections in ComfyUI workflow
- Verify audio file formats are supported
- Increase track volume above 100%
- Check start times aren't beyond output duration
- Look at console output for "Track outside timeline bounds" warnings

### Sample Rate Issues
**Solutions:**
- Use 44100Hz for most content
- Check console output for resampling warnings
- Ensure all input audio has valid sample rates
- Look for "Resampling from XHz to YHz" in console

### LazyAudioMap Errors
**Solutions:**
- Update ComfyUI to latest version
- Restart ComfyUI after installing node
- Check that audio input nodes are compatible
- Try connecting audio through different nodes

## 📊 Technical Details

### Supported Audio Formats
- **Input**: Any format supported by ComfyUI audio nodes
- **Output**: WAV (16/24-bit), MP3, FLAC
- **Channels**: Automatic mono-to-stereo conversion
- **Sample Rates**: 8kHz to 96kHz with high-quality resampling

### Audio Processing Pipeline
1. **Audio Extraction**: Handles ComfyUI's LazyAudioMap format
2. **Format Conversion**: Ensures consistent tensor format [channels, samples]
3. **Resampling**: High-quality sinc interpolation when needed
4. **Volume Application**: Per-track volume adjustment *(preserves relationships!)*
5. **Fade Processing**: Smooth fade in/out curves
6. **Timeline Mixing**: Sample-accurate additive mixing *(maintains ratios!)*
7. **Master Volume**: Applied to entire mix
8. **Smart Normalization**: Applied based on selected mode
9. **Compression/Limiting**: Optional final processing
10. **Output Formatting**: ComfyUI-compatible audio format

### New Volume Preservation System
- **Individual Processing**: Each track processed with its volume setting
- **Additive Mixing**: Tracks combined while preserving relative levels
- **Intelligent Normalization**: Only applied when beneficial
- **Detailed Logging**: Console shows exact levels at each processing stage
- **Master Control**: Final volume adjustment maintains relationships

### Performance Notes
- **Memory Efficient**: Processes tracks sequentially
- **High Quality**: Uses torchaudio for professional audio processing
- **Real-time Capable**: Optimized for workflow performance
- **Debug Information**: Detailed console logging shows exact processing steps

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Issues
1. Check existing [issues](https://github.com/GeekyGhost/ComfyUI_Geeky_AudioMixer/issues)
2. Provide detailed information:
   - ComfyUI version
   - Audio node versions you're using
   - Error messages from console
   - Steps to reproduce
   - Include console output showing volume levels

### Feature Requests
1. Open an [issue](https://github.com/GeekyGhost/ComfyUI_Geeky_AudioMixer/issues) with "Feature Request" label
2. Describe the feature and use case
3. Explain how it would benefit users

### Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests if applicable
5. Submit a pull request with clear description

### Development Setup
```bash
git clone https://github.com/GeekyGhost/ComfyUI_Geeky_AudioMixer.git
cd ComfyUI_Geeky_AudioMixer
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **ComfyUI Team**: For the amazing node-based interface
- **ComfyUI Community**: For inspiration and feedback on the volume control fix
- **Audio Processing Libraries**: PyTorch Audio team for excellent tools

## 📋 Changelog

### v1.1.0 - Volume Control Fix
- **🔥 FIXED**: Volume relationships now precisely preserved during mixing
- **🆕 NEW**: Smart normalization modes (`prevent_clipping`, `off`, `full_normalize`, `smart_normalize`)
- **🔧 IMPROVED**: Detailed console logging showing exact levels at each processing stage
- **⚙️ CHANGED**: Master volume default changed from 200% to 100% for better control
- **🐛 FIXED**: Normalization no longer destroys intended volume ratios

### v1.0.0 - Initial Release
- Multi-track audio mixing with up to 4 tracks
- Individual volume, timing, and fade controls
- Professional audio processing pipeline
- ComfyUI native integration

---

**Made with ❤️ for the ComfyUI community**

If this node helped you create amazing content, consider giving us a ⭐ on GitHub!
