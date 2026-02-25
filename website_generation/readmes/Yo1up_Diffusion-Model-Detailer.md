# Diffusion-Model-Detailer
ComfyUI node to allow the user to control the generation of diffusion models to increase and decrease level of detail. The model patch has no trainable parameters and can be applied to theoretically any diffusion model in existence. whether or not the implementation currently works as expected for every diffusion model in existence I do not know.

# Installation
You can now install it with the ComfyUI manager. if you experience any issues please let me know.

# Usage
## Detailer (UNet Patch)
 - **scaling factor**: determines the strength and "direction" of the modification. positive values increase the added noise during affected steps and negative values decrease the added noise at affected steps. this in turn means that positive values increase "detail" and negative values decrease "detail"
 - **scaling narrowness**: this determines how "narrow" (or wide) the affected steps are. a value of 0 affects every single step at the strength of the scaling factor. higher values decrease the width (or increases the "narrowness") of the affected step area according to an exponentiated sine wave (i.e. the schedule is a sine wave raised to the power of "scaling narrowness")

# Planned Features
- [ ] Add a "depth" parameter to alter when the scheduled noise injection/removal peaks.

- [X] Migrate to using the proper model patcher comfy commands.

- [X] Make the nodes able to run inside a folder so comfy manager will be able to install the nodes automatically.

- [ ] Add some example image grids

- [ ] Add some example workflows

