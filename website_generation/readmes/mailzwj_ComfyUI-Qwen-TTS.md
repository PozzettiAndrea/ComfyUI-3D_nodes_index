# ComfyUI-Qwen-TTS
Qwen-TTS nodes for ComfyUI\
使用该插件，依赖网络连接，请确保网络连接畅通。
# ChangeLog
`2025/09/23`：Support qwen3-tts-flash

![](./qwen-tts.png)

## 安装
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/mailzwj/ComfyUI-Qwen-TTS.git

cd ComfyUI-Qwen-TTS
pip install -r requirements.txt
```

## 配置
打开`ComfyUI-Qwen-TTS/config.json`，将`YOUR_BAILIAN_API_KEY`替换成自己在[百炼平台](https://bailian.console.aliyun.com/)申请的apiKey保存。

## 使用
启动ComfyUI，搜索添加“千问TTS”节点（或者右键-新建节点-Qwen-千问TTS），然后将输出音频连接到音频预览或保存音频节点即可使用。
