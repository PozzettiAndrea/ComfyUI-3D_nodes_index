# ComfyUI-PJLatent

A simple ComfyUI custom node that generates empty latents based on aspect ratio and a user-defined longest side.

## Features

- **Aspect Ratio Selection**: choose from common ratios like `1:1`, `16:9`, `4:3`, etc.
- **Longest Side Control**: define the size of the longest dimension (e.g., 1024, 1536). The other dimension is automatically calculated.
- **Auto-rounding**: calculates dimensions to be divisible by 8, ensuring compatibility with SD/Flux models.

## Installation

1.  Clone or download this repository into your `ComfyUI/custom_nodes/` folder:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/yourusername/ComfyUI-PJLatent.git
    ```
2.  Restart ComfyUI.

## Usage

1.  Right-click on the graph canvas.
2.  Navigate to `Add Node > PJ_Nodes > Latent > PJ Latent Generator`.
3.  Connect the `LATENT` output to a Sampler or other nodes requiring latent input.
4.  (Optional) Use the `width` and `height` outputs to drive other nodes (e.g., Image Resize, calculations).

### PJ Video Latent Generator
This node is similar to the standard generator but adds a `length` input for video frames.

- **Inputs**:
    - `aspect_ratio`: Select from common ratios.
    - `longest_side`: Set the pixel size of the longest dimension.
    - `duration_seconds`: Video length in seconds (converted to frames: seconds * 16 + 1).
    - `batch_size`: Number of video batches (default 1).
- **Outputs**:
    - `LATENT`: The generated empty latent (16 channels, Hunyuan/Wan compatible).
    - `width`, `height`, `length`, `batch_size`: Integer outputs.

