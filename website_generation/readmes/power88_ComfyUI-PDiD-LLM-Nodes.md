# ComfyUI-PDiD-LLM-Nodes

<div align="center">
    <img src="https://img.shields.io/badge/Requires-Python 3.10%2B-blue" alt="Python">
    <img src="https://img.shields.io/badge/Version-0.1.0-green" alt="Version">
</div>

![Overall Screenshot](./assets/overall.png)

## Intro

Some nodes created to do job with LLMs and VLMs (Such as `caption`, `draw bbox`, `simple chat`).

## There are alternatives, why created this node?

Some nodes rely on numerous libraries. Due to the project's non-modular structure, missing just one dependency can make all nodes inoperable.

Additionally, certain libraries required by these nodes—even ones I don't use—conflict with my local virtual environment. For example, the project depends on `aisuite`, causing dependency mismatches during ComfyUI deployment and preventing tools like `uv` from managing these dependencies properly.

## Nodes

### API LLM Loader

![API LLM Loader Screenshot](./assets/APILLMLoader.png)

This node load LLMs or VLMs for use. Supports many clients.

- Openai-compatible chat client
- Openai-compatible responses client (Which OpenAI strongly recommend)
- Ollama client
- Mistralai client.

> I cannot make sure that Anthropic client works well because I cannot reach any Anthropic services in my country. But it works on modelscope on Anthropic client.

### Extra Parameters

![Extra Parameters Screenshot](./assets/ExtraParameters.png)

This node controls some of the extra parameters of a model.
Only works on Openai-compatible client (chat and resposes).

Thinking enabled or disabled only works on some models on volcengine. (Seed 1.6 series.)
Thinking effort works on some newest thinking models so far. Such as `GPT-5`, `GPT-5.1`, `Seed-1.6` and so on.

### API Chat

![API Chat Screenshot](./assets/APIChat.png)

A chat node for LLMs and VLMs.

`unload_model_after_chat` works only on Ollama. `llama.cpp` will be supported when they finished [their jobs](https://github.com/ggml-org/llama.cpp/issues/16487). 

`top_k` works only on Ollama.

### Generate BBOXes

![Generate BBOXes Screenshot](./assets/GenerateBBOXes.png)

A node to generate bboxes from an image.

The bbox is competitable with some bbox nodes on `ComfyUI_LayerStyle`. You can use it with segment anything.

### Captioner

![Captioner Screenshot](./assets/Caption.png)

A node to generate caption from a image. (Maxium 10 sentences.)

You can specify the language to give a corresponding caption.

About `num_max_sentences`:
- Use 2 for CLIP-based model. (Such as SD-1.5 SDXL or CLIP part of the `ClipTextEncodeFlux`)
- Use 4 for T5-based model or Qwen-VL model. (Such as t5xxl part of the `ClipTextEncodeFlux` or Qwen-Image)
- Use 4 and above for Qwen-Image.

> If you want to use it to make caption for training or finetuning. These are also accepted. 

## Install

> Make sure you are using ComfyUI Version 0.3.51 and above.

Just install it by searching `ComfyUI-PDiD-LLM-Nodes` in `ComfyUI-Manager`


## Contributing

Any contributions on this repostory are welcome. (Especially about Anthropic nodes.)

## TODO

### Clients

- [x] OpenAI client support.
- [x] Anthropic client support.  
- [x] Ollama client support.
- [x] Mistralai client support.
- [ ] ComfyUI Clip client support.

### Functions

- [x] Chat
- [x] Generate bbox
- [x] Generate Caption
- [ ] Custom context.

## Licence

MIT