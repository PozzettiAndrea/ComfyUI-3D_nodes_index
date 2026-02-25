# ComfyUI-ASSSSA

Add ASS/SSA subtitle to video using ffmpeg.

> [!NOTE]
> This projected was created with a [cookiecutter](https://github.com/Comfy-Org/cookiecutter-comfy-extension) template. It helps you start writing custom nodes without worrying about the Python setup.

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
2. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
3. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under `ComfyUI/custom_nodes`.
4. Ensure FFmpeg is installed.
5. Restart ComfyUI.

## Features

- Extract ASS/SSA subtitle from video.
- Hard code or soft code subtitle to video.
- Video transcoding (Not tested).

## Available Nodes

- **FFMpegSettings**: FFmpeg Settings.
- **VideoTranscoding**: Video Transcoding based on FFmpeg setting.
- **SubtitleExtraction**: Extract soft encoded subtitle from mkv files.
- **SubtitleEmbedding**: Embed subtitle to video. Support soft subtitles in MKV, and hard subtitles in various formats.
- **ASSSubtitleReader**: Load ASS Subtitles from file to ComfyUI strings.
- **ASSSubtitleSave**: Save ComfyUI strings to subtitle file.
- **MultilineTextInput**: Multiline text input.