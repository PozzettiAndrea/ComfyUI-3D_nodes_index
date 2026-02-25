# ComfyUI Stillfront Custom Nodes

A consolidated collection of custom nodes for ComfyUI developed by Stillfront.

## Features

This package includes nodes for:

- **LLM Integration** - Claude and Gemini API support for text generation with optional image input
- **WaveSpeed API** - Image and video generation via WaveSpeed AI (VEO, Sora, Qwen, ByteDance, etc.)
- **Utility Nodes** - Resolution presets, dynamic prompt lists, and more

## Installation

### From GitHub

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/stillfront/comfyui-stillfront.git
cd comfyui-stillfront
pip install -r requirements.txt
```

### Configuration

1. Copy `config.ini.tmp` to `config.ini`
2. Add your API keys:
   - WaveSpeed API key
   - Claude API key (or set `ANTHROPIC_API_KEY` environment variable)
   - Gemini API key (or set `GEMINI_API_KEY` environment variable)

## Node Categories

All nodes are prefixed with "SF" for easy searching in ComfyUI.

### Stillfront/LLM
- **SF LLM Chat** - Chat with Claude or Gemini models, supports image input

### Stillfront/WaveSpeed
- **SF WaveSpeed Client** - API client configuration
- **SF VEO 3.1 Text to Video** - Google VEO video generation
- **SF Sora 2 Text to Video** - OpenAI Sora video generation
- **SF Qwen Image** - Qwen image generation and editing
- **SF ByteDance Seedream** - ByteDance image generation
- And many more...

### Stillfront/Utils
- **SF Qwen Resolution** - Resolution presets with visual preview
- **SF Dynamic Prompt List** - Dynamic text input list

## Requirements

- Python 3.10+
- ComfyUI
- See `requirements.txt` for Python dependencies

## License

MIT License