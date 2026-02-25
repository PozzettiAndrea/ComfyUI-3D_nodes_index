# StreamDiffusion Node for ComfyUI

A real-time StreamDiffusion pipeline node for ComfyUI with integrated ControlNet, IPAdapter, and LoRA support.

## Features
- Real-time, multi-control Stable Diffusion workflows
- Integrated ControlNet, IPAdapter, and LoRA support
- TensorRT acceleration for high performance
- Flexible configuration and batching
- Dynamically change parameter values at runtime via the streaming sampler node

## Installation

### Using ComfyUI Registry (Recommended)
```
comfy node install streamdiffusion
```

### Manual Installation
Clone this repository into your ComfyUI custom nodes directory:
```
git clone https://github.com/RUFFY-369/ComfyUI-StreamDiffusion.git
```
Install dependencies:
```
pip install -r requirements.txt
```

## Usage

After installation, launch ComfyUI. The StreamDiffusion node and its features will be available in the node menu.

### Example Workflows

1. **Build TensorRT Engines**
	- Use the workflow: [`examples/sd15_tensorrt_engine_build.json`](examples/sd15_tensorrt_engine_build.json)
	- This workflow demonstrates how to build TensorRT engines for your models within ComfyUI.
	- Alternatively, you can run the script [`scripts/build_tensorrt_engines.py`](scripts/build_tensorrt_engines.py) directly to build engines without using the ComfyUI workflow.

2. **Inference with Streaming Sampler**
	- Use the workflow: [`examples/sd15_all_dynamic_params_wlora.json`](examples/sd15_all_dynamic_params_wlora.json)
	- This workflow shows how to use the built engines for real-time inference and dynamically change parameters with the streaming sampler node.

To use these workflows:
1. Open ComfyUI.
2. Load the desired workflow JSON file from the `examples/` directory.
3. Follow the node connections and adjust parameters as needed.

## Requirements
- Python 3.10+
- NVIDIA GPU (for TensorRT acceleration)
- ComfyUI >= 1.0.0

## Support & Documentation
- [Documentation (README)](https://github.com/RUFFY-369/ComfyUI-StreamDiffusion#readme)
- [Bug Tracker](https://github.com/RUFFY-369/ComfyUI-StreamDiffusion/issues)

## License
This project is licensed under the terms of the [Apache License 2.0](LICENSE), the same as the original StreamDiffusion repository.
## Citation
If you use this node or its ideas in your research or projects, please cite the original StreamDiffusion paper:

StreamDiffusion: Real-Time Text-to-Image Generation on Video and Web Cameras
([arXiv:2312.12491](https://arxiv.org/abs/2312.12491))

```
@article{zhang2023streamdiffusion,
	title={StreamDiffusion: Real-Time Text-to-Image Generation on Video and Web Cameras},
	author={Zhang, Yifan and others},
	journal={arXiv preprint arXiv:2312.12491},
	year={2023}
}
```
