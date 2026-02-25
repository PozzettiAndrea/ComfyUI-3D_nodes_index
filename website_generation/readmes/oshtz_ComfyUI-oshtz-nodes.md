# ComfyUI-oshtz-nodes
Custom nodes for ComfyUI created for some of my workflows.

### LLM All-in-One Node
Easy GPT/Claude/OpenRouter integration in ComfyUI:
- OpenAI & Anthropic models
- Live OpenRouter model list fetched directly from the registry
- Image-to-text capabilities
<div style="display: flex; align-items: center; justify-content: space-between;">
  <img src="https://github.com/oshtz/ComfyUI-oshtz-nodes/blob/main/examples/prompt_enhancer.jpg?raw=true" alt="alt text" height="250"/>
  <a href="https://youtu.be/0KZ7sMd4jUo">
    <img src="https://img.youtube.com/vi/0KZ7sMd4jUo/maxresdefault.jpg" alt="Watch the video" height="250"/>
  </a>
</div>

### GPT Image 1 Node
Generate images via OpenAI's vision model:
- Direct OpenAI API integration
- Image editing capabilities with mask support
- Quality and size customization
- Transparent background option

### Easy Aspect Ratio Node
Simplify your workflow with preset aspect ratios:
- Large selection of common ratios (1:1, 16:9, 21:9, etc.)
- Returns width and height values

### String Splitter Node
Split text into multiple outputs:
- Up to 10 separate outputs
- Customizable separator

### LoRA Switcher (Dynamic)
Dynamic LoRA selection powered by a single configurable node:
- Drive LoRA choice via API-friendly widget data
- Unlimited rows with custom strengths managed from the UI
- Keeps workflows simpler than juggling fixed 10/20/40 variants

### Image Overlay Node (Beta 🚧)
Combine images with precision:

**Current Features**
- Basic image compositing
- Position control (X/Y)
- Transparency adjustment
- Auto size matching
- Alpha channel support

**Coming Soon**
- Advanced positioning
- Transform controls
- Multiple blend modes
- Layer management
- Interactive preview

## Installation

First navigate to your ComfyUI installation custom nodes directory.

1. Clone this repository:
```bash
git clone https://github.com/oshtz/ComfyUI-oshtz-nodes.git
```

2. Install the required dependencies:
```bash
cd ComfyUI-oshtz-nodes
pip install -r requirements.txt
```

## Requirements
- requests
- torch
- pydantic
- Pillow
- boto3 (>= 1.34.101)

## License
This project is open-source and available under the MIT License.



