# ComfyUI-PreviewImageNode

Standalone version of ComfyUI's PreviewImage and SaveImage nodes, extracted as an independent custom node for easy reuse and customization.

## Overview

This package contains standalone versions of two fundamental ComfyUI nodes:
- **Preview Image**: Display images in the UI without permanently saving them
- **Save Image**: Save images to the output directory with metadata

These nodes are extracted from ComfyUI's core `nodes.py` file and packaged as independent custom nodes for better modularity and reusability.

## Features

- Fully compatible with ComfyUI's IMAGE type
- Supports batch image processing
- Automatic metadata embedding (prompt, workflow info)
- Configurable compression levels
- Temporary file management for previews
- No external dependencies (uses ComfyUI's built-in systems)

## Installation

### Method 1: Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/eddyhhlure1Eddy/ComfyUI-PreviewImageNode.git
cd ComfyUI-PreviewImageNode
pip install -r requirements.txt
```

### Method 2: Direct Copy

1. Copy the `ComfyUI-PreviewImageNode` folder to `ComfyUI/custom_nodes/`
2. Restart ComfyUI

## Nodes

### Preview Image (Standalone)

**Purpose**: Display images in the ComfyUI interface without permanently saving them.

**Inputs**:
- `images` (IMAGE): The images to preview

**Outputs**:
- `images` (IMAGE): Pass-through of input images for downstream nodes

**Behavior**:
- Saves images to temp directory
- Uses fast compression (level 1)
- Auto-generates random temporary filenames
- Displays images directly in the node
- Passes images through to next node

**Use Cases**:
- Quick preview during workflow development
- Intermediate result inspection
- Debug visualization
- Temporary output checking
- Preview and continue processing

### Save Image (Standalone)

**Purpose**: Save images permanently to the ComfyUI output directory.

**Inputs**:
- `images` (IMAGE): The images to save
- `filename_prefix` (STRING): Prefix for saved files (default: "ComfyUI")

**Outputs**:
- `images` (IMAGE): Pass-through of input images for downstream nodes

**Behavior**:
- Saves to `ComfyUI/output/` directory
- Balanced compression (level 4)
- Embeds workflow metadata
- Sequential numbering
- Supports batch processing
- Passes images through to next node

**Use Cases**:
- Final output saving
- Result archiving
- Workflow export
- Production image generation
- Save and continue processing

## Technical Details

### Image Processing

Both nodes:
1. Accept ComfyUI IMAGE tensors (shape: [B, H, W, C])
2. Convert to numpy arrays
3. Scale from [0,1] to [0,255]
4. Convert to PIL Image
5. Save as PNG with optional metadata

### Metadata Embedding

Saved images include:
- Workflow prompt (if available)
- Generation parameters
- Node configuration
- Custom metadata fields

### File Naming

**Preview Image**:
```
{prefix}_temp_{random}_{counter:05}_.png
```

**Save Image**:
```
{filename_prefix}_{counter:05}_.png
```

### Directory Structure

```
ComfyUI/
├── output/              # SaveImage output
│   └── {saved images}
└── temp/               # PreviewImage temp files
    └── {preview images}
```

## Differences from Original Nodes

### Advantages of Standalone Version

1. **Independence**: Can be updated/modified without affecting core ComfyUI
2. **Modularity**: Easy to copy to other projects
3. **Customization**: Simple to extend with new features
4. **Learning**: Clear, isolated code for understanding node structure

### Identical Functionality

- Same input/output behavior
- Same image processing pipeline
- Same metadata handling
- Same UI integration

## Usage Examples

### Basic Preview

```
Load Image → Preview Image (Standalone) → [Continue processing...]
```

### Save with Custom Prefix

```
Generate Image → Save Image (Standalone) → [Continue processing...]
                 filename_prefix: "MyArt"
```

### Preview and Save Chain

```
Image Processing → Preview Image (Standalone) → Save Image (Standalone) → More Processing
                   [View in UI]                 [Save to disk]            [Pass through]
```

### Batch Processing

```
Batch Images [4 images] → Preview Image (Standalone) → Image Upscale
                          [Shows all 4 in node]        [Process further]
```

### Multi-Branch Workflow

```
Load Image → Preview Image (Standalone) ┬→ Save Image (filename: "original")
                                         ├→ Image Filter → Save Image (filename: "filtered")
                                         └→ Image Upscale → Save Image (filename: "upscaled")
```

### Checkpoint Preview

```
Image Gen → Preview Image → More Processing → Preview Image → Save Image
            [Check step 1]                    [Check step 2]  [Final save]
```

## Compatibility

- ComfyUI: All versions
- Python: 3.8+
- Dependencies: Pillow, NumPy (usually already installed)

## Performance

### Preview Image
- Compression: Level 1 (fastest)
- Storage: Temporary (auto-cleaned)
- Speed: ~10-50ms per image

### Save Image
- Compression: Level 4 (balanced)
- Storage: Permanent
- Speed: ~20-100ms per image

## Troubleshooting

### Images Not Displaying

**Problem**: Preview Image shows no output

**Solution**: 
- Check that input is IMAGE type
- Verify ComfyUI temp directory is writable
- Restart ComfyUI to clear cache

### Save Path Issues

**Problem**: Cannot save images

**Solution**:
- Ensure `ComfyUI/output/` directory exists
- Check write permissions
- Verify disk space

### Metadata Not Embedding

**Problem**: PNG files lack workflow info

**Solution**:
- Ensure `args.disable_metadata` is False
- Check ComfyUI settings
- Verify prompt/extra_pnginfo are passed correctly

## Customization

### Changing Compression

Edit `nodes.py`:
```python
class PreviewImage(SaveImage):
    def __init__(self):
        ...
        self.compress_level = 1  # Change: 0 (none) to 9 (max)
```

### Custom Output Directory

Edit `nodes.py`:
```python
class SaveImage:
    def __init__(self):
        self.output_dir = "/custom/path"  # Your path
```

### Adding Custom Metadata

Extend `save_images` method:
```python
metadata.add_text("custom_field", "custom_value")
```

## Project Structure

```
ComfyUI-PreviewImageNode/
├── __init__.py          # Node registration
├── nodes.py             # Core implementation
├── requirements.txt     # Dependencies
└── README.md           # Documentation
```

## Credits

- Original nodes: ComfyUI core team
- Standalone extraction: eddy
- Based on: ComfyUI `nodes.py`

## License

MIT License - Same as ComfyUI

## Contributing

Issues and pull requests welcome!

## Links

- [GitHub Repository](https://github.com/eddyhhlure1Eddy/ComfyUI-PreviewImageNode)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [Example Workflows](https://huggingface.co/eddy1111111/gift)

## Changelog

### Version 1.1.0
- Added IMAGE output to both nodes for pass-through capability
- Nodes can now be chained with downstream processing
- Supports multi-branch workflows
- Updated documentation with new usage examples

### Version 1.0.0
- Initial standalone release
- Extracted PreviewImage and SaveImage from ComfyUI core
- Full feature parity with original nodes
- Added comprehensive documentation
