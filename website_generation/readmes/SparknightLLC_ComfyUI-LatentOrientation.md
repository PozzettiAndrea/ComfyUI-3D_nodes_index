# ComfyUI-LatentOrientation

A simple node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that rotates or resizes the input latent to common orientations.

Comfy has built-in `Flip Latent` and `Rotate Latent` (by degrees), but this is a little different.

![workflow_install](example_workflows/install.png)

### Installation

Simply drag the image above into ComfyUI and use [ComfyUI Manager » Install Missing Custom Nodes](https://github.com/ltdrdata/ComfyUI-Manager). Alternatively, clone this repo into your `custom_nodes` folder.


### Inputs

- `samples` (LATENT): The input latent to adjust.
- `orientation` (CHOOSE): The adjustment logic, as defined below.
	- `portrait`: Rotates `samples` such that the height is greater than the width.
	- `landscape`: Rotates `samples` such that the width is greater than the height.
	- `min square`: Crops `samples` to equal width and height, using the smaller dimension of the two.
	- `max square`: Pads `samples` to equal width and height, using the greater dimension of the two.
	- `avg square`: Takes the average between width and height of `samples` and resizes both dimensions to this value.


### Outputs

- LATENT: The adjusted latent.