# PCVideoMask

Crop and stich nodes for smooth bounding box video masking in ComfyUI.

## Installation

- Navigate to your `/ComfyUI/custom_nodes/` folder
- Run `git clone https://github.com/pavelchezcin/pcvideomask ComfyUI-PCVideoMask`
- Restart ComfyUI

# Features

- `PC Video Mask Smooth Crop` node to crop and resize a input mask batch to a given resolution.
- `PC Video Mask Stitcher` to put a processed image batch back onto the original images.



<!--
TODO:

## Publishing to Registry

If you wish to share this custom node with others in the community, you can publish it to the registry. We've already auto-populated some fields in `pyproject.toml` under `tool.comfy`, but please double-check that they are correct.

You need to make an account on https://registry.comfy.org and create an API key token.

- [ ] Go to the [registry](https://registry.comfy.org). Login and create a publisher id (everything after the `@` sign on your registry profile). 
- [ ] Add the publisher id into the pyproject.toml file.
- [ ] Create an api key on the Registry for publishing from Github. [Instructions](https://docs.comfy.org/registry/publishing#create-an-api-key-for-publishing).
- [ ] Add it to your Github Repository Secrets as `REGISTRY_ACCESS_TOKEN`.

A Github action will run on every git push. You can also run the Github action manually. Full instructions [here](https://docs.comfy.org/registry/publishing). Join our [discord](https://discord.com/invite/comfyorg) if you have any questions!

-->
