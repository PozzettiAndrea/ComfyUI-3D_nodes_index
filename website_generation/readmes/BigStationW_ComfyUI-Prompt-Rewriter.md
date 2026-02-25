# ComfyUI Prompt Rewriter

This is a custom fork of [this repository](https://github.com/FranckyB/ComfyUI-Prompt-Manager) incorporating [some enhancements](https://github.com/FranckyB/ComfyUI-Prompt-Manager/pull/3).

## Use case
This node can rewrite your prompts with the help of a chosen instruct (or thinking) LLM/VLM (GGUF).

<img width="700" alt="AA" src="https://github.com/user-attachments/assets/c2b4de17-0121-4f9f-a845-3c0c52f74bce" />

## Installation

1) Navigate to the **ComfyUI/custom_nodes** folder, [open cmd](https://www.youtube.com/watch?v=bgSSJQolR0E&t=47s) and run:

```
git clone https://github.com/BigStationW/ComfyUI-Prompt-Rewriter
```
2) Navigate to the **ComfyUI\custom_nodes\ComfyUI-Prompt-Rewriter** folder, open cmd and run:

```
..\..\..\python_embeded\python.exe -s -m pip install -r "requirements.txt"
```
### Backend: Vulkan -> Works on all GPUs

If you have Windows, open cmd and run:
```
winget install llama.cpp
```
If you have another OS, you can refer to [this](https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md).

To update llama.cpp, open cmd and run:
```
winget upgrade llama.cpp
```

### Backend: CUDA -> Specialized for Nvdia
Double click the [Install llama.cpp (CUDA).bat](https://github.com/BigStationW/ComfyUI-Prompt-Rewriter/blob/BigStationW-patch-2/Install%20llama.cpp%20(CUDA).bat) file.

To update your version, you can run that file again.

## Instruct/Thinking LLMs

1) Navigate to the **ComfyUI\models** folder and create a folder named "LLM"
2) Navigate to the **ComfyUI\models\LLM** folder and create a folder named "gguf"
3) Navigate to the **ComfyUI\models\LLM\gguf** folder and place your chosen GGUF LLM file there.

For example you can go for this (Instruct model):
- https://huggingface.co/Qwen/Qwen3-4B-GGUF

Or something like this (thinking model):
-  https://huggingface.co/unsloth/Qwen3-4B-Thinking-2507-GGUF

You can even go for uncensored LLMs, like that one for example:
- https://huggingface.co/mradermacher/Josiefied-Qwen3-8B-abliterated-v1-GGUF

## Usage
It should look like this.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/e29ec62a-8770-41cf-99ed-7438a6fd4894" />

An example workflow (for Z-image turbo) can be found [here](https://github.com/BigStationW/ComfyUI-Prompt-Manager/blob/main/workflow/workflow_Z-image_turbo.json).

PS: **The Display Any (rgthree)** node can be found [here](https://github.com/rgthree/rgthree-comfy).

## MultiGPU and offloading

This node allows you to split the model into your GPUs and the CPU with the **gpu_layers** placeholder.

For example:
- Empty placeholder -> All layers go to the first GPU (default)
- gpu0:0.7 -> 70% to GPU:0, 30% to CPU
- gpu0:0.5, gpu1:0.4 -> 50% GPU:0, 40% GPU:1, 10% CPU

<img width="700" alt="image" src="https://github.com/user-attachments/assets/54bd5a5c-73c5-4271-856b-997bcb0a48c5" />

## Image inputs
For Vision Language Models (VLMs), you can add up to 5 images to the Prompt Generator Options node.

1. Download a VLM gguf file and put it to the **ComfyUI\models\LLM\gguf** folder, like that one for example:

- https://huggingface.co/unsloth/Qwen3-VL-4B-Thinking-GGUF

2. Download its mmproj file and put it to the **ComfyUI\models\LLM\gguf** folder.
- https://huggingface.co/unsloth/Qwen3-VL-4B-Thinking-GGUF/blob/main/mmproj-BF16.gguf

3. You have to rename "mmproj-BF16.gguf" to "Qwen3-VL-4B-Thinking-mmproj-BF16.gguf"

At the end it'll look like this:

<img width="700" alt="image" src="https://github.com/user-attachments/assets/a2f602a4-f156-49b8-b70b-4f94b7900d95" />



