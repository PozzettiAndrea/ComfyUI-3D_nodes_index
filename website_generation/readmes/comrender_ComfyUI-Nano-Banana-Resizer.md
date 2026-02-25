# ComfyUI-Nano-Banana-Resizer

A ComfyUI custom node that automatically calculates optimal output dimensions for Google's Nano Banana image editing model. 
Why its needed? To achiev exact sizes outputs without shifting/cropping original image.

## Updates
21112025 Added Support for Nano Banana II with 1K,2K,4K resolution.

## What it does

Nano Banana requires specific input dimensions (~1MP, divisible by 32) and uses aspect ratio bucketing. This node:

- Takes any input image size
- Automatically detects aspect ratio and orientation
- Calculates the correct output dimensions (width & height)
- Supports 22 aspect ratio buckets from 1:4 to 4:1

## Why you need it

Without proper resizing, your images may be unexpectedly cropped or distorted by the model. This node ensures your input images are stretched to the exact dimensions Nano Banana expects, preserving all content without cropping.

## Usage

1. Connect your image to the node
2. Use the width/height outputs to resize your image before sending to Nano Banana
3. No configuration needed - it just works!

## Supported Aspect Ratios


1:4, 1:3, 1:2, 9:16, 5:8, 2:3, 3:4, 7:9, 5:6, 1:1, 4:3, 3:2, 8:5, 16:9, 2:1, 3:1, 4:1 and everything in between.


