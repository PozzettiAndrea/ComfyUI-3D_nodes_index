# CS Transform Node for ComfyUI

## Overview
The `CS Transform` node is a custom node for ComfyUI that applies a series of transformations to an input image and mask. The transformations include scaling, rotation, and translation, all centered around a specified pivot point. The node ensures that the transformed image is properly accommodated within a canvas, which can be expanded if needed.

## Features
- **Scaling**: Adjust the size of the image by a specified factor.
- **Rotation**: Rotate the image around a specified pivot point.
- **Translation**: Move the image by specified x and y offsets.
- **Pivot Point Visualization**: Optionally display the pivot point as a red dot on the image.
- **Canvas Expansion**: Optionally expand the canvas to ensure the transformed image is not cut off.

## Inputs
- **image** (optional): The input image to be transformed.
- **mask** (optional): The input mask to be transformed.
- **canvas** (optional): The canvas image to determine canvas dimensions.
- **position_x** (required): The x position for translation.
- **position_y** (required): The y position for translation.
- **pivot_x** (required): The x coordinate of the pivot point.
- **pivot_y** (required): The y coordinate of the pivot point.
- **rotation** (required): The rotation angle in degrees.
- **scale** (required): The scaling factor.
- **canvas_width** (required): The width of the canvas.
- **canvas_height** (required): The height of the canvas.
- **expand_canvas** (required): Whether to expand the canvas to fit the transformed image.
- **show_pivot** (required): Whether to show the pivot point on the image.

## Outputs
- **image**: The transformed image.
- **mask**: The transformed mask.

## Usage

1. **Adding the Node**:
   To add the `CS Transform` node to your ComfyUI pipeline, ensure you have placed the `transform_node.py` file in the appropriate directory within your ComfyUI installation.

2. **Configuring Inputs**:
   Configure the inputs as required. You can provide an image, mask, and canvas. Specify the transformation parameters including position, pivot point, rotation, and scale.

3. **Executing the Node**:
   Execute the node to apply the transformations. The transformed image and mask will be produced as outputs.

4. **Visualizing the Pivot Point**:
   Enable the `show_pivot` option to display a red dot at the pivot point on the transformed image. This can help you verify the pivot point's position after transformations.

