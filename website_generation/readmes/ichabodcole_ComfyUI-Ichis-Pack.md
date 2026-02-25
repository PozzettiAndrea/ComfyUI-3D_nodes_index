# ComfyUI Ichis Pack

A collection of utility nodes for ComfyUI.

## Installation

1. Clone this repository to your ComfyUI's `custom_nodes` directory:

   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/yourusername/ComfyUI_Ichis_Pack.git
   ```

2. Restart ComfyUI

3. (Optional) To set up a development environment, run the `setup_venv.sh` script (requires the `uv` CLI tool for virtualenv and package management):

   ```bash
   ./setup_venv.sh
   ```

   Ensure you have `uv` installed before running this script.

4. Run tests

   - **Run the full test suite:**

     ```bash
     pytest
     ```

   - **Run a quick targeted test (by keyword):**

     ```bash
     pytest -q -k text_selector --maxfail=1
     ```

   - **Run a single test file:**

     ```bash
   pytest tests/test_text_selector.py -q
     ```

## Nodes

### ICHIS Aspect Ratio Plus

A node that provides a selection of common SDXL-optimized aspect ratios with advanced control options.

**Features:**

- Preset aspect ratios optimized for SDXL
- Upscale multiplier
- Dynamic modes: normal, step, and random
- Size mode filtering (all, portrait, landscape, square)
- Individual toggles for each aspect ratio
- Step index reset

### ICHIS Extract Tags

A node that extracts text segments from a comma-separated list based on matching concepts/tags.

**Features:**

- Extract segments containing specified tags/concepts
- Support for multiple concepts at once
- Concepts can be separated by commas and/or newlines
- Case-insensitive matching
- Custom delimiter for combining extracted segments

**Example:**

Input Text:

```text
portrait of a woman, beautiful eyes, big blue eyes, wearing big red clown nose, red lips, face paint, tall, running toward viewer, photorealistic, 8k
```

Input Tags/Concepts:

```text
eyes
nose
lips
face
```

Output with ", " delimiter:

```text
beautiful eyes, big blue eyes, wearing big red clown nose, red lips, face paint
```

This node is particularly useful for extracting specific attributes from longer prompts or creating detail-focused prompts by filtering out certain elements.

### ICHIS Text Selector

A node that allows selecting text segments from a multi-line input with various selection modes.

**Features:**

- Split text by @ markers
- Selection modes: normal, step, and random
- Index-based selection
- Excludable indices with range support (e.g., "1,3-6,8" excludes indices 1, 3, 4, 5, 6, and 8)
- Step mode with automatic progression
- Random selection with seed control

**Example of Exclude Indices:**

- Single indices: `1,3,5` (excludes items 1, 3, and 5)
- Range notation: `2-5` (excludes items 2, 3, 4, and 5)
- Mixed format: `1,3-6,8` (excludes items 1, 3, 4, 5, 6, and 8)

### ICHIS Tag File Loader

Parse CSV/JSON tag catalogs once, cache the metadata, and broadcast category lists for other nodes.

**Features:**

- Supports CSV (row-per-tag, row-per-category list, tag-only) and JSON array formats
- Optional base directory resolution and case-insensitive categories
- Refresh toggle to force re-read when files change
- Emits metadata payload, category list, all tags, resolved path, and cache-hit flag

### ICHIS Tag Category Select

Consume loader metadata and pick one or more categories through dynamic combo widgets.

**Features:**

- Dynamic dropdowns populated from loader metadata (via PromptServer event)
- Multi-category selection with newline-separated hidden string for compatibility
- Outputs selection payload, selected categories, and tags for the chosen categories

### ICHIS Tag Sampler

Sample tags using metadata provided by the loader + selector pipeline (or legacy file inputs).

**Features:**

- Accepts loader metadata plus optional selection payload or category list
- Random or deterministic sampling with min/max bounds
- Returns joined string, count, and list of sampled tags

### ICHIS Save Tags

Persist tag strings or lists to disk for reuse in other tools.

## License

MIT
