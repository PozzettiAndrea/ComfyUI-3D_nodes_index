# Illustrious Prompt Sorter 🛠️

A modular ComfyUI node that reorders prompt tags according to the Danbooru/Illustrious attention hierarchy. 

## 🚀 Features
- **Automatic Danbooru Sorting**: Ensures `1boy`/`1girl` tags stay at the start.
- **Deduplication**: Automatically removes redundant tags.
- **LoRA Interleaving**: Choose where your `<lora:...>` tags appear (after subjects or at the end).
- **Transparency**: Outputs the sorted string so you can verify the results with a Preview Text node.

## 📦 Installation
1. Copy the `comfyui-prompt-sorter-v1.0` folder to your `ComfyUI/custom_nodes/` directory.
2. Restart ComfyUI.

## 💡 Usage
1. Connect your prompt text (from a Trigger node or text box) to the `text` input.
2. Connect your CLIP model to the `clip` input.
3. Connect the `conditioning` output to your KSampler.
4. (Optional) Connect the `sorted_text` output to a **Preview Text** node to see the magic.

---
*Created by Revisionhiep.*

