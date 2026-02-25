# Simple ComfyUI Node for Remote VAE Decoding

This node enables the use of VAE decoding through HuggingFace's inference endpoints.

For more details, refer to the [VAE Decode with Hybrid Inference](https://huggingface.co/docs/diffusers/main/en/hybrid_inference/vae_decode) documentation.

> **Note:** This node does not support **SD1.5** or **SDXL** VAEs, as they typically perform faster on local hardware.

Currently, only **Flux** and **HunyuanVideo** are supported.

As HuggingFace expands [support for other VAEs](https://huggingface.co/docs/diffusers/main/en/hybrid_inference/vae_decode#available-vaes), they will be incorporated into this node.

This node does not rely on the `diffusers` library and has no external dependencies beyond ComfyUI-Core. It is designed to be minimalistic.

For more information on remote VAE decoding, you can refer to HuggingFace's [blog post](https://huggingface.co/blog/remote_vae)

Using this node is quite simple, just replace the built-in `VAE Decode` with `VAE Decode (Remote)` and that's it.

![Usage-Flux](https://raw.githubusercontent.com/Visionatrix/ComfyUI-RemoteVAE/main/screenshots/flux.png)
![Usage-HunyuanVideo](https://raw.githubusercontent.com/Visionatrix/ComfyUI-RemoteVAE/main/screenshots/hunyuan_video.png)
