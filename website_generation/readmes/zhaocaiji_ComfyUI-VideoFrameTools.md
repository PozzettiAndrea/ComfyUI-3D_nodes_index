# ComfyUI-VideoFrameTools

A custom node for ComfyUI to handle video frame sequences.
一个用于 ComfyUI 的自定义节点，用于处理视频帧序列。

## Features 功能
1. **Reorder Frames**: Splits the video sequence in half and swaps the order (Last half + First half). 
   (将视频帧序列对半切开并互换顺序)
2. **Frame Skipping**: Skips frames based on input interval (e.g., keep 1 frame every N frames).
   (根据输入的数值进行抽帧)

## How to Use 使用方法
- **Input**: 
  - `image_sequence`: Connect to the output of a VAE Decode or Image Load node.
  - `skip_interval`: 
    - 0 = Keep all frames.
    - 1 = Keep 1 frame every 1 frame (removes 50% frames).
    - 2 = Keep 1 frame every 2 frames.
- **Output**: 
  - `processed_images`: Connect to VideoCombine or SaveImage.

## Installation 安装
Git clone this repository into your `ComfyUI/custom_nodes/` directory.
