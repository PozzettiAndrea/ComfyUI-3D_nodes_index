**Text to video for Stable Video Diffusion in ComfyUI**

This is node replaces the init_image conditioning for the [Stable Video Diffusion](https://github.com/Stability-AI/generative-models) image to video model with text embeds, together with a conditioning frame. The conditioning frame is a set of latents.

It is recommended to input the latents in a noisy state. Default ComfyUI noise does not create optimal results, so using other noise e.g. Power-Law Noise helps.

Motion bucket, fps & augmentation level preserved as possible input for the conditioning.

The video generation needs a couple frames time to get on it's feet and run.

Maxing out EDM sigma helps getting more colour into the image, together with additional prompts like "realistic". 

CFG can be raised way above normal parameters using VideoLinearCFGGuidance. Keeping a small CFG guidance spread of around 2 (e.g. min_cfg 18 & sampler cfg 20) helps with image quality consistency.

Note 22.06.2025: Hello. This was a simple test to see if Stable Video Diffusion has text conditioning tokens inside it and can be prompted accordingly. 
There was no need for anything else except init.py as there is only one node. One uses it just like one would use the default SVD conditioning node, except instead of an image input, there is a positive and a negative text conditioning input.

There is no guarantee this node still works due to it being outdated. I recommend using newer video models like WAN2.1, HunyuanVideo or LTXV.

**This repo is not maintained and will be archived**
