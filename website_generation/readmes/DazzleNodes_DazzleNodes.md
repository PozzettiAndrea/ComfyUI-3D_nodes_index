# DazzleNodes

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![ComfyUI Registry](https://img.shields.io/badge/ComfyUI-Registry-green.svg)](https://registry.comfy.org/publishers/djdarcy/nodes/comfyui-dazzlenodes)
[![GitHub release](https://img.shields.io/github/v/release/DazzleNodes/DazzleNodes?include_prereleases&label=version)](https://github.com/DazzleNodes/DazzleNodes/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A curated collection of image/latent creation and transformation custom nodes for ComfyUI. Each node is independently developed and maintained, but packaged together for convenient installation.

## Included Nodes

### Smart Resolution Calculator (standalone: **[Github](https://github.com/djdarcy/ComfyUI-Smart-Resolution-Calc) & [Comfy Registry](https://registry.comfy.org/publishers/djdarcy/nodes/comfyui-smart-resolution-calc)**)
Flexible resolution and latent generation with intelligent aspect ratio handling.

**Features:**
- Toggle-based dimension control
- Automatic missing value calculation
- Preview image generation
- Direct latent output for sampling
- Custom widgets for enhanced UX

**Status:** Published standalone in [ComfyUI Registry](https://registry.comfy.org/publishers/djdarcy/nodes/comfyui-smart-resolution-calc) and in [DazzleNodes package](https://registry.comfy.org/publishers/djdarcy/nodes/comfyui-dazzlenodes) in ComfyUI Registry

### Fit Mask to Image (standalone: **[Github](https://github.com/DazzleNodes/fit-mask-to-image)**)
Automatically resizes masks to match image dimensions for inpainting workflows (for when the ksampler output dimensions no longer matches the input mask dimensions)

**Features:**
- Replaces [10-node workflow](https://gist.github.com/djdarcy/5796b7b2d705278aa4ad612248fd7c77) with single node
- Automatic dimension matching
- Preview output for verification
- Latent masking support
- Nearest-exact scaling for quality preservation

**Status:** Available from [DazzleNodes package](https://registry.comfy.org/publishers/djdarcy/nodes/comfyui-dazzlenodes) in the Comfy Registry; download from [Github](https://github.com/DazzleNodes/fit-mask-to-image) to `ComfyUI\custom_nodes` for standalone install

### Plasma Noise Generators (fork: **[Github](https://github.com/DazzleNodes/dazzle-comfy-plasma-fast)**)
GPU-accelerated noise generation with 100-200x speedup over CPU implementations. Fork of [comfy-plasma](https://github.com/Jordach/comfy-plasma) by Jordach with PyTorch optimization ([PR #7](https://github.com/Jordach/comfy-plasma/pull/7)).

**Features:**
- **OmniNoise unified generator** - All 5 noise types in one node with dynamic widgets
- 5 noise types: Plasma, Random, Grey, Pink, Brown
- Two random distributions: Uniform (TV Static) and Gaussian (Centered Gray)
- GPU acceleration via PyTorch tensors
- Automatic CPU fallback
- Per-channel RGB clamping
- Backwards compatible with original RandNoise node

**Note:** This fork may be removed if the upstream project merges the optimization changes.

### Dazzle Switch (standalone: **[Github](https://github.com/DazzleNodes/ComfyUI-DazzleSwitch)**)
Smart switch node with dropdown-based input selection and INT override for cascading workflows. Route any data type through a named dropdown instead of moving noodles.

**Features:**
- Dynamic input expansion (auto-grow/shrink slots as you connect)
- `select` dropdown populated with connected input names (supports user renames)
- `select_override` INT input for programmatic cascading across chained switches
- Type detection via graph walking with output type label
- Slot reordering (right-click Move Up / Move Down) for cascading alignment
- Active slot highlight for visual feedback
- Label cache preserves user renames across disconnect/reconnect cycles

**Status:** Available from [DazzleNodes package](https://registry.comfy.org/publishers/djdarcy/nodes/comfyui-dazzlenodes) in the Comfy Registry; download from [Github](https://github.com/DazzleNodes/ComfyUI-DazzleSwitch) to `ComfyUI\custom_nodes` for standalone install

### Preview Bridge Extended (standalone: **[Github](https://github.com/DazzleNodes/ComfyUI-PreviewBridgeExtended)**)
Extended preview bridge functionality for ComfyUI workflows.

**Status:** Available from [DazzleNodes package](https://registry.comfy.org/publishers/djdarcy/nodes/comfyui-dazzlenodes) in the Comfy Registry; download from [Github](https://github.com/DazzleNodes/ComfyUI-PreviewBridgeExtended) to `ComfyUI\custom_nodes` for standalone install

## Installation

### Method 1: ComfyUI Manager (Recommended)

```
Search for "DazzleNodes" in ComfyUI Manager and click Install
```

### Method 2: Git Clone with Submodules

```bash
cd ComfyUI/custom_nodes
git clone --recursive https://github.com/DazzleNodes/DazzleNodes.git
```

**⚠️ Important:** The `--recursive` flag is required to download all node submodules!

### Method 3: Manual Submodule Setup

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DazzleNodes/DazzleNodes.git
cd DazzleNodes
git submodule update --init --recursive
```

### Method 4: Symlink for Development

If you're developing DazzleNodes locally:

```bash
cd ComfyUI/custom_nodes
mklink /D DazzleNodes C:\code\DazzleNodes\local
```

## Usage

After installation, restart ComfyUI. All nodes will appear under the **DazzleNodes** category in the node menu.

### Example Workflows

See `examples/` directory for workflow JSON files demonstrating node usage.

## Updating

### Update All Nodes
```bash
cd ComfyUI/custom_nodes/DazzleNodes
git pull
git submodule update --remote
```

### Update Individual Node
```bash
cd ComfyUI/custom_nodes/DazzleNodes/nodes/smart-resolution-calc
git pull
```

## Architecture

DazzleNodes uses **git submodules** for local development to maintain clean, independent histories for each node:

```
DazzleNodes/local/
├── __init__.py              # Aggregator that imports all nodes
├── nodes/                   # Node submodules
│   ├── smart-resolution-calc/    # Submodule → separate git repo
│   ├── fit-mask-to-image/        # Submodule → separate git repo
│   ├── dazzle-comfy-plasma-fast/ # Submodule → separate git repo
│   ├── dazzle-switch/              # Submodule → separate git repo
│   └── preview-bridge-extended/    # Submodule → separate git repo
└── examples/                # Collection-level examples
```

**Why Submodules?**
- Each node maintains independent git history
- Nodes can be extracted to standalone repos later
- Version locking prevents unexpected breakage
- Supports selective node development

The aggregator uses `importlib` to dynamically load each submodule at startup, merging all `NODE_CLASS_MAPPINGS` into a single namespace. This handles Python's inability to import from hyphenated directory names and provides fault isolation so one broken node doesn't take down the collection.

For a detailed walkthrough of the loading system — including how to build your own multi-node collection — see [docs/dynamic-node-loading.md](docs/dynamic-node-loading.md).

## Development

### Working on a Node

Each node is developed in its own repository:

- **Smart Resolution Calculator**: `C:\code\smart-resolution-calc-repo\local`
- **Fit Mask to Image**: `C:\code\ComfyUI-ImageMask-Fix\local`

```bash
# Navigate to node's repository
cd nodes/fit-mask-to-image

# Make changes and commit as usual
git add -A
git commit -m "Add new feature"
git push

# Update collection to use new version
cd ../..
git add nodes/fit-mask-to-image
git commit -m "Update fit-mask-to-image to latest"
git push
```

### Dev Mode and Local Paths

The `dev_mode.py` script toggles nodes between dev mode (symlinks to local source repos) and publish mode (submodules). Since `.gitmodules` frequently contains GitHub URLs rather than local paths, you can configure local repo locations via `dev_mode_local.yaml`:

```bash
python scripts/dev_mode.py dev all --local    # Switch to dev mode using local paths
python scripts/dev_mode.py publish all         # Switch back to publish mode
```

For setup instructions, configuration options, and all available developer scripts, see [docs/developer-tools.md](docs/developer-tools.md).

### Adding a New Node

1. Create node repository
2. Add as submodule:
   ```bash
   git submodule add <repo-url> nodes/<node-name>
   ```
   > **Note:** `git submodule add` can silently fail on some Git versions (observed on Git 2.52.0 for Windows). If the command exits successfully but the submodule directory is empty or missing, see [docs/git-submodule-workaround.md](docs/git-submodule-workaround.md) for diagnostic steps and workarounds.
3. Update `__init__.py` to import the new node (follow the existing `load_node_module()` pattern)
4. Test in ComfyUI
5. Update version (`version.py`, `pyproject.toml`) and `CHANGELOG.md`
6. Commit changes

## Troubleshooting

### Nodes Not Loading

**Symptom:** ComfyUI says "No nodes loaded!" or specific nodes are missing.

**Solution:** Initialize submodules:
```bash
cd ComfyUI/custom_nodes/DazzleNodes
git submodule update --init --recursive
```

### Empty Node Directories

**Symptom:** `nodes/` subdirectories exist but are empty.

**Solution:** You cloned without `--recursive` flag. Run:
```bash
cd ComfyUI/custom_nodes/DazzleNodes
git submodule update --init --recursive
```

### Import Errors

**Symptom:** Python import errors in console.

**Solution:**
1. Verify submodules are initialized
2. Check each node's `__init__.py` exists
3. Restart ComfyUI completely
4. Check ComfyUI console for detailed error messages

## Contributing

Contributions welcome! Each node has its own repository and contribution guidelines. See individual node READMEs for details.

For collection-level issues (installation, documentation, architecture), open an issue in this repository.

Like the project?

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/djdarcy)

## License

DazzleNodes, Copyright (C) 2025 Dustin Darcy

Collection-level code is licensed under the MIT license - see the [LICENSE](LICENSE) file for details. 

See individual node directories for specific licenses. 
