# ComfyUI – Flux 2 Empty Latent Presets

A custom **ComfyUI node** that provides Flux 2–recommended resolution presets for quickly creating empty latents, without manually entering width and height values.


* Covers **Draft → Standard → High Detail** megapixel tiers
* Supports common **aspect ratios** (square, landscape, portrait)
* All resolutions are **divisible by 8**
* Optional **width/height inversion**
* Cleanly namespaced (`Flux 2 / Latents`)

---

## Reference

Preset values are based on the recommendations published here:

[https://help.scenario.com/en/articles/flux-2-models-the-essentials/#resolution-detail](https://help.scenario.com/en/articles/flux-2-models-the-essentials/#resolution-detail)

---

## Installation

1. Clone or download this repository into your ComfyUI `custom_nodes` directory:

```bash
ComfyUI/custom_nodes/ComfyUI-Flux2LatentPresets/
```

2. Ensure the folder structure looks like this:

```
ComfyUI-Flux2LatentPresets/
├── __init__.py
└── nodes/
    ├── __init__.py
    └── flux2_latent_presets.py
```

3. Restart **ComfyUI**

---

## Node Location in ComfyUI

After restarting, you’ll find the node under:

```
Add Node → Flux 2 → Latents → Flux 2 Empty Latent Presets
```

## Node Outputs

* **LATENT** — empty latent tensor
* **Width** — pixel width
* **Height** — pixel height

The latent is created with shape:

```
(batch_size, 4, height / 8, width / 8)
```

---

## Notes

* MP labels are informational only; ComfyUI uses pixel dimensions
* The 400² pixel preset is mentioned as the safe minimum by BFL and good for **draft / ideation**
* Higher MP presets require significantly more VRAM

---

## License

MIT 

