# ComfyUI-FlowMatch-Advanced

Custom nodes to make ComfyUI sampling closer to `ai-toolkit` flow-matching behavior for **Flux**, **Qwen-Image**, and **Z-Image**.

## Dependencies

- This custom node has a `requirements.txt` and needs:
  - ai-toolkit-matched `diffusers` pinned to commit `8600b4c10d67b0ce200f664204358747bd53c775`
- If you install manually, run in your ComfyUI Python environment:
  - `pip install -r custom_nodes/ComfyUI-FlowMatch-Advanced/requirements.txt`

## Node

- `FlowMatch Sampler (ai-toolkit exact)`  
  Single all-in-one sampler node: patches model sampling, builds ai-toolkit flowmatch sigmas, and runs sampling directly.

## Model Presets

- `flux`: dynamic shift (`base_shift=0.5`, `max_shift=1.15`, `max_seq_len=4096`)
- `qwen`: dynamic shift (`base_shift=0.5`, `max_shift=0.9`, `max_seq_len=8192`)
- `z-image`: static shift (`shift=3.0`)

## Workflow

1. Load your model and LoRA.
2. Use `FlowMatch Sampler (ai-toolkit exact)`:
   - `sampler_name=euler` (or `res_multistep` if your training setup uses it)
   - defaults match this repo's `config.yaml` sample block (`model_type=z-image`, `seed=42`, `steps=8`, `guidance_scale=1`, `width=768`, `height=1024`)
   - switch `model_type` only when sampling non Z-Image models
   - `width/height` must match your generation resolution
3. Decode the returned latent with VAE.

## Notes

- This node is the only supported path in this repo.
- `force_aitk_timesteps=true` uses `1.0 -> 1.0/steps` timesteps before shift math, matching ai-toolkit behavior more closely.
- When available, the node attempts to use ai-toolkit's own scheduler backend first and falls back to local formulas automatically.
