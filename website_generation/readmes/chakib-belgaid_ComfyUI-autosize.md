# Autosize 

A ComfyUI utility plugin designed to optimize the latent space for generating high-quality results. It approximates the closest size model for better generation results.

# Nodes 

## SDXLAutoSize 
a node that returns the closest sdxl resoltion to the input image while maintaining the aspect ratio.
### square resolutions:
- 1024 x 1024 pixels (1:1 Square)
# Widescreen resolutions:
- 2048 x 512 pixels
- 1920 x 512 pixels
- 1600 x 640 pixels
- 1536 x 640 pixels
- 1472 x 704 pixels
- 1344 x 768 pixels
# Portrait resolutions:
- 960 x 1024 pixels
- 896 x 1152 pixels
- 832 x 1216 pixels
- 768 x 1280 pixels
- 704 x 1408 pixels
- 640 x 1536 pixels

## CustomAutoSize
a node that tries to fit the total number of pixels to the total pixel used for training the model while maintaining the aspect ratio.
