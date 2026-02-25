# SD3-Scaling
Tools for scaling images and latents appropriate to SD3 in ComfyUI

## SD3 Image Scale To Total Pixels

This custom node is a wrapper for the builtin ImageScaleToTotalPixels that
works within the desired constraint of SD3 to operate on images whose
width and height are divisible by 64.

Generally ***only use this node when scaling an input image intended to be passed to a sampler***
(img2img) as the SD3-specific resolution only applies to sampler inputs.

Inputs:

* `upscale_method`—(inherited from `ImageScaleToTotalPixels`) see ComfyUI docs
* `megapixels`—(inherited from `ImageScaleToTotalPixels`) the desired total megapixels of the resulting image, see below

Outputs:

* `image`—The scaled image

SD3 wants input latents that have width and height divisible by 64. To meet this requirement, when scaling to a
specific megapixel resolution, the resulting width and height are checked and reduced to the nearest value that
is divisible by 64.

Because no cropping is performed, some stretching may occur if either dimension needs to be reduced. Since you
should be working at at least the megapixel range for your input image with SD3, this probably won't be
noticable, but you should be aware that this will occcur.
