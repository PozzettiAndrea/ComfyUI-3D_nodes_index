# ComfyUI-RMAutomation

A collection of workflow automation nodes for ComfyUI, designed to streamline AI image and video generation workflows.

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "RMAutomation"
3. Click Install

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-RMAutomation
```

## Nodes

### LoRA Nodes

#### RM Power LoRA Loader
A flexible node for loading multiple LoRAs with support for:
- Dynamic number of LoRA inputs (add as many as you need)
- Fixed or random strength per LoRA
- Style string import for automated LoRA loading

#### RM LoRA Collector
Combines multiple LoRA stacks into one. Accepts both LORA_STACK inputs and lora strings.

#### RM LoRA Apply
Applies all LoRAs from a collected stack to the model and CLIP.

### Styles Nodes

#### RM Styles Full
Load prompts from a JSON styles file with multiple selection modes:
- **Manual**: Use specific prompt number
- **Random**: Random selection within range
- **Increment**: Auto-increment after each generation
- **Decrement**: Auto-decrement after each generation

Features an **Edit Styles** button that opens a modal editor for managing your styles.

#### RM Styles Full (Display)
Same as RM Styles Full but displays the current prompt on the node.

#### RM Styles Pipe / RM Styles Pipe Out
Pack and unpack style data for easier workflow connections.

### Video Nodes

#### RM Video Combine
Combines images into video with:
- Multiple format support (H.264, H.265, VP9, GIF, WebP)
- Configurable output directory
- Metadata embedding
- Audio support
- Ping-pong looping

### Utility Nodes

#### RM Image Fallback
Returns the first non-empty image from multiple inputs. Useful for conditional workflows.

#### RM Mask Gate
Validates masks and passes through only valid ones. Outputs None for invalid masks, preventing crashes in downstream nodes.

#### RM Mask Gate (Guide)
Same as Mask Gate but for guide inputs. Disables guides when masks are invalid.

#### RM Set Latent Noise Mask
Improved latent noise mask setter with proper error handling for edge cases.

#### RM Positive/Negative Text Embed
CLIP text encoding nodes that combine optional string inputs with text fields.

## Styles JSON Format

The styles file (`data/styles.json`) uses this format:

```json
{
  "styles": [
    {
      "number": 1,
      "name": "Style Name",
      "positive": "positive prompt text",
      "negative": "negative prompt text",
      "motion": "motion prompt for video",
      "imageLoras": [
        {"path": "lora_name.safetensors", "weight": 1.0}
      ],
      "motionLoras": [],
      "motionLorasHigh": [],
      "motionLorasLow": []
    }
  ]
}
```

## Custom Video Formats

Add custom video formats by placing JSON files in the `video_formats` directory. Example format:

```json
{
  "extension": "mp4",
  "main_pass": ["-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p"],
  "audio_pass": ["-c:a", "aac", "-b:a", "192k"],
  "save_metadata": "True",
  "dim_alignment": 2
}
```

## License

MIT License - Do whatever you want with this code.

## Credits

- Video combine functionality based on [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
- Power LoRA loader concept inspired by [rgthree-comfy](https://github.com/rgthree/rgthree-comfy)
