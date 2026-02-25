# ComfyUI Qwen Rectified Flow Inverter

Custom nodes for ComfyUI that target rectified-flow models (for example, Qwen). This pack focuses on inversion and diagnostics; the latent/image/conditioning noise nodes live in `Skoogeer-Noise` (see `../Skoogeer-Noise`).

## Installation

1. Clone this repository into `ComfyUI/custom_nodes/ComfyUI-QwenRectifiedFlowInverter`.
2. (Optional but recommended) Also install `Skoogeer-Noise` into `ComfyUI/custom_nodes/Skoogeer-Noise` for the forward-diffusion/noise/conditioning helpers.
3. Restart ComfyUI.

## Data types

### `LATENT`

ComfyUI latents are dictionaries containing a `"samples"` tensor.

- Common SD-style latents: `samples` has shape `(B, C, H, W)`.
- Video / flow-matching latents may be 5D: `(B, C, T, H, W)`.

### `CONDITIONING`

ComfyUI represents prompt conditioning as a list of `[embedding, metadata]` entries. This pack reads the embedding tensor from `positive[0][0]` and uses it as the model context during inversion.

## Nodes

### Qwen Rectified Flow Inverter

Runs the rectified-flow integration to produce a partially inverted (re-noised) latent. Supports deterministic velocity amplification, seeded stochastic perturbation, and optional output normalization.

- **Menu category:** `Qwen/Sampling`
- **Returns:** `LATENT`

#### Inputs

| Field | Type | Default | Notes |
|------|------|---------|------|
| `model` | `MODEL` | – | Diffusion model / UNet used to predict velocity. |
| `latent_image` | `LATENT` | – | Source latent to invert. |
| `positive` | `CONDITIONING` | – | Positive prompt conditioning used as context. |
| `seed` | `INT` | `0` | Seed for the velocity perturbation noise. |
| `steps` | `INT` | `20` | Integration budget; effective steps = `int(steps * inversion_strength)`. |
| `inversion_strength` | `FLOAT` | `0.5` | Fraction of the schedule to traverse (0 = no-op). |
| `velocity_amplification` | `FLOAT` | `0.0` | Multiplies predicted velocity by `(1 + velocity_amplification)` each step. |
| `velocity_perturb_strength` | `FLOAT` | `0.0` | Adds seeded noise to velocity (scaled by velocity std). |
| `internal_precision` | enum | `bfloat16` | Autocast dtype while running the UNet (`force_float32` is most stable). |
| `normalize_output` | enum | `enable` | When enabled, normalizes each batch item to mean 0 / std 1 at the end. |

#### Notes

- If you see `NaN detected at step ...`, increase precision (`internal_precision = force_float32`) and/or reduce `velocity_amplification` / `velocity_perturb_strength`.
- `normalize_output = enable` is strongly recommended at higher `inversion_strength`.

---

### Latent Hybrid Inverter (Qwen)

Runs the inverter and an internal forward-diffusion anchor pass, then blends both latents via spherical interpolation (SLERP).

- **Menu category:** `Qwen/Sampling`
- **Returns:** `LATENT`

#### Inputs

| Field | Type | Default | Notes |
|------|------|---------|------|
| `model` | `MODEL` | – | Model used for both passes. |
| `latent_image` | `LATENT` | – | Source latent. |
| `positive` | `CONDITIONING` | – | Context used by the inverter pass. |
| `steps` | `INT` | `20` | Schedule/integration steps. |
| `strength` | `FLOAT` | `0.5` | Target noise level (also used as the forward-diffusion strength). |
| `blend_factor` | `FLOAT` | `0.5` | `0` = 100% forward diffusion (stable), `1` = 100% inverter (creative). |
| `inverter_seed` | `INT` | `0` | Seed for the inverter’s velocity perturbation. |
| `forward_diffusion_seed` | `INT` | `1` | Seed for the forward-diffusion anchor noise. |
| `velocity_amplification` | `FLOAT` | `1.0` | Passed through to the inverter node. |
| `velocity_perturb_strength` | `FLOAT` | `0.2` | Passed through to the inverter node. |
| `internal_precision` | enum | `bfloat16` | Passed through to the inverter node. |
| `normalize_output` | enum | `enable` | Passed through to the inverter node. |

---

### Memory Diagnostics (Pass-Through)

Passes any input through unchanged while printing basic GPU memory statistics to the console.

- **Menu category:** `Qwen/Diagnostics`
- **Returns:** same as input

#### Inputs

| Field | Type | Default | Notes |
|------|------|---------|------|
| `data` | any | – | Input payload (any ComfyUI type). |
| `label` | `STRING` | `""` | Optional label included in the printed line. |
| `synchronize` | enum | `enable` | When enabled, synchronizes GPU kernels before sampling memory. |

## Example workflows

### Manual composition (recommended with Skoogeer-Noise)

1. Encode an image to a latent.
2. Run `Qwen Rectified Flow Inverter`.
3. In `Skoogeer-Noise`, run `Forward Diffusion (Add Scheduled Noise)` with the same `steps` and `noise_strength` but a different seed (this gives an anchor latent samplers expect).
4. Blend the two latents (e.g. `Latent Slerp`) and sample with `denoise` matching the strength you used.

### Hybrid node quickstart

1. Encode an image to a latent.
2. Run `Latent Hybrid Inverter (Qwen)`.
3. Sample the output latent with `denoise = strength`.

## Running the tests

Run:

```bash
./run_tests.sh
```

The script creates (or reuses) a `.venv` folder, installs the dependencies from `requirements.txt`, and launches `pytest`.
