# Deep Live Cam for ComfyUI

This node integrates the face-swapping capabilities from Deep Live Cam into ComfyUI, allowing you to perform real-time face swapping on images and video streams.

## Features

- Real-time face swapping on images or video streams
- Option to process multiple faces in the same frame
- Mouth masking to preserve mouth movements from the original image/video
- Support for GPU acceleration through various ONNX Runtime execution providers
- Easy integration with existing ComfyUI workflows

## Usage

1. Ensure you have a valid source image containing a face
2. Add the "Deep Live Cam Face Swap" node to your workflow
3. Connect an image source to the "image" input
4. Provide the path to your source face image
5. Select appropriate execution provider for your hardware
6. Configure options as needed
7. Connect the output to your desired destination node

## Parameters

- **image**: The input image/frame (can be from a video stream)
- **source_image_path**: Path to the source face image (the face to swap onto the image/stream)
- **execution_provider**: Hardware acceleration option (CUDA for NVIDIA GPUs, ROCm for AMD GPUs, etc.)
- **many_faces**: Process all detected faces in the frame (instead of just the first one)
- **mouth_mask**: Preserve the original mouth movements by masking the mouth area

## Example Workflow

A basic workflow would look like:

1. Image/Video Source
2. → Deep Live Cam Face Swap
3. → Display/Output

For use with ComfyStream:
1. Stream Source (webcam, video file, etc.)
2. → Deep Live Cam Face Swap
3. → Stream Output/Display

## Requirements

This node requires the Deep Live Cam models. The first time you run the node, it will automatically download the required model files.

## Tested Versions

This node has been tested with the following versions:
- PyTorch 2.5.1+cu118 (NVIDIA GPU)
- PyTorch 2.5.1 (CPU/Mac)
- torchvision 0.20.1

## Performance Tips

- For best performance, select the appropriate execution provider:
  - **CUDA**: For NVIDIA GPUs
  - **ROCm**: For AMD GPUs
  - **DirectML**: For Windows DirectX-compatible GPUs
  - **CPU**: For systems without GPU acceleration
- Processing multiple faces will be more demanding on resources
- Consider using a lower resolution for smoother performance

## Troubleshooting

- If no face is detected, the original frame will be returned unchanged
- If you encounter issues with a particular execution provider, try falling back to CPU
- Check the logs for detailed error information if you encounter issues 

## Credits

This ComfyUI node is based on the [Deep Live Cam](https://github.com/hacksider/Deep-Live-Cam) project by [hacksider](https://github.com/hacksider). The core face swapping functionality and models are from the original repository. This implementation adapts the technology for use within ComfyUI workflows. 