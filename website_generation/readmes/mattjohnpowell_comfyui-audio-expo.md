# ComfyUI Audio Expo

A collection of custom nodes for ComfyUI focused on Audio and Video generation post-processing.
This pack allows you to save audio with rich metadata (ID3 tags, cover art), generate "karaoke-style" scrolling lyric videos, and send generated tracks straight to your system's default media player — perfect for building an infinite generative radio workflow.

## Nodes

### 1. Save Audio (MP3 w/ Tags)
Saves generated audio as an MP3 file with embedded ID3 metadata.
- **Inputs**:
  - `audio`: The audio waveform to save.
  - `filename_prefix`: Prefix for the saved file.
  - `artist`: Artist name tag.
  - `title`: Track title tag.
  - `album`: Album name tag.
  - `year`: Year tag.
  - `genre`: Genre tag.
  - `bpm`: (Optional) Beats Per Minute to embed.
  - `cover_image`: (Optional) An image to embed as the MP3 Cover Art (Front Cover).
  - `lyrics`: (Optional) Lyrics text to embed in the USLT frame.
  - `play_in_player`: (Optional, default off) When enabled, opens the saved MP3 in your system's default media player immediately after saving. Non-blocking — generation continues without waiting.

### 2. Lyrics Video Generator
Generates an `.mp4` video with a scrolling lyrics overlay on top of a background image.
- **Inputs**:
  - `image`: Background image.
  - `audio`: Audio track.
  - `lyrics`: Text to scroll.
  - `font_size`: Size of the text.
  - `font_color`: Hex code or color name for the text.
  - `outline_size`: Stroke width around each character.
  - `outline_color`: Stroke colour.
  - `scroll_speed`: Manual scroll speed (pixels per second).
  - `auto_speed`: If True, calculates speed to ensure the text scrolls completely within the audio duration.
  - `filename_prefix`: Prefix for the saved video file.
  - `play_in_player`: (Optional, default off) When enabled, opens the rendered MP4 in your system's default video player immediately after saving. Non-blocking — generation continues without waiting.

### 3. Open Audio in Player
Opens any `AUDIO` tensor in the system's default media player, non-blocking. Passes audio through so it can be placed anywhere in a chain.

Useful for an **infinite generative radio** workflow: chain a music generation node into `Save Audio (MP3 w/ Tags)` (with `play_in_player` on), or use this node standalone to preview audio mid-chain. Each generated track is queued in your media player as it finishes, while ComfyUI continues generating the next one.

> **Note:** Playback happens on the machine running ComfyUI. This works best for local instances. Remote/cloud deployments will play audio server-side.
>
> **Queue behaviour:** When `play_in_player` is enabled, use the `player` dropdown to control which app receives the file. The dropdown is platform-aware — options unavailable on your OS won’t appear.
>
> | Option | Platforms | Behaviour |
> |---|---|---|
> | `Auto` | All | Tries VLC → WMP (Windows) → mpv → OS default in order |
> | `VLC` | All | `--playlist-enqueue` — adds to queue without interrupting playback |
> | `mpv` | All | `--playlist-end` — appends to current playlist |
> | `Windows Media Player` | Windows only | `/QUEUE` flag |
> | `System Default` | All | OS native opener — may interrupt current playback |
>
> **Recommended:** Install VLC (all platforms) or mpv for proper queue support.
> - VLC: https://www.videolan.org/vlc/
> - mpv: https://mpv.io/

- **Inputs**: `audio`
- **Output**: `audio` (pass-through)

## Infinite Radio / Infinite Karaoke Workflow

Connect nodes like this for continuous generative playback:

**Audio only (infinite radio):**
```
[Music Gen] ──▶ [Save Audio (MP3 w/ Tags)]
                   (play_in_player = on)
```

**With visuals (infinite karaoke):**
```
[Music Gen] ──▶ [Lyrics Video Generator] ──▶ ...
                   (play_in_player = on)
```

Each track opens non-blocking in your default player (e.g. VLC, Windows Media Player), which queues them automatically as they arrive.

## Installation

### Option 1: Git Clone (Recommended)
1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
   ```bash
   git clone https://github.com/mattjohnpowell/comfyui-audio-expo.git
   ```
3. Install the requirements:
   ```bash
   cd comfyui-audio-expo
   pip install -r requirements.txt
   ```
   *Note: Ensure you are using the python environment used by ComfyUI (e.g. portable versions use `python_embeded`).*

### Option 2: ComfyUI Manager
If using ComfyUI Manager, you can install via "Install via Git URL" using the repository URL.

## Requirements
- **FFmpeg**: Required for MoviePy to write video files and for audio conversion. Ensure it is installed and in your system PATH.
- **Python Packages**:
  - `moviepy`
  - `mutagen`
  - `proglog`
  - `numpy`, `torch`, `torchaudio` (Standard with ComfyUI)
