# This repo is archived!

Please refer to its replacement: [Open Creative Studio Nodes for ComfyUI](https://github.com/alessandroperilli/OCS_Nodes#open-creative-studio-nodes-for-comfyui)

---

# APW Nodes for ComfyUI

A custom node suite to augment the capabilities of the [AP Workflows for ComfyUI](https://perilli.com/ai/comfyui/).

## Nodes

### Image Saver v1

This node allows you to save the input image/s in various formats: `.png`, `.jpg`/`.jpeg`, and `.webp`.

For each supported format, the node allows you to save a string of your preference in the EXIF tag `UserComment` (tag ID: `0x9286`).

The `UserComment` tag can then be displayed by any image manipulation software supporting EXIF. Here's an example with [XnView MP](https://www.xnview.com/en/):

<img width="412" alt="EXIF UserComment in XnView MP" src="/Images/XnViewMP.png" />

If you choose the `.png` format, the node also allows you to embed the ComfyUI workflow in the `extra` section of the image metadata.

You can customize the filename with the following variables: `%seed%`, `%date%`, and `%time%`.

<img width="412" alt="Image Saver v1" src="/Images/Image_Saver_v1.png" />

Credit: This code is based on receyuki's `SD Prompt Saver`, available [here](https://github.com/receyuki/comfyui-prompt-reader-node), and willmiao's `Save Image (LoraManager)`, available [here](https://github.com/willmiao/ComfyUI-Lora-Manager). All credit to them.

### Image Size (Local Models) v1

This node offers a list of preset resolutions for all local image generation models supported by APW for ComfyUI: Black Forest Labs FLUX.1, Stability AI Stable Diffusion 3.5, XL, and 1.5.

The resolutions are organized by number of megapixels rather than by model as FLUX and SD3.5 are capable of generating both 1MP and 2MP images.

The user can also set a custom resolution.

<img width="412" alt="Image Size (Local Models) v1" src="/Images/Local_Image_Size_v1.png" />

<img width="412" alt="Image Size (Local Models) Menu v1" src="/Images/Local_Image_Size_Menu_v1.png" />

### Image Size (Cloud Models) v1

This node offers a list of preset resolutions for all hosted image generation models supported by APW for ComfyUI: OpenAI GPT-Image-1.

<img width="412" alt="Image Size (Cloud Models) v1" src="/Images/Cloud_Image_Size_v1.png" />

<img width="412" alt="Image Size (Cloud Models) Menu v1" src="/Images/Cloud_Image_Size_Menu_v1.png" />

### Video Size (Local Models) v1

This node offers a list of preset resolutions for all local video generation models supported by APW for ComfyUI: WanVideo 2.1, Hunyuan Video, CogVideoX 1.5 and 1.0.

The user can also set a custom resolution.

<img width="412" alt="Video Size (Local Models) v1" src="/Images/Local_Video_Size_v1.png" />

<img width="412" alt="Video Size (Local Models) Menu v1" src="/Images/Local_Video_Size_Menu_v1.png" />

### Image List Filter v1

This node takes an `image list` as input, filters out images smaller than either width or height, and outputs a new `image list` without the excluded images.

If no input image remains after the filtering, the node outputs a new `image list` with the optional fallback image input.

<img width="412" alt="Image List Filter v1" src="/Images/Image_List_Filter_v1.png" />

Credit: This code is based on Kijai's `Image Batch Filter`, available [here](https://github.com/kijai/ComfyUI-KJNodes/). All credit to him.

## Installation

Install from ComfyUI Manager:

<img width="1378" alt="APW Nodes ComfyUI Manager" src="https://github.com/user-attachments/assets/0893fccf-3a5e-4726-a6e6-0e32c60d28b8" />

or clone this repo into the `/comfyui/custom_nodes` folder.
