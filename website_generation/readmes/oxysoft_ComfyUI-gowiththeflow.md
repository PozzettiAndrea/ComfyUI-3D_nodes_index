# ComfyUI-gowiththeflow

Implementation of GoWithTheFlow, original code at https://github.com/Eyeline-Research/Go-with-the-Flow/ and https://github.com/RyannDaGreat/CommonSource/blob/master/noise_warp.py

## Usage

1. Add NoiseWarperNode
2. Pass a BGR flow map
3. (Leave width and height zero to detect dimensions from flow map)
4. (you probably want 3 noise_channels for most models without alpha channels)
5. Pass the latent to the model and enjoy!

The noise warper node will preserve the noise state and only update it each time that the workflow is invoked.
