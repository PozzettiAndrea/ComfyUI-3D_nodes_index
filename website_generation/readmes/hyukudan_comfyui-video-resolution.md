# ComfyUI Video Resolution

A simple ComfyUI node for selecting video resolutions. Outputs `width` and `height` for video generation models like **LTX**, **CogVideo**, **Hunyuan**, and others.

## Installation

### Option 1: ComfyUI Manager
Search for "Video Resolution" in ComfyUI Manager and install.

### Option 2: Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/hyukudan/comfyui-video-resolution.git
```

Restart ComfyUI after installation.

## Usage

Search for **"Video Resolution"** in the node menu (or use aliases: "video size", "ltx resolution", "ltx2").

### Inputs

| Parameter | Description |
|-----------|-------------|
| **resolution** | Preset: 480p, 720p, 1080p, 1440p (2K), 2160p (4K), 4320p (8K), or Custom |
| **aspect_ratio** | 1:1, 16:9, 9:16, 4:3, 3:4, 21:9, 9:21, 3:2, 2:3 |
| **scale** | Multiply resolution: 0.25x, 0.5x, 0.75x, 1x, 1.25x, 1.5x, 2x |
| **divisible_by** | Ensure dimensions are divisible by: 8, 16, 32, or 64 |
| **add_one** | Add +1 to dimensions (required for LTX models: 32n+1) |
| **swap** | Swap width and height |
| **custom_width** | Custom width (only used when resolution = "Custom") |
| **custom_height** | Custom height (only used when resolution = "Custom") |

### Outputs

| Output | Type | Description |
|--------|------|-------------|
| **width** | INT | Width in pixels |
| **height** | INT | Height in pixels |
| **resolution_str** | STRING | Resolution as text (e.g., "1281x721") |

## Resolution Examples (with add_one=True)

| Preset | 1:1 | 16:9 | 9:16 |
|--------|-----|------|------|
| 480p | 481x481 | 833x481 | 481x833 |
| 720p | 705x705 | 1281x705 | 705x1249 |
| 1080p | 1057x1057 | 1921x1057 | 1057x1889 |
| 4K | 2145x2145 | 3841x2145 | 2145x3809 |

*Values shown with divisible_by=32, add_one=True (LTX format)*

## Model Recommendations

| Model | divisible_by | add_one |
|-------|-------------|---------|
| **LTX Video / LTX2** | 32 | True |
| CogVideoX | 16 | False |
| Hunyuan Video | 16 | False |
| Mochi | 64 | False |

## License

MIT License
