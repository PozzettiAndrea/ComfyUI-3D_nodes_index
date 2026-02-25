# ComfyUI YSC HighRes-Fix

A custom node for **[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** designed to simplify the "High-Resolution Fix" process. This node takes an input image, performs a direct upscale, and then re-encodes it into a latent image, preparing it for a final sampling pass to add details.

## What It Does

This node replicates the functionality of a high-resolution fix pipeline. Instead of just resizing an image, it upscales it and then uses a diffusion sampling process (denoising) to add fine details that are consistent with the original image's content.

## How It Works

The node's operation is straightforward:

1.  **Image Input:** You provide a low-resolution image (e.g., the output of your initial generation).
2.  **Brute Upscale:** The node applies a simple, direct upscale to the image to increase its dimensions.
3.  **Latent Encoding:** This larger, upscaled image is then encoded back into the latent space.
4.  **Image sampling**: This latent image will be denoised by a ksampler-like method, generating a greater and better image.
5.  **Latent Output:** The node outputs this new, larger latent image.

## How to Use (Example Workflow)

1.  Generate your initial image (e.g., 512x512) as you normally would.
2.  Connect the output image from your `VAE Decode` node to the `image` input of the **YSC HighRes-Fix** node.
3.  Connect the model, VAE, positive and negative prompt and a upscale model to the respective input of **YSC HighRes-Fix** node.
4.  **Crucially, set the `denoise` on this second `KSampler` to a value like `0.3` to `0.55`.** This value controls how much detail is added. **I recommend do not use high values (0.7+) because the image will be broken.**
5.  Adjust the upscale range (1 to 4x upscale). **For low VRAM users, I recommend upscaling up to 2 times using this node.**
6.  Connect the `LATENT` output of this node to a final `VAE Decode` node to get your high-resolution image.
7.  **Optional**: After generating your upscaled image, you can increase even more the resolution using **[Ultimate SD Upscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)**

## Inputs

* `image`: The source image (from a `VAE Decode` or `Load Image` node) that you want to upscale and refine.
* `checkpoint model`: A checkpoint used to generate images. This one will be used by the embedded ksampler of the node.
* `positive and negative prompts`: For quality handling
* `VAE`: For the embedded VAE encoder of the node.
* `Upscale model`: Used to make the first raw upscale. 

## Outputs

* `LATENT`: The upscaled and encoded latent image, ready for a VAE decode.

## Installation

1.  Navigate to your `ComfyUI/custom_nodes/` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/yannickcruz/ComfyUI-YSC-HighResFix.git
    ```
    (Replace the URL with your actual repository URL)
3.  Alternatively, download the `.py` files from this repository and place them directly in the `ComfyUI/custom_nodes/` directory.
4.  Restart **[ComfyUI](https://github.com/comfyanonymous/ComfyUI)**.

**You can now install this node via ComfyUI Manager!**

## Credits

* This node was possible thanks to the code of the [TheBill2001's](https://github.com/TheBill2001) [comfyui-upscale-by-model](https://github.com/TheBill2001/comfyui-upscale-by-model/tree/main), that inspired me to build the first raw upscale of this node.
