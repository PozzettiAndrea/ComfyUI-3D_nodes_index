# ComfyUI-ShakaNodes
A collection of custom nodes for ComfyUI. Hang loose! 🤙

## About
A set of custom nodes that I create to both improve my workspaces and learn more about Generative Image and Video generation.
Over time, I hope this repo will be a collection of useful tools for everyone, but for now, this is a work in progress repo and not recommended for production. But hey, feel free to play around with these if they help you :)

**Install**
The best way to install and stay up to date with the repo is to use ComfyUI-Manager. Look for ComfyUI-ShakaNodes

Alternatively, you can do a manual install:
1. Copy the repository folder into your ComfyUI `custom_nodes` directory:
   - ComfyUI/custom_nodes/ComfyUI-ShakaNodes
2. Restart ComfyUI.
3. The nodes will appear under the "ShakaNodes" category (or similar).

## Quick summary
- ShakaWanKeyframes — Add a set of batch images and prepare a Wan Generation with multiple input images at any keyframe. Set indices to indicate where the images should be located and the weight of the input images. All other inputs are pretty much passthroughs (though used for some sanity checking too).
- ShakaTensorDebug - Simply used to read out information about the tensors. Early days, but I want to use this node to help debug and understand what goes on behind the scenes in some of the nodes.

Proper documentation will come over time.
