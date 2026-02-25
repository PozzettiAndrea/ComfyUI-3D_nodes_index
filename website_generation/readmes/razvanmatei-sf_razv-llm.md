# ComfyUI Razv LLM Node

Custom ComfyUI node for integrating Claude and Gemini APIs with image and text capabilities.

## Features

- Text-based chat with latest Claude and Gemini models
- Optional image input support for vision tasks
- Support for Claude's "Extended thinking" capability across all models
- Multiple Claude models: Opus 4.1, Sonnet 4.5, Haiku 4.5
- Multiple Gemini models: 3 Pro Preview, 2.5 Pro, 2.5 Flash, 2.5 Flash Lite
- Adjustable parameters (temperature, max tokens, system prompt, seed for Gemini)

## Installation

### Option 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "razv-llm"
3. Click Install

### Option 2: Git Clone
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/razvanmatei-sf/razv-llm.git
cd razv-llm
pip install -r requirements.txt
```

## Configuration

### Claude API
Set your Anthropic API key using one of these methods:
1. Environment variable: `ANTHROPIC_API_KEY` or `CLAUDE_API_KEY`
2. Direct input in the node's API key field

### Gemini API
Set your Google API key using one of these methods:
1. Environment variable: `GEMINI_API_KEY` or `GOOGLE_API_KEY`
2. Direct input in the node's API key field

## Usage

1. Add the "RazvLLMChat" node to your workflow
2. Connect an image (optional) and provide a text prompt
3. Configure model and parameters as needed
4. Execute to get Claude's response

## Node Parameters

- **prompt**: Text input for the LLM
- **model**: Choose from available models (see below)
- **temperature**: Control response randomness (0.0 - 2.0)
- **max_tokens**: Maximum response length (up to 200,000)
- **system_prompt**: Optional system message to guide the model's behavior
- **api_key**: Your API key (if not set via environment)
- **image**: Optional image input for vision tasks
- **seed**: Random seed for reproducible results (Gemini models only)
- **timeout**: Request timeout in seconds (10-3600, default: 500)

## Available Models

### Claude Models (as of November 2025)
- **claude-sonnet-4-5** / **claude-sonnet-4-5-20250929**: Best balance of speed, cost, and intelligence. Recommended for most use cases. ($3/$15 per million tokens)
- **claude-opus-4-1** / **claude-opus-4-1-20250805**: Most capable model for complex tasks. Best coding model (72.5% SWE-bench). ($15/$75 per million tokens)
- **claude-haiku-4-5** / **claude-haiku-4-5-20251001**: Fast and cost-efficient for simple tasks. Near-frontier performance. ($1/$5 per million tokens)

All Claude models support "Extended thinking" capability for deep reasoning and can work continuously for several hours on long-running tasks.

### Gemini Models (as of November 2025)
- **gemini-3-pro-preview**: Most intelligent model with advanced reasoning capabilities. 1M context window. ($2-4/$12-18 per million tokens)
- **gemini-2.5-pro**: Capable reasoning model
- **gemini-2.5-flash**: Best price-performance balance
- **gemini-2.5-flash-lite**: Fastest, most cost-efficient

## Requirements

- ComfyUI
- Python 3.8+
- See `requirements.txt` for Python dependencies

## License

MIT