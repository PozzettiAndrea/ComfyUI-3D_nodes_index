# Open Creative Studio Nodes for ComfyUI

A custom node suite to augment the capabilities of [Open Creative Studio for ComfyUI](https://oc.studio).

## Nodes

### Image Grid 4x4 v1

This node merges sixteen input images into a 4x4 grid using row and column-labeled inputs (`image_r1c1`, `image_r1c2`, …, `image_r4c4`).

Each row is concatenated horizontally and then stacked vertically, producing a single tiled output image.

<img width="412" alt="Image Grid 4x4 v1" src="/Images/Image_Grid_4x4_v1.png" />

Credit: This code is based on Kijai's `Image Grid Composite 3x3`, available [here](https://github.com/kijai/ComfyUI-KJNodes/). All credit to him.

### Image List Filter v1

This node takes an `image list` as input, filters out images smaller than either width or height, and outputs a new `image list` without the excluded images.

If no input image remains after the filtering, the node outputs a new `image list` with the optional fallback image input.

<img width="412" alt="Image List Filter v1" src="/Images/Image_List_Filter_v1.png" />

Credit: This code is based on Kijai's `Image Batch Filter`, available [here](https://github.com/kijai/ComfyUI-KJNodes/). All credit to him.

### Image Saver v1

This node allows you to save the input image/s in various formats: `.png`, `.jpg`/`.jpeg`, and `.webp`.

For each supported format, the node allows you to save a string of your preference in the EXIF tag `UserComment` (tag ID: `0x9286`).

The `UserComment` tag can then be displayed by any image manipulation software supporting EXIF. Here's an example with [XnView MP](https://www.xnview.com/en/):

<img width="412" alt="EXIF UserComment in XnView MP" src="/Images/XnViewMP.png" />

If you choose the `.png` format, the node also allows you to embed the ComfyUI workflow in the `extra` section of the image metadata.

You can customize the filename with the following variables: `%seed%`, `%date%`, and `%time%`.

<img width="412" alt="Image Saver v1" src="/Images/Image_Saver_v1.png" />

Credit: This code is based on receyuki's `SD Prompt Saver`, available [here](https://github.com/receyuki/comfyui-prompt-reader-node), and willmiao's `Save Image (LoraManager)`, available [here](https://github.com/willmiao/ComfyUI-Lora-Manager). All credit to them.

### First Not Empty v1

This node returns the first input that holds data, falling back to the second input when the first is empty.

<img width="412" alt="First Not Empty v1" src="/Images/First_Not_Empty_v1.png" />

Credit: This code is based on rgthree's Any Switch, available [here](https://github.com/rgthree/rgthree-comfy). All credit to him.

### Image Size (Cloud Models) v1

This node offers a list of preset resolutions for all hosted image generation models supported by OCS for ComfyUI: OpenAI GPT-Image-1.

<img width="412" alt="Image Size (Cloud Models) v1" src="/Images/Cloud_Image_Size_v1.png" />

<img width="412" alt="Image Size (Cloud Models) Menu v1" src="/Images/Cloud_Image_Size_Menu_v1.png" />

### Image Size (Local Models) v1

This node offers a list of preset resolutions for all local image generation models supported by OCS for ComfyUI: Black Forest Labs FLUX.1, Stability AI Stable Diffusion 3.5, XL, and 1.5.

The resolutions are organized by number of megapixels rather than by model as FLUX and SD3.5 are capable of generating both 1MP and 2MP images.

The user can also set a custom resolution.

<img width="412" alt="Image Size (Local Models) v1" src="/Images/Local_Image_Size_v1.png" />

<img width="412" alt="Image Size (Local Models) Menu v1" src="/Images/Local_Image_Size_Menu_v1.png" />

### Model Downloader v1

This node assists you in downloading an AI model from the [Hugging Face repository](https://huggingface.co/perilli/OCS_Models) containing all models used by Open Creative Studio.

You can specify the folder where you want to save a model, and the name the model will have in your folder.

If the folder structure you specify in the node doesn't exist, the node will create it for you.

If the file you specified already exists in the set folder, the node will ignore the request without errors.

The node supports absolute or relative folders, optional Bearer token authentication (you can reference an env var with `$VARNAME`), and the ComfyUI download progress bar if you are using the most recent versions of ComfyUI.

<img width="412" alt="Model Downloader v1" src="/Images/Model_Downloader_v1.png" />

### Video Size (Local Models) v1

This node offers a list of preset resolutions for all local video generation models supported by OCS for ComfyUI: WanVideo 2.1, Hunyuan Video, CogVideoX 1.5 and 1.0.

The user can also set a custom resolution.

<img width="412" alt="Video Size (Local Models) v1" src="/Images/Local_Video_Size_v1.png" />

<img width="412" alt="Video Size (Local Models) Menu v1" src="/Images/Local_Video_Size_Menu_v1.png" />

### Watermarker v1

This node overlays a watermark image onto one of the four corners of a source image.

`corner_padding` defines how many pixels of spacing to leave between the watermark and the corner edges.

`percent_of_image` controls how large the watermark becomes relative to the source image dimensions (for example, `20` scales it to 20% of the width/height while keeping proportions).

`opacity` defines the level of transparency the watermark image must have.

<img width="412" alt="Watermarker v1" src="/Images/Watermarker_v1.png" />

## Installation

Install from ComfyUI Manager:

<img width="1378" alt="Open Creative Studio Nodes in ComfyUI Manager" src="/Images/ComfyUI_Manager.png" />

or clone this repo into the `/comfyui/custom_nodes` folder.
