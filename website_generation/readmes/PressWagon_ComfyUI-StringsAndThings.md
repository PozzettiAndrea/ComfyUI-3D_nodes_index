# ComfyUI Strings&Things

A collection of ComfyUI custom nodes for formatting and debugging string data with the intention of collecting generation data to be processed by a custom node pack like comfy-image-saver, as well as miscellaneous extra nodes that I find useful or interesting to experiment with. Nodes are not currently set up to take batched inputs.

## Part 1 - String Formatting
**Lora Selector** - lets you pick a LoRa while also outputting its name as a string.

**Lora Name Collector** - takes up to 5 LoRas, should now work chaining multiple together for >5 loras.

**Debug String** - Attempts to print input to the console. Primarily useful for strings, but tries to take anything as input.

**Formatting and Concattenating 3 Strings** - Added pre and post text to up to 3 input strings and concatenates them in order with a separator. Empty body inputs will not have their pre and post text included. 

**Formatting Single String** - Pre and post text for a single string.

## Part 2 - Extras
**Mosaic Effect Node** - Applies a mosaic effect (aka tile censoring) to the entire image. Useful for pixelart style generations, or in combination with BBox/SEGS for censoring. (Example workflow are available in the 'Example workflows' folder)

**Fourier Analysis Node** - Some people claim some stuff about AI and repetitive patterns being visible in the fourier analysis. Don't ask me, I'm not a scientist, I just think they look cool. 

**Text Embedding Interrogator** - Calculates the Cosine Similarity and Euclidean Distance between the Pooled Attention CLIP text embeddings for two embeddings.

**Image Difference** - Calculates the simple pixel-wise difference between two images and outputs an image of the result. It also calculates the Mean Square Error as a measure of difference between the images and displays the value in the console as a percentage (0% = same image, 100% = one black vs one white image). The SME calculation can be skipped by toggling console_mse to false. For images with subtle differences you can toggle contrast_boost to true, increasing the magnitude of the displayed differences by a factor of 5.
