# Prompt Splitter (Text Only) – ComfyUI

Custom nodes for ComfyUI that split a multiline text prompt into multiple independent STRING outputs.

Each line (ENTER) becomes its own text output, ready to connect to CLIP Text Encode or any node that accepts strings.

---

## Features

- Multiline text input
- One line = one STRING output
- Text-only (no CLIP input required)
- Fixed-output nodes for cleaner workflows
- Works with SD / SDXL / WanVideo / AnimateDiff
- No external dependencies

---

## Included Nodes

This package includes three separate nodes:

Prompt Splitter (3 lines)  
Splits text into 3 outputs

Prompt Splitter (5 lines)  
Splits text into 5 outputs

Prompt Splitter (10 lines)  
Splits text into 10 outputs

Unused lines are returned as empty strings ("") to avoid ComfyUI errors.

---

## Installation

Clone into your ComfyUI custom_nodes folder:

cd ComfyUI/custom_nodes  
git clone https://github.com/elgalardi/comfyui-prompt-splitter

Restart ComfyUI and the nodes will appear under:

comfyui-prompt-splitter

---

## Notes

- This is a text-only splitter
- No prompt processing or formatting is applied
- Lines are split strictly by ENTER
- Designed for clean, readable graphs
