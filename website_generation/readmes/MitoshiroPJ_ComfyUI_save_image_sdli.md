# ComfyUI SaveImage SDLI

SDLI (Stable Diffusion Latents in Imagefile) is file format, that contains latents and lossy (decoded) image.

Detailed format is written at [SDLI Tools](https://github.com/MitoshiroPJ/sdli_tools).

## Node: Save SDLI Image

Input:
 - samples: Latents
 - vae: vae (optional)
 - latent_type: Select proper SD type
 - reduction_ratio: shrink image for WebP. latents will not be shrinked.
 - filename_prefix: The prefix of output filename.
 - positive_prompt: Additional metadata.
 - negative_prompt: Additional metadata.

This node requires latents. (not image)

If vae was not given, use [TAESD](https://github.com/madebyollin/taesd).

If you want to use TAESD, download models into `models/vae_approx`.


## Node: Preview SDLI Image

Similar to Save SDLI Image.

Generate SDLI (*.webp) for preview.

You can download these webp via browser.

