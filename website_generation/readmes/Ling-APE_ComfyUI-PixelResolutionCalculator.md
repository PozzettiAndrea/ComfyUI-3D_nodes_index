# ComfyUI-PixelResolutionCalculator

This node is used in the [All-in-one Flux Dev workflow](https://github.com/Ling-APE/ComfyUI-All-in-One-FluxDev-Workflow) I made.

There is two nodes:
* PixelResolutionCalculator

![node1](Nodes_Demo/PixelCal.png)
* LatentSizeToPixelSize

![node1](Nodes_Demo/LatentTOPixel.png)


## PixelResolutionCalculator
The pixel resolution calculator is just a simple node that generate the closest "latent friendly" pixel resolution from your mega pixel and aspect ratio of choice. Took inspiration from the ImageScaleToTotalPixels node I saw from the original Flux demo workflow, since with flux everyone seems to talk about it with pixel resolution instead of width and height pixel count like SDXL. 
## LatentSizeToPixelSize
LatentSizeToPixelSize convert a laten samlpe input to width and height pixel count.
