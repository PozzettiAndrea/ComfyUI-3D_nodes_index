

https://github.com/user-attachments/assets/3fd31dac-508d-48c5-96c4-7c02c4f897b7

# Awesome ComfyUI 3D

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated index of 220+ ComfyUI nodes for 3D generation, processing, and visualization.

**[Browse the visual index →](https://pozzettiandrea.github.io/ComfyUI-3D_nodes_index/)**

## Categories

- Image-to-3D
- Text-to-3D
- Multi-View Generation
- Mesh Processing
- Texturing
- Gaussian Splatting
- Rigging & Animation
- Depth & Normal
- Visualization
- CAD
- Human Body

## How It Works

1. **Fetch** - Pulls ~3700 nodes from [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) + the Comfy Registry
2. **Filter** - Uses AI (DeepSeek via OpenRouter) to classify 3D-relevant packages
3. **Index** - Generates a searchable visual catalog (`index.html`)

## Updating the index

All tooling lives in `website_generation/`. The pipeline is **three scripts run in order**,
each writing a dated CSV that the next stage reads:

```bash
# One-time setup (from repo root)
python3 -m venv .venv
.venv/bin/pip install tqdm

# Run the pipeline (from website_generation/)
cd website_generation
export OPENROUTER_API_KEY=...                 # your OpenRouter key

../.venv/bin/python fetch_all_nodes.py        # 1. FETCH    -> all_comfyui_nodes_<date>.csv   (no key needed)
../.venv/bin/python run_deepseek_prompt.py    # 2. CLASSIFY -> ai_3d_nodes_<date>.csv + ai_non_3d_nodes_<date>.csv   (uses key, costs $)
../.venv/bin/python generate_index.py         # 3. GENERATE -> ../index.html
```

Then commit and push the regenerated `index.html` plus the two new dated CSVs:

```bash
cd ..
git add index.html website_generation/ai_3d_nodes_*.csv website_generation/ai_non_3d_nodes_*.csv
git commit -m "Update index: N 3D nodes (<date> refresh)"
git push
```

**Notes**
- **Incremental.** Both fetch and classify skip any repo already present in an
  `ai_3d_nodes*.csv` / `ai_non_3d_nodes*.csv`, so each run only processes *new* repos. The
  full catalog is the union of all dated `ai_3d_nodes*.csv` files (newest entry wins).
  Tradeoff: a repo already in the index won't have its README/stars refreshed.
- **Stages are independent.** The dated CSVs are checkpoints — if stage 3 fails you can
  re-run it without re-fetching or re-classifying.
- `all_comfyui_nodes_*.csv` and `.venv/` are gitignored.

## Contributing

PRs welcome to add packages or improve classifications.

## License

MIT
