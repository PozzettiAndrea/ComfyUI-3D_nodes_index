# ComfyUI ImageWithMetadata Nodes

**English** | [日本語版 README](README_ja.md)

Custom nodes for ComfyUI that enable batch image loading with metadata extraction and saving with comprehensive metadata embedding.

## Features

### Load Image with Metadata

![Load Image with Metadata workflow example](./images/load_01.webp)

- **Batch processing**: Load images sequentially from a folder
- **Metadata extraction**: Extract prompts, seed, steps, CFG from saved images
- **Two modes**: 
  - `single_image`: Load specific image by index
  - `incremental_image`: Auto-advance through folder
- **Multiple format support**: PNG, JPG, WebP, BMP, GIF
- **Based on WAS Node Suite**: Uses proven, stable code pattern
- **Loop support**: Automatically wraps to first image when reaching end

### Save Image with Metadata

![Save Image with Metadata workflow example](./images/save_01.webp)

- **Comprehensive metadata**: Save all generation parameters
- **Multiple formats**: PNG, WebP, JPG
- **Dual output**: PNG metadata + optional text file
- **Flexible text format**: JSON or plain text
- **Date-based naming**: Automatic folder organization by date

### Checkpoint Loader with Names

![Checkpoint Loader with Names example](./images/cp.webp)

- **Model name output**: Returns checkpoint name as STRING
- **VAE name output**: Returns VAE name as STRING
- **Baked VAE support**: Option to use checkpoint's baked VAE
- **Connect to Save node**: Pass model/VAE names to SaveImageWithMetadata

### Random Checkpoint Loader with Names

![Random Checkpoint Loader with Names example](./images/random_cp.webp)

![Random Checkpoint Loader with Names example](./images/random_cp_single01.webp)

![Random Checkpoint Loader with Names example](./images/random_cp_single02.webp)

- **Two modes**: 
  - `single`: Sequential switching with external index (batch processing)
  - `random`: Seed-based random selection
- **Folder specification**: Select checkpoints only from specific folder
- **Subfolder support**: Search models in subfolders
- **Pattern filter**: Filter by filename (e.g., `anime_*`)
- **BaseModel management**: Separate SDXL/SD1.5/Illustrious usage
- **Name output**: Model and VAE names as STRING

## Installation

1. Clone or download this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/shin131002/ComfyUI-ImageWithMetadata.git ImageWithMetadata
```

2. Restart ComfyUI

No additional dependencies required - uses ComfyUI's built-in libraries.

## Usage

For detailed usage instructions, see [USAGE.md](USAGE.md) (English) or [USAGE_ja.md](USAGE_ja.md) (日本語).

### Quick Start: Batch Upscaling

**Recommended Pattern: Group Node with Integer Counter**

1. Add **Integer** node
   - Set `control_before_generate`: increment
2. Add **Load Image with Metadata**
   - Set `mode`: single_image
   - Set `path`: your image folder
   - Connect Integer output to `index` input
3. Select both nodes → Right-click → **Convert to Group**

![Convert to Group example](./images/load_02.webp)

This creates a unified batch processing node!

### Load Image with Metadata

**Key Parameters:**
- `mode`: single_image (with external counter) or incremental_image
- `path`: Image folder path
- `pattern`: File filter (* = all files)
- `label`: Batch identifier
- `index`: Starting position (0-based)

**Outputs:**
- image, positive_prompt, negative_prompt, info, filename_text, seed, steps, cfg

### Save Image with Metadata

**Key Parameters:**
- `filename_prefix`: Supports date format like `%date:yyMMdd-hhmmss%`
- `metadata_save`: png_metadata_only / text_file_only / both
- `text_format`: json / plain_text

Connect generation parameters from other nodes for complete metadata capture.

## Mode Comparison

### incremental_image Mode
- Always starts from last position
- Cannot start from middle (e.g., image #50)
- Best for: Complete folder processing from start

### single_image Mode + External Counter (Recommended)
- Start from any position
- See current index value
- Manually adjust if needed
- Best for: Flexible batch processing

## Examples

### Example 1: Auto Batch Generation with Multiple Models
```
Integer (increment, value=0)
  ↓
Random Checkpoint Loader with Names (single mode)
  ├→ path: F:\models\SDXL
  ├→ index: ← Integer connection
  ├→ checkpoint_name → Save Image with Metadata
  └→ MODEL, CLIP, VAE → KSampler
```

### Example 2: Auto Upscaling Workflow
```
Integer (increment, value=0)
  ↓
Load Image with Metadata (single_image)
  ↓
Upscale Model
  ↓
Save Image with Metadata
```

### Example 3: img2img Batch Processing
```
Integer (increment, value=50)  ← Start from 51st image
  ↓
Load Image with Metadata (single_image)
  ├→ image → VAE Encode → KSampler
  ├→ positive_prompt → CLIP Text Encode
  └→ negative_prompt → CLIP Text Encode
```

## Metadata Format

### Text File (JSON)
```json
{
  "positive_prompt": "1girl, solo, ...",
  "negative_prompt": "worst quality, ...",
  "model": "model_name.safetensors",
  "vae": "vae_name.pt",
  "seed": 123456789,
  "sampler_name": "dpmpp_2m",
  "scheduler": "karras",
  "steps": 20,
  "cfg": 7.0
}
```

### Text File (Plain Text)
```
Model: model_name.safetensors
VAE: vae_name.pt
Seed: 123456789
Sampler: dpmpp_2m
Scheduler: karras
Steps: 20
CFG: 7.0
Positive: =======================================
1girl, solo, ...
Negative: =======================================
worst quality, ...
```

## Troubleshooting

### Images not loading
- Check if path exists
- Verify pattern matches files (use `*` for all)
- Check console for error messages

### Slow performance
- This is expected for large batches
- Use single_image + Integer for better control

### Metadata not extracted
- Ensure images were saved with metadata
- Check if text file exists (filename.txt)
- Supported formats: This node's format, A1111 format

## Credits and License

This project is based on **WAS Node Suite** by WASasquatch.
- Repository: https://github.com/WASasquatch/was-node-suite-comfyui
- License: MIT License

The `LoadImageWithMetadata` node uses the `BatchImageLoader` pattern from WAS Node Suite with added metadata extraction functionality.

## License

MIT License - See [LICENSE](LICENSE) file for details.

When using or distributing this software, please maintain attribution to both:
- This project
- WAS Node Suite (original BatchImageLoader implementation)

## Support Policy

This is a personal project provided free of charge with limited support:

**Not provided:**
- Individual technical support
- Guaranteed bug fixes or feature additions
- Guaranteed compatibility with future ComfyUI updates

**Provided:**
- ✅ Open source code (free to modify and fork)
- ✅ Basic documentation
- ✅ GitHub discussions (responses not guaranteed)

**If you encounter issues:**
1. Check this README and USAGE.md/USAGE_ja.md
2. Search existing issues
3. Open a new issue (responses not guaranteed)
4. Fork and fix yourself (MIT License)

**Disclaimer:** This software is provided "as is" without warranty of any kind. The author is not responsible for any damages arising from the use of this software.

## Contributing

Issues and Pull Requests are welcome, but please note that response time may vary due to time constraints.

## Changelog

### v1.1.0 (2026-01-26)
- Added Random Checkpoint Loader with Names node
  - single/random mode for checkpoint switching
  - Folder specification and subfolder support
  - Pattern filter functionality
  - BaseModel-specific management support

### v1.0.0 (2026-01-25)
- Initial release
- Load Image with Metadata node
- Save Image with Metadata node
- Checkpoint Loader with Names node
- Based on WAS Node Suite's BatchImageLoader pattern
