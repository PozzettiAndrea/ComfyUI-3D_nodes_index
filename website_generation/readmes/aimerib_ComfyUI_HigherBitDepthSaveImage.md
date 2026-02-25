# Higher Bit Density SaveImage Node
This is a ComfyUI node that allows you to save images with a higher bit depth.

## Installation
1. Download the `save_image_node.py` file.
2. Place the file in the `custom_nodes` directory of your ComfyUI installation.

## Usage
1. Add the `Save Image Higher Bit Depth` node to your graph.
2. Connect the image you want to save to the `IMAGE` input of the node. (Can be used in combination with other nodes that output images, like `SaveImage`)
3. Set the `filename_prefix` to the desired prefix for the filename of the image you want to save.
4. Set the `bit_depth` to the bit depth of the image you want to save.
  4.1 For 8bits (8-bit per channel - 24bit RGB) images, set `bit_depth` to `8`.
  4.2 For 16bits (16-bit per channel - 48bit RGB) images, set `bit_depth` to `16`.
  4.3 For 32bits (32-bit per channel - 96bit RGB) images, set `bit_depth` to `32`.
5. Set the `format` to the format of the image you want to save. Can be `PNG`, `TIFF`, or `JPEG`. Default is `PNG`.



## Notes
- The `format` can be `PNG`, `TIFF`, or `JPEG`.
- The `filename_prefix` is the prefix of the filename of the image you want to save.
- The `bit_depth` is the bit depth of the image you want to save.
- For 32 bit images, only TIFF is supported, and will be automatically used if selected.
