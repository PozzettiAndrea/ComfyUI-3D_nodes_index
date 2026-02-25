# ComfyUI-Differential-Encode

Seed-sensitive CLIP text encoder for ComfyUI. Designed to fight seed collapse with z-image and similar models that tend to ignore seed changes by injecting controlled, seed-driven perturbations into token embeddings and pooled outputs.

## Visual comparison
Same prompt & same seed; only the text encoder differs.

Prompt used: **阳光雀斑女孩：金发扎成松散的侧马尾，脸上有可爱的雀斑，淡妆，笑容灿烂。穿着淡蓝色碎花吊带裙，身材苗条修长。背景是午后的向日葵花田。画风：电影级写实，光影柔和.**

<table>
  <tr>
    <th align="left">Native CLIP Text Encode</th>
    <td align="center"><img width="360" alt="Vanilla-1" src="https://github.com/user-attachments/assets/d1acbc83-ae22-4bd1-afc4-d7352dce5f85" /></td>
    <td align="center"><img width="360" alt="Vanilla-2" src="https://github.com/user-attachments/assets/feb79b9c-697e-4998-be73-984b042451cb" /></td>
    <td align="center"><img width="360" alt="Vanilla-3" src="https://github.com/user-attachments/assets/0c9faab5-2040-40be-a0dc-daca203965f7" /></td>
  </tr>
  <tr>
    <th align="left">CLIP Text Encode (Differential)</th>
    <td align="center"><img width="360" alt="Differential-1" src="https://github.com/user-attachments/assets/76186952-98ad-4db9-aeb2-c5212ef275bf" /></td>
    <td align="center"><img width="360" alt="Differential-2" src="https://github.com/user-attachments/assets/07815b1a-f717-457d-9367-e487350fcf26" /></td>
    <td align="center"><img width="360" alt="Differential-3" src="https://github.com/user-attachments/assets/d8d82d95-7632-470d-8001-c1609d2db8cd" /></td>
  </tr>
</table>

## Workflow example
<img width="1406" height="940" alt="Workflow" src="https://github.com/user-attachments/assets/62ebcac7-6da9-4a84-b7e0-f0e78a042f31" />

## Install
Copy or clone this folder into `ComfyUI/custom_nodes/ComfyUI-Differential-Encode/` and restart ComfyUI. The node appears as **CLIP Text Encode (Differential)** under `conditioning`.

## Usage
Replace the standard `CLIPTextEncode` in your workflow with **CLIP Text Encode (Differential)**. Wire:
- `clip`: your usual CLIP from the checkpoint loader.
- `text`: prompt.
- `seed`: tie to your sampler seed for consistent runs, or vary independently for extra diversity.

## Parameters
- `noise_std` (default 0.18): Gaussian noise per token. Higher = more diversity, too high can drift semantics.
- `token_dropout` (default 0.10): Probability to drop entire token embeddings.
- `per_token_gain_std` (default 0.12): Multiplicative jitter per token (1 + N(0,std)) to reshape emphasis.
- `global_offset_std` (default 0.08): Seeded shift shared by all tokens; nudges conditioning between seeds.
- `pooled_noise_std` (default 0.05): Noise on pooled_output for models using the pooled branch.
- `pooled_global_offset_std` (default 0.04): Global shift on pooled_output.
- `preserve_magnitude` (default True): Re-normalize to original mean/std to avoid blowing up magnitudes.
- `orthogonalize_noise` (default True): Project noise off the original token directions to keep semantics while adding variety.
- `min_std_scale` (default 1e-3): Floor for scaling noise so low-variance prompts still get variation.

## Tuning tips
- Start with defaults; if images still look identical, raise `noise_std` to 0.25–0.35 and `global_offset_std` to ~0.12, or increase `token_dropout` to 0.15.
- If prompts get too loose, lower `per_token_gain_std` and keep `orthogonalize_noise` on.
- For refiner-heavy or pooled-dependent models, bump `pooled_noise_std`/`pooled_global_offset_std` together.

## Notes
- All perturbations are deterministic per seed.
- Metadata fields `differential_*` are stored in the conditioning dict for downstream inspection.


