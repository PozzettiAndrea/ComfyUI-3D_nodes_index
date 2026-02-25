[中文](README-CN.md) | [English](README.md)

# Kokoro Text-to-Speech Node for ComfyUI

- Near real-time fast text-to-speech,
- **Supports two-person dialogue**
- Multiple voice options available
- Supports text in multiple languages
- Easy integration with ComfyUI workflows

## 📣 Updates

[2025-06-02]⚒️: **Supports two-person dialogue**.

[2025-03-22]⚒️: Code refactoring, faster generation speed.

[2025-03-05]⚒️: Supports 8 languages, 150 voices.

## Supported Languages

- American English 美式英语
- British English 英语
- Japanese 日语
- Chinese 中文
- Spanish 西班牙语
- French 法语
- Hindi 印地语
- Italian 意大利语
- Brazilian Portuguese 巴西葡萄牙语

## Usage

- Text-to-Speech:

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-02-17_01-39-16.png)

- English Two-Person Dialogue:

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-03-05_17-09-35.png)

- Chinese Two-Person Dialogue:

![image](https://github.com/billwuhao/ComfyUI_KokoroTTS_MW/blob/master/images/2025-06-02_21-08-34.png)

## Installation

```
cd ComfyUI/custom_nodes
git clone https://github.com/billwuhao/ComfyUI_KokoroTTS_MW.git
cd ComfyUI_KokoroTTS_MW
pip install -r requirements.txt

# python_embeded
./python_embeded/python.exe -m pip install -r requirements.txt
```

## Model Download

- Models and voices need to be manually downloaded and placed in the `ComfyUI\models\Kokorotts` path:

[Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
[Kokoro-82M-v1.1-zh](https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh)

Structure should be as follows:
```
ComfyUI\models\Kokorotts
│ Kokoro-82M
   └── voices
   config.json
   kokoro-v1_0.pth
| Kokoro-82M-v1.1-zh
   └── voices
   config.json
   kokoro-v1_1-zh.pth
```

## Acknowledgements

- [Kokoro](https://github.com/hexgrad/kokoro)