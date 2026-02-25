# ComfyUI Linear Theme

A dark, minimal theme for ComfyUI inspired by [Linear](https://linear.app), [Vercel](https://vercel.com), and [Raycast](https://www.raycast.com).

Near-black surfaces, no shadows, indigo accents, 1px borders. Every pixel is intentional.

## What it does

- **Color palette** for the node canvas (LiteGraph) — nodes, links, widgets, slots
- **Full CSS overhaul** for the entire UI — Manager dialog, buttons, dropdowns, tabs, tables, scrollbars, tooltips, context menus, sidebars, inputs, and more
- Everything loads automatically as a custom node extension

## Before / After

The theme replaces the default bright blue buttons in ComfyUI Manager and other dialogs with a cohesive dark UI that matches the canvas.

## Install

### Option 1: Clone into custom_nodes

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Arroz-11/ComfyUI-Linear-Theme.git
```

### Option 2: Manual

1. Download this repo
2. Copy the folder into `ComfyUI/custom_nodes/`
3. Restart ComfyUI

### Color palette (optional)

For the full canvas color palette, import `linear_dark.json` in **Settings > Appearance > Color Theme > Import**.

The CSS overrides load automatically from the custom node — the JSON is optional but recommended for the complete experience.

## Design tokens

| Token | Value | Usage |
|---|---|---|
| Background | `#09090b` | Canvas background |
| Surface | `#18181b` | Nodes, dialogs, panels |
| Elevated | `#1c1c20` | Widgets, inputs, buttons |
| Border | `#27272a` | All borders (1px) |
| Accent | `#818cf8` | Selection, active states, connecting links |
| Text primary | `#f4f4f5` | Main text |
| Text secondary | `#a1a1aa` | Secondary labels |
| Text muted | `#71717a` | Descriptions, hints |
| Danger | `#ef4444` | Errors, destructive actions |
| Shadow | `rgba(0,0,0,0)` | None — flat surfaces only |

## Slot colors

All slot colors are vibrant and unchanged from the widely-used Obsidian Dark palette for maximum readability.

## License

MIT
