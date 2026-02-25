# ComfyUI-VideoChatWrapper

Nodes related to video chat workflows

## I/O Nodes

### Load Video

load a video to comfyui input directory, and return the video path

input:

- video: The video file to be loaded

output:

- video_path: The video path

### Load Model

load a video chat model

input:

- model: The model to use for the summary

output:

- model: The model
- processor: The processor

### Video Summary

generate a text summary of the uploaded video

input:

- model: The model to use for the summary
- processor: The processor to use for the summary
- video_path: The video path

output:

- text: The summary of the video

## References

- [OpenGVLab/VideoChat-R1_7B](https://huggingface.co/OpenGVLab/VideoChat-R1_7B)
- [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
