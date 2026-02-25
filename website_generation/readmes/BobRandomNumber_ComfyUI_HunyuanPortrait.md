# This is an enthusiast level node pack for experimental and educational exploration

# ComfyUI_HunyuanPortrait Node Pack

This node pack integrates the [Tencent HunyuanPortrait](https://github.com/Tencent-Hunyuan/HunyuanPortrait) framework into ComfyUI. It allows users to generate portrait animations driven by a video, using a source image for appearance.

## Features

*   **Simplified Model Loading:** Uses a single folder input for main models and a dropdown for VAE selection.
*   **Local Model Loading:** All models are loaded from local paths. No automatic HuggingFace Hub downloads by the nodes.
*   **Portrait Animation:** Generates videos based on a source portrait image and a driving video.
*   **Customizable Preprocessing & Generation:** Offers various parameters to control the preprocessing and video generation stages.

![Workflow Example](https://github.com/BobRandomNumber/ComfyUI_HunyuanPortrait/blob/main/example_workflows/HunyuanPortrait.png)

## Setup

### Clone or download this repository.

### Install Dependencies

### Download Models

You need to download the model weights from the official HunyuanPortrait sources.

*   **HunyuanPortrait Models:**

    *   Go to the [HunyuanPortrait Huggingface repository](https://huggingface.co/tencent/HunyuanPortrait/tree/main).
	
    *   You need all the models downloaded into `ComfyUI/models/HunyuanPortrait/hyportrait`
	*   `unet.pth`, `dino.pth`, `expression.pth`, `headpose.pth`, `image_proj.pth`, `motion_proj.pth`, `pose_guider.pth`
	
        *   `arcface.onnx` downloaded to `ComfyUI/models/HunyuanPortrait` from https://huggingface.co/FoivosPar/Arc2Face/resolve/da2f1e9aa3954dad093213acfc9ae75a68da6ffd/arcface.onnx
        *   `yoloface_v5m.pt` downloaded to `ComfyUI/models/HunyuanPortrait` from https://huggingface.co/LeonJoe13/Sonic/resolve/main/yoloface_v5m.pt
		
*   **VAE Model:**

    *   The HunyuanPortrait project uses a Stable Video Diffusion VAE. A common one is `stabilityai/stable-video-diffusion-img2vid-xt`'s VAE.
    *   You can download it from Hugging Face: [stabilityai/stable-video-diffusion-img2vid-xt - vae/diffusion_pytorch_model.fp16.safetensors](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/main/vae/diffusion_pytorch_model.fp16.safetensors)

### Organize Models (Crucial Step)

Organize the downloaded files as follows:

1.  Create a main directory for HunyuanPortrait models within your ComfyUI models folder:
    `ComfyUI/models/HunyuanPortrait/`

2.  Inside `ComfyUI/models/HunyuanPortrait/`, place:
    *   The entire `hyportrait` folder (which you downloaded, containing the various `.pth` files).
    *   `arcface.onnx`
    *   `yoloface_v5m.pt`

3.  Place the VAE model (e.g., `diffusion_pytorch_model.fp16.safetensors`) in your standard ComfyUI VAE directory:
    `ComfyUI/models/vae/` (e.g., `ComfyUI/models/vae/diffusion_pytorch_model.fp16.safetensors`)

**The final structure should look like this:**
```
ComfyUI/
└── models/
	├── HunyuanPortrait/ <-- This is your 'model_folder' for the node
	│ ├── arcface.onnx
	│ ├── yoloface_v5m.pt
	│ └── hyportrait/ <-- folder containing dino.pth, unet.pth, etc.
	│   ├── dino.pth
	│   ├── expression.pth
	│   ├── headpose.pth
	│   ├── image_proj.pth
	│   ├── motion_proj.pth
	│   ├── pose_guider.pth
	│   └── unet.pth
	└── vae/
	  └── diffusion_pytorch_model.fp16.safetensors <-- Or your chosen VAE file
```
      
## How to Use

1.  **Load HunyuanPortrait Models:**
    *   Add the `Load HunyuanPortrait Models` node (found under the `HunyuanPortrait` category).
    *   **Model Folder:** Set this to your main HunyuanPortrait weights directory (e.g., `ComfyUI/models/HunyuanPortrait`).
    *   **VAE Name:** Select the correct VAE file (e.g., `diffusion_pytorch_model.fp16.safetensors`) from the dropdown.

2.  **Load Inputs:**
    *   Use a `LoadImage` node for the source portrait image.
    *   Use a `LoadVideo (VHS)` node or similar to load your driving video frames.

3.  **Preprocess Data:**
    *   Add the `HunyuanPortrait Preprocessor` node.
    *   Connect `hunyuan_models` from the `Load HunyuanPortrait Models` node.
    *   Connect the `source_image` from your `LoadImage` node.
    *   Connect the `driving_video_frames` from your video loading node.
    *   Set `driving_video_fps` to match the actual FPS of your input driving video.
    *   Adjust other preprocessing parameters like `limit_frames` and `output_crop_size` as needed.

4.  **Generate Video:**
    *   Add the `HunyuanPortrait Generator` node.
    *   Connect `hunyuan_models` from the `Load HunyuanPortrait Models` node.
    *   Connect `preprocessed_data` from the `HunyuanPortrait Preprocessor` node.
    *   Connect `driving_data` output from the `HunyuanPortrait Preprocessor` to the `driving_data` input of the `HunyuanPortrait Generator`. This carries information about the temporary video file for cleanup.
    *   Adjust generation parameters such as `height`, `width`, `num_inference_steps`, `fps_generation` (FPS of the output video), guidance scales, etc.

5.  **Preview/Save Output:**
    *   Connect the `IMAGE` output of the `HunyuanPortrait Generator` to a `PreviewImage` node to see individual generated frames.
    *   Alternatively, connect it to a `VideoCombine (VHS)` node to assemble the frames into a video file (e.g., MP4, GIF). Ensure the `frame_rate` in `VideoCombine` matches your `fps_generation` setting in the Generator for correct playback speed.

## Notes
*   **Use a color match node to restore color levels as outputs are messy**
*   **Dependency Version:** It is crucial to use `diffusers==0.29.0` as specified in `requirements.txt`. Newer versions of `diffusers` may have breaking API changes that are incompatible with the vendored code in this node pack.
