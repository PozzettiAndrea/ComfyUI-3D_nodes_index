# Comfyui-Distill-Any-Depth

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) nodes to use [Distill-Any-Depth](https://distill-any-depth-official.github.io/) prediction.

![](./example_workflows/workflow.png)

Original repo: https://github.com/Westlake-AGI-Lab/Distill-Any-Depth

Huggingface demo: https://huggingface.co/spaces/xingyang1/Distill-Any-Depth

## Updates

- [2025-07-18] 🌟🌟🌟 Support `small`, `base`, `teacher-large` model.
- [2025-07-14] Support `Large` model.

## How to Use

This video demonstrates how to download and use nodes in ComfyUI.



https://github.com/user-attachments/assets/13ae515c-af85-4d2d-8b3c-6c62e3f79a86



### ComfyUI-Manager

1. Run ComfyUI
2. `Manager` → `Custom Nodes Manager`
3. search and install `Comfyui-Distill-Any-Depth`
4. Run the Distill-any-thing node and enjoy it.
> Typically, the inference model will be automatically downloaded to the `/models/distill_any_depth` directory on the first run.

### Git Clone

1. Clone this repo to `ComfyUI/custom_nodes` 
2. Install requirements: `pip install -r requirements.txt`

## Model Support

- [x] [Large model](https://huggingface.co/xingyang1/Distill-Any-Depth/tree/main/large)
- [x] [Small model](https://huggingface.co/xingyang1/Distill-Any-Depth/tree/main/small)
- [x] [Base model](https://huggingface.co/xingyang1/Distill-Any-Depth/tree/main/base)
- [x] [Teacher-Large model](https://huggingface.co/xingyang1/Distill-Any-Depth/tree/main/Distill-Any-Depth-Dav2-Teacher-Large-2w-iter)

## Acknowledgements

This ComfyUI node implementation is based on the excellent work from [Distill-Any-Depth](https://github.com/Westlake-AGI-Lab/Distill-Any-Depth). 

We are grateful to the authors for their outstanding research and for making their code publicly available.
