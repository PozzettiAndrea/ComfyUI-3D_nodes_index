![PPD sample output](https://raw.githubusercontent.com/Apache0ne/ComfyUI-pixel-perfect-depth/main/examples/ImageToStl.com_PPD_00020_.ply.gif)


# Pixel Perfect Depth Maps

- IMPORTANT: Use the V2 nodes (formerly Open3D). Open3D can crash on file save in the newest ComfyUI; use `scipy` in the V2 point cloud node.
- Have not been able to pin point the issue due to differences in environments 

## No auto-downloads

This repo does **not** auto-download models or weights. If a model file is missing, the app will error out so you can provide it locally.

## Install

pip install -r requirements.txt

- TODO: Video node WIP (cant run at speed to test, has full debug logs for future help)
- TODO: maybe using this for `utils3d` fixes the crashing (unsolved per-base issue):

```text
git+https://github.com/EasternJournalist/utils3d.git@c5daf6f6c244d251f252102d09e9b7bcef791a38
```

## Nodes

Use the V2 nodes (renamed from the Open3D variants).

- Pixel Perfect Depth (Depth Map)
- Pixel Perfect Depth (Depth Map - V2)
- Pixel Perfect Depth (Video Depth)
- Pixel Perfect Depth (Save Video Depth)
- Pixel Perfect Depth (Unpack Depth)
- Pixel Perfect Depth (Save Point Cloud)
- Pixel Perfect Depth (Save Point Cloud - V2)

## Models: where to place them

In comfyUI's models folder inside a subfolder named ComfyUI-pixel-perfect-depth
Matching huggingfaces repo layout:
https://huggingface.co/ApacheOne/ComfyUI-pixel-perfect-depth


## Acknowledgement

We are grateful to the [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2), [MoGe](https://github.com/microsoft/MoGe) and [DiT](https://github.com/facebookresearch/DiT) teams for their code and model release. We would also like to sincerely thank the NeurIPS reviewers for their appreciation of this work (ratings: 5, 5, 5, 5).

## Citation

If you find this project useful, please consider citing:

```bibtex
@article{xu2025pixel,
  title={Pixel-perfect depth with semantics-prompted diffusion transformers},
  author={Xu, Gangwei and Lin, Haotong and Luo, Hongcheng and Wang, Xianqi and Yao, Jingfeng and Zhu, Lianghui and Pu, Yuechuan and Chi, Cheng and Sun, Haiyang and Wang, Bing and others},
  journal={arXiv preprint arXiv:2510.07316},
  year={2025}
}
