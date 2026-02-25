# Dream Painter Nodes for ComfyUI

This repository contains a set of nodes for generation of simple 2D graphics ComfyUI. These are intended for guiding 
image generation, for instance using controlnets. For that reason the nodes are very much a quick-and-dirty solution, 
not intended to produce the final artwork. 

## Installation

### Simple option

You can install Dream Painter using the ComfyUI Manager.

### Manual option

Run within (ComfyUI)/custom_nodes/ folder:

* git clone https://github.com/alt-key-project/comfyui-dream-painter.git
* cd comfyui-dream-painter

Then, if you are using the python embedded in ComfyUI:
* (ComfyUI)/python_embedded/python.exe -s -m pip install -r requirements.txt

With your system-wide python:
*  pip install -r requirements.txt

Finally:
* Start ComfyUI.

## Concepts used

These are some concepts used in nodes:

### BitMap

A BitMap within Dream Painter is a monochrome image. It can be convert to images or masks.

### Shape

A shape is a simple vector drawing. It can be transformed in various ways and rendered as a bitmap.

## The nodes

### Bitmap AND [DPaint]
AND bitmap combine operation. Produces a white pixel if both bitmap have white pixels in the same position.

### Bitmap Crop Center [DPaint]
Crops the center part of a bitmap.

### Bitmap Dimensions [DPaint]
Returns dimensions of a bitmap.

### Bitmap Edge Detect [DPaint]
Basic edge detection for bitmap images. Should work well in most cases, but an alternative is to convert to an image and
use the various different nodes available in ComfyUI.

### Bitmap Expand Canvas [DPaint]
Expends the canvas of a bitmap image by adding a border.

### Bitmap Invert [DPaint]
Returns the inverted bitmap. 

### Bitmap OR [DPaint]
OR bitmap combine operation. Produces a white pixel if either bitmap has a white pixel in the same position.

### Bitmap Resize [DPaint]
Resize/scale of bitmap.

### Bitmap Rotate [DPaint]
Arbitrary rotation of a bitmap image.

### Bitmap To Image & Mask [DPaint]
Converts a bitmap into an RGB image and a mask.

### Bitmap XOR [DPaint]
Exclusive OR bitmap combine operation. Produces a white pixel if only one of the bitmaps has a white pixel at the position.

### Draw Shape As Bitmap [DPaint]
Renders a shape as a bitmap.

### Image To Bitmap [DPaint]
Converts an image into a bitmap by converting it to grayscale and applying a threshold.

### Random Number Generator [DPaint]
Utility for generating random numbers.

### Shape Center & Fit [DPaint]
Centers a shape and fits it within (0,0)-(1,1).

### Shape Combiner [DPaint]
Combines multiple shapes into a single shape.

### Shape Copycat Tool [DPaint]
Creates copies of shapes with translation, rotation and scale adjustments.

### Shape Find Bounds [DPaint]
Calculates the bounds and center of a shape. The center is calculated as the center of the bounds.

### Shape Flip [DPaint]
Flips a shape horizontally or vertically.

### Shape Grid [DPaint]
Creates a grid with scaled copies of the provided input shape.

### Shape Resize [DPaint]
Resizes/scales a shape. Scaling is either in global coordinates or shape coordinates.

### Shape Rotate [DPaint]
Rotates a shape around its own center.

### Shape of Circular Rays [DPaint]
Circular rays shape. 

### Shape of N-Polygon [DPaint]
Generates a rounded polygon with N edges. N=3 produces a triangle and a high N will look lika an ellipse.

### Shape of Rectangle [DPaint]
Generates a rectangle shape.

### Shape of Star [DPaint]
Generates a star shape.

## Examples

### Checkerboard

Very simple checkerboard generation. Not very useful on its own.

[checkerboard](examples/checkerboard.json)

### Rays of Color

Geometric pattern generation combined with a control net - very typical use of the dream painter modules.

[rays_of_color](examples/rays_of_color.json)

### Butterfly

Geometric pattern generation combined with a control net and bitmap masking.

[butterfly](examples/butterfly.json)
