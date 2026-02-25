# ComfyUI_lynx
 [lynx](https://github.com/bytedance/lynx):Towards High-Fidelity Personalized Video Generation, you can use this node in comfyUI with origin pipeline


# Update
* 10/10 测试用的sage加速导致面部对齐失效，也导致full模式下无法正常使用方法修改过的flash-attn，直接去掉，推理速度恢复正常，12G VRAM 8步 300s左右（推理时长），注意更换工作流；  
* 测试环境cu128+torch2.8.0， Vram 4070 12G，Ram 64G ，python3.11 ,勉强能跑，建议上24G

1.Installation  
-----
  In the ./ComfyUI/custom_nodes directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_lynx
```
2.requirements  
----
* 通常不需要
```
pip install -r requirements.txt
```
3.checkpoints 
----
* [ Comfy org](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) wan 2.1 T2V 14B dit  or [kijai](https://huggingface.co/Kijai/WanVideo_comfy/tree/main)  or  [city96](https://huggingface.co/city96/Wan2.1-T2V-14B-gguf) 'Wan2.1-T2V-14B-gguf'  /  Comfy官方或 kj 的wan 2.1 T2V 14B dit 或者city96的gguf     
* Lynx checkpoints [links](https://huggingface.co/ByteDance/lynx)  / full 或者lite 模型，不预下载,选择菜单类型会自动调用抱抱脸下载     
* Comfy umT5 ，wan 2.1 vae   [links](https://huggingface.co/Comfy-Org/models)   #comfy  umT5 以及wan 2.1 vae   
```
├── ComfyUI/models/
|     ├── diffusion_models/wan2.1_t2v_14B_fp8_e4m3fn.safetensors # optional 可选gguf
|     ├── gguf/wan2.1-t2v-14b-Q6_K.gguf  # optional 可选dit
|     ├── vae/wan2.1vae.safetensors  #comfy 
|     ├── clip/umt5_xxl_fp8_e4m3fn_scaled.safetensors  # comfy 
|     ├── lynx/lynx_full # optional
|        ├──ip_layers.safetensors #8G
|        ├──ref_layers.safetensors #8G
|        ├──resampler.safetensors  # 350M
|     ├── lynx/lynx_lite # optional
         ├──ip_layers.safetensors #1.2G
|        ├──resampler.safetensors  # 320M
```

# 4 Example
* lite  
![](https://github.com/smthemex/ComfyUI_lynx/blob/main/example_workflows/example_l.png)
* full   
![](https://github.com/smthemex/ComfyUI_lynx/blob/main/example_workflows/example_f.png)



# Citation
```
@article{sang2025lynx,
  title    = {Lynx: Towards High-Fidelity Personalized Video Generation},
  author   = {Sang, Shen and Zhi, Tiancheng and Gu, Tianpei and Liu, Jing and Luo, Linjie},
  journal  = {arXiv preprint arXiv:2509.15496},
  year     = {2025}
}
```
