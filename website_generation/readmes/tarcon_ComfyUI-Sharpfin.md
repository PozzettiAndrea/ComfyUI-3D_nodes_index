# ComfyUI Sharpfin

ComfyUI node to use advanced Torchvision transforms built for accuracy, visual quality, and speed.

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
2. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
3. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under
   `ComfyUI/custom_nodes`.
4. Restart ComfyUI.

## Features

- Improved upscaling and resizing: Specially optimized for accuracy, visual quality, and speed
- Ten different interpolation kernels: The superior Magic Kernel as well as basics like bilinear or multiple versions of
  Lanczos
- High flexibility: Dimensions from 64 to 8192 (in increments of 64)
- Optional sRGB conversion: For precise colour calculation and correct colour space conversion

**More Details**: Confer to the documentation of the underlying library [Sharpfin](https://github.com/drhead/Sharpfin)

## Dependencies

This node uses code from the [Sharpfin library](https://github.com/drhead/Sharpfin) licensed under Apache 2.0

## Develop

To install the dev dependencies and pre-commit (will run the ruff hook), do:

```bash
cd sharpfin
pip install .
pre-commit install
```

The `-e` flag above will result in a "live" install, in the sense that any changes you make to your node extension will
automatically be picked up the next time you run ComfyUI.

## Tests

This repo contains unit tests written in Pytest in the `tests/` directory. It is recommended to unit test your custom
node.

- [build-pipeline.yml](.github/workflows/build-pipeline.yml) will run pytest and linter on any open PRs

## Publishing to Registry

A GitHub action will run on every git push. You can also run the GitHub action manually. Full
instructions [here](https://docs.comfy.org/registry/publishing). Join our [discord](https://discord.com/invite/comfyorg)
if you have any questions!
