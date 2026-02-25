# ComfyUI Smart Color Match (Masked)

A custom node for ComfyUI that performs color matching between a reference image and a generated image, with support for masking.

## Features

- **Mask Support**: Can ignore specific areas (like clothes) when calculating color statistics, ensuring the background color tone matches the reference perfectly while preserving the subject.
- **Algorithms**:
  - `mkl_neutral`: Only adjusts mean (White Balance), very stable.
  - `reinhard_lab`: Adjusts mean and standard deviation in LAB color space (A/B channels only).
- **Blend Factor**: Adjust the intensity of the color correction.

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/YOUR_USERNAME/ComfyUI-Smart-Color-Match.git
   ```
