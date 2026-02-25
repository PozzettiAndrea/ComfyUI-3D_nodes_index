## ComfyUI FunAsr Nodes

使用FunAsr进行语音识别，并转为文本或字幕文件。

![workflow](example_workflow/workflow.webp)

## 更新

- [ 1.0.1 ] 1. 提升运行速度，2. 优化工作流，3. 字幕默认保存为utf-8编码

## 功能

- [x] 语音识别
- [x] 语音时间戳预测
- [x] 语音转字幕

## 安装

```
cd ComfyUI/custom_nodes
git clone https://github.com/avenstack/ComfyUI-AV-FunASR.git
cd ComfyUI-AV-FunASR
pip install -r requirements.txt
```

## 模型下载

1. [语音识别](https://modelscope.cn/models/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/files)
2. [语音端点检测](modelscope.cn/models/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch/files)
3. [语音时间戳预测](modelscope.cn/models/iic/speech_timestamp_prediction-v1-16k-offline)

模型存放目录：`models/ASR/FunASR/iic`
```
 iic
    ├── speech_fsmn_vad_zh-cn-16k-common-pytorch
    │   ├── README.md
    │   ├── am.mvn
    │   ├── config.yaml
    │   ├── configuration.json
    │   ├── example
    │   ├── fig
    │   └── model.pt
    ├── speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
    │   ├── README.md
    │   ├── am.mvn
    │   ├── asr_example_hotword.wav
    │   ├── config.yaml
    │   ├── configuration.json
    │   ├── example
    │   ├── fig
    │   ├── model.pt
    │   ├── seg_dict
    │   └── tokens.json
    └── speech_timestamp_prediction-v1-16k-offline
        ├── README.md
        ├── am.mvn
        ├── config.yaml
        ├── configuration.json
        ├── example
        ├── model.pt
        ├── seg_dict
        └── tokens.json
```

## 鸣谢

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)