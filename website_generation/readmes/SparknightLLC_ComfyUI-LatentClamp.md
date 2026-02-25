# ComfyUI-LatentClamp

A node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that modifies the values in the `samples` input that fall outside of a `min` and `max` range using a multiplier.

Additional controls are available for experimental purposes.

In img2img operations, latent clamping has been observed to improve prompt adherence. Issues with image fidelity resulting from the clamp can be rectified with a quick second diffusion pass.

### Inputs

- `min`: Values in `samples` below this value will be multiplied by `outside_multiplier`.
- `max`: Values in `samples` above this value will be multiplied by `outside_multiplier`.
- `inside_multiplier`: Values in `samples` between `min` and `max` will be multiplied by this value.
- `outside_multiplier`: Values in `samples` outside of `min` and `max` will be multiplied by this value.
- `extra_noise`: Add compensatory noise to the values in `samples`.