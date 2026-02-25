# Latent Bridge Matching (LBM) ComfyUI Nodes

This is a fork of https://github.com/gojasper/LBM with ComfyUI node wrappers.

These nodes will automatically download the StableDiffusion VAE and Scheduler from huggingface hub (stabilityai/stable-diffusion-xl-base-1.0)

You need to download the https://huggingface.co/jasperai/LBM_relighting/tree/main `model.safetensors` and place it in the ComfyUI `models/diffusion_models` directory for the `LBMLoader` node to find it.
