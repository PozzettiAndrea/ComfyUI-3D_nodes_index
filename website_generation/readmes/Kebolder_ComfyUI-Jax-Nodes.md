# ComfyUI-Jax-Nodes

Custom ComfyUI nodes for some niche Krita-focused workflows and easier prompt / pipeline handling.

## Nodes Overview

### Utility / Workflow

- `Conditional Select` (`JAX_ConditionalSelect`)
  - Simple if/else node: chooses between `true_value` and `false_value` based on a boolean `condition` and outputs the selected value.

- `Sampler Pipe In` (`JAX_KritaPipeIn`)
  - Packs a set of sampler-related inputs (`model`, `positive`, `negative`, `vae`, `image`, `clip`, `latent`) into a single `pipe` dictionary that can be passed around a workflow.

- `Sampler Pipe Out` (`JAX_SamplerPipeOut`)
  - Unpacks the `pipe` dictionary back into individual outputs (`model`, `positive`, `negative`, `vae`, `image`, `clip`, `latent`), useful for branching or recombining pipelines.

- `Image Size Multiplier` (`JAX_ImageSizeMultiplier`)
  - Multiplies an input `width` and `height` by a `multiplier` and outputs the new dimensions plus a small Markdown string summarizing the final size.

### Prompt / Conditioning

- `Easy Prompt (W/ Append)` (`JAX_EasyPrompt`)
  - CLIP text encoder that lets you write prompts with inline LoRA tags like `<lora:name:weight>` and append extra positive/negative text. It loads and applies LoRAs to the `model`/`clip`, then returns the updated model and positive/negative conditioning.

- `Easy Prompt` (`JAX_EasyPromptSimple`)
  - Simpler version of the above: supports `<lora:...>` tags but without extra append fields, just `positive` and `negative` inputs.

### Krita Integration


- `Krita Strength` (`JAX_KritaStrength`)
  - Given `sigmas`, a `strength`, and a `denoise` value, computes an integer step index that approximates Krita-style strength control for diffusion, clamping values to safe ranges.
