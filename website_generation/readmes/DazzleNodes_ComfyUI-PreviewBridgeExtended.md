# ComfyUI Preview Bridge Extended

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![ComfyUI Registry](https://img.shields.io/badge/ComfyUI-Registry-green.svg)](https://registry.comfy.org/publishers/djdarcy/nodes/comfyui-preview-bridge-extended)
[![GitHub release](https://img.shields.io/github/v/release/DazzleNodes/ComfyUI-PreviewBridgeExtended?include_prereleases&label=version)](https://github.com/DazzleNodes/ComfyUI-PreviewBridgeExtended/releases)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Enhanced Preview Bridge node with optional mask input support. Extends the Preview Bridge concept with configurable mask source selection and proper empty mask detection.

## Overview

ComfyUI's IMAGE type is RGB-only (3 channels) - alpha channels are separated to MASK at load time. This means the original Preview Bridge cannot detect masks from input images. This node solves that limitation by:

1. Adding an optional MASK input from upstream nodes (LoadImage, SAM, detection nodes, etc.)
2. Allowing users to select how input masks interact with MaskEditor drawings
3. Properly detecting empty masks for blocking decisions

## Background

This node extends the Preview Bridge concept from [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack). We've contributed minimal fixes to the original node via PRs:

- [PR #1172](https://github.com/ltdrdata/ComfyUI-Impact-Pack/pull/1172) - Fix for current MaskEditor compatibility
- [PR #1009](https://github.com/ltdrdata/ComfyUI-Impact-Pack/pull/1009) - Earlier fix contribution

Since Impact-Pack maintains a conservative approach to major changes, this repo was created to develop extended features (two-layer mask editing, editor target modes, instant preview refresh) in this standalone node or as a part of the [DazzleNodes pack](https://github.com/DazzleNodes/DazzleNodes). This allows for more rapid iteration, while keeping the upstream PRs focused on essential fixes.

## Features

- **Optional Mask Input**: Accept masks from upstream nodes alongside MaskEditor drawings
- **Configurable Mask Output**: Choose between combined, input_mask, or mask_editor modes
- **Two-Layer Visualization**: Red tint for input mask, orange tint for editor mask
- **Instant Preview Refresh**: Preview updates immediately when changing display mode widgets
- **Mask Restoration**: Persist masks across image changes (never, always, if_same_size)
- **Smart Empty Detection**: Detects placeholder masks (64x64) and all-zero masks
- **Mask Combination**: OR (union) combination of multiple mask sources
- **Flexible Blocking**: Block on empty mask or always (debugging backstop)
- **Preview Display**: Visual overlay showing masked areas with distinct colors
- **Debug Info Output**: Detailed information about mask processing state

## Prerequisites

- ComfyUI installation
- Python 3.10+ (or ComfyUI's embedded Python)
- PyTorch (included with ComfyUI)

## Installation

### Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DazzleNodes/ComfyUI-PreviewBridgeExtended.git
```

Then restart ComfyUI or use **Manager → Refresh Node Definitions**.

### Manual Installation

1. Download the [latest release](https://github.com/DazzleNodes/ComfyUI-PreviewBridgeExtended/releases)
2. Extract to `ComfyUI/custom_nodes/ComfyUI-PreviewBridgeExtended/`
3. Restart ComfyUI
4. Find the node in: **DazzleNodes → Preview Bridge Extended**

## Usage

### Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| images | IMAGE | Yes | Input image(s) |
| mask_opt | MASK | No | Optional mask from upstream (LoadImage, SAM, etc.) |
| mask_output | Selection | No | What goes to output mask slot (default: combined) |
| editor_target | Selection | No | Which layer MaskEditor affects (default: combined) |
| restore_mask | Selection | No | Mask restoration mode (default: never) |
| block | Selection | No | Blocking mode (default: never) |

### Mask Output Options

Controls what goes to the OUTPUT mask slot:

| Option | Behavior |
|--------|----------|
| `combined` | OR (union) combine input_mask + editor mask |
| `input_mask` | Only output the input mask layer |
| `mask_editor` | Only output the editor mask layer |

### Editor Target Options

Controls which layer MaskEditor affects:

| Option | Behavior |
|--------|----------|
| `combined` | Edit both input + editor masks together (default) |
| `mask_editor` | Only edit editor mask (input mask shown as red, locked) |
| `input_mask` | Only edit input mask (editor mask shown as orange, locked) |

### Restore Mask Options

| Option | Behavior |
|--------|----------|
| `never` | Do not restore cached masks (default) |
| `always` | Always restore cached mask, resize if needed |
| `if_same_size` | Only restore if new image has same dimensions |

### Block Options

| Option | Behavior |
|--------|----------|
| `never` | Never block execution (default) |
| `if_empty_mask` | Block when OUTPUT mask is empty |
| `if_empty_editor` | Block if user hasn't drawn in MaskEditor |
| `always` | Always block execution (debugging backstop) |

### Outputs

- **image**: Pass-through of input image
- **mask**: Final processed mask based on mask_output selection
- **info**: Debug string showing mask processing details

### Common Use Cases

#### 1. Combine LoadImage Mask with MaskEditor

Connect LoadImage's MASK output to `mask_opt`, set `mask_output` to "combined":
- Users can draw additional mask areas in MaskEditor
- Both sources are combined using OR operation
- Preview shows red (input) + orange (editor) overlays

#### 2. Use Detection Node Masks

Connect SAM or other detection node output:
- Set `mask_output` to "input_mask" to use only the detection
- Or "combined" to allow refinement with MaskEditor
- Set `editor_target` to control which layer is editable

#### 3. Fallback to MaskEditor Only

Set `mask_output` to "mask_editor":
- Ignores any input mask for output
- Uses only user-drawn masks from MaskEditor

## How It Works

1. **Mask Detection**: Checks if input mask is valid (not None, not all zeros, not placeholder 64x64)
2. **Output Selection**: Based on `mask_output`, determines what goes to output slot
3. **Combination**: For "combined" mode, uses OR operation (sum + clamp)
4. **Resizing**: Automatically resizes masks to match image dimensions
5. **Blocking**: If `block` enabled and final mask is empty, blocks execution

## Technical Details

### LayerCache Architecture

The node uses a unified `LayerCache` system for mask storage with three explicit layers:
- **upstream**: Original mask from `mask_opt` input (immutable reference)
- **additions**: User additions from MaskEditor
- **subtractions**: User erasures/subtractions from original mask

The "additions win" formula ensures predictable output: `combined = max(upstream - subtractions, additions)`

### Empty Mask Detection

Masks are considered empty if:
- None or numel() == 0
- Shape is (1, 64, 64) or (64, 64) with all zeros (Preview node placeholder)
- All values are zero

### Mask Combination (OR)

```python
combined = torch.sum(torch.stack(masks_to_combine, dim=0), dim=0)
combined = torch.clamp(combined, 0, 1)
```

### Instant Preview Refresh

When `mask_output` or `editor_target` widgets change, JavaScript listeners trigger an API call to regenerate the preview from the current LayerCache state. This provides WYSIWYG behavior without re-running the workflow.

## Troubleshooting

### Debug Logging

By default, the node produces minimal console output. To enable verbose debug logging for troubleshooting:

**Option 1: Environment Variable (Recommended)**
```bash
# Windows
set PBE_DEBUG=1
python main.py

# Linux/Mac
PBE_DEBUG=1 python main.py
```

**Option 2: Python Code**
```python
import logging
logging.getLogger("PreviewBridgeExtended").setLevel(logging.DEBUG)
```

## Development

This project uses Git-RepoKit hooks for automatic version tracking.

```bash
# Clone repository
git clone https://github.com/DazzleNodes/ComfyUI-PreviewBridgeExtended.git
cd ComfyUI-PreviewBridgeExtended

# Install hooks for version tracking
bash scripts/install-hooks.sh

# Symlink to ComfyUI for development
cd /path/to/ComfyUI/custom_nodes
ln -s /path/to/ComfyUI-PreviewBridgeExtended ComfyUI-PreviewBridgeExtended
```

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test changes in ComfyUI
4. Submit a pull request

Like the project?

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/djdarcy)

## Acknowledgements

Part of the [DazzleNodes](https://github.com/DazzleNodes) collection.

Inspired by:
- [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) Preview Bridge node
- [WAS Node Suite](https://github.com/WASasquatch/was-node-suite-comfyui) mask combination patterns

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
