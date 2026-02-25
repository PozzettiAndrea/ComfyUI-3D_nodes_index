# ComfyUI-ModelSamplingSD3Advanced

A ComfyUI node that adds **windowed, curved “shift” control** for **Flow Matching** samplers (SD3-style / flow schedules). It is a drop-in replacement for Comfy's included ModelSamplingSD3 node.

This was built specifically for Flow Match models such as bigASP, where I have observed:

- **Better prompt adherence** at **higher shift** (especially early in denoising),
- but **worse image quality / texture / coherence** if that high shift persists into later steps.
- Especially when using character LoRAs.

ModelSamplingSD3Advanced lets you apply a high shift in early steps (to lock in prompt adherence), then transition to a lower shift later (to maintain quality.)

---

### What this node does

The node patches the model’s `model_sampling` with a custom flow schedule where **shift varies over denoise progress**:

- `shift_start` used near the beginning (high noise / early steps)
- `shift_end` used later (low noise / late steps)
- a **window** (`start_percent` → `end_percent`) defines where the transition occurs
- a **curve** controls how that transition feels (linear, cosine, smoothstep, etc.)

---

### Installation

You can clone this repo into `comfyui/custom_nodes/ComfyUI-ModelSamplingSD3Advanced` or search for "Model Sampling SD3 Advanced" in the ComfyUI Manager.

---

### Inputs

- **model**: The incoming model.
- **shift_start**: Shift value at the beginning (early/high-noise steps).
- **shift_end**: Shift value at the end (late/low-noise steps).
- **start_percent**: Denoise progress where the transition window begins.
- **end_percent**: Denoise progress where the transition window ends.
- **curve**: Shape of the transition inside the window:
  - `linear`, `cosine`, `smoothstep`, `ease_in`, `ease_out`, `sigmoid`
- **outside_window**: Controls behavior outside the window:
  - `hold` (default): before `start_percent` uses `shift_start`, after `end_percent` uses `shift_end`
  - `baseline`: outside the window uses the model’s default shift (strictly windowed modulation)
  - `linear_extrapolate`: extends the shift trend beyond the window (advanced)
- **multiplier**: Flow schedule timestep multiplier (typically 1000). Keep default unless you know why you’re changing it.

### Output

- **MODEL**: A patched model with the modified sampling schedule.

---

## Notes / Caveats

- This node modifies the sampling schedule; results can be model-specific.
- The node is meant for **Flow Matching / SD3-style schedules** (not classic epsilon/DDIM schedules).
- If your workflow/sampler expects strictly monotonic sigmas, this implementation enforces monotonicity as a safety measure.