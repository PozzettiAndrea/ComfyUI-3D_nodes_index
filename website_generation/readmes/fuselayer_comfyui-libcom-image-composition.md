# ComfyUI Image Harmonization (Multi‑Model)

A comprehensive ComfyUI custom node set for image harmonization with multiple research‑grade models:
- CDTNet (CVPR 2022)
- iSSAM (lightweight CDTNet variant)
- Harmonizer (EfficientNet‑based)
- PCT‑Net (CVPR 2023, RakutenTech) — vendor‑integrated with full‑resolution application

This repository is self‑contained:
- Checkpoints are included under `checkpoints/` (small files, <20 MB each).
- The required PCT‑Net upstream code is vendored under `model/vendor/pctnet_rt/upstream/`.
- No auto‑download steps are required; clone → restart ComfyUI → use.

---

## At a Glance

- Multi‑model node (“Image Harmonization”) with a model dropdown
- Auto node (“Image Harmonization (Auto)”) that picks a model by input size
- PCT‑Net adapter that:
  - runs the parameter network at 256×256 (as in paper),
  - applies the color transform at full resolution (foreground region),
  - exposes two controls: `pctnet_strength` and `pctnet_blend_mode`.
- Harmony score node (BargainNet) to evaluate composites.

The PCT‑Net controls are always visible on the Multi‑Model node UI for convenience, and are ignored when the selected model is not a PCT‑Net.

---

## Supported Models

| Model          | Type                  | LR Size | Notes                                                                 |
|----------------|-----------------------|---------|-----------------------------------------------------------------------|
| CDTNet_iHarmony4_256 | CDTNet (full)         | 256     | LUT + refinement                                                      |
| CDTNet_HAdobe5k_2048 | CDTNet (full)         | 512 base| High‑res finetune; best quality                                       |
| CDTNet_sim_base256   | CDTNet (sim)          | 256     | LUT only (fast)                                                       |
| iSSAM_256           | iSSAM                  | 256     | Lightweight CDTNet path                                               |
| Harmonizer          | Filter‑based           | 256     | EfficientNet backbone                                                 |
| Enhancer            | Filter‑based           | 256     | Variant of Harmonizer                                                 |
| PCTNet_CNN          | PCT‑Net (CNN)          | 256     | Low‑res param net; full‑res application                               |
| PCTNet_ViT          | PCT‑Net (ViT)          | 256     | Low‑res param net; full‑res application                               |

---

## Installation

1) Clone into ComfyUI custom_nodes
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/comfyui-libcom-image-composition.git
cd comfyui-libcom-image-composition
````

2. (Portable ComfyUI Python) Install minimal deps


```
# from ComfyUI root
cd python_embeded
.\python.exe -m ensurepip --upgrade
.\python.exe -m pip install --upgrade pip wheel setuptools
.\python.exe -m pip install torchvision kornia albumentations easydict
```

3. Checkpoints

- Checkpoints are included in this repo under `checkpoints/`:
    - `CDTNet_iHarmony4_256.pth`
    - `CDTNet_HAdobe5k_2048.pth`
    - `CDTNet_sim_base256.pth`
    - `issam256.pth`
    - `harmonizer.pth`
    - `enhancer.pth`
    - `PCTNet_CNN.pth`
    - `PCTNet_ViT.pth`

4. Vendored PCT‑Net upstream code

- Included under `model/vendor/pctnet_rt/upstream/iharm/` (no download needed).
- The builder uses `BMCONFIGS['CNN_pct']['params']` and `BMCONFIGS['ViT_pct']['params']` to instantiate PCT‑Net exactly as trained, then loads checkpoints (parameters + buffers).

5. Restart ComfyUI

- On startup, the console will list available models and PCT‑Net variants.

---

## Usage

![test all example](example_workflows/test_all_workflow.png)

### Image Harmonization (Multi‑Model)

- Inputs:
    - `composite_image` (IMAGE)
    - `mask` (MASK, white=foreground region to harmonize)
    - `model_variant` (dropdown)
    - `pctnet_strength` (FLOAT): scales PCT‑Net color‑transform parameters (ignored for non‑PCT‑Net). Default 1.0 (no change).
    - `pctnet_blend_mode` (dropdown): upstream | mask | attention (ignored for non‑PCT‑Net). Default upstream.
    - `max_resolution` (INT): resize ceiling for processing (default 1024).
- Output:
    - `harmonized_image` (IMAGE)

Tips for PCT‑Net:

- CNN: for sharper edges, set `pctnet_blend_mode="mask"` (avoids attention smoothing).
- ViT: `upstream` blend is usually fine; adjust `pctnet_strength` around 0.8–1.1 as needed.

### Image Harmonization (Auto)

- Inputs:
    - `composite_image`, `mask`
    - `prefer_quality` (bool), `max_resolution` (int)
- Behavior:
    - Picks a model by input size and preference. The PCT‑Net controls are not used here.

### Harmony Score

- Inputs:
    - `composite_image`, `mask`, optional `harmonized_image`
- Output:
    - `harmony_score` (FLOAT), `score_text` (STRING)

---

## Project Layout

text

```
comfyui-libcom-image-composition/
├── __init__.py
├── nodes.py                              # ComfyUI nodes (Multi‑Model, Auto, Harmony Score)
├── checkpoints/                          # Included .pth files (small models)
├── model/
│   ├── base.py, cdtnet.py, issam.py, harmonizer.py, enhancer.py, filter.py, module.py, unet.py
│   ├── vendor/
│   │   └── pctnet_rt/
│   │       ├── __init__.py               # Builder: PCTNet(**BMCONFIGS['...']['params'])
│   │       └── upstream/iharm/           # Vendored PCT‑Net repo subset
│   │           ├── mconfigs/base.py      # BMCONFIGS { 'CNN_pct': {'params': …}, 'ViT_pct': {'params': …} }
│   │           ├── model/base/pct_net.py # PCTNet network (only class, no builder logic)
│   │           └── … (data/, engine/, model/modeling/, utils/)
│   └── evaluation/                       # Harmony score (BargainNet)
│       └── harmony_scorer.py
└── utils/
    └── model_registry.py
```

---

## Technical Notes

### CDTNet / iSSAM / Harmonizer

- Implementations follow the original repos (CDTNet includes LUT + refinement except `sim_*`).

### PCT‑Net (CNN & ViT)

- Exact training config is read from `BMCONFIGS['…']['params']` and passed as `PCTNet(**params)`.
- Checkpoints are loaded in full: parameters + buffers (`strict=False`).
- The adapter:
    - Pads inputs to multiples of 16 (down/upsample stability),
    - Runs the parameter net at 256×256,
    - Applies the color transform at full resolution via `image_fullres/mask_fullres`,
    - Exposes optional `strength` and `blend_mode`:
        - `strength`: scalar applied to parameters before transform.
        - `blend_mode`: `upstream` (as returned by model), `mask`, or `attention` (force attention blend).
- Results:
    - CNN attention can be slightly soft (low‑res attention upsampled). Use `mask` blend for sharper edges.
    - ViT and CNN can look tonally different (different normalizations/backbones); use `strength` to tune.

---

## Troubleshooting

- “Checkpoint not found”: ensure the filename exists in `checkpoints/` and matches the selected variant.
- PCT‑Net artifacts (“metallic/dark” or “checkerboard”):
    - Check console for `[PCTNet vendor kwargs]` and `PCTNet weights loaded perfectly.`.
    - If you see “Missing=… Unexpected=…”, your code or BMCONFIGS may be mismatched; ensure `PCTNet(**BMCONFIGS['…']['params'])`.
    - For CNN blur, use `pctnet_blend_mode="mask"`.
- CUDA OOM: reduce `max_resolution` or use faster variants (`sim`/iSSAM/Harmonizer).

---

## Performance Tips

- CDTNet_HAdobe5k_2048 is highest quality (slower, high memory).
- CDTNet_sim_base256 and iSSAM are fast.
- PCT‑Net runs LR param net (fast) but applies full‑res transform (memory depends on image size).

---

## Credits
- [bcmi/libcom](https://github.com/bcmi/libcom), Niu, Li and Cong, Wenyan and Liu, Liu and Hong, Yan and Zhang, Bo and Liang, Jing and Zhang, Liqing (2021) 
- CDTNet: [Cong et al., CVPR 2022](https://github.com/bcmi/CDTNet-High-Resolution-Image-Harmonization)
- PCT‑Net: [Guerreiro et al., CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Guerreiro_PCT-Net_Full_Resolution_Image_Harmonization_Using_Pixel-Wise_Color_Transformations_CVPR_2023_paper.html)
- Harmonizer: [https://github.com/ZHKKKe/Harmonizer](https://github.com/ZHKKKe/Harmonizer)
- Harmony Score (BargainNet): part of the Libcom toolkit.

If you use these models, please cite the original papers.

---

## License

- This repository: Apache 2.0 (see LICENSE).
- Vendored PCT‑Net upstream code and weights retain their original licenses. Please review and comply with those terms.

---

## Contributing

PRs welcome! Please:

1. Fork
2. Create a feature branch
3. Submit a PR with clear description and minimal diffs
