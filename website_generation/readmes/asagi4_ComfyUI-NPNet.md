# ComfyUI NPNet (Golden Noise)

A very barebones mostly-copypaste implementation of https://github.com/xie-lab-ml/Golden-Noise-for-Diffusion-Models

## Requirements
You need the pre-trained weights for your model. Download and place them under `models/npnet` in your ComfyUI folder, or add an extra path in `extra_model_paths.yaml` for the `npnet` type.

You can find safetensors-converted weights at https://huggingface.co/asagi4/NPNet

The original pickle-format checkpoints are found at https://drive.google.com/drive/folders/1Z0wg4HADhpgrztyT3eWijPbJJN5Y2jQt?usp=drive_link

## Usage
Use with custom sampling and pass in an initial noise from eg. `RandomNoise` and a prompt as a conditioning. See tooltips on the node for an explanation for the options.

You can also run it on the CPU, though that appears to change the output for some reason.

## Notes
The model works with 128x128 latents, apparently. If you pass in other shaped latents, it will reshape the noise into a square before running the noise model, and then reshape the result back to the original resolution. You can control how the reshape happens with the `reshape` and `method` parameters.

If you get an error from the timm module when running this, update your timm package. It may be too old.

You can use `convert_to_safetensors.py` to convert the pre-trained models into safetensors files (with fixed keys)
