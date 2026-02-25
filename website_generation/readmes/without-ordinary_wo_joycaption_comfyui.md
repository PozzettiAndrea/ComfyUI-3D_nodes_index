# JoyCaption ComfyUI Nodes

Fork of [fpgaminer's nodes](https://github.com/fpgaminer/joycaption_comfyui) with substantial changes to fit our use cases.

[fancyfeast/llama-joycaption-beta-one-hf-llava](https://huggingface.co/fancyfeast/llama-joycaption-beta-one-hf-llava)

## Usage

The `JoyCaption` node allows you to pick the desired Caption Type, Caption Length, and via the `JoyCaption Extra Options` node, various additional options for tweaking the captions.  It takes an `Image` as input, and will output the Query that was built and sent to the JoyCaption model based on your settings, and the resulting Caption.  This node automatically downloads the JoyCaption model into `LLavacheckpoints`.  The model can be loaded in 8-bit or 4-bit quantization if low memory usage is needed (though quality will degrade).


The `JoyCaption (Custom)` node works much like the `JoyCaption` node but lets you input a custom System Prompt and Query.

There are two model loader nodes (three if GGUF support is enabled, se below). The standard node will load models from your `models/LLavacheckpoints` folder (fully supports ComfyUI's `extra_model_paths.yaml` feature). The `JoyCaption Download And Load` node will automaticly download [fancyfeast/llama-joycaption-beta-one-hf-llava](https://huggingface.co/fancyfeast/llama-joycaption-beta-one-hf-llava) (or optionally the alpha models) to your models dir if it has not already being downloaded. 

Example usage. This image can also be used to load this workflow.
![Screenshot of example workflow](https://raw.githubusercontent.com/without-ordinary/wo_joycaption_comfyui/refs/heads/main/workflow_example.png)

## GGUF Support (optional)

**Requires [llama-cpp-python](https://llama-cpp-python.readthedocs.io/en/latest/) with cuda support.**

The GGUF loader node will be available if `llama-cpp-python` is installed. Adapted from [judian17/ComfyUI-joycaption-beta-one-GGUF](https://github.com/judian17/ComfyUI-joycaption-beta-one-GGUF) and the reference implementation of llava in `llama-cpp-python`.

GGUF models are loaded from `models/llava_gguf` and `models/llava_mmproj` (fully supports ComfyUI's `extra_model_paths.yaml` feature).

GGUF models that have been had limited testing so far*:
* [concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf](https://huggingface.co/concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf)
* [mradermacher/llama-joycaption-beta-one-hf-llava-i1-GGUF](https://huggingface.co/mradermacher/llama-joycaption-beta-one-hf-llava-i1-GGUF)
* [mradermacher/llama-joycaption-beta-one-hf-llava-GGUF](https://huggingface.co/mradermacher/llama-joycaption-beta-one-hf-llava-GGUF)

Save [llama-joycaption-beta-one-llava-mmproj-model-f16.gguf](https://huggingface.co/concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf/resolve/main/llama-joycaption-beta-one-llava-mmproj-model-f16.gguf) to `models/llava_mmproj`

*In my limited testing, the GGUF quants would often output fake user-assistant conversation or assistant speach at the end.*


## Differences from the original fork

* Separate load node to allow picking different models and reusing the same loaded model multiple times in a workflow
* Configurable device to use for inference, (original was hardcoded to use all accessible GPUs, multi-GPU support was dropped due to difficulties making it configurable on Transformers)
* Split Extra Options off to its own node to clean up the main node and make it easy to reuse with additional captioner nodes
* Added seed support
* Added configurable and fixed model unloading
* GGUF support
* Probably a bunch of stuff I've forgotten about

Many thanks to [silveroxides](https://github.com/silveroxides) for bug fixes, helping refactor, and generally putting up with my shit. :)
