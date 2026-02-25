# ComfyUI Prompt Saver

A ComfyUI custom node that saves images alongside formatted prompt reference cards for easy browsing and organization.

## Features

- **Reference Cards**: Creates side-by-side images with thumbnail + formatted prompt text
- **JSON Syntax Highlighting**: Automatically highlights JSON prompts with color-coded keys, values, and braces
- **Multiple Output Formats**: Save full image, reference card, and/or JSON metadata
- **Auto Text Sizing**: Dynamically adjusts font size to fit prompts in available space
- **Prompt Cleaning**: Handles escaped characters and JSON parsing automatically

## Example Output

The reference card displays your generated image as a thumbnail alongside the formatted prompt:

```
┌─────────────────────────────────────────────────┐
│  ┌──────────┐  {                                │
│  │          │    "scene": "mountain landscape", │
│  │  Image   │    "style": "oil painting",       │
│  │ Thumbnail│    "lighting": "golden hour"      │
│  │          │  }                                │
│  └──────────┘                                   │
└─────────────────────────────────────────────────┘
```

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Prompt Saver"
3. Click Install

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/robomello/comfyui-prompt-saver
```

Restart ComfyUI after installation.

## Usage

1. Find the node under `image/save` category as **"Save Image + Prompt Reference"**
2. Connect your image output and prompt string
3. Configure options as needed

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| `images` | IMAGE | Required. The generated image(s) to save |
| `prompt` | STRING | Required. The prompt text (supports plain text or JSON) |
| `filename_prefix` | STRING | Prefix for saved files (default: "prompt_ref") |
| `thumbnail_size` | INT | Size of thumbnail in reference card (128-1024, default: 512) |
| `save_full_image` | BOOLEAN | Save the full-resolution image (default: True) |
| `save_reference_card` | BOOLEAN | Save the reference card with thumbnail + prompt (default: True) |
| `save_json` | BOOLEAN | Save prompt metadata as JSON file (default: True) |
| `negative_prompt` | STRING | Optional. Negative prompt to include in metadata |
| `extra_metadata` | STRING | Optional. Additional metadata to include |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `images` | IMAGE | Passthrough of input images |
| `saved_path` | STRING | Comma-separated list of saved file paths |

## Output Files

Files are saved to `ComfyUI/output/prompt_references/` with the following naming:
- `{prefix}_{timestamp}_{index}_full.png` - Full resolution image
- `{prefix}_{timestamp}_{index}_ref.png` - Reference card
- `{prefix}_{timestamp}_{index}.json` - Prompt metadata

## Requirements

- ComfyUI
- Pillow
- numpy

## License

MIT License - see [LICENSE](LICENSE)

## Author

Roberto de Mello ([@robomello](https://github.com/robomello))
