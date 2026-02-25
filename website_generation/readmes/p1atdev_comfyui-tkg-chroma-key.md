# TKG-DM (Training-free Chroma Key Content Generation Diffusion Model) for ComfyUI 

This repository provides an unofficial ComfyUI custom node implementation of the paper **TKG-DM: Training-free Chroma Key Content Generation Diffusion Model**.

- **arXiv:** [https://arxiv.org/abs/2411.15580](https://arxiv.org/abs/2411.15580)
- **GitHub:** [https://github.com/ryugo417/TKG-DM](https://github.com/ryugo417/TKG-DM)

![](./examples/screenshot-01.jpg)

## Workflows

You can either drag and drop the workflow json or image into ComfyUI to load the workflow.

| Type | Workflow json | Example output |
| - | - | - |
| Simple | [./examples/TKG-Chroma-Key-Simple.json](./examples/TKG-Chroma-Key-Simple.json) | <img src="./examples/TKG-Chroma-Key-Simple.png" /> |
| Advanced | [./examples/TKG-Chroma-Key-Advanced.json](./examples/TKG-Chroma-Key-Advanced.json) | <img src="./examples/TKG-Chroma-Key-Advanced.png" /> |



## Acknowledgments & Citation

This custom node is an implementation of the following paper. Please cite the original paper if you use this work.

```bibtex
@article{morita2024tkg,
  title={TKG-DM: Training-free Chroma Key Content Generation Diffusion Model},
  author={Morita, Ryugo and Frolov, Stanislav and Moser, Brian Bernhard and Shirakawa, Takahiro and Watanabe, Ko and Dengel, Andreas and Zhou, Jinjia},
  journal={arXiv preprint arXiv:2411.15580},
  year={2024}
}
```