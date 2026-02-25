[中文](README.md) | [English](README-EN.md) 

# ComfyUI 的 IndexTTS 声音克隆节点

声音克隆质量非常高, 速度非常快, 支持中英文, 支持自定义音色，**支持无限情绪表达**！

## 📣 更新

[2025-09-09]⚒️: 发布 v2.0.0. **支持IndexTTS2！声音生成，克隆王者登基！**

```
[S1] 2024年02月14日 Valentine’s Day，你居然忘了？！
[S2] Babe 对不起！我特意订了 dinner at 7:30 PM，还买了你最爱的 rose，99朵，每朵¥13.14，total ¥1300.86！
[S1] 哼…那520.13元的红包呢？去年你说“我爱你一生”都发了，今年呢？
[S2] Already sent！Alipay 提示音你没听到？
[S1] …那周末去三亚的机票？你上个月说“March 15日出发，住海景房¥2888.88/晚”？
[S2] Confirmed！Flight MU5378，3月15日08:45起飞。房费我pay，你负责…smile like sunshine！
[S1] 这还差不多～但下次纪念日别用“Babe”糊弄我！
[S2] Yes, my Queen！下次发红包¥1314.52。
```

- 提示词：  
男：大笑笑笑笑。。。女：哭哭哭。。。

https://github.com/user-attachments/assets/6de33c3a-439b-4921-8f94-796c8852508b

[2025-05-30]⚒️: 发布 v1.2.0. **支持双人对话, 支持预览说话者, Windows 正常安装 pynini, 不再是阉割版 TTS!**

`IndexTTS 正式发布1.5 版本了，效果666,晕XUAN4是一种GAN3觉,我爱你！,I love you!,“我爱你”的英语是“I love you”,2.5平方电线,共465篇，约315万字,2002年的第一场雪，下在了2003年.`

https://github.com/user-attachments/assets/b67891f2-0982-4540-8c3b-1a870305466f

[2025-05-14]⚒️: 支持 v1.5 版本. 模型下载并更名放到 `ComfyUI\models\TTS\Index-TTS` 路径下:
- https://huggingface.co/IndexTeam/IndexTTS-1.5/blob/main/bigvgan_generator.pth  → `bigvgan_generator_v1_5.pth`
- https://huggingface.co/IndexTeam/IndexTTS-1.5/blob/main/bpe.model → `bpe_v1_5.model`
- https://huggingface.co/IndexTeam/IndexTTS-1.5/blob/main/gpt.pth → `gpt_v1_5.pth`

[2025-05-02]⚒️: 可用 DeepSpeed 加速, 需要安装 DeepSpeed, Windows 详见 [DeepSpeed 安装](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/windows/08-2024/chinese/README.md). 加速不明显.

[2025-04-30]⚒️: 发布 v1.0.0.

## 使用

**V2重要参数说明（全是可选的）**：
- `deepspeed`: 是否开启 deepspeed 加速（需要先安装deepspeed）。
- `emo_audio_prompt`: 第一个说话人，情绪音频参考。
- `emo_alpha`: 第一个说话人，情绪强度。
- `emo_vector`: 第一个说话人，情绪控制向量，英文格式输入类似这样的列表 `[0, 0, 0, 0, 0, 0, 0.45, 0]`（每一个强度范围0-1，表示惊喜强度 0.45），数字分别对应 : [Happy, Angery, Sad, Fear, Hate, Low, Surprise, Neutral]， 几乎无限组合。
- `use_emo_text`: 第一个说话人，是否开启提示词控制情绪。如果使用提示词控制，情绪参考音频失效。
- `emo_text`: 第一个说话人，情绪控制提示词。随便写，例如 `哭哭。。。苦苦。。。`
- `use_random`: 第一个说话人，是否开启随机性。

- `emo_audio_prompt_s2`: 第二个说话人，同上。
- `emo_alpha_s2`: 第二个说话人，同上。
- `emo_vector_s2`: 第二个说话人，同上。
- `use_emo_text_s2`: 第二个说话人，同上。
- `emo_text_s2`: 第二个说话人，同上。
- `use_random_s2`: 第二个说话人，同上。

**如果不提供任何情绪控制，自动使用克隆音频作为情绪参考**。

---

重要参数说明(其他参数不是很重要的就不一一介绍了):
- `max_mel_tokens`: 控制生成的语音长度, 长文本需要增加这个参数.
- `max_text_tokens_per_sentence`: 分句的最大token数，越小，推理速度越快，占用内存更多，可能影响质量
- `sentences_bucket_max_size`: 分句分桶的最大容量，越大，推理速度越快，占用内存更多，可能影响质量
- `fast_inference`: 开启快速推理
- `custom_cuda_kernel`: 开启自定义 CUDA 内核, 第一次运行将自动构建 CUDA 内核扩展
- `dialogue_audio_s2`: 双人会话时的第二个音频, 如果输入这个音频, 自动启动会话模式. 会话模式下, 输入文本必须如下([S1] 表示第一个说话者, [S2] 表示第二个说话者):
```
[S1] 轻喘像风掠过耳畔，
[S2] 你靠近时，连呼吸都慢了半拍。
[S1] 指尖在我锁骨上游移，
[S2] 仿佛试探一扇未曾开启的门。
```

- 情绪控制：

![image](https://github.com/billwuhao/ComfyUI_IndexTTS/blob/main/images/20250909114313_825_51.png)

- 加载音频:

![image](https://github.com/billwuhao/ComfyUI_IndexTTS/blob/main/images/2025-04-30_19-22-46.png)

- 预览说话者:

我将会把所有 TTS 节点的说话者音频全部统一放到 `ComfyUI\models\TTS\speakers` 路径下, 这些节点包括 `IndexTTS, CSM, Dia, MegaTTS, QuteTTS, SparkTTS, StepAudioTTS` 等.

![image](https://github.com/billwuhao/ComfyUI_IndexTTS/blob/main/images/2025-05-30_22-30-05.png)

- 双人对话:

![image](https://github.com/billwuhao/ComfyUI_IndexTTS/blob/main/images/2025-05-30_22-15-23.png)

## 安装

- **Windows** 先安装以下依赖:

[pynini-windows-wheels](https://github.com/billwuhao/pynini-windows-wheels/releases/tag/v2.1.6.post1) 下载相应 python 版本的 pynini 轮子.

示例:
```
D:\AIGC\python\py310\python.exe -m pip install pynini-2.1.6.post1-cp3xx-cp3xx-win_amd64.whl
D:\AIGC\python\py310\python.exe -m pip install importlib_resources
D:\AIGC\python\py310\python.exe -m pip install WeTextProcessing>=1.0.4 --no-deps
```

- **Linux**, **Mac**, **Windows**:
```
cd ComfyUI/custom_nodes
git clone https://github.com/billwuhao/ComfyUI_IndexTTS.git
cd ComfyUI_IndexTTS
pip install -r requirements.txt

# python_embeded
./python_embeded/python.exe -m pip install -r requirements.txt
```

## 模型下载

**V2模型下载**：

模型手动下载到 `ComfyUI\models\TTS` 下的指定文件夹：

- https://hf-mirror.com/nvidia/bigvgan_v2_22khz_80band_256x/tree/main

- https://hf-mirror.com/funasr/campplus/tree/main

- https://hf-mirror.com/IndexTeam/IndexTTS-2/tree/main

- https://hf-mirror.com/amphion/MaskGCT/tree/main/semantic_codec

- https://hf-mirror.com/facebook/w2v-bert-2.0/tree/main

```
- bigvgan_v2_22khz_80band_256x
   bigvgan_generator.pt
   config.json
- campplus
   campplus_cn_common.bin
- IndexTTS-2
│  .gitattributes
│  bpe.model
│  config.yaml
│  feat1.pt
│  feat2.pt
│  gpt.pth
│  README.md
│  s2mel.pth
│  wav2vec2bert_stats.pt
│
└─ qwen0.6bemo4-merge
        added_tokens.json
        chat_template.jinja
        config.json
        generation_config.json
        merges.txt
        model.safetensors
        Modelfile
        special_tokens_map.json
        tokenizer.json
        tokenizer_config.json
        vocab.json
- MaskGCT
   semantic_codec
        model.safetensors
- w2v-bert-2.0
    .gitattributes
    config.json
    conformer_shaw.pt
    model.safetensors
    preprocessor_config.json
    README.md
```

---

- 模型需要手动下载放到 `ComfyUI\models\TTS\Index-TTS` 路径下:

[Index-TTS](https://huggingface.co/IndexTeam/Index-TTS/tree/main) 结构如下:

```
bigvgan_generator.pth
bpe.model
gpt.pth
```

## 鸣谢


- [index-tts](https://github.com/index-tts/index-tts)
