# ComfyUI_YuE
[YuE](https://github.com/multimodal-art-projection/YuE) is a groundbreaking series of open-source foundation models designed for music generation, specifically for transforming lyrics into full songs (lyrics2song). you can use it in comfyUI

# Update
* install quantization moudle (mmgp and exllamav2) if you need ； 
* mmgp and exllamav2 的量化库在菜单选中的时候才会需要，避免有些人安装不上； 


# 1. Installation

In the ./ComfyUI /custom_node directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_YuE.git
```
---

# 2. Requirements  
```
pip install -r requirements.txt
```
* triton is not necessary，I don't test it，you can try
* triton库不是必须的，不过节点里的加速方法用了或许更快，不保真
* use -no-deps if descript-audiotools need high torch 如果descript-audiotools安装需要高版本的torch ，使用pip install -no-deps descript-audiotools
  
* if use mmgp
```
  pip install mmgp
```
* if use exllamav2
```
  pip install exllamav2
```
 - or
```
git clone https://github.com/turboderp/exllamav2
cd exllamav2
pip install -r requirements.txt
pip install .
```
# 3.models
* 3.1 download from [here](https://huggingface.co/m-a-p/xcodec_mini_infer/tree/main/final_ckpt) and [here](https://huggingface.co/m-a-p/YuE-upsampler/tree/main) path like below，模型路径结构如下
```
--   ComfyUI/models/yue
    ├── ckpt_00360000.pth
    ├── decoder_131000.pth
    ├── decoder_151000.pth
```
* 3.2 download from [here](https://huggingface.co/m-a-p/xcodec_mini_infer/tree/main/semantic_ckpts/hf_1_325000), path like below，模型路径结构如下
```
--   ComfyUI/custom_nodes/ComfyUI_YuE/inference/xcodec_mini_infer/semantic_ckpts/hf_1_325000/
    ├── pytorch_model.bin
```

* 3.3 if your GPU is 4090 or 5090 or best，just use repo below,Of course, you can also just fill out the repo，如果你是4090以上，可以用fp16，只填repo会自动下载，以下是离线版；   
* 3.3.1 english [YuE-s1-7B-anneal-en-cot](https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-cot) or[YuE-s1-7B-anneal-en-icl](https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-icl)  or chinese [YuE-s1-7B-anneal-zh-cot](https://huggingface.co/m-a-p/YuE-s1-7B-anneal-zh-cot),or other ,path like below，模型路径结构如下
```
--   anypath/YuE-s1-7B-anneal-en-icl   # 11.5G
    ├── config.json
    ├── generation_config.json
    ├── model.safetensors.index.json
    ├── tokenizer.model
    ├── model-00001-of-00003.safetensors
    ├── model-00002-of-00003.safetensors
    ├── model-00003-of-00003.safetensors
```
* 3.3.2 just one  [YuE-s2-1B-general](https://huggingface.co/m-a-p/YuE-s2-1B-general/tree/main) path like below，模型路径结构如下
```
--   anypath/YuE-s2-1B-general  #  3.65G
    ├── config.json
    ├── generation_config.json
    ├── model.safetensors
    ├── tokenizer.model
```
* 3.4 if your VRAM=<16G,you can use 3.3 origin repo and [int8 or int4](https://github.com/alisson-anjos/YuE-Interface),[exllamav2](https://github.com/sgsdxzy/YuE-exllamav2),[deepbeepmeep](https://github.com/deepbeepmeep/YuEGP) Three quantitative acceleration methods and models,Thanks to these open-source projects ，below is list.如果显存在16G以下，可以用社区的三种量化加速方法和模型，列表如下：
  - [exllamav2](https://huggingface.co/Doctor-Shotgun/YuE-s1-7B-anneal-en-cot-exl2) use fp16 Q8,Q6... [@sgsdxzy](https://github.com/sgsdxzy)
  - [int8](https://huggingface.co/Alissonerdx/YuE-s1-7B-anneal-en-cot-int8)  bitsandbytes  [@alisson-anjos](https://github.com/alisson-anjos)
  - [exllamav2](https://huggingface.co/collections/Alissonerdx/yue-models-exllamav2-67a539be76b5225ebda95323)   use fp16 Q8,Q6...[@alisson-anjos](https://github.com/alisson-anjos)
  - [deepbeepmeep](https://github.com/deepbeepmeep/YuEGP) use fp16,int8... [@deepbeepmeep](https://github.com/deepbeepmeep)
 3.4.1 path like below，模型路径结构如下
```
--   anypath/YuE-s1-7B-anneal-en-cot-exl2-8.0bpw
    ├── config.json
    ....
--   anypath/YuE-s2-1B-general-exl2-8.0bpw 
    ├── config.json
    ....
```
# 4.Use Tips
* if VRAM>=24G,use origin repo,'quantization_model'choice 'fp16',keep 'use_mmgp' false,prompt_end_time is sampler length,try 30s first.(best quality);
* if VRAM<=16G,use origin repo,'quantization_model'choice 'fp16',keep 'use_mmgp' ture,mmgp_profile choice 2,prompt_end_time is sampler length,try 30s first (best quality,slowly);
* if VRAM<=16G,use int8 repo,'quantization_model'choice 'int8',keep 'use_mmgp' false,prompt_end_time is sampler length,try 30s first.(nromal quality,very slowly 6716s,don't try it)
* if VRAM<=16G,use exllamav2 Q8 repo,'quantization_model'choice 'exllamav2',keep 'use_mmgp' false,exllamav2_cache_mode choice Q8,prompt_end_time is sampler length,try 30s first.(nromal quality,very fast)
* if VRAM>=16G,use origin repo,'quantization_model'choice 'exllamav2',keep 'use_mmgp' false,exllamav2_cache_mode choice fp16,prompt_end_time is sampler length,try 30s first.(best quality, fast and maybe OOM if VRAM<24)
* 显存大于24G，用原生的repo，quantization_model选fp16，关闭use_mmgp，prompt_end_time就是渲染时长先设置为30秒测试（普通玩家的最佳效果）
* 显存小于等于16G，用原生的repo，quantization_model选fp16，开启use_mmgp，prompt_end_time就是渲染时长先设置为30秒测试（效果好，但是慢，需要大内存）
* 显存小于等于16G，用int8的repo，'quantization_model'选int8，关闭use_mmgp，prompt_end_time就是渲染时长先设置为30秒测试（效果还行，速度奇慢6716s，不要尝试）
* 显存小于等于16G，用exllamav2的Q8 repo，'quantization_model'选exllamav2，关闭use_mmgp，exllamav2_cache_mode选择Q8，prompt_end_time就是渲染时长先设置为30秒测试（效果一般，速度非常快）
* 显存大于等于16G，用原生的repo，'quantization_model'选exllamav2，关闭use_mmgp，exllamav2_cache_mode选择fp16,prompt_end_time就是渲染时长先设置为30秒测试（效果和速度未测试）
* if "use_dual_tracks_prompt"  set ture ,will Instrumental from file 'pop.00001.Instrumental.mp3' or if set "use_audio_prompt" ture and "use_dual_tracks_prompt" False will Instrumental from file "pop.00001.mp3",you can replace it ,but keep name in same.
* 开启use_dual_tracks_prompt 会借鉴'pop.00001.Instrumental.mp3'，开启"use_audio_prompt"并关闭"use_dual_tracks_prompt" 会借鉴 "pop.00001.mp3"，你可以用其他歌曲替换掉这两个，但是逐一保持命名不要动，因为在代码里写死了。我迟点再改。
* use_mmgp model have 5 choice（mmgp_profile） ，3-4 will quantization model auto，mmgp模式在mmgp_profile有5个选项，大于等于3会自动量化，数字越大需要内存越大，需要显存越小，但是越慢.

# 5.Prompt Engineering Guide 提示词和歌词撰写官方指导
* look [Here](https://github.com/multimodal-art-projection/YuE?tab=readme-ov-file#prompt-engineering-guide) to find how to edit your Genre Tagging Prompt and Lyrics Prompt，链接直达官方的歌词和提示词指导。
* use [top_200_tags.json](https://github.com/smthemex/ComfyUI_YuE/blob/main/top_200_tags.json) to edit your prompts，查看top_200_tags.json来撰写你的歌词提示
  
# 6.Example
* use fp16 and use_mmgp
![](https://github.com/smthemex/ComfyUI_YuE/blob/main/example.png)
* use int8 bitsandbytes
![](https://github.com/smthemex/ComfyUI_YuE/blob/main/int8_example.png)
  
# 7.Citation
```
@misc{yuan2025yue,
  title={YuE: Open Music Foundation Models for Full-Song Generation},
  author={Ruibin Yuan and Hanfeng Lin and Shawn Guo and Ge Zhang and Jiahao Pan and Yongyi Zang and Haohe Liu and Xingjian Du and Xeron Du and Zhen Ye and Tianyu Zheng and Yinghao Ma and Minghao Liu and Lijun Yu and Zeyue Tian and Ziya Zhou and Liumeng Xue and Xingwei Qu and Yizhi Li and Tianhao Shen and Ziyang Ma and Shangda Wu and Jun Zhan and Chunhui Wang and Yatian Wang and Xiaohuan Zhou and Xiaowei Chi and Xinyue Zhang and Zhenzhu Yang and Yiming Liang and Xiangzhou Wang and Shansong Liu and Lingrui Mei and Peng Li and Yong Chen and Chenghua Lin and Xie Chen and Gus Xia and Zhaoxiang Zhang and Chao Zhang and Wenhu Chen and Xinyu Zhou and Xipeng Qiu and Roger Dannenberg and Jiaheng Liu and Jian Yang and Stephen Huang and Wei Xue and Xu Tan and Yike Guo}, 
  howpublished={\url{https://github.com/multimodal-art-projection/YuE}},
  year={2025},
  note={GitHub repository}
}
```

