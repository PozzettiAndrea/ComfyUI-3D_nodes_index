# Dehypnotic Save nodes

Save nodes for Audio (mp3), Video & Frames, and Images.

Installation
1) Go to the `custom_nodes/` directory in ComfyUI.
2) Clone or copy the `comfyui-dehypnotic-save-nodes` folder:
   ```bash
   git clone https://github.com/Dehypnotic/comfyui-dehypnotic-save-nodes.git
   ```
3) Restart ComfyUI.

## Security and external save paths (ComfyUI Manager compliant)
- By default, saving is allowed under ComfyUI’s `output/` directory.
- To allow external locations (e.g., other drives), create a local JSON file next to this node named `dehypnotic_save_allowed_paths.json` with:
  ```json
  { "allowed_roots": ["D:/AudioExports", "E:/TeamShare/Audio"] }
  ```
Alternatively (advanced): you can set the environment variable `SAVE_MP3_ALLOWED_PATHS` to point to the JSON file. This is optional — for most users it’s enough to place the JSON file next to the node or in one of the global ComfyUI locations listed below.
- You can also place the file globally under your ComfyUI root:
  - `<ComfyUI>/dehypnotic_save_allowed_paths.json`
  - `<ComfyUI>/config/dehypnotic_save_allowed_paths.json`
  - `<ComfyUI>/user/dehypnotic_save_allowed_paths.json`
  - `<ComfyUI>/user/config/dehypnotic_save_allowed_paths.json`
- The node refuses writes outside `output/` unless the path is under one of the whitelisted roots. Edit this file offline and restart ComfyUI.

Whitelist behavior and safety
- Recommended location under ComfyUI root (e.g., `ComfyUI/config/`) so it survives node updates.
- Loader lookup order: env var → global ComfyUI locations → node folder.
- A node‑local file is used only if it defines at least one allowed root; empty example files are ignored.
- Lines starting with `#` are treated as comments in the JSON file.
- An allowed root permits saving in that folder and all subfolders; whitelist a deeper path to restrict more tightly.

Path and filename templates
Placeholders supported in `file_path` and `filename_prefix`:
- `[time(%Y-%m-%d)]` → formatted time (strftime)
- `[date]` → `YYYY-MM-DD`
- `[datetime]` → `YYYY-MM-DD_HH-MM-SS`
- `[unix]` → epoch seconds
- `[guid]` / `[uuid]` → random UUID4 hex
- `[model]` → tries `extra_pnginfo` keys: `model`, `checkpoint`, `ckpt_name`, `model_name`; else `unknown`
- `[env(NAME)]` → environment variable `NAME`

Examples
- `audio/[time(%Y-%m-%d)]`
- `runs/[model]/[datetime]`
- `D:/Exports/[env(USERNAME)]/[guid]`

---
# Save MP3

Simple, flexible MP3 saver with bitrate options and handy path/filename templates.

Features
- Audio input: accepts common formats used by audio nodes
- Bitrate mode: variable, constant, average
- Quality: low, medium, high (mapped per mode)
- Outputs: `AUDIO` and `STRING` (bitrate info summary), output node compatible (can terminate a graph)

Paths & placeholders
- `file_path` and `date_subfolder_pattern` with placeholder system (`[date]`, `[time(...)]`, `[guid]`, `[env(NAME)]`, etc.)
- Leave `file_path` empty to use ComfyUI’s default `output/` directory
- `date_subfolder_pattern` defaults to `%Y-%m-%d`; clear the field to disable dated folders

Optional backends (no system install required)
- Auto-download ffmpeg: `pip install imageio-ffmpeg` (first run caches a static ffmpeg)
- Drop-in ffmpeg: place `ffmpeg`/`ffmpeg.exe` in a `bin/` folder next to the node
- Or install `lameenc`: `pip install lameenc`
- If neither ffmpeg nor lameenc is available, the node raises an error with install hints.

Backend preference: uses ffmpeg when available; otherwise falls back to `lameenc`.

Bitrate/quality mapping
- Variable (VBR): high → `-q:a 0` (~245 kbps), medium → `-q:a 4` (~165 kbps), low → `-q:a 7` (~100 kbps)
- Constant (CBR): high → `320k`, medium → `192k`, low → `128k`
- Average (ABR): high → `256k`, medium → `192k`, low → `160k` (uses `-abr 1`)

<img width="347" height="239" alt="image" src="https://github.com/user-attachments/assets/7cfa5081-c81e-4d3e-8634-699449ef8d9f" />

# Save Images

Multi-format image saver with sequential naming, workflow embedding, and thumbnail support.

Features
- Image input: batches supported (returns original tensor passthrough)
- Formats: PNG, JPG/JPEG, WEBP, GIF, BMP, TIFF via Pillow
- Filename control: prefix + delimiter + padded counter (`number_start`/`number_padding`)
- Optional metadata: embed workflow JSON (PNG/WEBP) and PNG thumbnail preview block
- Quality controls: JPEG/WebP quality slider, PNG optimization toggle, lossless WebP, DPI setting
- Outputs: `IMAGE` passthrough (for chaining) and `STRING` with newline-separated saved paths

Paths & placeholders
- `file_path` and `date_subfolder_pattern` share the same placeholder system the other nodes (`[date]`, `[time(...)]`, `[guid]`, `[env(NAME)]`, etc.)
- Leave `file_path` empty to use ComfyUI’s default `output/` directory
- `date_subfolder_pattern` defaults to `%Y-%m-%d`; clear the field to disable dated folders

Workflow tip
- Enable `embed_workflow` to inject the current workflow JSON into PNG/WEBP outputs

<img width="259" height="340" alt="image" src="https://github.com/user-attachments/assets/608d94b8-72b8-48a2-b140-dfd2b64dcadc" />

# Save Video & Frames

Flexible video encoder that can also export selected frames, with automatic audio looping and preview thumbnails.

Features
- Save modes: `video`, `frames`, or `video & frames`
- Containers: MP4, MKV, WEBM, MOV (auto-adjusted codec compatibility)
- Codecs: H.264, H.265/HEVC, VP9, AV1, ProRes 422 HQ, DNxHR HQ
- Audio: optional track input; single still frames can loop to match audio duration
- Encoding controls: FPS, CRF, preset (ultrafast → veryslow), container-specific extras
- Frame export: choose index list (`0,5,10`), sentinel values (`-1` all, `-2` last), or skip entirely
- Preview: optional temp-image sequence surfaced in the ComfyUI UI result
- Outputs: `IMAGE` passthrough and `STRING` pointing to the saved video (or frame folder)

Paths & placeholders
- `file_path`, `date_subfolder_pattern`, and `frames_dir` accept the same placeholders as the other nodes (`[date]`, `[time(...)]`, `[guid]`, `[env(NAME)]`, etc.)
- Default date pattern `%Y-%m-%d`; clear to keep everything in the root folder
- When `frames_dir` is relative it resolves under the chosen video directory

Dependencies
- Requires Python packages `imageio` and `imageio-ffmpeg` (`pip install imageio imageio-ffmpeg`)
- Uses the static ffmpeg binary bundled by `imageio-ffmpeg`; no system-wide ffmpeg needed
- Gracefully reports missing dependencies at node load/run time with install guidance

Best practices
- Keep `show_progress` on during setup to see ffmpeg command info
- For WebM/V9 or AV1 targets, expect longer encode times at higher quality
- Use `loop_still_to_audio=True` to turn a single frame + audio into a slideshow-style export

<img width="349" height="597" alt="image" src="https://github.com/user-attachments/assets/fbf8c3e4-dbda-4f6d-bd30-2fdcc9618397" />





