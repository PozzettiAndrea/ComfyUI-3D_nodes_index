# CLIP Prompt Splitter (5 lines) – ComfyUI

Custom node for ComfyUI that splits a multiline prompt into 5 independent CLIP conditionings.

Each line (ENTER) becomes its own conditioning output.

---

## Features

- Multiline prompt input
- One line = one CLIP conditioning
- 5 fixed outputs
- Works with SD / SDXL / WanVideo / AnimateDiff
- No external dependencies

---

## Installation

Clone into your ComfyUI custom_nodes folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/clip_prompt_splitter
