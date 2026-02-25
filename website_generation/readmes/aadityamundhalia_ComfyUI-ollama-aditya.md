# ComfyUI Ollama Nodes

Custom ComfyUI node for integrating Ollama LLMs into your image generation workflows.

**Created by Aditya Mundhalia**

## Features

### Ollama Prompt Generator
Generates detailed image prompts using Ollama models. Supports both text-only and vision-based image analysis.

**Inputs:**
- `ollama_host`: Ollama server URL (default: http://localhost:11434)
- `model`: Model name to use (e.g., llama3.2, qwen3-vl, ministral, etc.)
- `image`: (Optional) Input image to analyze with vision models
- `system_prompt`: System instruction for the LLM
- `user_prompt`: (Optional) Your request or idea for the image
- `temperature`: Control randomness (0.0 = deterministic, 2.0 = very creative)
- `keep_alive`: Model keep-alive duration in seconds (0 = default)

**Output:**
- `generated_prompt`: The generated image prompt

## Installation

1. Make sure Ollama is installed and running on your system
   - Download from: https://ollama.com

2. Install the required Python packages:
```bash
cd ComfyUI/custom_nodes/ComfyUI-ollama-aditya
pip install -r requirements.txt
```

3. Pull some Ollama models:
```bash
# For text-to-prompt (any model works)
ollama pull llama3.2

# For image-to-prompt (needs vision support)
ollama pull qwen3-vl:8b
```

4. Restart ComfyUI

## Usage

### Finding Available Models
When ComfyUI starts, the extension will automatically print a list of available models in the console. Check the console output to see what models you have installed on your Ollama server.

If you encounter errors, the node will also attempt to list available models to help you debug.

### Text to Prompt Example:
1. Add "Ollama (Aditya)" node to your workflow
2. Enter your Ollama host URL (or leave default if using localhost)
3. Type the model name (e.g., `llama3.2`, `qwen3-vl`)
4. Set system prompt: "You are an expert at creating detailed Stable Diffusion prompts"
5. Set user prompt: "A cyberpunk city at night"
6. Connect the output to your CLIP Text Encode node

### Image to Prompt Example:
1. Add "Ollama (Aditya)" node to your workflow
2. Enter your Ollama host URL (or leave default if using localhost)
3. Connect an image input (optional)
4. Type a vision model name (e.g., `llava`, `qwen3-vl:8b`)
5. Set system prompt: "Describe this image in detail for image generation"
6. Connect the output to your CLIP Text Encode node

## Requirements

- Ollama installed and running
- Python packages: requests, pillow, numpy
- At least one Ollama model pulled

## How It Works

This node communicates with Ollama via HTTP API calls:
- `GET /api/tags` - Lists available models
- `POST /api/chat` - Sends messages and images to the model

No additional Ollama Python package needed - just standard HTTP requests.

## Troubleshooting

**Cannot connect to Ollama:**
- Make sure Ollama is running
- Check that Ollama API is accessible (default: http://localhost:11434)
- If Ollama is on a different host/port, update the `ollama_host` field in the node
- Check the console output - available models are listed when ComfyUI starts

**Using a custom Ollama host:**
Simply change the `ollama_host` input field to match your setup:
- Remote server: `http://192.168.1.100:11434`
- Different port: `http://localhost:8080`
- HTTPS: `https://your-ollama-server.com`

**Model not found errors:**
- Check the console output when ComfyUI starts to see available models
- Make sure you've pulled the model: `ollama pull <model-name>`
- For custom models, use the full model name
- If errors occur, the node will automatically try to list available models from your specified host

**Image input not working:**
- Make sure you're using a vision-capable model (llava, qwen3-vl, llama3.2-vision variants, etc.)
- Regular text-only models don't support image input
- Check the error output - it will list available models and remind you about vision requirements
