# Comfyui_DJ_nodes

This is a small collection of nodes designed for efficiency and the reduction of screen-clutter. ComfyUI can get messy fast, and I've been on a mission to create the cleanest workflow possible while maintaining full-control of all important settings. Part of this pack is tailored for a two-stage SDXL workflow, but many of the most useful nodes can be used in any context.

Drag the image below onto your workspace for a visual tour of the nodes, or scroll further for a brief overview.

![FOCUS Node Guide](https://github.com/user-attachments/assets/5c4ea7b7-c2ba-4edf-accd-2f55f3a0fefb)

## Documentation

(credit where it's due: some of these nodes are refactors/branches of various nodes that already exist, most notably, the Wildcard Processor and Global Seed from Impact and Inspire. My versions trim some things I don't need, and add a few new useful features)

**Global Seed Controller**
Inspired by Inspire's node; this one adds a simple toggle to flip between fixed and randomize (the only two modes the average user needs). It also offers a toggle for either full randomization or a truly global shared seed.

**SDXL All-in-One**
I love this node so much. Designed to compactly handle most of the boiler-plate stuff that happens at the front of your workflow. Generates an empty latent for the selected resolution, handles any wildcards in your prompt, applys prompt styles, takes care of CLIP encoding, and injects your final expected image resolution into the output conditioning. It's great.

**Control Module / Control Pipe**
Designed to bring all of the controls for frequently adjusted parameters into a single node. Integrates with the Style Injector and Wildcard Processor, but those are optional.

**Model Unloader**
Designed to be placed in between main stages to reduce memory requirements on your GPU. Comfy does not like it when your dedicated VRAM maxes out, and it does not manage it sufficiently on its own. This node is a noticable speed boost for my RTX 4080 (16GB).

**Wildcard Processor**
(Standalone node of the functionality built-in to the All-in-One). Replaces all text formatted as _ _ wildcard _ _ (no spaces) with an entry from the appropriate .txt file in the focus_wildcards folder. I.e, if you have a text file with a list of colors, type __color__ into your prompt and this processor will select a random entry from the list. Excellent tool to let RNG take you to different parts of Latent Space! _Includes a toggle to freeze_wildcards_, so if you land somewhere cool you can just lock it in and let the Global Seed explore different variations via the noise-seed on your Ksampler. 

**Style Injector**
(Standalone node of the functionality built-in to the All-in-One). Modifies your prompt to push it toward a certain style of your choice. The built-in options are tailored for photography and portraits, but it's very easy to expand. Just follow the formatting in the focus_style.csv and you can add any categories you like. Note: Style effectiveness will vary depending on what checkpoint and LORAs you're using, and how complex/long your base prompt is. Simpler/shorter prompts leave more "token space" for the style words to shine through. 

**Prompt Box**
This is a fairly basic text-entry box. Only difference is that it has a dropdown menu that displays all available wildcard categories. (Just useful as a quick reference while you're in the workflow).

**FOCUS Upscaler**
Quick and easy upscaling/downscaling. Scale_factor is based on the resolution of the input image, so if your upscale model wants to 4x it, this node will first do the upscale then downscale it to 2x (if you have the scale_factor set to 2).

## Workflows

1. FOCUS Workflow (basic).
   Everything you need to generate an endless amount of pro-quality portraits with a single click. Add additional wildcards/styles for even MORE variation. The model-unloader node ensures the workflow can run smoothly on even 12GB gpus. Users with > 18GB vram can disable it to save a few seconds of generation time.

![FocusWorkflow](https://github.com/user-attachments/assets/c41025c4-f3f8-4d41-8d28-9045e699cdaa)

2. FOCUS Workflow (advanced). Adds a SAM/SEGS face detailer and a LORA stack. The detailer is only useful for certain combinations of checkpoints/LORAs. It doesn't really do much for the workflow's default checkpoints, but good to have available when you need it.

![FocusWorkflow_advanced](https://github.com/user-attachments/assets/ecf0bd22-8171-4a17-8df6-d58ec85ee4c7)

