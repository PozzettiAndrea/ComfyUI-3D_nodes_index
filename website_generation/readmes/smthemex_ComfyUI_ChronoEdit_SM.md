# ComfyUI_ChronoEdit_SM
[ChronoEdit](https://github.com/nv-tlabs/ChronoEdit): Towards Temporal Reasoning for Image Editing and World Simulation,you can use this node in comfyUI,and Vram >8G

# Update
* 支持新的画笔lora，垫图画几笔，提示词输入修改的内容即可，修复latent兼容性问题导致的偏色问题
* 支持fp8量化模型和放大lora，两个lora一起用时最好步数大一点（8-12步）
* support paintbrush lora ,fix lantens bug
* support upscale lora  and fp8 dit，if use 8 step and upscale need step>12  



1.Installation  
-----
  In the ./ComfyUI/custom_nodes directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_ChronoEdit_SM

```

2.requirements  
----

```
pip install -r requirements.txt
```

3.checkpoints 
----

1. gguf [links](https://huggingface.co/QuantStack/ChronoEdit-14B-GGUF/tree/main)   
2. dit fp8 [links](https://huggingface.co/cocorang/ChronoEdit-14B-Diffusers-FP8) optional
3. 8 steps lora [links](https://huggingface.co/nvidia/ChronoEdit-14B-Diffusers/tree/main/lora) 
4. upscale lora [links](https://huggingface.co/nvidia/ChronoEdit-14B-Diffusers-Upscaler-Lora)
5 .wan T5 clipvison vae [ links](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) 
```
├── ComfyUI/models/gguf # or fp8 
|     ├── ChronoEdit-14B-Q6_K.gguf # or Q8
├── ComfyUI/models/vae
|        ├──Wan2.1_VAE.pth
├── ComfyUI/models/clip
|        ├──umt5_xxl_fp8_e4m3fn_scaled.safetensors
|        ├──qwen_2.5_vl_7b.safetensors # OPTIONAL if use vl 可选 太慢
├── ComfyUI/models/clip_vision 
|        ├──clip_vision_h.safetensors
├── ComfyUI/models/loras 
|        ├──chronoedit_distill_lora.safetensors
|        ├──upsample_lora_diffusers.safetensors

```

# 4 Example
* edit
![](https://github.com/smthemex/ComfyUI_ChronoEdit_SM/blob/main/example_workflows/example.gif)
* paintbrush
![](https://github.com/smthemex/ComfyUI_ChronoEdit_SM/blob/main/example_workflows/example_paint.png)

# 5 Citation
```
@article{wu2025chronoedit,
    title={ChronoEdit: Towards Temporal Reasoning for Image Editing and World Simulation},
    author={Wu, Jay Zhangjie and Ren, Xuanchi and Shen, Tianchang and Cao, Tianshi and He, Kai and Lu, Yifan and Gao, Ruiyuan and Xie, Enze and Lan, Shiyi and Alvarez, Jose M. and Gao, Jun and Fidler, Sanja and Wang, Zian and Ling, Huan},
    journal={arXiv preprint arXiv:2510.04290},
    year={2025}
}
```
