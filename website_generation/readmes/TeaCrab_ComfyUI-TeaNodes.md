# ComfyUI-TeaNodes

Adds a few new nodes:

### Image Equalization CLAHE (This node can't be any more Kornia)
*  When images have their histogram smoothly distributed, I'd say it gives ControlNet preprocessor an easier time.
*  Works great when image BG is removed.

### Image Size Approximation
*  Works based on pixel count that retains Image ratio.
*  This algorithm is really dumbly written, but it works.
*  Great for stabilizing the speed of image-to-image generation.

### Image Resize
*  Takes size tuple from Size Approximation Node.
*  Seriously, image size always has 2 numbers, why can't it fit through a single wire?
*  It also defaults to a node socket instead of having to convert it into input from a widget.

### Image Scale
*  Simply multiplies image size by a factor.
*  20240425: Now scales smoothly when multiplied by non-power-of-2 factors - use LANCZOS option now
*  Have an easier time saving in-process scrap images at half or quarter resolution.

### Crop To
*  Crop an image to the same size of the reference image
*  Hate some of those nodes that complains about bad tensor dimensions for whatever reasons? Fear no longer.

### KorniaGamma
*  This works like an easy/complex/idk brightness/contrast/level adjustment node
*  Image processing power must be utilized for better results.

### Random & Non-Random Color Fill
*  Fill based on reference image size
*  Randomness defined by original color and a variance in hue, saturation and value
*  Hopefully the color input field works for most color string formats.
