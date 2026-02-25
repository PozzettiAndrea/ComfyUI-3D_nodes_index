# ComfyUI-PromptEnhance

A ComfyUI custom node for enhancing prompts using OpenAI-compatible APIs (like DeepSeek, OpenAI, etc.).

## Features

- **Prompt Enhancement**: Transform simple prompts into detailed, visual descriptions suitable for image generation models
- **OpenAI-compatible API**: Works with any OpenAI-compatible API (DeepSeek, OpenAI, Azure OpenAI, etc.)
- **Customizable Template**: Use the default prompt enhancement template or provide your own
- **Configurable Parameters**: Adjust temperature, max tokens, and timeout settings

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone or copy this folder:
   ```bash
   git clone <repo_url> ComfyUI-PromptEnhance
   # or simply copy the folder
   ```

3. Install dependencies (if not already installed):
   ```bash
   pip install requests
   ```

4. Restart ComfyUI

## Nodes

### Prompt Enhance (LLM)

Basic prompt enhancement node.

**Inputs:**
- `prompt` (required): The original prompt to enhance
- `api_endpoint` (required): OpenAI-compatible API endpoint (default: DeepSeek)
- `api_key` (required): Your API key
- `model` (required): Model name (e.g., `deepseek-chat`, `gpt-4`)
- `prompt_template` (optional): Custom enhancement template (use `{prompt}` as placeholder)
- `temperature` (optional): Sampling temperature (0.0-2.0, default: 0.7)
- `max_tokens` (optional): Maximum response tokens (100-8192, default: 2048)
- `timeout` (optional): Request timeout in seconds (10-300, default: 60)

**Output:**
- `enhanced_prompt`: The enhanced prompt string

### Prompt Enhance Advanced (LLM)

Advanced version with additional options.

**Additional Inputs:**
- `system_prompt` (optional): System prompt for the LLM
- `top_p` (optional): Top-p sampling parameter (0.0-1.0, default: 1.0)

**Outputs:**
- `enhanced_prompt`: The enhanced prompt string
- `original_prompt`: The original input prompt (for comparison/reference)

## API Endpoints

### DeepSeek (Default)
```
https://api.deepseek.com/v1/chat/completions
```
Model: `deepseek-chat`

### OpenAI
```
https://api.openai.com/v1/chat/completions
```
Model: `gpt-4`, `gpt-3.5-turbo`, etc.

### Azure OpenAI
```
https://<your-resource>.openai.azure.com/openai/deployments/<deployment>/chat/completions?api-version=2024-02-15-preview
```

## Default Prompt Template

The default template is designed to transform user prompts into detailed, visual descriptions that are:
- Faithful to the original intent
- Rich in visual details
- Free of metaphors and emotional rhetoric
- Directly usable by text-to-image models

## Example Usage

1. Add the "Prompt Enhance (LLM)" node to your workflow
2. Connect a text input or type directly in the prompt field
3. Configure your API endpoint and key
4. Connect the `enhanced_prompt` output to your CLIP Text Encode or other text processing nodes

## Example Workflows

Ready-to-use example workflows are available in the `examples/` directory:

- **[SDXL Prompt Enhance Workflow](examples/sdxl_prompt_enhance_workflow.json)**: A complete SDXL workflow demonstrating prompt enhancement with visual preview of enhanced prompts. Perfect for learning how to integrate Prompt Enhance nodes into your workflows.

See the [examples/README.md](examples/README.md) for detailed instructions on using the example workflows.

## License

MIT License
