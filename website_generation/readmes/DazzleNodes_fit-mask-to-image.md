# ComfyUI Fit Mask to Image

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![ComfyUI Registry](https://img.shields.io/badge/ComfyUI-Registry-green.svg)](https://registry.comfy.org/publishers/djdarcy/nodes/DazzleNodes)
[![GitHub release](https://img.shields.io/github/v/release/DazzleNodes/fit-mask-to-image?include_prereleases&label=version)](https://github.com/DazzleNodes/fit-mask-to-image/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Automatically resizes masks to match image dimensions for seamless inpainting workflows. Replaces a [10-node workflow chain](https://gist.github.com/djdarcy/5796b7b2d705278aa4ad612248fd7c77) with a single, efficient node.

## Overview

This node solves a common inpainting problem: when your KSampler output dimensions (i.e. 960x960) no longer match your input (i.e. 958x958) mask dimensions due to the KSampler outputs being divisible by 8. This is also helpful for workflows where masks and images come from different sources or when upscaling changes dimensions.

## Features

- **One-Node Solution**: Replaces 10-node workflow with single node
- **Smart Dimension Matching**: Automatically scales masks to match image dimensions
- **Missing Mask Handling**: Auto-generates masks when none provided (default: entire image visible)
- **Multiple Outputs**: Fixed mask, preview image, debug mask, and masked latent
- **Inpainting Ready**: Direct integration with KSampler via latent output
- **Debug Information**: Detailed info output showing dimension changes
- **Nearest-Exact Scaling**: Preserves mask quality during resize

## Prerequisites

- ComfyUI installation
- Python 3.10+ (or ComfyUI's embedded Python)
- No additional dependencies (uses ComfyUI's PyTorch, PIL, numpy)

## Installation

### ComfyUI Registry (Recommended - Coming Soon)

The easiest way to install is through the ComfyUI Registry:

1. Open **ComfyUI Manager** in your ComfyUI interface
2. Search for **"DazzleNodes"** ("Fit Mask to Image" isn't a standalone node)
3. Click **Install** and restart ComfyUI

The node will appear under: **DazzleNodes → Fit Mask to Image**

Alternatively, use the command line:
```bash
comfy node install fit-mask-to-image
```

### Git Clone

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DazzleNodes/fit-mask-to-image.git
```

Then restart ComfyUI or use **Manager → Refresh Node Definitions**.

### Manual Installation

1. Download the [latest release](https://github.com/DazzleNodes/fit-mask-to-image/releases) and extract to `ComfyUI/custom_nodes/fit-mask-to-image/`
2. Restart ComfyUI
3. Find the node in: **DazzleNodes → Fit Mask to Image**

### Part of DazzleNodes Collection

This node is also included in the [DazzleNodes](https://github.com/DazzleNodes/DazzleNodes) collection. If you install DazzleNodes, you automatically get this node along with other useful nodes.

## Usage

### Basic Workflow

1. Add "Fit Mask to Image" node to your workflow (found under "DazzleNodes")
2. Connect your source **IMAGE** (for dimension reference)
3. Connect your **MASK** (to fix dimensions)
4. Set **missing_mask** parameter (default: `pass_through` - preserves original behavior)
5. Optionally connect a **LATENT** for inpainting workflows

### Missing Mask Handling

The `missing_mask` parameter controls what happens when no mask is connected or mask is empty:
- **pass_through** (default): Process empty mask as-is (original behavior)
- **all_visible**: Creates white mask (entire image visible)
- **all_hidden**: Creates black mask (entire image masked)
- **error**: Fails with error message (useful for debugging)

### Outputs

- **fixed_mask**: Final mask with corrected dimensions (from alpha channel)
- **preview_image**: RGB+alpha merged image for visual verification
- **info**: Text showing original→target dimensions and processing status
- **masked_latent**: Latent with mask applied (if latent input provided)

### Common Use Case

**Problem**: You're running an inpainting workflow where:
- Your input image is 512×512
- KSampler upscales to 1024×1024
- Your original mask is still 512×512
- KSampler fails with dimension mismatch

**Solution**: Insert Fit Mask to Image between upscaler and second KSampler:
1. Connect upscaled IMAGE → Fit Mask to Image → `image` input
2. Connect original MASK → Fit Mask to Image → `mask` input
3. Connect LATENT → Fit Mask to Image → `latent` input (optional)
4. Connect `masked_latent` output → KSampler for inpainting

### Example Workflow

See `examples/` folder for workflow JSON files demonstrating the node in action.

## How It Works

1. Extracts target dimensions from input image
2. Resizes mask to match using nearest-neighbor scaling (preserves mask values)
3. Converts mask to alpha channel for preview
4. Applies mask to latent if latent input provided
5. Outputs fixed mask, preview, dimensions info, and masked latent

## Troubleshooting

### Mask dimensions still don't match

**Solution**: Verify the image input is the target dimension source (usually the upscaled image, not the original).

### Preview looks wrong

**Solution**: The preview is for verification only. Use the `fixed_mask` output for your workflow.

### Latent output has wrong dimensions

**Solution**: Ensure the latent input matches the image dimensions (width/8 × height/8).

## Development

For contributors: This project uses Git-RepoKit hooks for automatic version tracking. Run `./scripts/install-hooks.sh` to set up versioning hooks.

### Working on This Node

```bash
# Clone repository
git clone https://github.com/DazzleNodes/fit-mask-to-image.git
cd fit-mask-to-image

# Install hooks for version tracking
bash scripts/install-hooks.sh

# Make changes and test in ComfyUI
# Symlink to ComfyUI custom_nodes for development:
cd /path/to/ComfyUI/custom_nodes
ln -s /path/to/fit-mask-to-image fit-mask-to-image
```

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test changes in ComfyUI
4. Submit a pull request

Like the project?

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/djdarcy)

## License

Fit Mask to Image, Copyright (C) 2025 Dustin Darcy

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Part of the [DazzleNodes](https://github.com/DazzleNodes/DazzleNodes) collection.
