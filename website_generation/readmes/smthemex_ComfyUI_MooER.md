# ComfyUI_MooER
MooER is an LLM-based Speech Recognition and Translation Model from Moore Threads.     
You can use MooER when install ComfyUI_MooER node.    

MooER (摩耳)  From: [MooER (摩耳)](https://github.com/MooreThreads/MooER)
---
**UPDATE**   
*2024/09/03*  
* add MooER-MTL-80K support,only ASR now/增加官方80K模型的内容，目前只支持ASR，先等等吧。    
* if using 80K fill mtspeech/MooER-MTL-80K in repo_id ,will download auto,/填写mtspeech/MooER-MTL-80K会自动下载，国内请选魔搭，下载好之后，可以用菜单来选择模型；     



1.Installation
-----
In the ./ComfyUI /custom_node directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_MooER.git
```  
  
2.requirements  
----
```
python -m pip install -r requirements.txt
```
如果爆红，查看requirements.txt文件里被#注释的库是否缺失，  
If the library is missing, check if the library annotated with # in the requirements. txt file is missing,   

3 Need  models
----
3.1   

 保持节点默认情况下，点击就从huggingface下载，如果开启use_modelscope，会自动从魔搭下载模型，模型下载的路径是comfyUI/models/diffusers目录下，方便第二次使用菜单； 
 
"mtspeech/MooER-MTL-5K" huggingface： [MooER-MTL-5K](https://huggingface.co/mtspeech/MooER-MTL-5K) , or modelscope:[MooER-MTL-5K](https://modelscope.cn/models/MooreThreadsSpeech/MooER-MTL-5K)    

"mtspeech/MooER-MTL-80K" huggingface： [MooER-MTL-80K](https://huggingface.co/mtspeech/MooER-MTL-80K), or modelscope:[MooER-MTL-80K](https://modelscope.cn/models/MooreThreadsSpeech/MooER-MTL-80K)  

"Qwen/Qwen2-7B-Instruct" huggingface： [Qwen2-7B-Instruct](https://huggingface.co/Qwen/Qwen2-7B-Instruct) ,or modelscope:[qwen2-7b-instruct](https://modelscope.cn/models/qwen/qwen2-7b-instruct)

3.2 offline   
--"mtspeech/MooER-MTL-5K"
```
./comfyUI/models/diffusers/mtspeech/MooER-MTL-5K
|-- paraformer_encoder
|   |-- am.mvn                           # dc1dbdeeb8961f012161cfce31eaacaf
|   `-- paraformer-encoder.pth           # 2ef398e80f9f3e87860df0451e82caa9
|-- asr
|   |-- adapter_project.pt               # 2462122fb1655c97d3396f8de238c7ed
|   `-- lora_weights
|       |-- README.md
|       |-- adapter_config.json          # 8a76aab1f830be138db491fe361661e6
|       `-- adapter_model.bin            # 0fe7a36de164ebe1fc27500bc06c8811
|-- ast
|   |-- adapter_project.pt               # 65c05305382af0b28964ac3d65121667
|   `-- lora_weights
|       |-- README.md
|       |-- adapter_config.json          # 8a76aab1f830be138db491fe361661e6
|       `-- adapter_model.bin            # 12c51badbe57298070f51902abf94cd4
|-- asr_ast_mtl
|   |-- adapter_project.pt               # 83195d39d299f3b39d1d7ddebce02ef6
|   `-- lora_weights
|       |-- README.md
|       |-- adapter_config.json          # 8a76aab1f830be138db491fe361661e6
|       `-- adapter_model.bin            # a0f730e6ddd3231322b008e2339ed579
|-- README.md
`-- configuration.json
```
--"Qwen/Qwen2-7B-Instruct"
```
./comfyUI/models/diffusers/Qwen/Qwen2-7B-Instruct
|-- model-00001-of-00004.safetensors # d29bf5c5f667257e9098e3ff4eec4a02
|-- model-00002-of-00004.safetensors # 75d33ab77aba9e9bd856f3674facbd17
|-- model-00003-of-00004.safetensors # bc941028b7343428a9eb0514eee580a3
|-- model-00004-of-00004.safetensors # 07eddec240f1d81a91ca13eb51eb7af3
|-- model.safetensors.index.json
|-- config.json                      # 8d67a66d57d35dc7a907f73303486f4e
|-- configuration.json               # 040f5895a7c8ae7cf58c622e3fcc1ba5
|-- generation_config.json           # 5949a57de5fd3148ac75a187c8daec7e
|-- merges.txt                       # e78882c2e224a75fa8180ec610bae243
|-- tokenizer.json                   # 1c74fd33061313fafc6e2561d1ac3164
|-- tokenizer_config.json            # 5c05592e1adbcf63503fadfe429fb4cc
|-- vocab.json                       # 613b8e4a622c4a2c90e9e1245fc540d6
|-- LICENSE
|-- README.md
```
4 Example
----
 ![](https://github.com/smthemex/ComfyUI_MooER/blob/main/example/example.png)

5 Function Description of Nodes  
---
--use_torch_musa：使用摩尔线程显卡时开启；
--use_modelscope：国内用户首次使用时开启，下载用，需要安装modelscope库；  
--encoder_name :only support paraformer now 目前仅支持paraformer;   
--audio_dir：Batch generated from directory when not 'NONE', not tested temporarily 非空时，从目录批量生成，暂时未测试;   
--adapter_downsample_rate： 未测试;     
--mode_choice：choice ASR AST or ALL，选择识别，翻译或者二者；     
--asr_prompt/ast_prompt：LLM的提示词，LLM prompt；    
--prompt_key： 选择使用那种prompt，对应asr_prompt 或ast_prompt;      

6 My ComfyUI node list：
-----
1、ParlerTTS node:[ComfyUI_ParlerTTS](https://github.com/smthemex/ComfyUI_ParlerTTS)     
2、Llama3_8B node:[ComfyUI_Llama3_8B](https://github.com/smthemex/ComfyUI_Llama3_8B)      
3、HiDiffusion node：[ComfyUI_HiDiffusion_Pro](https://github.com/smthemex/ComfyUI_HiDiffusion_Pro)   
4、ID_Animator node： [ComfyUI_ID_Animator](https://github.com/smthemex/ComfyUI_ID_Animator)       
5、StoryDiffusion node：[ComfyUI_StoryDiffusion](https://github.com/smthemex/ComfyUI_StoryDiffusion)  
6、Pops node：[ComfyUI_Pops](https://github.com/smthemex/ComfyUI_Pops)   
7、stable-audio-open-1.0 node ：[ComfyUI_StableAudio_Open](https://github.com/smthemex/ComfyUI_StableAudio_Open)        
8、GLM4 node：[ComfyUI_ChatGLM_API](https://github.com/smthemex/ComfyUI_ChatGLM_API)   
9、CustomNet node：[ComfyUI_CustomNet](https://github.com/smthemex/ComfyUI_CustomNet)           
10、Pipeline_Tool node :[ComfyUI_Pipeline_Tool](https://github.com/smthemex/ComfyUI_Pipeline_Tool)    
11、Pic2Story node :[ComfyUI_Pic2Story](https://github.com/smthemex/ComfyUI_Pic2Story)   
12、PBR_Maker node:[ComfyUI_PBR_Maker](https://github.com/smthemex/ComfyUI_PBR_Maker)      
13、ComfyUI_Streamv2v_Plus node:[ComfyUI_Streamv2v_Plus](https://github.com/smthemex/ComfyUI_Streamv2v_Plus)   
14、ComfyUI_MS_Diffusion node:[ComfyUI_MS_Diffusion](https://github.com/smthemex/ComfyUI_MS_Diffusion)   
15、ComfyUI_AnyDoor node: [ComfyUI_AnyDoor](https://github.com/smthemex/ComfyUI_AnyDoor)  
16、ComfyUI_Stable_Makeup node: [ComfyUI_Stable_Makeup](https://github.com/smthemex/ComfyUI_Stable_Makeup)  
17、ComfyUI_EchoMimic node:  [ComfyUI_EchoMimic](https://github.com/smthemex/ComfyUI_EchoMimic)   
18、ComfyUI_FollowYourEmoji node: [ComfyUI_FollowYourEmoji](https://github.com/smthemex/ComfyUI_FollowYourEmoji)   
19、ComfyUI_Diffree node: [ComfyUI_Diffree](https://github.com/smthemex/ComfyUI_Diffree)    
20、ComfyUI_FoleyCrafter node: [ComfyUI_FoleyCrafter](https://github.com/smthemex/ComfyUI_FoleyCrafter)   
21、ComfyUI_MooER: [ComfyUI_MooER](https://github.com/smthemex/ComfyUI_MooER)

7 Citation
------
MooER (摩耳): an LLM-based Speech Recognition and Translation Model from Moore Threads    
Moore Threads Website:  [https://www.mthreads.com/](https://www.mthreads.com/)
```
@article{liang2024mooer,
  title   = {MooER: an LLM-based Speech Recognition and Translation Model from Moore Threads},
  author  = {Zhenlin Liang, Junhao Xu, Yi Liu, Yichao Hu, Jian Li, Yajun Zheng, Meng Cai, Hua Wang},
  journal = {arXiv preprint arXiv:2408.05101},
  year    = {2024}
}
```
