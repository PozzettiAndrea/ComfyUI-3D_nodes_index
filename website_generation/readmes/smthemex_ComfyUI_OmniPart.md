# ComfyUI_OmniPart
[OmniPart](https://github.com/HKU-MMLab/OmniPart): Part-Aware 3D Generation with Semantic Decoupling and Structural Cohesion,this node ,you can use it in comfyUI

# Upadte
*  test  cu128 torch2.8.0 Vram 12G
*  因为要手动标记合并，所以要分两步运行，不知道就看我B站视频吧。

  
1.Installation  
-----
  In the ./ComfyUI/custom_nodes directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_OmniPart
```
2.requirements  
----
* 比较难装，当然你有安装trellis，基本上没什么难度，除了要再装一个seg和detectron2  
```
pip install -r requirements.txt
```

3.checkpoints 
----

* 3.1 [OmniPart repo](https://huggingface.co/omnipart/OmniPart)  微调的trellis模型？可能也没微调
* 3.2[ omnipart/OmniPart_modules](https://huggingface.co/omnipart/OmniPart_modules) all checkpoints  目录下三个模型   
* 3.3 [ dinov2](https://huggingface.co/facebook/dinov2-with-registers-large/tree/main)  only model.safetensors 只下model.safetensors and [links](https://dl.fbaipublicfiles.com/dinov2/dinov2_vitl14/dinov2_vitl14_reg4_pretrain.pth) dinov2_vitl14_reg4_pretrain.pth； 
* 3.4 [RMBG-2.0 ](https://huggingface.co/briaai/RMBG-2.0/tree/main) only model.safetensors 只下model.safetensors；  
```
├── ComfyUI/models/OmniPart
|     ├── bbox_gen.ckpt
|     ├── model.safetensors #RMBG-2.0
|     ├── partfield_encoder.ckpt
|     ├── sam_vit_h_4b8939.pth
├── ComfyUI/models/dinov2
|        ├──model.safetensors #facebook/dinov2-with-registers-large
|        ├──dinov2_vitl14_reg4_pretrain.pth
├── any-path/omnipart/OmniPart  # https://huggingface.co/omnipart/OmniPart/tree/main 全下，保持目录一致，几G而已  
```
  

# Example
![](https://github.com/smthemex/ComfyUI_OmniPart/blob/main/example_workflows/example1015.png)

# Acknowledgements
[TRELLIS](https://github.com/microsoft/TRELLIS)  
[PartField](https://github.com/nv-tlabs/PartField)  
[FlexiCubes](https://github.com/nv-tlabs/FlexiCubes)  


# Citation
```
@article{yang2025omnipart,
        title={Omnipart: Part-aware 3d generation with semantic decoupling and structural cohesion},
        author={Yang, Yunhan and Zhou, Yufan and Guo, Yuan-Chen and Zou, Zi-Xin and Huang, Yukun and Liu, Ying-Tian and Xu, Hao and Liang, Ding and Cao, Yan-Pei and Liu, Xihui},
        journal={arXiv preprint arXiv:2507.06165},
        year={2025}
}

``
