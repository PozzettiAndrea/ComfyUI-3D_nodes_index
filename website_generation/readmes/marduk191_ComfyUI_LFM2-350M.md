# ComfyUI LFM2-350M Node

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) to load and use my custom tuned [LFM2-350M](https://huggingface.co/marduk191/lfm2-350m-dp-marduk191) model trained on 60k base pairs to work as a prompt enhancer for z-image turbo or any other long token model.

## Features

- **Load from HuggingFace** or a **local path**
- Supports fine-tuned models saved with `torch.compile()` (automatically fixes `_orig_mod.` weight prefix)
- Configurable generation parameters (temperature, top_p, top_k, min_p, repetition_penalty)
- System prompt and user prompt inputs

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` folder:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/marduk191/ComfyUI_LFM2-350M.git
   ```

2. Install dependencies:
   ```bash
   cd ComfyUI_LFM2-350M
   pip install -r requirements.txt
   ```

3. Restart ComfyUI.

## Nodes

### LiquidAI LFM-2-350M Loader

Loads the model and tokenizer.

| Input | Description |
|-------|-------------|
| `repo_id` | HuggingFace repository ID (default: `marduk191/lfm2-350m-dp-marduk191`) |
| `local_path` | Optional local path to a pre-downloaded/fine-tuned model |
| `precision` | Model precision: `bf16`, `fp16`, `fp32`, or `auto` |
| `device` | `cuda` or `cpu` |

### LiquidAI LFM-2-350M Generator

Generates text based on prompts.

| Input | Description |
|-------|-------------|
| `model_context` | Connect to Loader's model output |
| `tokenizer` | Connect to Loader's tokenizer output |
| `system_prompt` | System instructions for the model |
| `prompt` | User input text |
| `max_new_tokens` | Maximum tokens to generate (1-4096) |
| `temperature` | Randomness control (default: 0.3) |
| `top_p` | Nucleus sampling parameter |
| `top_k` | K sampling parameter |
| `min_p` | Minimum probability (default: 0.15) |
| `repetition_penalty` | Penalty for repeating tokens (default: 1.05) |

## Recommended Parameters

For best results with LFM2-350M:
- `temperature`: 0.3
- `min_p`: 0.15
- `repetition_penalty`: 1.05

## Requirements

- Python 3.10+
- PyTorch 2.0+
- Transformers 4.55+
- CUDA GPU recommended

## Credits

- Model: [LiquidAI](https://liquid.ai/) - [LFM2-350M on HuggingFace](https://huggingface.co/LiquidAI/LFM2-350M)
- ComfyUI: [comfyanonymous](https://github.com/comfyanonymous/ComfyUI)

## License

MIT License
