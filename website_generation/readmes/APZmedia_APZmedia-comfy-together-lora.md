# APZmedia Together Image Generator for ComfyUI
A ComfyUI node to implement Together AI API image generation 

## Overview
This ComfyUI custom node integrates with the Together API to generate images from text prompts. It (should) support LoRA models.[Work in progress]

## Features
- Generate images via the Together API.
- Supports LoRA models via external URLs.
- Adjustable width, height, and step count.

## Installation
1. Install dependencies:
pip install -r requirements.txt

2. Restart ComfyUI and use the node.

## Usage
- Input a prompt and model.
- (Optional) Provide LoRA URLs and scales.
- Generates an image for use in ComfyUI workflows.
