# comfyui-smooth-step-lora-loader

v1.1.0: Updated to support more lora types, including video generating ones (tested with LTX-Video)

Frustration over long lora training times coupled with undertrained results (SDXL on 3060), I started wondering if it was possible to do anything similar with loras (which of course is a completely different concept from TI)

Would it be possible to enhance desirable elements, while diminishing undesirable ones? After some experimenting with normalization functions I ended up with a smooth step function. In simple terms, smooth step increases values above the mean, while lowering values under it.

The idea being that, hopefully, the lora has learned the concept you want to train on for relevant elements to be above the mean. And if there is any contamination, it is below the mean and thus will have a lesser impact.

I'm not sure it worked out that way. The issue is that you won't necessarily know what the lora has learned. But it does something, and I've had some positive results from it, even though not consistently, as it varies from seed to seed.

While I've mostly tested it on "narrow concept" lora's, where I thought it would do best, here is an example from the opposite, using the ad-detail-xl lora, which must be considered broad. The model is dreamshaper lightning xl. The prompt: "product placement". 

The leftmost column is only the lora. Down: Increased lora strength. Right: Increased smooth step strength


![comfy-ui-smooth-step-lora-loader-and-python-script-for-non-v0-38t85xulgs5d1](https://github.com/user-attachments/assets/1af98148-29f1-4e71-9c77-1f187dcaf0c1)



Usage:

clone into ComfyUI/custom_nodes/

It resides in the "loaders" category.

![Screenshot from 2024-06-10 20-48-11](https://github.com/neph1/comfyui-smooth-step-lora-loader/assets/7988802/e898dba8-8e78-427d-8424-3ea0d0984873)

Explanation:
https://www.reddit.com/r/StableDiffusion/comments/1dctns3/comfy_ui_smooth_step_lora_loader_and_python/

Gist (put in kohya_ss sd-scripts/networks) for non-comfy users (or to make it permanent):
https://gist.github.com/neph1/499f608ca88bc8443facb95d3831e901
