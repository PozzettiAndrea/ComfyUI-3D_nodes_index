
# Immac Tools

A small collection of ComfyUI extension nodes created for personal use.

## Quick summary

- Package: `ComfyUI-ImmacTools`
- Purpose: ComfyUI extension providing utility nodes.

## Installation

This repository is intended to be used as a ComfyUI custom node. Install it by one of the following methods:

A) ComfyUI Manager (When/If published)

- Use ComfyUI's built-in extension/manager (if available) to add this repo directly by URL. The manager will clone the repository into the appropriate `custom_nodes` folder and keep it updated.

B) Clone into your ComfyUI `custom_nodes` folder

1. From your ComfyUI repository root (or wherever you keep custom nodes), clone this repo into the `custom_nodes` directory:

```bash
# Example (from ComfyUI repo root)
git clone https://github.com/Immac/ComfyUI-ImmacTools custom_nodes/ComfyUI-ImmacTools
```

2. Restart ComfyUI. The extension's `comfy_entrypoint` should be discovered and the nodes will appear in the node list.

# Immac Tools

A small collection of ComfyUI custom nodes created for personal use and convenience.

## Quick summary

- Package: `immac_tools`
- Purpose: Utility nodes for ComfyUI (sigma schedule helpers and small helpers).

## Installation

This repository is intended to be installed as a ComfyUI custom node. Two common installation methods:

1) Clone into your ComfyUI `custom_nodes` folder

From your ComfyUI repository root (or wherever you keep custom nodes), clone this repo into the `custom_nodes` directory:

```bash
# Example (from ComfyUI repo root)
git clone https://github.com/Immac/ComfyUI-ImmacTools custom_nodes/immac_tools
```

Then restart ComfyUI. The extension entrypoint should be discovered and the nodes will appear in the node list.

2) ComfyUI Manager (if available)

If you use a community manager/extension manager that supports installing extensions by Git URL, add this repo's URL and let the manager clone/update it for you.

## Where the code lives

- Node implementations: `src/immac_tools/nodes.py` and `src/immac_tools/forwarding_nodes.py`.
- Python package metadata: `pyproject.toml` and top-level package under `src/immac_tools`.

## Nodes included

The main utility nodes included today are:

- Concatenate Sigmas Node
  - Class: `ConcatenateSigmasImmacTools`
  - Display name: `Concatenate Sigmas Node`
  - Inputs: `sigmas_1`, `sigmas_2` (sigma schedules as tensors or lists)
  - Outputs: concatenated sigma schedule
  - Behavior: concatenates two sigma schedules, tolerating None inputs and non-torch objects by converting them to tensors.

- Splice Sigmas At %
  - Class: `SpliceSigmasAtImmacTools`
  - Display name: `Splice Sigmas At %`
  - Inputs: `sigmas_a`, `sigmas_b`, `splice` (float 0.0 - 1.0)
  - Outputs: `spliced_sigmas` (full), `first_part`, `second_part`
  - Behavior: picks a boundary on `sigmas_a` based on `splice` and combines `sigmas_a` and `sigmas_b` around that boundary. Accepts tensor or list inputs.

- Skip Every Nth Image
  - Class: `SkipEveryNthImagesImmacTools`
  - Display name: `Skip Every Nth Image`
  - Inputs: `images` (batch as list/tuple or torch tensor), `n` (int; n<=0 yields empty output)
  - Outputs: filtered images batch, indices removed
  - Behavior: drops every nth image while preserving the order of remaining items; returns the kept batch plus the zero-based indices that were removed.

For full details see the source files mentioned above.



## Contributing

- Bug reports and feature requests: open an issue on the GitHub repository.

## License & contact

MIT — see `LICENSE`.
For questions or issues open an issue at: https://github.com/Immac/ComfyUI-ImmacTools
