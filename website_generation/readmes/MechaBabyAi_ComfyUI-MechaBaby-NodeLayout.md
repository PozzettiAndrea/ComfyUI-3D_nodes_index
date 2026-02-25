# ComfyUI-MechaBaby-NodeLayout

[中文说明](README_ZH.md) | **English**

A node layout helper extension for ComfyUI. Assists in arranging and aligning nodes on the canvas **without modifying workflow files** — all operations are frontend-only.

## Features

### Shortcuts

| Shortcut | Action |
|----------|--------|
| **F8** (default) | Open arrangement mode menu |
| **F9** (default) | Open expand/collapse menu |

Both shortcuts are customizable via **⚙ 排列菜单快捷键** (arrangement menu) or **⚙ 展开菜单快捷键** (expand menu) in the respective submenus.

### Arrangement Modes

| Mode | Description |
|------|-------------|
| **By Type** | Group nodes of the same type, right-aligned within each group |
| **By Execution Order** | Arrange left-to-right by topological sort |
| **Spider Web** | Mind-map style: center node with recursive left/right expansion; each branch stacks vertically |
| **Level Columns** | Center node with level-based columns: inputs on the left, outputs on the right; no overlap within columns |
| **Grid** | Arrange nodes in a regular grid |
| **Built-in (Left)** | Use ComfyUI's built-in `arrange` method |

**Spider Web** and **Level Columns** use the selected node as center; if none is selected, they use the last output node (e.g. SaveImage) or the last node on the canvas.

Nodes without outputs (e.g. SaveImage, PreviewImage) are placed to the **right** of their input provider, not on the left.

### Expand / Collapse

| Action | Description |
|--------|-------------|
| **Collapse selected** | Collapse selected nodes to title bar only |
| **Expand selected** | Expand selected nodes to full content |
| **Collapse all** / **Expand all** | Apply to all nodes on canvas |
| **Node right-click** | Right-click a node for "▶ Collapse" or "◀ Expand" |

### Shrink to Min Size

- **Shrink to min height**: Keep width, compute height from inputs/outputs/widgets
- **Shrink to min width**: Keep height, compute width from content
- **Shrink to min size**: Both width and height to the minimum needed to show all properties

### Alignment Tools

For selected nodes (or all nodes if none selected):

- **Align**: Left, Right, Top, Bottom
- **Center**: Horizontal, Vertical
- **Match size**: Equal width, Equal height
- **Distribute**: Horizontal, Vertical

## Usage

1. **Shortcut**: Press **F8** (or your custom key) to open the arrangement menu
2. **Context menu**: Right-click on empty canvas → **▣ MechaBaby 节点布局** → choose layout or alignment

When nodes are selected, alignment/distribution affects only the selection; arrangement modes apply to the selection if any, otherwise to all nodes.

## Installation

Place this extension in `ComfyUI/custom_nodes/` and restart ComfyUI.

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/MechaBabyAi/ComfyUI-MechaBaby-NodeLayout.git
```

## Compatibility

Works with standard ComfyUI (LiteGraph). Can coexist with ComfyUI-Custom-Scripts, KayTool, etc.

---

[中文说明](README_ZH.md)
