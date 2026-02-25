# ComfyUI IG1 Tools

This repository contains ComfyUI nodes to assist generation in ComfyUI. It is mostly direct toward high resolution image generation and automation.

## Installation

### Manual

1. Either clone this repository or download the ZIP and extract it into your `custom_nodes` directory of ComfyUI.
2. Restart ComfyUI to load the new node.

### ComfyUI Manager

1. Open ComfyUI Manager.
2. Click on "Install via Git URL".
3. Enter the following URL: `https://github.com/iguanesolutions/comfyui-ig1-tools.git`.

## Usage

Once installed, you will find the following nodes under the `IG1 Tools` category:

* `Resolution` - Allows to enter (or receive) a width and a height and package them as a resolution, allowing to pass a single parameter. Resolution parameters have an enhanced string representation that can be viewed with the ComfyUI `Preview Any` node.
* `Resolution Properties` - Allows to unpack a resolution properties: width, height, rounded megapixels, and aspect ratio parameter.
* `Aspect Ratio Properties` - Allows to unpack a aspect ratio parameter: nominator, denominator, raw value
* `Image Selector` - A lazy image selector (require and so trigger generation of only one of the input image) to help automate workflows with output from the advisor.
* `Resolution Advisor` - A helper to compute valid resolutions for various models from an input resolution. Currently supports QwenImage, FluxDev and SDXL. See below for more details.
* `Qwen Image Natives Resolutions` - A list of Qwen Image native resolutions. Native means the model has been trained on these resolutions and so should have the best possible output quality and coherence with them.
* `Flux Licensing Usage Report` - Allows to automatically report to Black Forest Lab images generated with a licensed Flux Dev model.
* `Load input/output Image` - Allows to load an image from the input or output directories.

### Resolution and Aspect Ratio parameters

![helpers_screenshots](res/helpers_nodes.png)

### Resolution Advisor

This node takes a desired resolution and computes the closest valid resolution the selected model, including whether a HiRes fix is needed and a final upscale is needed to reach the input resolution from the computed generation resolution.

Example with Flux Dev:
1. Input resolution is `3844x2160`. The resolution is not valid because:
    1. It does not respect the stepping (`3840x2160` would have, it is made on purpose for this example)
    2. It is over the max size of Flux
2. The first step will be to compute a resolution respecting the stepping (we use 16 instead of 32 more information below) and minimum length for width and height but also max size of the image (total pixels for the generated image). It will first search a ratio closest to the original ratio and then a resolution with the closest valid ratio closest to the input resolution (in our case, the biggest possible). In our example the generate resolution will be `1280x720`.
4. Because the input resolution `3840x2160` is bigger than the `1280x720` generate resolution, the `need_upscale` boolean will be set to true: it indicates that a second pass is needed to upscale the image to reach (or get closer) to the input resolution. We recommended to perform 2x HiRes fix on this step (instead of a simple upscale).
5. Because the HiRes fix will upscale (and add details to) the image to `2560x1440` (x2) and because this resolution is still under the input resolution, the `need_upscale` boolean will be set to true: it indicates that a third pass is needed to upscale the image to the reference resolution. We recommended to perform a simple upscale on this step.
6. By upscaling the hires image by x2 again we will optain a final image of `5120x2880` that is finally bigger than the input resolution, at this step a downscale will be needed to get the final image.
7. For the final downscale you have 2 choices:
    * Downscale the image to the input image while stretching it in order to reach the `3844x2160` input resolution (it will be bearly visible).
    * Downscale the image by respecting its generation proportion (here 16/9) to get a non stretched image of `3840x2160`, the closest possible of the input resolution.

By using conditionnal nodes on your workflow you can acheive a fully automated workflow that:

1. Take any desired width and height as input
2. Compute the optimal generate resolution for the model
3. Perform **automatically** and *if necessary* a second HiRes pass
4. Perform **automatically** and *if necessary* an additionnal upscale pass
5. Downscale the image and adapt its ratio or not

Check the example below !

### Flux Licensing Usage Report

This nodes allows you to seamlessly report your generation to Black Forest Labs if you have a licensed Flux Dev model. It supports multi images batches too.

Check the example below !

## Example

![workflow_screenshot](res/flux_hires_generate.png)

You can [download](res/Flux.1-Dev_HiRes.json) the example workflow to test an automatic Flux HiRes generation. You will need an additional extension ([ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)) to help streamline the final downscale.

### Load input/output image

This node allows you to load an image from the input or output directories.
The refresh button will make a call to the `/ig1api/images` endpoint to refresh the images list.

![load_image_screenshot](res/load_image_node.png)

### API Server endpoints

* `/ig1api/images`

    **Method**: GET

    **Description**: Get all input and output images names.

    **Example**:

    ```bash
    curl -s -X GET "http://127.0.0.1:8188/ig1api/images"
    ["input1.png", "input2.png", "output1.png [output]", "output2.png [output]"]
    ```
