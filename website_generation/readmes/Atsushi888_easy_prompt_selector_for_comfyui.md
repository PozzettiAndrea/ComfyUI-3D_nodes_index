# Easy Prompt Selector For ComfyUI

A simple custom node for ComfyUI that loads `ill_hair.yml` and provides
an all-in-one dropdown selector to build a prompt string.

This node is designed for stable and repeatable prompt construction,
especially useful for LoRA training and batch generation.

---

## Features

- Load hair-related prompt definitions from `ill_hair.yml`
- Provide dropdown selectors for all categories
- Auto-select default values for specified categories
- Output a single combined prompt string
- YAML is loaded once at ComfyUI startup (fast & stable)

---

## Installation

### 1. Go to your ComfyUI custom_nodes directory

```bash
cd /workspace/ComfyUI/custom_nodes
```

### 2. Clone this repository
```bash
git clone https://github.com/Atsushi888/easy_prompt_selector_for_comfyui.git
```

### 3. Install dependency
```bash
pip install pyyaml
```

### 4. Restart ComfyUI

⸻

## Usage
	1.	Open ComfyUI
	2.	Add node:
## Easy Prompt Selector (All Hair from YAML)
	3.	Select options from dropdown menus
	4.	Connect the prompt (STRING) output to:
	•	Text Concatenate / Join node, or
	•	CLIP Text Encode node directly

⸻

## Auto-select Defaults

Inside easy_prompt_selector/__init__.py, edit:
```bash
DEFAULT_AUTO_SELECT_CATEGORIES = [
    "前髪",
    "髪色（単色）",
]
```
## Notes
	•	ill_hair.yml is loaded once at ComfyUI startup
	•	If you modify ill_hair.yml, restart ComfyUI to apply changes
	•	This node does not support live YAML reloading by design

⸻

## License

MIT License

