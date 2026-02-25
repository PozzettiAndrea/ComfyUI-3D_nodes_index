# Latent Astronaut - ComfyUI Nodes

Custom nodes for ComfyUI focused on batch processing and iteration workflows.

## Installation

Clone this repository into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui-latent-astronaut.git
```

Restart ComfyUI.

## Nodes

### For Loop

A simple for loop that iterates a fixed number of times.

**For Loop Start**
- Inputs:
  - `count` - Number of iterations (1 to 10000)
  - `initial_value0-3` - Optional pass-through values (preserved between iterations)
- Outputs:
  - `flow` - Connect to For Loop End
  - `index` - Current iteration index (0 to count-1)
  - `value0-3` - Pass-through values

**For Loop End**
- Inputs:
  - `flow` - From For Loop Start
  - `value0-3` - Values to pass to next iteration or output
- Outputs: `value0-3` - Final values after all iterations


### String List

Utilities for working with lists of strings.

**String List from Text**

Convert multi-line text to a list of strings with wildcard expansion.

```
a {red|blue|green} cat
a {happy|sad} dog
a flying bird
```

With `seed=42`, wildcards expand deterministically. With `seed=0`, they're random each run.

- Input: `text` (multiline), `seed`
- Outputs: `strings` (list), `count`

**String List Combine**

Combine up to 4 string lists into one.

**String List Index**

Get a single string from a list by index.

### LoRA Selector

Select and load one LoRA from a list based on an index. Useful for batch processing or iterating through LoRAs in a loop.

**LoRA Loader Selector**

Full LoRA loader with model and CLIP support. Supports up to 16 LoRA slots.

- Inputs:
  - `model`, `clip` - Model and CLIP to modify
  - `index` - Which LoRA to load (0-15)
  - `strength_model`, `strength_clip` - LoRA strengths
  - `lora_0` through `lora_15` - LoRA slots
- Outputs: `model`, `clip`, `lora_name`, `count` (number of configured LoRAs)

**LoRA Loader Model Only Selector**

Model-only version (no CLIP modification).

- Inputs: `model`, `index`, `strength`, `bypass`, `lora_0` through `lora_15`
- Outputs: `model`, `lora_name`, `count`

Set unused slots to "None". Toggle `bypass` to quickly disable all LoRA loading without changing your selections.

## Example Workflows

Example workflows are available in the `workflows/` folder.

### Basic For Loop

1. Use **For Loop Start** with `count=5`
2. Use `index` output to drive parameters
3. Connect outputs through **For Loop End**
4. Values passed to End are available in next iteration

## License

MIT
