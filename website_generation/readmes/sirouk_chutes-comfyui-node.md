# Chutes.ai ComfyUI Nodes

Custom nodes for ComfyUI that integrate with [Chutes.ai](https://chutes.ai) video generation API.

## Nodes

### Chutes Wan 2.2 Fast (API)

Generate videos from images using the Wan 2.2 I2V-14B Fast model via Chutes.ai API.

**Required Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| `image` | IMAGE | Input image for video generation |
| `prompt` | STRING | Text prompt describing the desired motion |
| `api_key` | STRING | Your Chutes.ai API key |

**Optional Inputs:**
| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `negative_prompt` | STRING | (Chinese quality prompt) | What to avoid in generation |
| `resolution` | COMBO | 480p | Output resolution: 480p or 720p |
| `frames` | INT | 81 | Number of frames (21-140) |
| `fps` | INT | 16 | Frames per second (16-24) |
| `fast` | BOOLEAN | True | Ultra-fast Pruna mode |
| `seed` | INT | -1 | Generation seed (-1 = random) |
| `guidance_scale` | FLOAT | 1.0 | Guidance scale (0.0-10.0) |
| `guidance_scale_2` | FLOAT | 1.0 | Secondary guidance scale (0.0-10.0) |

**Output:**
- `video_path`: Filename of the generated MP4 in ComfyUI output directory

## Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Chutes"
3. Install this node pack

### Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/chutes-comfyui-node.git
cd chutes-comfyui-node
pip install -r requirements.txt
```

Restart ComfyUI after installation.

## Getting an API Key

1. Sign up at [chutes.ai](https://chutes.ai)
2. Navigate to your account settings
3. Generate an API key
4. Use the key in the node's `api_key` input

## Requirements

- ComfyUI v0.5.11+
- Python 3.10+
- Active Chutes.ai API key

## License

MIT
