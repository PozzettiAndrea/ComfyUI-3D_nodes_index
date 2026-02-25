# ComfyUI wrapper nodes for [HunyuanVideo](https://github.com/Tencent/HunyuanVideo)

# Update 5

So I know I said I'd stop working on this, but with all the new stuff out I wanted to work on those and have included the official I2V, it's "fixed" version 2 and the [LoRAs](https://huggingface.co/Kijai/HunyuanVideo_comfy/blob/main/hyvid_I2V_lora_embrace.safetensors) they included in the release

https://github.com/user-attachments/assets/8ce4b1ee-fb63-49a2-83b4-ba8ef1a8b842




and the [dashtoon keyframe LoRA](https://github.com/dashtoon/hunyuan-video-keyframe-control-lora).

https://github.com/user-attachments/assets/2b6e32e4-470f-4feb-b299-5a453e2b4fa1

Also because there's been so much trouble in using the transformer model for text encoding, I figured a way to use the text embeds from native ComfyUI text encoding, like this:

![image](https://github.com/user-attachments/assets/80b23087-a66d-4937-bb2c-d15d5a20304b)

Not that it does give somewhat different results and using these nodes like that can't be considered as original implementation wrapper anymore.

# Update 4, the non-update:


As the native implementation exists, and has support for most features by now, I will mostly stop working on these nodes for anything but it's main purpose: early access and testing of potential new features that are difficult (at least for me) to implement natively.

## Some resources for native workflows:

Flowedit and enhance-a-video can be found from these nodes: https://github.com/logtd/ComfyUI-HunyuanLoom

TeaCache equilevant FirstBlockCache, as well as torch.compile with LoRA support: https://github.com/chengzeyi/Comfy-WaveSpeed

Sageattention can be enabled by `--use-sage-attention` startup argument for ComfyUI, or with a patcher node found in [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) as well as some other node packs.

Leapfusion I2V can be used with my patcher node found in the KJNodes as well, example workflow: https://github.com/kijai/ComfyUI-KJNodes/blob/main/example_workflows/leapfusion_hunyuuanvideo_i2v_native_testing.json

What remains missing from native implementation currently:
- context windowing
- direct image embed support through IP2V
- manual memory management

# Update 3:

It's been hectic couple of weeks with this model, I've lost track of what has happened since the start, but I'll try to present some of the more important updates:

## Official scaled fp8 weights were released:

https://huggingface.co/tencent/HunyuanVideo/blob/main/hunyuan-video-t2v-720p/transformers/mp_rank_00_model_states_fp8.pt

Even if this file is .pt it's completely safe and it is loaded with weights_only, the scale map is included with the nodes. To use this model you have to use the `fp8_scaled` -quantization option in the model loader.
The quality of these weights is much closer to the original bf16, downside is that they do not currently support fp8 fast mode, or LoRAs.

## Almost free quality increase with [Enhance-A-Video](https://github.com/NUS-HPC-AI-Lab/Enhance-A-Video):

This has a very slight hit on inference speed and zero hit on memory use, initial tests indicate it's absolutely worth using.

![image](https://github.com/user-attachments/assets/68f0b5eb-aa23-49e1-a48f-fd3c4b1108ed)

https://github.com/user-attachments/assets/e19b30e1-5f67-4e75-9c73-716d4569c319

https://github.com/user-attachments/assets/083353a2-e9aa-43e9-a916-ff3af1d581c1



# Update 2: Experimental IP2V - Image Prompting to Video via VLM by @Dango233
## WORK IN PROGRESS - But it should work now!

Now you can feed image to the VLM as condition of generations! This is different from image2video where the image become the first frame of the video. IP2V uses image as a part of the prompt, to extract the concept and style of the image.
So - very much like IPAdapter - but VLM will do the heavy lifting for you!

Now this is a tuning free approach but with further task specific tuning we can expand the use scenarios.

## Guide to Using `xtuner/llava-llama-3-8b-v1_1-transformers` for Image-Text Tasks

## Step 1: Model Selection
Use the original `xtuner/llava-llama-3-8b-v1_1-transformers` model which includes the vision tower. You have two options:
- Download the model and place it in the `models/LLM` folder.
- Rely on the auto-download mechanism.

**Note:** It's recommended to offload the text encoder since the vision tower requires additional VRAM.

## Step 2: Load and Connect Image
- Use the comfy native node to load the image.
- Connect the loaded image to the `Hunyuan TextImageEncode` node.
  - You can connect up to 2 images to this node.

## Step 3: Prompting with Images
- Reference the image in your prompt by including `<image>`.
- The number of `<image>` tags should match the number of images provided to the sampler.
  - Example prompt: `Describe this <image> in great detail.`

You can also choose to give CLIP a prompt that does not reference the image separately.

## Step 4: Advanced Configuration - `image_token_selection_expression`
This expression is for advanced users and serves as a boolean mask to select which part of the image hidden state will be used for conditioning. Here are some details and recommendations:

- The hidden state sequence length (or number of tokens) per image in llava-llama-3 is 576.
- The default setting is `::4`, meaning every four tokens, one token goes into conditioning, interleaved, resulting in 144 tokens per image.
- Generally, more tokens lean more towards the conditional image.
- However, too many tokens (especially if the overall token count exceeds 256) will degrade generation quality. It's recommended not to use more than half the tokens (`::2`).
- Interleaved tokens generally perform better, but you might also want to try the following expressions:
  - `:128` - First 128 tokens.
  - `-128:` - Last 128 tokens.
  - `:128, -128:` - First 128 tokens and last 128 tokens.
- With a proper prompting strategy, even not passing in any image tokens (leaving the expression blank) can yield decent effects.

# Update

Scaled dot product attention (sdpa) should now be working (only tested on Windows, torch 2.5.1+cu124 on 4090), sageattention is still recommended for speed, but should not be necessary anymore making installation much easier.

Vid2vid test:
[source video](https://www.pexels.com/video/a-4x4-vehicle-speeding-on-a-dirt-road-during-a-competition-15604814/)

https://github.com/user-attachments/assets/12940721-4168-4e2b-8a71-31b4b0432314


text2vid (old test):

https://github.com/user-attachments/assets/3750da65-9753-4bd2-aae2-a688d2b86115


Transformer and VAE (single files, no autodownload):

https://huggingface.co/Kijai/HunyuanVideo_comfy/tree/main

Go to the usual ComfyUI folders (diffusion_models and vae)

LLM text encoder (has autodownload):

https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer

Files go to `ComfyUI/models/LLM/llava-llama-3-8b-text-encoder-tokenizer`

Clip text encoder (has autodownload)

Either use any Clip_L model supported by ComfyUI by disabling the clip_model in the text encoder loader and plugging in ClipLoader to the text encoder node, or 
allow the autodownloader to fetch the original clip model from:

https://huggingface.co/openai/clip-vit-large-patch14, (only need the .safetensor from the weights, and all the config files) to:

`ComfyUI/models/clip/clip-vit-large-patch14`

Memory use is entirely dependant on resolution and frame count, don't expect to be able to go very high even on 24GB. 

Good news is that the model can do functional videos even at really low resolutions.
