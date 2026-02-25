# Skin Tone Detector for ComfyUI

A ComfyUI node that detects the skin tone of a person in an image and matches it to the standard emoji skin tone palette.

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes` directory:
 clone https://github.com/yourusername/skin-tone-detector custom_nodes/SkinToneDetector

2. Install requirements:
 install -r custom_nodes/SkinToneDetector/requirements.txt

## Usage

The node accepts an image input and returns one of five skin tone values:
- LIGHT
- MEDIUM_LIGHT
- MEDIUM
- MEDIUM_DARK
- DARK

## Implementation Details

The node uses facial recognition to identify skin regions and color space analysis to match the detected skin tone to the closest emoji skin tone value.
