# guy-nodes-comfyui

These are designed to be custom nodes i found usefulness to that hopefully others can share. 

## Empty Latent creation by desired size with scale

This node is for knowing the desired output images sizes and reverse engineering based on what SDXL supports. It will them output:
1. a blank Latent
2. the Width & Height of generated Latent
3. The CLIP Width & Height based on the input scale
4. a ratio for your Upscaler. 

![alt text](images/Output.png)

This is all based on this repo: https://github.com/marhensa/sdxl-recommended-res-calc who created a great tool and I just enhanced it for my needs. 

# Manual Installation
To install it as ComfyUI custom node using the Git Clone Operation:

1. Go to this folder on your machine: `/ComfyUI/custom_nodes/`
2. Open command prompt to that folder, enter this below:
`git clone 
https://github.com/guyaton/guy-nodes-comfyui.git`
3. Restart ComfyUI
4. This custom node can be searched using:
   * "Guy Recommended Resolution Calculator and Latent Generator"
   * It can be located in "utils" node section
