# ComfyUI_efficient_sam_node
Unofficial EfficientViT_sam_nodes for the https://huggingface.co/mit-han-lab/efficientvit-sam models

<img width="2121" height="869" alt="Screenshot 2025-09-08 204734" src="https://github.com/user-attachments/assets/6d3fb857-8e12-4c84-8d25-0c1e2f5771ce" />

## Installation 
- Manual Install required\
Inside Custom_nodes Folder\
```https://github.com/Apache0ne/ComfyUI_efficient_sam_node.git ```\
IF using Matrix \
Inside venv\Scripts\
```activate```\
```pip install git+https://github.com/mit-han-lab/efficientvit.git```\
Ran into one issue: try this fix
```export SETUPTOOLS_USE_DISTUTILS=stdlib```\
then try again: ```pip install git+https://github.com/mit-han-lab/efficientvit.git```\

## Models go into models/sam
[Pretrained_models](https://huggingface.co/mit-han-lab/efficientvit-sam/tree/main)

## Acknowledgements
- This node relies on the excellent work done by the MIT-HAN-Lab
- https://github.com/kijai/ComfyUI-Florence2
- https://github.com/kijai/ComfyUI-segment-anything-2
- https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite

```bibtex
@inproceedings{cai2023efficientvit,
  title={Efficientvit: Lightweight multi-scale attention for high-resolution dense prediction},
  author={Cai, Han and Li, Junyan and Hu, Muyan and Gan, Chuang and Han, Song},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={17302--17313},
  year={2023}
}

@article{zhang2024efficientvit,
  title={EfficientViT-SAM: Accelerated Segment Anything Model Without Performance Loss},
  author={Zhang, Zhuoyang and Cai, Han and Han, Song},
  journal={arXiv preprint arXiv:2402.05008},
  year={2024}
}
```
