# ComfyUI-OmniGen2

ComfyUI-OmniGen2 is now available in ComfyUI, [OmniGen2](https://github.com/VectorSpaceLab/OmniGen2) is a powerful and efficient unified multimodal model. Its architecture is composed of two key components: a 3B Vision-Language Model (VLM) and a 4B diffusion model.



## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-OmniGen2.git
```


## Environment Setup

#### ✅ Recommended Setup

```bash
# 1. Environment
cd ComfyUI-OmniGen2

# 2. (Optional) Create a clean Python environment
conda create -n omnigen2 python=3.11
conda activate omnigen2

# 3. Install dependencies
# 3.1 Install PyTorch (choose correct CUDA version)
pip install torch==2.6.0 torchvision --extra-index-url https://download.pytorch.org/whl/cu124

# 3.2 Install other required packages
pip install -r requirements.txt

# Note: Version 2.7.4.post1 is specified for compatibility with CUDA 12.4.
# Feel free to use a newer version if you use CUDA 12.6 or they fixed this compatibility issue.
pip install flash-attn==2.7.4.post1 --no-build-isolation
```

#### 🌏 For users in Mainland China

```bash
# Install PyTorch from a domestic mirror
pip install torch==2.6.0 torchvision --index-url https://mirror.sjtu.edu.cn/pytorch-wheels/cu124

# Install other dependencies from Tsinghua mirror
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Note: Version 2.7.4.post1 is specified for compatibility with CUDA 12.4.
# Feel free to use a newer version if you use CUDA 12.6 or they fixed this compatibility issue.
pip install flash-attn==2.7.4.post1 --no-build-isolation -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---


## Model


### Download Pretrained Models

**OmniGen2**, a multimodal generation model, model weights can be accessed in [huggingface](https://huggingface.co/OmniGen2/OmniGen2) and [modelscope](https://www.modelscope.cn/models/OmniGen2/OmniGen2).



## 💡 Usage Tips

To achieve optimal results with OmniGen2, you can adjust the following key hyperparameters based on your specific use case.
- `text_guidance_scale`: Controls how strictly the output adheres to the text prompt (Classifier-Free Guidance).
- `image_guidance_scale`: This controls how much the final image should resemble the input reference image.
    - **The Trade-off**: A higher value makes the output more faithful to the reference image's structure and style, but it might ignore parts of your text prompt. A lower value (~1.5) gives the text prompt more influence.
    - **Tip**: For image editing task, we recommend to set it between 1.2 and 2.0; for in-context generateion task, a higher image_guidance_scale will maintian more details in input images, and we recommend to set it between 2.5 and 3.0.
- `max_pixels`: Automatically resizes images when their total pixel count (width × height) exceeds this limit, while maintaining its aspect ratio. This helps manage performance and memory usage.
  - **Tip**: Default value is 1024*1024. You can reduce this value if you encounter memory issues.
- `max_input_image_side_length`: Maximum side length for input images.
- `negative_prompt`: Tell the model what you don't want to see in the image.
    - **Example**: blurry, low quality, text, watermark
    - **Tip**: For the best results, try experimenting with different negative prompts. If you're not sure, just use the default negative prompt.
- `enable_model_cpu_offload`: **Reduces VRAM usage by nearly 50% with a negligible impact on speed**.
  - This is achieved by offloading the model weights to CPU RAM when they are not in use.
  - See: [Model Offloading](https://huggingface.co/docs/diffusers/optimization/memory#model-offloading)
- `enable_sequential_cpu_offload`: Minimizes VRAM usage to less than 3GB, but at the cost of significantly slower performance.
  - This works by offloading the model in submodules and loading them onto the GPU sequentially as needed.
  - See: [CPU Offloading](https://huggingface.co/docs/diffusers/optimization/memory#cpu-offloading)

**Some suggestions for improving generation quality:**
- Use high-resolution and high-quality images. Images that are too small or blurry will also result in low-quality output. We recommend ensuring that the input image size is greater than 512 whenever possible.
- Provide detailed instructions. For in-context generation tasks, specify which elements from which image the model should use.
- Try to use English as much as possible, as OmniGen2 currently performs better in English than in Chinese.

