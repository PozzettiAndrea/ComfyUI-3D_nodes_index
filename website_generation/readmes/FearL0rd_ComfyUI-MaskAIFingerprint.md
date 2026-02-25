# ComfyUI MaskAIFingerprint

Attempt to create a ComfyUI node for masking AI-generated fingerprints.
Still need improvement
License: Apache License Version 2.0
## Features

- Accepts an input image
- Outputs basic information about the image masked

## Installation

### Installation
1. Locate your ComfyUI custom nodes directory (usually at `ComfyUI/custom_nodes/`)
2. Clone this project in that directory:

## Dependencies Management

torch, torchvision, PIL, io and numpy

## Usage

1. Start ComfyUI
2. Find "MaskAIFingerprint" node in the node list
3. Connect an image node to the Image Info node's input
4. Run the workflow to see the image information
