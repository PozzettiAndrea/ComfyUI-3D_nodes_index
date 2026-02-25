# Voxta ComfyUI Nodes

ComfyUI nodes to create and integrate with Voxta

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
1. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

## Nodes Overview

- Voxta: Output Folder — Centralize the output root + subfolder. Connect its outputs to other Voxta nodes instead of configuring the same paths repeatedly.
- Voxta: Export Character — Save character images with flexible naming/enumeration strategies.
- Voxta: Filter Existing Combinations — Skip generation of combinations that already have enumerated files on disk.

All consumer nodes accept either a direct string value or the connected output of the Output Folder node for `output_path` and `subfolder`.

## Develop

To install the dev dependencies and pre-commit (will run the ruff hook), do:

```bash
pip install -e .[dev]
pre-commit install
```

The `-e` flag above will result in a "live" install, in the sense that any changes you make to your node extension will automatically be picked up the next time you run ComfyUI.

## Sample Workflow

Use the simple workflow to see the general principles, the advanced workflow contains more nodes and logic to demonstrate a more complex use case.

In Voxta, go to the Asset tab of a character, copy the path, and paste it in the "Voxta: Output Folder" node.

- [Voxta Character Generator (Simple).json](workflows/Voxta Character Generator (Simple).json)
- [Voxta Character Generator (Advanced).json](workflows/Voxta Character Generator (Advanced).json)

## License

MIT License. See [LICENSE](LICENSE) for details.
