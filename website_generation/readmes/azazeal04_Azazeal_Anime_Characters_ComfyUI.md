# Azazeal_Anime_Characters_ComfyUI

Anime character selector nodes for ComfyUI.

## What changed (Node 2.0)

This pack now uses a **Node 2.0-style data-driven design** by default:

- Registers only a small fixed set of nodes at startup.
- Uses an on-disk index cache (`anime_data/.index.json`).
- Loads full prompt maps lazily when needed.

This avoids creating one ComfyUI node per anime during import, which significantly improves startup performance on large datasets.

## Nodes

### 1) Anime Character Prompt Selector (V2)
Category: `Anime_Character`

Inputs:
- `anime_title` (dropdown)
- `character_name` (string)

Outputs:
- `character_prompt`
- `character_name`
- `anime_title`

### 2) Anime Character List (V2)
Category: `Anime_Character/Tools`

Helper node that provides a character dropdown for an anime title.

## Backward compatibility (Node 1.0)

Legacy per-anime nodes are still supported but are **disabled by default** for performance.

Enable them when you need to load old workflows:

```bash
AZAZEAL_ENABLE_LEGACY_NODES=1
```

When enabled, the package dynamically registers legacy `AnimePromptNode_*` node types so older workflows can deserialize.

## Installation

```bash
git clone https://github.com/azazeal04/Azazeal_Anime_Characters_ComfyUI.git
```

Clone into `ComfyUI/custom_nodes` and restart ComfyUI.

## Requirements

- Python 3.10+
- ComfyUI

## License

MIT
