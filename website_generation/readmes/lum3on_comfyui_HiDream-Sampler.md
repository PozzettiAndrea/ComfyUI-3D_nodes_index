## [comfyanonymous](https://github.com/comfyanonymous/ComfyUI/commit/9ad792f92706e2179c58b2e5348164acafa69288) is now supporting HiDream natively, so I will focus on improving the HiDream Advanced Node and abandon the dependency of diffusers soon(TM).

In the meanwhile update your comfy and you can test the model with less struggle you might have installing this node ;) 
You need their official [HiDream Model](https://huggingface.co/city96/HiDream-I1-Dev-gguf/tree/main) and the four [text encoders](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/text_encoders).
Sample Workflow is in the Workflow folder

## Announcement

We have now a bunch of forks for this, and with [SanDiegoDude/ComfyUI-HiDream-Sampler](https://github.com/SanDiegoDude/ComfyUI-HiDream-Sampler/) actively maintaining, feel free to check out his awsome work, which might solve some issues.

I will have a bit of time over easter to work on the node, but it will be updated at my pace and capabilities.

If anyone would like to contribute, I'd LOVE you to reach out or do PRs, as I am not able to solve all the issues alone (Used to be an [illustrator](https://benjaminbertram.com/) not a dev by trade :D )

What is on my list and where you could support me:

- [ ] **Edit capabilites:** Integrate [editing capabilities](https://github.com/HiDream-ai/HiDream-E1)
- [ ] **GGUF Support:** Integrate [Calcuis Model](https://huggingface.co/calcuis/hidream-gguf/tree/main)
- [ ] **Local Checkpoints:** Get rid of hugging face download logic
- [ ] **Bat installer:** For the standalone/ windows/ portable users of ComfyUI
- [ ] **Make installation overall easier:** currently many users have problems with the installation process. Meanwhile try to follow this [video](https://www.youtube.com/watch?v=KRnJCLdgdRE) to get you going. 
- [ ] **Multi Image for Img2img:** multi in, multi out
- [ ] **Better uncensored LLM:** LLM which does not OOM, so if you have suggestions
- [ ] **Manual attention checker:** At least for the advance mode, choose between sage, sdpa or flash manually
- [ ] **Beautifiy codebase:** Currently a lot of repetition and thus prone to errors
- [ ] **Cancel generation:** Currently generation can't be cancelled with the stop button
- [ ] **System Prompt presets:** Explore good working system prompts for various use cases
- [ ] **Clean up UI:** Clearer naming, tooltips for inputs and rearrange the fields for faster work
- [ ] **Explore Lora:** While the first Loras for HiDream are being explored it would be good to know how to implement them without big performance losses
- [ ] **Explore HiResFix Capabilites via Img2img:** Dig into HiResFix to have a propper Upscale via native HiDream

## Updates 14.04.

- fixed uncensored llm support
- fixed pipelines
- fixed image output
- fixed cache overload
- Added multi image generation (up to 8) (Img2img not yet supported!)
- Fixed Sageattention fetch as first attention method.
- Fixed according to [burgstall](https://github.com/Burgstall-labs): Not require auto-gptq anymore! Make sure to git pull and pip install -r requirements.txt! 
- Added Image2image functionality
- Flash Attention is no longer needed thanks to [power88](https://github.com/power88)
- added working uncensored Llama Support (Available via HiDream Sampler Advanced) thanks to [sdujack2012](https://github.com/sdujack2012) but beware its not quantified so you could get an OOM

![image](sample_workflow/workflow.png)

# HiDreamSampler for ComfyUI

A custom ComfyUI node for generating images using the HiDream AI model.

## Features
- Supports `full`, `dev`, and `fast` model types.
- Configurable resolution and inference steps.
- Uses 4-bit quantization for lower memory usage.

## Installation
### Basic installation.
1. Clone this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   git clone https://github.com/lum3on/comfyui_HiDream-Sampler ComfyUI/custom_nodes/comfyui_HiDream-Sampler
   ```

2. Install requirements
    ```bash
    pip install -r requirements.txt
    ```
    or for the portable version:
   ```bash
   .\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\comfyui_HiDream-Sampler\requirements.txt
   ```
   
4. Restart ComfyUI.

Steps to install SageAttention 1:
- Install triton.
Windows built wheel, [download here](https://huggingface.co/madbuda/triton-windows-builds):
```bash
.\python_embeded\python.exe -s -m pip install (Your downloaded whl package)
```
linux:
```bash
python3 -m pip install triton
```

- Install sageattention package
```bash
.\python_embeded\python.exe -s -m pip install sageattention==1.0.6
```
PyTorch SDPA is automantically installed when you install PyTorch 2 (ComfyUI Requirement). However, if your torch version is lower than 2. Use this command to update to the latest version.
- linux
```
python3 -m pip install torch torchvision torchaudio
```
- windows
```
.\python_embeded\python.exe -s -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

## Download the weights
Here's some weight that you need to download (Which will be automantically downloaded when running workflow). Please use huggingface-cli to download.
- Llama Text Encoder

| Model | Huggingface repo | 
|------------------------|---------------------------|
| 4-bit Llama text encoder       | hugging-quants/Meta-Llama-3.1-8B-Instruct-GPTQ-INT4  | 
| Uncensored 4-bit Llama text encoder      | John6666/Llama-3.1-8B-Lexi-Uncensored-V2-nf4  | 
| Original Llama text encoder       | nvidia/Llama-3.1-Nemotron-Nano-8B-v1  | 

- Quantized Diffusion models (Thanks to `azaneko` for the quantized model!)

| Model | Huggingface repo | 
|------------------------|---------------------------|
| 4-bit HiDream Full       | azaneko/HiDream-I1-Full-nf4  | 
| 4-bit HiDream Dev       | azaneko/HiDream-I1-Dev-nf4  | 
| 4-bit HiDream Fast       | azaneko/HiDream-I1-Fast-nf4  | 

- Full weight diffusion model (optional, not recommend unless you have high VRAM)

| Model | Huggingface repo | 
|------------------------|---------------------------|
| HiDream Full       | HiDream-ai/HiDream-I1-Full  | 
| HiDream Dev       | HiDream-ai/HiDream-I1-Dev  | 
| HiDream Fast       | HiDream-ai/HiDream-I1-Fast  | 

You can download these weights by this command.
```shell
huggingface-cli download (Huggingface repo)
```
For some region that cannot connect to huggingface. Use this command for mirror.

Windows CMD
```shell
set HF_ENDPOINT=https://hf-mirror.com
```
Windows Powershell
```shell
$env:HF_ENDPOINT = "https://hf-mirror.com"
```
Linux
```shell
export HF_ENDPOINT=https://hf-mirror.com
```

## Usage
- Add the HiDreamSampler node to your workflow.
- Configure inputs:
    model_type: Choose full, dev, or fast.
    prompt: Enter your text prompt (e.g., "A photo of an astronaut riding a horse on the moon").
    resolution: Select from available options (e.g., "1024 × 1024 (Square)").
    seed: Set a random seed.
    override_steps and override_cfg: Optionally override default steps and guidance scale.
- Connect the output to a PreviewImage or SaveImage node.

## Requirements
- ComfyUI
- GPU (for model inference)
- Models are cached after the first load to improve performance and use 4-bit quantization models from https://github.com/hykilpikonna/HiDream-I1-nf4.
- Ensure you have sufficient VRAM (e.g., 16GB+ recommended for full mode).

## Credits

Merged with [SanDiegoDude/ComfyUI-HiDream-Sampler](https://github.com/SanDiegoDude/ComfyUI-HiDream-Sampler/) who implemented a cleaner version for my originial NF4 / fp8 support.

- Added NF4 (Full/Dev/Fast) download and load support
- Added better memory handling
- Added more informative CLI output for TQDM
- Full/Dev/Fast requires roughly 27GB VRAM
- NF4 requires roughly 15GB VRAM

Build upon the original [HiDream-I1]https://github.com/HiDream-ai/HiDream-I1

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=lum3on/comfyui_HiDream-Sampler&type=Date)](https://www.star-history.com/#lum3on/comfyui_HiDream-Sampler&Date)
