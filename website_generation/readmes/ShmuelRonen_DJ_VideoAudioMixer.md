# DJ Video Audio Mixer for ComfyUI

A powerful ComfyUI custom node for combining video clips with synchronized audio, background music, and advanced audio controls.

![image](https://github.com/user-attachments/assets/dc5df155-51e5-4dd5-8180-0d844a4dccf9)

## Features

- ✅ Combine two video clips with smooth transitions
- ✅ Mix audio tracks from both videos
- ✅ Add background music with intelligent volume control
- ✅ Control where background music is applied (entire video, first clip, or second clip)
- ✅ Automatic speech detection for dynamic volume adjustment
- ✅ Fade-in and fade-out effects for seamless audio transitions
- ✅ Compatible with VideoHelperSuite and other ComfyUI video nodes
- ✅ Robust audio normalization to prevent encoding errors

## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/ShmuelRonen/DJ_VideoAudioMixer.git
```

3. Restart ComfyUI

The node should now appear in the "audio/video processing" category in your node browser.

## Requirements

- ComfyUI (latest version recommended)
- PyTorch
- torchaudio (for audio resampling)
- VideoHelperSuite (for VHS_VIDEOINFO type compatibility)

## Usage

The DJ_VideoAudioMixer node accepts two video inputs (with frames, audio, and video info) and combines them into a single video output.

### Inputs

#### Required:
- **images1**: Image frames from the first video (IMAGE)
- **audio1**: Audio from the first video (AUDIO) 
- **video_info1**: Video info from the first video (VHS_VIDEOINFO)

#### Optional:
- **images2**: Image frames from the second video (IMAGE)
- **audio2**: Audio from the second video (AUDIO)
- **video_info2**: Video info from the second video (VHS_VIDEOINFO)
- **bgm**: Background music to mix into the video (AUDIO)
- **bgm_mode**: Where to apply background music (all, first_video, second_video)
- **bgm_volume**: Volume level for background music (0.0-1.0)
- **fade_in_sec**: Duration of fade-in effect in seconds
- **fade_out_sec**: Duration of fade-out effect in seconds
- **audio_match_method**: How to handle audio shorter than video ("pad_with_silence" or "repeat_audio")

### Outputs

- **images_output**: Combined image frames (IMAGE)
- **audio_output**: Combined audio with background music (AUDIO)
- **video_info_output**: Updated video information (VHS_VIDEOINFO)

## Examples

### Basic Video Concatenation

Connect two videos to concatenate them with their original audio:

```
Video1 Loader → ┐
                │ → DJ_VideoAudioMixer → Video Exporter
Video2 Loader → ┘
```

### Adding Background Music

Add background music to your video with dynamic volume control:

```
Video1 Loader → ┐
                │
Video2 Loader → ┼ → DJ_VideoAudioMixer → Video Exporter
                │
Audio Loader → ┘ (connect to bgm input)
```

### Advanced Workflow

Use with other ComfyUI nodes for a complete video processing workflow:

```
Video1 Loader → ┐
                │
Video2 Loader → ┼ → DJ_VideoAudioMixer → VHS_VideoCombine → Video File Output
                │
Audio Loader → ┘ (bgm)
```

## Custom BGM Application Modes

The node offers three modes for applying background music:

1. **all**: Applies BGM to the entire combined video
2. **first_video**: Applies BGM only to the first video segment with a fade-out at the transition
3. **second_video**: Applies BGM only to the second video segment with a fade-in at the transition

## Audio Duration Handling

When an audio track is shorter than its corresponding video, the node offers two ways to handle this:

1. **pad_with_silence**: Adds silence to the end of the audio to match the video duration (default)
2. **repeat_audio**: Loops/repeats the audio to fill the entire video duration

This is particularly useful for short sound effects or music tracks that you want to extend to cover the full video segment.

## Technical Details

### Smart Volume Control

The node automatically analyzes speech patterns in the primary audio tracks and dynamically adjusts the BGM volume to ensure dialogue clarity. When speech is detected, BGM volume is automatically reduced, and when there's silence, the BGM volume increases.

### Audio Sanitization

The node implements comprehensive audio normalization and sanitization to prevent common encoding errors with FFmpeg:
- Removes NaN and infinity values
- Prevents audio clipping
- Applies a soft limiter for optimal audio levels
- Ensures audio is in valid range for encoders

## Troubleshooting

If you encounter audio issues:

1. **NaN/Infinity errors in FFmpeg**: The node already has built-in sanitization, but if you still encounter these errors, try reducing the bgm_volume setting.

2. **Audio out of sync**: Make sure the fps values in your video_info inputs are accurate.

3. **Missing audio**: Verify that your input audio is properly formatted as a ComfyUI AUDIO type.

## License

[MIT License](LICENSE)

## Acknowledgments

- The VideoHelperSuite team for their excellent VHS nodes that complement this one
- The ComfyUI community for inspiration and support

## Support

If you encounter issues or have feature requests, please open an issue on the [GitHub repository](https://github.com/ShmuelRonen/DJ_VideoAudioMixer/issues).
