# ComfyUI MetaSaver

A powerful ComfyUI custom node for saving images with flexible custom metadata fields embedded in PNG files.

## Features

- **Up to 10 Metadata Fields**: Standard version with 10 optional metadata slots
- **Up to 20 Metadata Fields**: Dynamic version with 20 optional metadata slots
- **Custom Field Names**: Give each metadata field a custom name
- **Flexible Input Types**: Supports ANY type - strings, integers (seeds), floats (CFG), and more
- **PNG Metadata Embedding**: All custom data is saved in the PNG file
- **Workflow Preservation**: Maintains standard ComfyUI workflow metadata
- **Multiple Formats**: Metadata saved both as structured JSON and individual fields
- **All Optional**: Only fill in the fields you need - empty fields are ignored

## Why MetaSaver?

Unlike standard image save nodes, MetaSaver lets you:
- Save **seeds** from KSampler nodes
- Store **positive and negative prompts**
- Record **model names, LoRA weights, CFG values**
- Add **any custom text or numbers** you want to track
- **Name your fields** exactly how you want them

Perfect for tracking generation parameters, comparing outputs, or sharing images with full context!

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "MetaSaver"
3. Click Install

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/SorenWeile/ComfyUI_MetaSaver.git
   ```

3. Restart ComfyUI

## Usage

### Basic Example

1. Add the **"Save Image with Custom Metadata"** node to your workflow
2. You'll see pairs of inputs for metadata (10 pairs in standard, 20 in dynamic version):
   - `meta_name_0`: Name of first field (e.g., "seed")
   - `meta_value_0`: Value to save (e.g., connect from KSampler seed output)
   - `meta_name_1`: Name of second field (e.g., "positive_prompt")
   - `meta_value_1`: Value to save
   - ... and so on

3. Fill in only the metadata fields you want to use (empty ones are ignored)
4. Connect your image output to the `images` input
5. Run your workflow!

**Note**: All metadata fields are optional - you can use as many or as few as you need!

### Reading Metadata

The saved PNG files contain metadata in multiple formats:

1. **Structured JSON** (key: `custom_metadata`):
   ```json
   {
     "seed": 12345,
     "positive_prompt": "a beautiful landscape",
     "negative_prompt": "blurry, low quality",
     "cfg_scale": 7.5,
     "model_name": "sd_xl_base_1.0"
   }
   ```

2. **Individual fields** (keys: `meta_seed`, `meta_positive_prompt`, etc.)

You can read this metadata with:
- ComfyUI: Drag the image back into ComfyUI to see all metadata
- Python:
  ```python
  from PIL import Image
  img = Image.open("your_image.png")
  metadata = img.info.get("custom_metadata")
  print(metadata)
  ```
- ExifTool: `exiftool your_image.png`

## Node Variants

### MetaSaver (Standard)
Standard version with **10 optional metadata field pairs** (meta_name_0 through meta_name_9).
Perfect for most use cases.

### MetaSaverDynamic (Advanced)
Advanced version with **20 optional metadata field pairs** (meta_name_0 through meta_name_19).
For power users who need to track many parameters at once.

## Common Use Cases

1. **Track Generation Parameters**:
   - Seed, steps, CFG scale, sampler name
   - Easy to reproduce exact results later

2. **Model Comparison**:
   - Save model name, version, hash
   - Compare outputs from different models

3. **Prompt Engineering**:
   - Store positive/negative prompts with images
   - Build a library of what works

4. **LoRA Experimentation**:
   - Record LoRA names and weights
   - Track which combinations work best

5. **Batch Processing**:
   - Add batch IDs, timestamps, custom notes
   - Organize large generation runs

## Technical Details

- **File Format**: PNG with embedded metadata
- **Metadata Storage**: Both structured JSON and individual text fields
- **Image Processing**: Uses PIL/Pillow for reliable PNG handling
- **ComfyUI Integration**: Follows standard node conventions
- **Workflow Compatibility**: Preserves standard ComfyUI workflow data

## Comparison with Other Nodes

| Feature | MetaSaver | SaveImageWithMetaData | Crystools | comfy-image-saver |
|---------|-----------|----------------------|-----------|-------------------|
| Custom field names | ✅ | ❌ | ⚠️ (JSON) | ❌ |
| Dynamic field count | ✅ | ❌ | ❌ | ❌ |
| Visual UI for fields | ✅ | ⚠️ | ❌ | ❌ |
| Any input type | ✅ | ⚠️ | ✅ | ⚠️ |
| Structured JSON output | ✅ | ⚠️ | ✅ | ✅ |
| Individual field access | ✅ | ❌ | ❌ | ⚠️ |

## Troubleshooting

### Node doesn't appear in ComfyUI
- Restart ComfyUI completely
- Check that the folder is in `ComfyUI/custom_nodes/`
- Look for errors in the console

### Metadata not saving
- Ensure field names are not empty
- Check that values are connected to inputs
- Verify PNG format is selected

### Can't read metadata
- Use `exiftool` or Python PIL to verify metadata exists
- Check the `custom_metadata` field for structured JSON
- Individual fields are prefixed with `meta_`

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License - see LICENSE file for details

## Credits

Inspired by excellent existing nodes:
- [ComfyUI-SaveImageWithMetaData](https://github.com/nkchocoai/ComfyUI-SaveImageWithMetaData)
- [comfy-image-saver](https://github.com/giriss/comfy-image-saver)
- [ComfyUI-Crystools](https://github.com/crystian/ComfyUI-Crystools)

## Support

Found a bug or have a feature request?
- Open an issue on GitHub
- Provide workflow examples if possible
- Include ComfyUI console errors

---

**Enjoy tracking your AI generations with full metadata control!** 🎨✨
