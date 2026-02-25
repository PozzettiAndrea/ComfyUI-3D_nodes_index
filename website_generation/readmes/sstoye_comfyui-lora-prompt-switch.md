# ComfyUI LoRA Prompt Switch

Custom nodes for ComfyUI that combine LoRA loading with prompt text injection and a boolean enable/disable switch. Chain multiple nodes together to build switchable LoRA+prompt stacks.

## Features

- **Toggle list UI** for prompt tags — each trigger word gets its own enable/disable checkbox
- **Compact lora+strength combo row** — lora dropdown and strength in a single line
- **Color feedback** — nodes tint green when enabled, red when disabled
- **Automatic comma chaining** — trailing comma for clean multi-node prompt composition
- **Notes field** — store lora links, usage hints, or trigger word documentation
- **Backward compatible** — old workflows with plain text fields load correctly

## Nodes

### LoRA Prompt Switch

Loads a LoRA and appends prompt text when enabled. When disabled, model/clip and prompts pass through unchanged.

**Inputs:**

| Input | Type | Description |
|---|---|---|
| model | MODEL | Base model |
| clip | CLIP | CLIP model |
| lora_name | dropdown | LoRA file to load |
| strength | FLOAT | LoRA strength (-10.0 to 10.0, default 1.0) |
| add_positive | toggle list | Positive prompt tags (each individually togglable) |
| add_negative | toggle list | Negative prompt tags (each individually togglable) |
| enable | BOOLEAN | (optional) Toggle this LoRA on/off, default on |
| positive_prompt | STRING | (optional) Incoming positive prompt to extend |
| negative_prompt | STRING | (optional) Incoming negative prompt to extend |
| notes | STRING | (optional) Notes, links, usage hints (not used in output) |

**Outputs:** `model`, `clip`, `positive_prompt`, `negative_prompt`

### Dual LoRA Prompt Switch

Same concept but for two model/clip pairs (e.g. high-noise and low-noise models in a dual-pass workflow). Each pair gets its own LoRA selection and strength. Prompt text is shared across both.

**Inputs:**

| Input | Type | Description |
|---|---|---|
| model_high | MODEL | High-noise model |
| model_low | MODEL | Low-noise model |
| lora_high | dropdown | LoRA for high-noise model |
| strength_high | FLOAT | Strength for high-noise LoRA |
| lora_low | dropdown | LoRA for low-noise model |
| strength_low | FLOAT | Strength for low-noise LoRA |
| add_positive | toggle list | Shared positive prompt tags |
| add_negative | toggle list | Shared negative prompt tags |
| enable | BOOLEAN | (optional) Toggle on/off, default on |
| clip_high | CLIP | (optional) CLIP for high-noise model |
| clip_low | CLIP | (optional) CLIP for low-noise model |
| positive_prompt | STRING | (optional) Incoming positive prompt |
| negative_prompt | STRING | (optional) Incoming negative prompt |
| notes | STRING | (optional) Notes, links, usage hints |

**Outputs:** `model_high`, `clip_high`, `model_low`, `clip_low`, `positive_prompt`, `negative_prompt`

### Text Prompt Switch

A simple text switch node. Appends text to an input string when enabled, passes through unchanged when disabled. Chain multiple to compose prompts from togglable blocks. Tints green/red based on state.

**Inputs:**

| Input | Type | Description |
|---|---|---|
| enable | BOOLEAN | Toggle on/off |
| text | STRING | Text to append when enabled |
| input_text | STRING | (optional) Incoming text to extend |

**Outputs:** `text`

## Installation

Clone or copy this folder into your ComfyUI `custom_nodes` directory:

```
ComfyUI/custom_nodes/comfyui-lora-prompt-switch/
```

Restart ComfyUI. The nodes appear under the **loaders/lora** and **text** categories.

## Usage

1. Add a **LoRA Prompt Switch** node
2. Select a LoRA and set strength (shown as a compact combo row)
3. Add trigger words to the toggle list — paste comma-separated text to auto-split into entries
4. Toggle individual entries on/off with checkboxes
5. Chain multiple nodes by connecting `model` -> `model` and `positive_prompt` -> `positive_prompt`
6. Use the `enable` toggle or connect it to a boolean switch for quick on/off

## Note

This project was mostly AI-generated using [Claude Code](https://claude.com/claude-code).

## License

MIT
