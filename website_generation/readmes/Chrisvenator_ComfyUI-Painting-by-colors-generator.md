# ComfyUI-PaintingByColors

Create a painting-by-colors image from an image
![Overview.png](assets/Overview.png)
> [!NOTE]
> This projected was created with a [cookiecutter](https://github.com/Comfy-Org/cookiecutter-comfy-extension) template.
> It helps you start writing custom nodes without worrying about the Python setup.

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
1. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under
   `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

Or manually by:

```bash
# Inside your ComfyUI root directory
cd custom_nodes
git clone https://github.com/your-name/comfyui-paint-by-numbers
pip install torch numpy pillow scikit-learn opencv-python scipy
```

# Features

- Use arbitrary #RRGGBB values of colors you have lying around at home, so you don't have to go buy new colors.
- _Paint by Numbers Preprocessor: K-Mean_ flattens colours with K-Means, optional bilateral smoothing, noise removal,
  and tiny-blob
  cleanup
- _Paint by Numbers: Calculate numbers_ extracts regions, merges near-identical shades, picks centroids, and prints
  crisp
  numbers plus a printer-friendly palette sheet.
- _Paint by Numbers: overlay Numbers:_ paste calculated numbers on a lineart.

# Usage

1. Load Image.
2. Resize Image. Too big images will take too long to compute. I reccommend up to 3000px for the longest side
3. (optional) fill in the "Hex Color Stack" with the colors you have lying around at home.
4. "Paint by Numbers Preprocessor: K-Mean" will then reduce the amount of colors to either the specified amount or the
   amount of colors present in the Hex Stacker. I recommend putting white in the Stacker too (since most paper is
   white).
5. Put the preprocessed image into a LineArt converter. Any converter is fine. Like the Controlnet ones. And invert it.
   I am using the AnyLineart Lineart.
6. Put the preprocessed image into the "Paint by Numbers: Calculate numbers" node. This will then calculate where to
   place each number. It will output an image "numbers_image" where all numbers are placed on the image.
7. Then combine the lineart and the numbers_image with the "Paint by Numbers: overlay Numbers". This write all black
   pixels from numbers_image onto input_image.

Example Workflow (with embedded workflow):
![workflow.png](example_workflows/workflow.png)

## Example
1. Original Image: ![Original_image.png](assets/Original_image.png)
2. Paint by Numbers Preprocessor: K-Mean ![Preprocessed.png](assets/Preprocessed.png)
3. Lineart: ![lineart.png](assets/lineart.png)
4. Numbers Image: ![numbers_image.png](assets/numbers_image.png)
5. numbers overlayed onto the lineart: ![lineart_with_numbers.png](assets/lineart_with_numbers.png)
6. numbers overlayed onto the k-mean: ![fully_colored_and_numbered_image.png](assets/fully_colored_and_numbered_image.png)



## Develop

To install the dev dependencies and pre-commit (will run the ruff hook), do:

```bash
cd paintingbycolors
pip install -e .[dev]
pre-commit install
```

The `-e` flag above will result in a "live" install, in the sense that any changes you make to your node extension will
automatically be picked up the next time you run ComfyUI.

## Tests

This repo contains unit tests written by [Claude.AI](https://claude.ai/new) in Pytest in the `tests/` directory.
Something is wrong with the config right now. I might fix them if I find the time for it...

## Publishing to Registry

If you wish to share this custom node with others in the community, you can publish it to the registry. We've already
auto-populated some fields in `pyproject.toml` under `tool.comfy`, but please double-check that they are correct.

You need to make an account on https://registry.comfy.org and create an API key token.

- [ ] Go to the [registry](https://registry.comfy.org). Login and create a publisher id (everything after the `@` sign
  on your registry profile).
- [ ] Add the publisher id into the pyproject.toml file.
- [ ] Create an api key on the Registry for publishing from
  Github. [Instructions](https://docs.comfy.org/registry/publishing#create-an-api-key-for-publishing).
- [ ] Add it to your Github Repository Secrets as `REGISTRY_ACCESS_TOKEN`.

A Github action will run on every git push. You can also run the Github action manually. Full
instructions [here](https://docs.comfy.org/registry/publishing). Join our [discord](https://discord.com/invite/comfyorg)
if you have any questions!

