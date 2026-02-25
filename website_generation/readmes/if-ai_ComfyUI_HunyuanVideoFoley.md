# ComfyUI HunyuanVideo-Foley Custom Node

This is a ComfyUI custom node wrapper for the HunyuanVideo-Foley model, which generates realistic audio from video and text descriptions.

## Features

- **Text-Video-to-Audio Synthesis**: Generate realistic audio that matches your video content
- **Flexible Text Prompts**: Use optional text descriptions to guide audio generation
- **Multiple Samples**: Generate up to 6 different audio variations per inference
- **Configurable Parameters**: Control guidance scale, inference steps, and sampling
- **Seed Control**: Reproducible results with seed parameter
- **Model Caching**: Efficient model loading and reuse across generations
- **Automatic Model Downloads**: Models are automatically downloaded to `ComfyUI/models/foley/` when needed
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/cace6b70-0eb7-4eda-a4f5-c21c95559b38" />


## Features

- **Text-Video-to-Audio Synthesis**: Generate realistic audio that matches your video content
- **Flexible Text Prompts**: Use optional text descriptions to guide audio generation
- **Multiple Samples**: Generate up to 6 different audio variations per inference
- **Configurable Parameters**: Control guidance scale, inference steps, and sampling
- **Seed Control**: Reproducible results with seed parameter
- **Model Caching**: Efficient model loading and reuse across generations
- **Automatic Model Downloads**: Models are automatically downloaded to `ComfyUI/models/foley/` when needed

## Installation

1. **Clone this repository** into your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/if-ai/ComfyUI_HunyuanVideoFoley.git
   ```

2. **Install dependencies**:
   ```bash
   cd ComfyUI_HunyuanVideoFoley
   pip install -r requirements.txt
   ```

3. **Run the installation script** (recommended):
   ```bash
   python install.py
   ```

4. **Restart ComfyUI** to load the new nodes.

### Model Setup

The models can be obtained in two ways:

#### Option 1: Automatic Download (Recommended)
- Models will be automatically downloaded to `ComfyUI/models/foley/` when you first run the node
- No manual setup required
- Progress will be shown in the ComfyUI console

#### Option 2: Manual Download
- Download models from [HuggingFace](https://huggingface.co/tencent/HunyuanVideo-Foley)
- Place models in `ComfyUI/models/foley/` (recommended) or `./pretrained_models/` directory
- Ensure the config file is at `configs/hunyuanvideo-foley-xxl.yaml`

## Operation Guide: How to Use the Nodes

This custom node package is designed in a modular way for maximum flexibility and efficiency. Here is the recommended workflow and an explanation of what each node does.

### Recommended Workflow

The most powerful and efficient way to use these nodes is to chain them together in the following order:

`Model Loader` → `Dependencies Loader` → `Torch Compile` → `Generator (Advanced)`

This setup allows you to load the models only once, apply performance optimizations, and then run the generator multiple times without reloading, saving significant time and VRAM.

### Node Details

#### 1. HunyuanVideo-Foley Model Loader (FP8)
This is the starting point. It loads the main (and very large) audio generation model into memory.

-   **quantization**: This is the most important setting for saving VRAM.
    -   `none`: Loads the model in its original format (highest VRAM usage).
    -   `fp8_e5m2` / `fp8_e4m3fn`: These options use **FP8 quantization**, a technique that stores the model's weights in a much smaller format. This can save several gigabytes of VRAM with a minimal impact on audio quality, making it possible to run on GPUs with less memory.
-   **cpu_offload**: If `True`, the model will be kept in your regular RAM instead of VRAM. This is not the same as the generator's offload setting; use this if you are loading multiple different models in your workflow and need to conserve VRAM.

#### 2. HunyuanVideo-Foley Dependencies
This node takes the main model from the loader and then loads all the smaller, auxiliary models required for the process (the VAE, text encoder, and visual feature extractors).

#### 3. HunyuanVideo-Foley Torch Compile
This is an optional but highly recommended performance-enhancing node. It uses `torch.compile` to optimize the model's code for your specific hardware.
-   **Note**: The very first time you run a workflow with this node, it will take a minute or two to perform the compilation. However, every subsequent run will be significantly faster (often 20-30%).

-   **`compile_mode`**: This controls the trade-off between compilation time and the amount of performance gain.
    -   `default`: The best balance. It provides a good speedup with a reasonable initial compile time.
    -   `reduce-overhead`: Compiles more slowly but can reduce the overhead of running the model, which might be faster for very small audio generations.
    -   `max-autotune`: Takes the longest to compile initially, but it tries many different optimizations to find the absolute fastest option for your specific hardware.

-   **`backend`**: This is an advanced setting that changes the underlying compiler used by PyTorch. For most users, the default `inductor` is the best choice.

#### 4. HunyuanVideo-Foley Generator (Advanced)
This is the main workhorse node where the audio generation happens.

-   **video / images**: Your visual input. You can provide either a video file or a batch of images from another node.
-   **compiled_model**: The input for the model prepared by the upstream nodes.
-   **text_prompt / negative_prompt**: Your descriptions of the sound you want (and don't want).
-   **guidance_scale / num_inference_steps / seed**: Standard diffusion model controls for creativity vs. prompt adherence, quality vs. speed, and reproducibility.
-   **enabled**: A simple switch. If `False`, the node does nothing and passes through an empty/silent output. This is useful for disabling parts of a complex workflow without having to disconnect them.
-   **silent_audio**: Controls what happens when the node is disabled or fails. If `True`, it outputs a valid, silent audio clip, which prevents downstream nodes (like video combiners) from failing. If `False`, it outputs `None`.

### Understanding the Memory Options

The two memory-related checkboxes on the Generator node are crucial for managing your GPU's resources. Here is exactly what they do:

-   **`cpu_offload`**:
    -   **What it does:** If this is `True`, the node will always move the models to your regular RAM (CPU) after the generation is complete. This is the best option for freeing up VRAM for other nodes in your workflow while still keeping the models ready for the next run without having to reload them from disk.
    -   **Use this when:** You want to run other VRAM-intensive nodes after this one and plan to come back to the Foley generator later.

-   **`memory_efficient`**:
    -   **What it does:** This is a more aggressive option. If `True`, the node will completely unload the models from memory (both VRAM and RAM) after the generation is finished.
    -   **Important Distinction:** This process is smart. It will **only** unload the model if it was loaded by the generator node itself (the simple workflow). If the model was passed in from the `HunyuanVideoFoleyModelLoader` (the advanced workflow), it will **not** unload it, respecting the fact that you may want to reuse the pre-loaded model for another generation.
    -   **Use this when:** You are finished with audio generation and want to free up as much memory as possible for completely different tasks.

### Performance Tuning & VRAM Usage

The most memory-intensive part of the process is visual feature extraction. We've implemented batched processing to prevent out-of-memory errors with longer videos or on GPUs with less VRAM. You can control this with two settings on the **Generator (Advanced)** node:

-   **`feature_extraction_batch_size`**: This determines how many video frames are processed by the feature extractor models at once.
    -   **Lower values** significantly reduce peak VRAM usage at the cost of slightly slower processing.
    -   **Higher values** speed up processing but require more VRAM.

-   **`enable_profiling`**: If you check this box, the node will print detailed performance timings and peak VRAM usage for the feature extraction step to the console. This is highly recommended for finding the optimal batch size for your specific hardware.

#### Recommended Batch Sizes

These are general starting points. The optimal value can vary based on your exact GPU, driver version, and other running processes.

| VRAM Tier | Video Resolution | Recommended Batch Size | Notes |
| :--- | :--- | :--- | :--- |
| **≤ 8 GB** | 480p | 4 - 8 | Start with 4. If successful, you can try increasing it. |
| | 720p | 2 - 4 | Start with 2. 720p videos are demanding on low VRAM cards. |
| **12-16 GB** | 480p | 16 - 32 | The default of 16 should work well. Can be increased for more speed. |
| | 720p | 8 - 16 | Start with 8 or 16. |
| **≥ 24 GB**| 480p | 32 - 64 | You can safely increase the batch size for maximum performance. |
| | 720p | 16 - 32 | A batch size of 32 should be easily achievable. |

## Usage

### Node Types

#### 1. HunyuanVideo-Foley Generator
Main node for generating audio from video and text.

**Inputs:**
- **video**: Video input (VIDEO type)
- **text_prompt**: Text description of desired audio (STRING)
- **guidance_scale**: CFG scale for generation control (1.0-10.0, default: 4.5)
- **num_inference_steps**: Number of denoising steps (10-100, default: 50)
- **sample_nums**: Number of audio samples to generate (1-6, default: 1)
- **seed**: Random seed for reproducibility (INT)
- **model_path**: Path to pretrained models (optional, leave empty for auto-download)
- **enabled**: Enable or disable the entire node. If disabled, it will pass through a silent or null audio output without processing. (BOOLEAN, default: True)
- **silent_audio**: Controls the output when the node is disabled or fails. If true, it outputs a silent audio clip. If false, it outputs `None`. (BOOLEAN, default: True)

**Outputs:**
- **video_with_audio**: Video with generated audio merged (VIDEO)
- **audio_only**: Generated audio file (AUDIO) 
- **status_message**: Generation status and info (STRING)

## ⚠ Important Limitations

### **Frame Count & Duration Limits**
- **Maximum Frames**: 450 frames (hard limit)
- **Maximum Duration**: 15 seconds at 30fps
- **Recommended**: Keep videos ≤15 seconds for best results

### **FPS Recommendations**
- **30fps**: Max 15 seconds (450 frames)
- **24fps**: Max 18.75 seconds (450 frames)  
- **15fps**: Max 30 seconds (450 frames)

### **Long Video Solutions**
For videos longer than 15 seconds:
1. **Reduce FPS**: Lower FPS allows longer duration within frame limit
2. **Segment Processing**: Split long videos into 15s segments
3. **Audio Merging**: Combine generated audio segments in post-processing


## Example Workflow

1. **Load Video**: Use a "Load Video" node to input your video file
2. **Add Generator**: Add the "HunyuanVideo-Foley Generator" node
3. **Connect Video**: Connect the video output to the generator's video input
4. **Set Prompt**: Enter a text description (e.g., "A person walks on frozen ice")
5. **Adjust Settings**: Configure guidance scale, steps, and sample count as needed
6. **Generate**: Run the workflow to generate audio

## Model Requirements

The node expects the following model structure:
```
ComfyUI\models\foley\hunyuanvideo-foley-xxl
├── hunyuanvideo_foley.pth          # Main Foley model
├── vae_128d_48k.pth                # DAC VAE model  
└── synchformer_state_dict.pth      # Synchformer model

configs/
└── hunyuanvideo-foley-xxl.yaml     # Configuration file
```

## TODO
- [x] ADD VHS INPUT/OUTPUTS (Thanks to YC)
- [x] NEGATIVE PROMPT (Thanks to YC)  
- [x] MODEL OFFLOADING OPS
- [x] TORCH COMPILE
- [ ] QUANTISE MODEL


## Support

If you find this tool useful, please consider supporting my work by:

- Starring this repository on GitHub
- Subscribing to my YouTube channel: [Impact Frames](https://youtube.com/@impactframes?si=DrBu3tOAC2-YbEvc)
- Following on X: [@ImpactFrames](https://x.com/ImpactFramesX)

You can also support by reporting issues or suggesting features. Your contributions help me bring updates and improvements to the project.



## License

This custom node is based on the HunyuanVideo-Foley project. Please check the original project's license terms.

## Credits

Based on the HunyuanVideo-Foley project by Tencent. Original paper and code available at:
- Paper: [HunyuanVideo-Foley: Text-Video-to-Audio Synthesis]

- Code: [https://github.com/tencent/HunyuanVideo-Foley]

<img src="https://count.getloli.com/get/@IFAI_HyVideoFoley?theme=moebooru" alt=":IFAIloadImages_comfy" />




