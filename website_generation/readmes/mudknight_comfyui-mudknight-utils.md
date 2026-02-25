# ComfyUI mudknight utils

Nodes to clean up your workflow.

![full workflow](assets/workflow-full.png)

I designed these nodes as an alternative to the `comfyui-easy-use` pipe system. I like easy-use nodes in concept, but I don't like how long it takes to use `pipe-in`, which ruins their flexibility.

I also designed FastDetailer as an alternative to FaceDetailer, with the self-explanatory goal of making a detailer that's faster.

## Dependencies
This node pack requires the following node packs:

- [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)

## Nodes

### Full Pipe
A full pipe can either be made with the `Loader (full-pipe)` node or manually with `full pipe pack`. The pipe functions as the only necessary connection between discrete sections of a workflow, storing all necessary data.

The main differences between easy use pipes and full pipes are:
- Full pipes store additional information, like `ckpt_name`, `positive_text`, and `negative_text`
- Easy use's pipe in node takes ~5 seconds to run, compared to full pipe in which is almost instantaneous.
- Less ambiguity with the seed input.
- Pipe nodes can be used independently, without relying on the loader node (but you'll need to use a `Full Pipe Pack` node).

### Loader (full-pipe)
Loads a selected checkpoint, sets CLIP skip, sets a seed, and optionally applies a LoRA stack from the input.

### Prompt (full-pipe)
This is a combined positive and negative prompt box that lets you use pre-defined prompt text. Features include:
- Accepts LoRA syntax
- Ignores `#` commented lines
- Automatically applies quality tags, embeddings, style tags, character tags, and preset tags from Preset Manager.
- Splits quality tags+embeddings, style tags, character tags, and the main prompt into separate conditionings and then concatenates the conditionings.

### Base (full-pipe)
This is the base image generation node. By default it will use an empty latent with the dimensions defined by the node, but it also has an `image` input and `denoise` parameter for img2img generation.

### Upscale (full-pipe)
This is an upscaling node that will upscale using lanczos and an upscale model (or none) to a target scale value and then resample the image.

### FastDetailer
The FastDetailer nodes are an alternative to FaceDetailer that are intended to be faster and more detailed, at the (potential) cost of cohesion with the rest of the image. It simply crops a region, upscales it to 1MP, samples the image, scales it back down to its original size, and uncrops it. The `bbox_fallback` model will run if no SEGS were detected with the primary model, with the use-case to be used with models like `full_eyes_detect_v1.pt` and `Eyes.pt` as a fallback if only one eye is detected.

### Save (full-pipe)
This node saves the image with the ComfyUI workflow and A1111 metadata. I use a tool on my images that pulls the A1111 prompt (since pulling a prompt from a comfy workflow isn't standardized in any way), so that's the main focus of the node.

### OpenCV Denoise
Based on the opencv script [here](https://rentry.org/RemovingDiffusionGunk). It removes noise left behind by the diffusion process.

ComfyUI seems to limit nodes to a single core, so using the CPU for this node is excruciatingly slow. 

<details>

<summary> GPU selection on multi-GPU systems </summary>

If you want to use a specific gpu on a multi-gpu system, use `clinfo -l` to get a list of devices and set the environment variable `OPENCV_OPENCL_DEVICE` to `<platform>:GPU:<index>`, where `<platform>` is everything listed after `Platform #*:` and `<index>` is the `Device #`. For example:

```
Platform #0: Intel(R) OpenCL Graphics
 `-- Device #0: Intel(R) Arc(TM) B580 Graphics
Platform #1: rusticl
 `-- Device #0: AMD Radeon RX 6800 (radeonsi, navi21, LLVM 21.1.6, DRM 3.64, 6.18.2-arch2-1)
```

Here you would use `OPENCV_OPENCL_DEVICE=Intel(R) OpenCL Graphics:GPU:0` or `OPENCV_OPENCL_DEVICE=rusticl:GPU:0`

</details>

### Auto-level
Adjusts black and white levels to the closest values within a threshold.

## Preset Manager
The Preset Manager is a web interface that lets you define all of your prompt prests, with sections for characters, models, styles, and tags.

## Extensions

### Tag Autocomplete
This was originally just for the Preset Manager, but I now consider it an upgrade from the [pythongosssss/ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts) autocomplete extension. Features include:

- Count-based sorting
- Color coding based on tag category
- Redirect tag aliases (`looking_aside` -> `looking_to_the_side`)
- Preset Manager tags merged
- Thumbnails for LoRAs, embeddings, and Preset Manager characters. LoRA and embedding thumbnails pull from image previews from [LoRA Manager](https://github.com/willmiao/ComfyUI-Lora-Manager).
- Custom tag sources
- Tag blacklist

### Preset Manager Button
The node pack automatically adds a button to the left of the ComfyUI Manager button, that brings up a web interface for managing prompt presets used in the `Prompt (full-pipe)` node.

### Full Pipe Previews
This adds previews of the completed image to in-pack generation nodes when execution finishes, replacing the live preview.

### Preview File Sizes
This adds a label to the bottom right of an image preview, showing the filesize of the image.

### Keyboard shortcuts
- Alt+Up/Down will increment/decrement the batch count by 1
- Shift+Alt+Up/Down will double/halve the batch count

### Node Runtime
This shows how long nodes take to execute. Code taken from `comfyui-easy-use`.

### Line Numbers
Adds line numbers to the left side of all textarea inputs when focused.
