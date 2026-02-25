# ComfyUI ZeptaframePromptMerger

A ComfyUI custom node for merging different types of text prompts into a cohesive, structured prompt for text-to-video generation systems. This node uses LLama to intelligently combine general descriptions, subject-specific prompts, and system-generated captions with proper emphasis on the most important elements.

## Features

- Intelligently merges multiple prompt components with specified importance weighting
- Prioritizes subject descriptions and movements over general descriptions
- Uses LLama for natural language understanding and generation
- Easy integration with ComfyUI workflows

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/your-username/ComfyUI-ZeptaframePromptMerger.git
   ```

2. Install the required packages:
   ```bash
   pip install llama-cpp-python
   ```

3. Download a LLama GGUF model:
   - Recommended: llama-2-7b-chat.Q8_0.gguf for high quality on GPU systems
   - Place the model in a directory named `zepta` in your ComfyUI directory

## Usage

The node takes three inputs:

1. **generalSa2VAPrompt** (String, JSON): System-generated video caption
   - Importance: Low (2/10)
   - Provides background context

2. **generalTextPrompt** (String, JSON): User-generated general description
   - Importance: Medium-High (7/10)
   - Describes the overall video content/scene

3. **subjectTextPrompts** (String, JSON): Subject-specific descriptions
   - Importance: Highest (8/10)
   - Describes how specific subjects should move or appear
   - Format: JSON object with subjects as keys and movement descriptions as values

### Example Input

```json
// subjectTextPrompts
{
  "bear near creek": "walking fast",
  "bear near tree": "walking slow",
  "fish jumping in the river": "flapping around"
}

// generalTextPrompt
"A serene forest scene with wildlife by a flowing creek"

// generalSa2VAPrompt
"Nature documentary showing wildlife interaction in a forest environment"
```

## Configuration

You can modify the model path in the `nodes/text_nodes.py` file if you want to use a different LLama model:

```python
model_path = "zepta/llama-2-7b-chat.Q8_0.gguf"  # Change this to your preferred model
```

Other parameters you can adjust:
- `n_ctx`: Context window size (default: 4096)
- `max_tokens`: Maximum tokens in generation (default: 512)
- `temperature`: Higher values = more creative output (default: 0.7)
- `top_p`: Nucleus sampling parameter (default: 0.95)

## Requirements

- ComfyUI
- llama-cpp-python
- A LLama GGUF model file (recommended: llama-2-7b-chat.Q8_0.gguf)
- CUDA-capable GPU recommended for faster inference


