# ComfyUI-TBG-Takeaways
# TGB’s ComfyUI Development Takeaways

A curated set of reusable ComfyUI nodes created by TGB, these sidecodes capture major advances in model sampling, noise scheduling, and image refinement to enhance stable diffusion workflows. All nodes in this pack are extracted from micro-developments created during the development of TBG ETUR. They’ve been turned into standalone “micro nodes” for testing purposes and for anyone who enjoys experimenting with them.
---
[Visit TBG enhanced tiled upscaler and refiner pro](https://github.com/Ltamann/ComfyUI-TBG-ETUR)



## Table of Contents

- [Included Nodes](#included-nodes)  
- [Overview](#overview)  
- [License](#license)  
- [Support](#support)  

---

## Included Nodes

TBG Sampler - Now with split-aware and inpaint-aware sampling controls!

- **TBG KSampler Advanced (Inpaint Split Aware)** *(New!)*  
[infos here]([True differential diffusion with split sampling using TBG Dual Model and Inpaint Split-Aware Samplers.](https://www.patreon.com/posts/true-diffusion-144805227)
- **TBG Dual Model KSampler (Inpaint Split Aware)** *(New!)*  
[infos here]([True differential diffusion with split sampling using TBG Dual Model and Inpaint Split-Aware Samplers.](https://www.patreon.com/posts/true-diffusion-144805227)

  The TBG Dual Sampler enables sampling with both low- and high-step models. It allows you to specify separate prompts for low and high steps, choosing different models to control structure and detail in your image generation. The models must be compatible, sharing similar latent spaces or VAEs.  

  Example working combinations:  
  - Qwen + ControlNet and WAN 2.1-low as refiners  
  - Flux1 + Z-Image  
  - Chroma + Flux  
  - Chroma + Z-Image

- **VAE Decode ColorFix** *(New!)*  
  VAE Decode (ColorFix) - Fast, Color-Accurate Decoding for Flux Models
Solves the brightness shift and washed-out color problem that affects Flux models 
when using the standard VAE Decode node.
WHY THIS NODE?
Standard VAE Decode produces washed-out, brightened images with Flux models because 
it processes the entire image at once, causing normalization drift in the VAE decoder. 
This node uses tiled processing to maintain accurate colors while offering speed 
optimizations not available in the standard VAE Decode (Tiled) node.
HOW IT WORKS
The node breaks your image into smaller tiles during decode. Smaller tiles keep the 
VAE's normalization statistics closer to training values, preventing color shift. 
By default, it uses a single-pass approach (3x faster than standard tiled decode) 
while maintaining color accuracy.

- **PromptBatchGenerator** *(New!)*  
  Ever get super frustrated with those 81-frame batch videos where the same prompt just keeps repeating over and over? 😫 I know I did! Like, every 81 frames I’d have to smile or move my hands exactly the same way because the prompts were crazy repetitive. No no, that’s not fun for me.
But here’s a cool trick: did you know you can enter as many prompts as you like, separated by |, and the node will automatically calculate the time per prompt? That means you can actually tell a story! 🎉
Still, I wanted more… so I asked my team to build a nicer random prompt generator. Now you can:
Input multiple prompts with different behavior strengths
Mix them all across your video
Let the node decide how the behaviors combine, so it feels natural and dynamic

- **TBG_FluxKontextStabilizer** 
  Developed specifically for the **TBG ETUR** (Enhanced Tiled Upscaler and Refiner), this node maintains exact positioning of reference images in final outputs. It stabilizes spatial context during tiled upscaling and refinement to ensure high-fidelity alignment and image coherence. Stay with euler beta and between 16 and 30 steps. Add to Promt: Repair and enhance this this this photo.

- **ModelSamplingFluxGradual**  
  Implements gradual flux-based sampling control for smoother transitions during model sampling - ModelSamplingFluxGradual interpolates between ModelSamplingFlux and ModelSamplingFlux Normalized. This allows for the best of both approaches.
Detailed Inforamtion here: https://www.patreon.com/posts/125571636/edit

- **PolyExponentialSigmaAdder  Highres Fix Flux**  
  The PolyExponential Sigma Adder node adds the ability to manipulate curve parameters, such as adjusting the curve’s rigidity, and allows for the application of a negative poly-exponential curve to the Sigmas.
The PolyExponential Sigma Adder introduces a resolution-independent curve, ensuring a consistent adjustment to img2img processing across different resolutions. Sustitución for resolutions depending ModelSamplingFlux

- **BasicSchedulerNormalized**  
  A scheduler node with built-in denoise  normalization to ensure stable consistent sampling results across schedulers.

- **LogSigmaSamplerNode** & **LogSigmaStepSamplerNode**
  These nodes offer direct access to the internal model noise curve—the curve the model expects from sigma values during diffusion.
  LogSigmaSamplerNode enables manipulation of this curve directly, allowing users to enhance fine details, introduce natural imperfections, or soften the final image by shifting how the model interprets noise over time.
  This approach gives precise control over the model's behavior—similar in effect to techniques used by Detail Deamon or Lying Sigmas.
  These nodes are ideal for users looking to experiment with or customize the core diffusion response for artistic or technical purposes.
  
- **TBG_Preview_Sender_WebSocket**
  This node lets you send images directly from memory to memory, right through ComfyUI’s websocket no need to save anything to disk. Just plug it in as an output for your images, and you can instantly fetch the previews      from another web interface or app connected to your ComfyUI websocket. [TBG_Preview_Sender_WebSocket](https://www.patreon.com/posts/new-tbg-takeaway-142394428)

- **TBG Hex Cone Mask**
Generates a hexagonal cone pattern mask for variable denoise strength across an image. Creates gradients from center (maximum denoise) to edges (minimum denoise) of each hexagon. Control the gradient zones with inner_fraction (start of gradient), outer_fraction (end of gradient), and curve_power (gradient steepness). Outputs both a visual IMAGE of the pattern and a MASK for denoise control. Perfect for creating organic, non-uniform enhancement patterns. [TBG Hex Cone Mask]([https://www.patreon.com/posts/new-tbg-takeaway-142394428](https://www.patreon.com/posts/tbg-take-aways-142316016))
  
[Detailed Inforamtion on my Patreon: ](https://www.patreon.com/c/TB_LAAR)
---

## Overview

TGB’s sidecodes provide practical solutions distilled from complex development work into simple, easy-to-integrate nodes. These tools offer enhanced control over sampling dynamics, noise management, and image refinement, making them valuable assets for artists, developers, and researchers using ComfyUI and stable diffusion workflows.

Explore this repository to discover how these nodes can streamline your image generation pipeline and help push the boundaries of creative and technical possibilities.

## License

Copyright (C) 2025  Tobias Laarmann
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program comes with ABSOLUTELY NO WARRANTY; 
    This is free software, and you are welcome to redistribute it
    under certain conditions;

---

## Support

For updates and detailed development insights, visit TGB’s [Patreon page](https://www.patreon.com/c/TB_LAAR)).

---

## Tags

`ComfyUI` `Stable Diffusion` `AI Art` `Model Sampling` `Noise Scheduling` `Image Refinement` `Upscaling` `Tiled Upscaler` `Patreon` `Open Source` `AI Nodes` `Flux Control`

---

*Happy creating!*

