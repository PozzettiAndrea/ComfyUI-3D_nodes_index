- [ComfyLatentTools](#comfylatenttools)
  - [Installation](#installation)
  - [Optional math notes](#optional-math-notes)
  - [Node Overview](#node-overview)
    - [Rescaled PAG ( Perturbed Attention Guidance )](#rescaled-pag--perturbed-attention-guidance-)
      - [Parameters](#parameters)
    - [Latent Normalized Lanczos Resize (LNLR)](#latent-normalized-lanczos-resize-lnlr)
      - [Internal Operation Order](#internal-operation-order)
      - [Parameters](#parameters-1)
  - [Additional pages](#additional-pages)

# ComfyLatentTools

A set of custom nodes for ComfyUI, providing a specialized **Latent Normalized Lanczos Resize** workflow.

## Installation

1. Download or clone this repository into your ComfyUI's `custom_nodes` folder.
2. Restart ComfyUI. The node(s) will appear in the **image/upscaling** category.

## Node Overview

MANY MISSING NODES HERE - WILL BE UPDATED

### Rescaled PAG ( Perturbed Attention Guidance )

Implementation of Perturbed Attention Guidance that also takes into account the insight of RescaleCFG.

Compared to vanilla PAG this results in much better dynamic range and much less "deep frying" or oversaturation.

This is still a little bit experimental and some amount of experimentation with sampling parameters and PAG parameters is recommended.
pag_scale = 1/2 cfg is a good starting point and I recommend a post rescale close to 1.0.

The samplers seem to converge faster with this turned on so a decrease of number of steps might be possible with little loss of quality.

#### Parameters

### Latent Normalized Lanczos Resize (LNLR)

A specialized upscaling node designed to:
- Perform a Lanczos upscale in **image space**,
- Re-encode to latent space,
- Match the original latent's mean/variance,
- Optionally add correlated noise or blend with a pure latent-based upscale.

This aims to produce an upscaled latent that stays more faithful to the original diffusion pass, avoiding excessive blur, and optionally adding noise.
It can serve as a fast base for subsequent (re-)diffusion or refinement steps, in which case the noise addition can help to introduce additional details and variations at different scales.

#### Internal Operation Order

1. **Soft Outlier Clamp** (optional)  
   Uses a “huberize_quantile” method to softly clamp outliers.
2. **Decode**  
   Converts latent to image.
3. **Lanczos Upscale**  
   Upscales the image.
4. **Encode**  
   Converts upscaled image back to latent space.
5. **Weighted Latent Upscale** (optional)  
   Blends the new latent with a nearest exact upsampled version of the original latent, if the corresponding weight > 0
6. **Moment Matching**  
   Aligns mean and variance of the upscaled latent with the original.
7. **Add Correlated Gaussian Noise** (optional)  
   Injects correlated noise for additional variation.

#### Parameters

- **size_multiplier**  
  Multiplies original spatial dimensions (width/height).  
  *(Default: 2.0; Range: 0.1–4.0)*

- **soft_clamp_outliers** (enable/disable)  
  Toggles outlier soft-clamping before decoding.  
  *(Default: enable)*

- **outlier_quantile**  
  Quantile threshold for outlier soft-clamping.  
  *(Default: 0.01; Range: 0–1)*

- **outlier_clamp_slope**  
  Slope of the clamp outside the quantile range.  
  *(Default: 0.1; Range: 0–1)*

- **add_latent_noise** (enable/disable)  
  Adds correlated Gaussian noise to the final latent.  
  *(Default: disable)*

- **latent_noise_std**  
  Standard deviation for the generated noise.  
  *(Default: 1.0; Range: 0–10)*

- **latent_noise_scale**  
  Scaling factor applied to the correlated noise before adding.  
  *(Default: 0.1; Range: 0.01–10)*

- **add_latent_upscale_with_weight**  
  Blends the newly encoded latent with a direct “latent nearest” upscale.  
  *(Default: 0.0; Range: 0–1)*

## Additional pages
- [Some Comfy friendly maths](some_maths.md)

