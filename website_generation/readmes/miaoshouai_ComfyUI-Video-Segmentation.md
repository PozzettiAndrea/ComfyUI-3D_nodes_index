# ComfyUI Video Segmentation Node

A ComfyUI custom node for automatic video scene segmentation using TransNetV2.

## Description

This node segments videos into individual scenes automatically using the TransNetV2 deep learning model. TransNetV2 is a state-of-the-art neural network for shot boundary detection in videos.

## Features

- Automatic scene detection and segmentation
- Uses TransNetV2 for accurate shot boundary detection
- Fallback to OpenCV-based scene detection when TransNetV2 is unavailable
- Configurable scene detection parameters
- Outputs individual video segments

## Installation

1. Clone or download this repository to your ComfyUI custom_nodes directory:
   ```
   D:\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-Video-Segmentation\
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg (required for video processing):
   - **Windows**: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
   - **Linux**: `sudo apt-get install ffmpeg`
   - **macOS**: `brew install ffmpeg`

4. Download TransNetV2 model weights (for best performance):
   - Download the `transnetv2-weights` directory from [TransNetV2 repository](https://github.com/soCzech/TransNetV2/tree/master/inference/transnetv2-weights)
   - Place it in the node directory or your preferred model directory

5. Alternative TransNetV2 installation:
   ```bash
   pip install transnetv2
   ```

6. Restart ComfyUI

## Usage

### Inputs

- **video**: Path to the input video file (STRING)
- **output_dir**: Directory where segmented videos will be saved (STRING)
- **min_scene_length**: Minimum scene length in frames (INT, default: 30)
- **threshold**: Scene detection threshold (FLOAT, default: 0.5)

### Outputs

- **output_directory**: Path to the directory containing segmented videos (STRING)
- **num_segments**: Number of video segments created (INT)
- **segment_paths**: List of paths to individual segment files (LIST)

### Example Workflow

1. Add the "Video Segmentation" node to your ComfyUI workflow
2. Set the input video path
3. Specify the output directory (optional - defaults to ComfyUI output directory)
4. Adjust min_scene_length and threshold as needed
5. Run the workflow

## Dependencies

### Required
- ComfyUI
- Python 3.8+
- PyTorch
- NumPy
- PIL (Pillow)

### Optional (for better performance)
- TransNetV2: `pip install transnetv2`
- OpenCV: `pip install opencv-python` (used as fallback)
- FFmpeg (for video segment creation)

## Technical Details

### TransNetV2 Integration

The node first attempts to use TransNetV2 for scene detection. TransNetV2 is a neural network specifically designed for shot boundary detection and provides superior accuracy compared to traditional methods.

### Fallback Method

If TransNetV2 is not available, the node falls back to an OpenCV-based scene detection algorithm that:
1. Analyzes frame-to-frame differences
2. Identifies sudden changes in visual content
3. Segments the video based on detected boundaries

### Output Format

- Segmented videos are saved as MP4 files
- Files are named sequentially: `segment_000.mp4`, `segment_001.mp4`, etc.
- Original video quality and codec are preserved when possible

## Configuration

### Scene Detection Parameters

- **min_scene_length**: Controls the minimum duration of detected scenes. Shorter scenes are merged with adjacent ones.
- **threshold**: Controls the sensitivity of scene detection. Lower values detect more scene changes, higher values are more conservative.

## Troubleshooting

### TransNetV2 Not Found
If you see errors about TransNetV2 not being found:
1. Install TransNetV2: `pip install transnetv2`
2. Or ensure the TransNetV2 source code is available in your project

### FFmpeg Not Found
For video segmentation, FFmpeg is required:
1. Install FFmpeg and ensure it's in your system PATH
2. Or install via conda: `conda install ffmpeg`

### Permission Errors
Ensure the output directory is writable and you have sufficient disk space for the segmented videos.

## References

- [TransNetV2 Paper](https://arxiv.org/abs/2008.04838)
- [TransNetV2 GitHub Repository](https://github.com/soCzech/TransNetV2)
- [ComfyUI Documentation](https://github.com/comfyanonymous/ComfyUI)

## License

This project is licensed under the same terms as ComfyUI. Please refer to the original TransNetV2 license for the underlying model.