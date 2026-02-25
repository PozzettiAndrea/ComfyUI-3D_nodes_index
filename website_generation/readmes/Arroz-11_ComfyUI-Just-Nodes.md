# ComfyUI-Just-Nodes

Utility nodes for ComfyUI that solve common tasks without chaining multiple nodes.

## Nodes

### Prompt Stack
Multiline text input that strips empty lines and outputs clean text joined by newlines.

### Picker
Connect multiple text inputs and select one by index or randomly. Inputs grow dynamically as you connect them.

- **manual** mode: select which connected input to use (`list`) and which line within it (`index`)
- **random** mode: uses `seed` to pick a line (`seed % num_lines`)

### Search & Replace
Takes text input and applies search/replace pairs sequentially. Pairs appear as you fill them in (up to 20). Replace widgets support "Convert to input" for dynamic values.

### Labeled Index
Decorative labels alongside an integer passthrough. Write label names in the multiline field as visual reference — the output is the `value` integer unchanged.

## Installation

### ComfyUI Manager
Search for "Just Nodes" in the ComfyUI Manager.

### Manual
Clone into your `custom_nodes` folder:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Arroz-11/ComfyUI-Just-Nodes.git
```

Restart ComfyUI. Nodes appear under the **Just Nodes** category.

## License

MIT
