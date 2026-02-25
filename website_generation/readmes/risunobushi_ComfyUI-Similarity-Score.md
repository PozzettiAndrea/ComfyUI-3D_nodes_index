# ComfyUI Image Similarity Node

A custom node for ComfyUI that calculates CLIP and LPIPS similarity scores between two images.

## Features

- CLIP similarity score (semantic similarity)
- LPIPS similarity score (perceptual similarity)
- GPU acceleration support

## Installation

Clone this repository to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/risunobushi/ComfyUI-Similarity-Score.git
cd ComfyUI/custom_nodes/ComfyUI-Similarity-Score
pip install -r requirements.txt
