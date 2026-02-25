# ComfyUI-AV-LatentSync 1.5

一个ComfyUI节点，用于使用LatentSync 1.5进行唇形同步和音频驱动视频生成。

## 依赖

使用前需要安装以下依赖和工具：

1. [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

2. 需要安装[FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases)并添加到系统PATH

## 安装

1. 将此存储库克隆到您的ComfyUI custom_nodes目录中:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/avenstack/ComfyUI-AV-LatentSync.git
cd ComfyUI-AV-LatentSync
pip install -r requirements.txt
```

## 依赖包
```
diffusers>=0.32.2
transformers
huggingface-hub
omegaconf
einops
opencv-python
mediapipe
face-alignment
decord
ffmpeg-python
safetensors
soundfile
```

### 模型目录

模型下载地址：[LatentSync-1.5](https://huggingface.co/ByteDance/LatentSync-1.5)


请把模型放置在`ComfyUI\models\lipsync\latentsync`目录下，`latentsync`内部目录中文件结构如下：

```
│  config.json
│  latentsync_unet.pt
│  README.md
│  stable_syncnet.pt
│  v1.5.txt
│
├─auxiliary
│  │  2DFAN4-cd938726ad.zip
│  │  i3d_torchscript.pt
│  │  koniq_pretrained.pkl
│  │  s3fd-619a316812.pth
│  │  sfd_face.pth
│  │  syncnet_v2.model
│  │  vgg16-397923af.pth
│  │  vit_g_hybrid_pt_1200e_ssv2_ft.pth
│  │
│  └─models
│      └─buffalo_l
│              1k3d68.onnx
│              2d106det.onnx
│              det_10g.onnx
│              genderage.onnx
│              w600k_r50.onnx
├─sd-vae-ft-mse
│      config.json
│      diffusion_pytorch_model.bin
│      diffusion_pytorch_model.safetensors
│
└─whisper
        tiny.pt
```

### 节点参数说明：

1. lips_expression: 唇部动作表现力控制（默认：1.5）

- 较高值（2.0-3.0）：更明显的口型变化，适合富有表现力的演讲

- 较低值（1.0-1.5）：更细微的唇部动作，适合平静对话

- 该参数通过调整模型的引导尺度，平衡自然动作与口型同步精度

2. inference_steps: 推理过程中的去噪步骤数（默认：20）

- 较高值（30-50）：质量更优但处理时间更长

- 较低值（10-15）：处理更快但质量可能降低

- 默认20步通常能较好平衡质量与速度

### 优化建议：

- 对于需要清晰口型的演讲场景，建议将嘴唇表情值调至2.0-2.5

- 日常对话场景使用默认值1.5即可

- 若口型动作不自然或夸张，可尝试降低嘴唇表情值

- 不同语言和说话方式可能需要调整不同参数

- 需要高质量输出时可增加推理步数至30-50

- 快速预览或非关键应用可减少步数至10-15

### 已知限制
- 最适用于面部正对镜头的清晰视频

- 暂不支持动漫/卡通人物面部

- 视频需为25帧率（将自动转换）

- 面部需全程可见

### 致谢

本实现基于以下项目非官方开发：
- 字节跳动研究的[LatentSync 1.5](https://github.com/bytedance/LatentSync)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)框架
- [ComfyUI-LatentSyncWrapper](github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper)

### 许可协议

本项目遵循Apache License 2.0开源协议，详见LICENSE文件。