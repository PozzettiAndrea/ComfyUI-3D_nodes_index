# UNET Loader with Model Name

A ComfyUI custom node that extracts the model name as a string when
loading UNET models (Diffusion Models).

## Features

This node extends the standard `UNETLoader` (Load Diffusion Model) node
and provides the following outputs:

- **MODEL**: Standard model output
- **STRING**: Model name (new feature)

## Usage

1. Open the `loaders` category in the node menu
2. Select the `Load Diffusion Model (with Name)` node
3. Choose a model from the dropdown
4. Select the weight data type (default, fp8, etc.)
5. Use the two outputs:
   - MODEL output → Connect to KSampler or other nodes
   - STRING output → Connect to Save Image filename prefix or metadata

## Example Use Case

### Include Model Name in Filename

```text
Load Diffusion Model (with Name)
  ├─ MODEL → KSampler → VAE Decode → Save Image
  └─ STRING → (Connect to Save Image's filename_prefix)
```

This automatically includes the model name used in the generated image filename.

## Output String Format

If the model filename is `flux1-dev-Q8_0.gguf`, the STRING output will be
`flux1-dev-Q8_0` (filename without extension).

## Weight Data Type Options

- **default**: Default precision
- **fp8_e4m3fn**: FP8 format (E4M3)
- **fp8_e4m3fn_fast**: FP8 format (E4M3) optimized version
- **fp8_e5m2**: FP8 format (E5M2)

## Installation

Simply place this folder in the `ComfyUI/custom_nodes/` directory.
The node will be automatically loaded when you restart ComfyUI.

### For Developers: Git Hooks Setup

If you're contributing to this project, it's recommended to set up Git
hooks that check for sensitive information before commits.

Method 1: Use Setup Script (Recommended)

```bash
# For Windows
setup-git-hooks.bat

# For Linux/Mac
chmod +x .git-hooks/pre-commit
chmod +x .git-hooks/pre-commit.py
git config core.hooksPath .git-hooks
```

Method 2: Manual Setup

```bash
git config core.hooksPath .git-hooks
```

Once the hooks are properly configured, the following checks will run
automatically on commit:

- Detection of sensitive information such as API keys, passwords, and tokens
- Detection of files that should be excluded (`__pycache__`, `.env`, etc.)

For more details, see [PRE_COMMIT_CHECKLIST.md](PRE_COMMIT_CHECKLIST.md).

## Compatibility

- Compatible with the latest version of ComfyUI
- Uses the new node definition format with `comfy_api.latest`
- Uses the same model folder (`diffusion_models`) as the standard `UNETLoader`

## License

This custom node is based on ComfyUI's `UNETLoader` implementation.

- License: GPL-3.0
- Original Project: [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- Original License: GPL-3.0

For details, see the [LICENSE](LICENSE) file.
