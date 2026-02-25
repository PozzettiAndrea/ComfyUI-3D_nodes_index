# ComfyUI-GPUCLIP
Make CLIPs / text encoders load on GPU device

This is a subset of the [MultiGPU node pack](https://github.com/pollockjj/ComfyUI-MultiGPU)

ComfyUI sometimes loads text encoders on CPU for various reasons. These nodes can load them onto GPU, enabling accelerated prompt encoding.

Enables wrappers for GGUF nodes if [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) is installed
