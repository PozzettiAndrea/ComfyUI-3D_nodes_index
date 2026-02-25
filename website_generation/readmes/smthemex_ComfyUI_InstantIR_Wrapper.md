# ComfyUI_InstantIR_Wrapper
You can InstantIR to Fix blurry photos in ComfyUI   
[InstantIR](https://github.com/instantX-research/InstantIR):Blind Image Restoration with Instant Generative Reference    
喜欢这个项目的，请给InstantIR项目个星星！（If you like this project, please give the InstantIR project a star!）    

----

Update
-----
**2024-11-11**
* change some code for lowram,The inference speed of 4070 12G is 20 times faster than before(21s at 20 steps );
* 修改了一些代码，目前4070 12G的推理速度比之前演示的快20倍（感觉这个才是正常的，显存峰值10G左右,20步跑完20秒左右)


1.Installation  
-----
  In the ./ComfyUI /custom_node directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_InstantIR_Wrapper.git
```
2.requirements  
----
```
pip install -r requirements.txt
```

3.checkpoints 
----
3.1 any SDXL checkpoint   
3.2 InstantIR checkpoints [InstantIR](https://huggingface.co/InstantX/InstantIR)   
```
├── ComfyUI/models/InstantIR/models
|     ├── adapter.pt
|     ├── aggregator.pt
|     ├──previewer_lora_weights.bin
```
3.3 dino: online or any local path  [dinov2-large](https://huggingface.co/facebook/dinov2-large)  
3.4 lcm lora [lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl)   

----

4.Example
----   

![](https://github.com/smthemex/ComfyUI_InstantIR/blob/main/example.png)

----  

5.Citation
------

**instantX-research/InstantIR**
``` python  
@article{huang2024instantir,
  title={InstantIR: Blind Image Restoration with Instant Generative Reference},
  author={Huang, Jen-Yuan and Wang, Haofan and Wang, Qixun and Bai, Xu and Ai, Hao and Xing, Peng and Huang, Jen-Tse},
  journal={arXiv preprint arXiv:2410.06551},
  year={2024}
}```
