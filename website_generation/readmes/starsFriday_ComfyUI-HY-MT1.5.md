# ComfyUI-HY-MT1.5

ComfyUI node for Hunyuan Translation 1.5 (1.8B). Forked and adapted from the upstream project: [Tencent-Hunyuan/HY-MT](https://github.com/Tencent-Hunyuan/HY-MT.git).

<img width="875" height="846" alt="Image" src="https://github.com/user-attachments/assets/10c61cda-bcbe-4695-b04d-8fb59835da2b" />

## Install
- Place model weights under `models/HY-MT1.5/<model_dir>` (e.g. `models/HY-MT1.5/HY-MT1.5-1.8B`). The node scans this folder only. Quantized or FP16/BF16 versions are both fine as long as transformers can load them.
- Ensure `transformers` and `torch` are available (repo root already lists `transformers>=4.50.3`).
- Put this folder in `custom_nodes/ComfyUI-HY-MT1.5` (already done).
- Restart ComfyUI.

## Nodes
- `HY-MT1.5 Loader` (Category: `HY-MT1.5`): Select a subfolder inside `models/HY-MT1.5/` (e.g. `HY-MT1.5-1.8B`) and load the tokenizer/model. Outputs a reusable model handle.
- `HY-MT1.5 Translator` (Category: `HY-MT1.5`): Accepts the optional model handle from the loader (or auto-loads the first available model), target language dropdown（显示中文名称，38 个语种代码：`"zh": "中文",
    "zh-Hant": "繁体中文",
    "yue": "粤语",
    "en": "英语",
    "fr": "法语",
    "pt": "葡萄牙语",
    "es": "西班牙语",
    "ja": "日语",
    "tr": "土耳其语",
    "ru": "俄语",
    "ar": "阿拉伯语",
    "ko": "韩语",
    "th": "泰语",
    "it": "意大利语",
    "de": "德语",
    "vi": "越南语",
    "ms": "马来语",
    "id": "印尼语",
    "tl": "菲律宾语",
    "hi": "印地语",
    "pl": "波兰语",
    "cs": "捷克语",
    "nl": "荷兰语",
    "km": "高棉语",
    "my": "缅甸语",
    "fa": "波斯语",
    "gu": "古吉拉特语",
    "ur": "乌尔都语",
    "te": "泰卢固语",
    "mr": "马拉地语",
    "he": "希伯来语",
    "bn": "孟加拉语",
    "ta": "泰米尔语",
    "uk": "乌克兰语",
    "bo": "藏语",
    "kk": "哈萨克语",
    "mn": "蒙古语",
    "ug": "维吾尔语",`）, source text, and decoding params (`max_new_tokens`, `temperature`, `top_p`, `top_k`, `repetition_penalty`). Outputs a translated string.

## How it works
- Scans `models/HY-MT1.5/<model_dir>` and lazy-loads the tokenizer/model once (cached per path) with `torch_dtype` auto-chosen (`bfloat16` if CUDA is available).
- Builds a prompt using the official templates (Chinese template when input/target involves Chinese or Cantonese; otherwise English).
- Generates and returns only the new tokens after the prompt for a clean translation string.

## Notes
- Increase `max_new_tokens` if you need longer outputs (default 512; hard cap 4096). Longer generations cost more VRAM/time; stay within your GPU/CPU limits.
- Longer generations cost more VRAM/time; stay within your GPU/CPU limits.
