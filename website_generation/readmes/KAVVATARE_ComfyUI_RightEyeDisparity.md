# ComfyUI_RightEyeDisparity

A simple ComfyUI custom node for generating right eye disparity videos for VR. Generates right eye videos efficiently based on left eye video and depth maps.

## Features

- 🎬 **Video Batch Processing**: Memory-efficient design
- 👁️ **Right Eye Only Output**: Saves memory by processing only what's needed
- 🔧 **High-Quality Disparity Generation**: Uses proven algorithms from ComfyStereo
- 📹 **Workflow Integration**: Works seamlessly with Video Combine and Meta Batch nodes

## Installation

1. Clone into ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/KAVVATARE/ComfyUI_RightEyeDisparity.git
```

2. Install dependencies:
```bash
cd ComfyUI_RightEyeDisparity
pip install -r requirements.txt
```

## Usage

### Video Right Eye Disparity Node

**Inputs:**
- `images`: Left eye video frames (batch)
- `depth_maps`: Depth map for each frame
- `fill_technique`: Occlusion filling technique

**Output:**
- `images`: Generated right eye video frames

**Key Parameters:**
- `divergence` (0.05-15): Disparity strength. Higher values create stronger 3D effect
- `separation` (-5-5): Horizontal offset adjustment
- `stereo_balance` (-0.95-0.95): Left/right disparity balance
- `fill_technique`: Recommended "Fill - Polylines Soft"

### Example Workflow

1. **Load Video** → Load left eye video
2. **MiDaS Depth Map** → Generate depth maps
3. **Video Right Eye Disparity** → Generate right eye video
4. **Upscale** → Optionally upscale left/right separately
5. **Video Combine** → Save as video with Meta Batch

## Memory Optimization Tips

- Adjust batch size to control memory usage
- `direction_aware_depth_blur` is disabled for faster processing
- Depth map output is omitted to save memory

## Troubleshooting

### Out of Memory
- Process with smaller batch sizes
- Reduce resolution and upscale after processing

### Unnatural Disparity
- Adjust `divergence` between 2-5
- Check depth map quality

## License

MIT License

## Acknowledgments

This project uses `stereoimage_generation.py` from [ComfyStereo](https://github.com/Dobidop/ComfyStereo).
