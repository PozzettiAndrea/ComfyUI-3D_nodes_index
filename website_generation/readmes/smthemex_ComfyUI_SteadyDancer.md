# ComfyUI_SteadyDancer
[SteadyDancer](https://github.com/MCG-NJU/SteadyDancer): Harmonized and Coherent Human Image Animation with First-Frame Preservation,Minimize the number of libraries and VRAMs as much as possible


# Update
* test env ：12G Vram 64G ram / 因为开启卸载，请确保内存够大，显存可能8G也行，未测试
* support safetensor and gguf( a little different of city96 quant ) 支持safetensor的dit 和gguf 与city96量化的稍有不同，不清楚是否能共用

1.Installation  
-----
  In the ./ComfyUI/custom_nodes directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_SteadyDancer
```
2.requirements  
----
* 通常不需要
```
pip install -r requirements.txt
```
3.checkpoints 
----
 
* dit or gguf    [links](https://huggingface.co/smthem/SteadyDancer-14B-diffusers-gguf-dit/tree/main)   #gguf有别于city96的
* [夸克网盘](https://pan.quark.cn/s/1047c55e4ab5)，提取码：2s6k
* Comfy umT5 ，wan 2.1 vae  clip-vision-h  [links](https://huggingface.co/Comfy-Org/models)   #comfy  umT5 以及wan 2.1 vae   
```
├── ComfyUI/models/
|     ├── diffusion_models/SteadyDancer-14B-Bf16.safetensors # optional 可选gguf
|     ├── gguf/SteadyDancer-14B-Q6_K.safetensors.gguf  # optional 可选dit or Q8_0
|     ├── vae/wan2.1vae.safetensors  #comfy 
|     ├── clip/umt5_xxl_fp8_e4m3fn_scaled.safetensors  # comfy 
|     ├── clip_vision/clip_vison_h.safetensors  # comfy 
```

# Example
![](https://github.com/smthemex/ComfyUI_SteadyDancer/blob/main/example_workflows/example.png)


# Citation
```
@misc{zhang2025steadydancer,
      title={SteadyDancer: Harmonized and Coherent Human Image Animation with First-Frame Preservation}, 
      author={Jiaming Zhang and Shengming Cao and Rui Li and Xiaotong Zhao and Yutao Cui and Xinglin Hou and Gangshan Wu and Haolan Chen and Yu Xu and Limin Wang and Kai Ma},
      year={2025},
      eprint={2511.19320},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2511.19320}, 
}

``
