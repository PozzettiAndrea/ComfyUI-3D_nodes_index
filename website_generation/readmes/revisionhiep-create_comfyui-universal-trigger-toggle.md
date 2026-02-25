# ComfyUI Universal Trigger Toggle

A standalone custom node for ComfyUI that provides an interactive tag-based interface to enable/disable trigger words from **any** LoRA loader or gallery node.

## Features
- **Universal Compatibility**: Works with `Local Lora Gallery`, `Lora Info`, `LoraLoaderTagsQuery`, and any node that outputs trigger words as a string.
- **Smart Sync**: Automatically "scrapes" trigger words from connected upstream nodes. If a node outputs a LoRA path or JSON list, it fetches the real trained trigger words via the Lora-Manager API.
- **Interactive Tags**: Toggle individual words or groups on/off with a clean, pill-shaped UI.
- **Group Mode**: Treats double-comma separated words as a single toggleable unit.
- **Strength Support**: Supports mouse-wheel strength adjustment for individual tags.
- **Zero-Config**: No WebSocket setup required; it monitors node connections in real-time.

## Installation
1. Clone or download this folder into your `ComfyUI/custom_nodes/` directory.
2. Ensure you have [ComfyUI-Lora-Manager](https://github.com/willmiao/ComfyUI-Lora-Manager) installed for trigger word database lookups.
3. Restart ComfyUI.

## Usage
1. Add the **Universal Trigger Toggle** node from the `Lora Manager/utils` category.
2. Connect any LoRA loader's `trigger_words` output to this node's `trigger_words` input.
3. The tags will populate automatically. Click them to toggle their inclusion in the final output string.
4. Use the `filtered_trigger_words` output in your prompt concatenation.

## Credits
- Based on the architectural patterns of the Lora-Manager project.
- Pill UI design optimized for professional workflows.


