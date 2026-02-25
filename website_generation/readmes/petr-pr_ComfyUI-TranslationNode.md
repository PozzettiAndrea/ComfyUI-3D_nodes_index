# 🈯 ComfyUI Translation Node (Offline)
Offline translation node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), powered by **Facebook's M2M-100** multilingual model. Translate text between 100+ languages — completely **offline and private**.

## 🚀 Features
- 🌍 Translate between 100+ languages
- 🧠 Automatic source language detection
- ⚡ Works entirely offline once the model is downloaded
- 🧩 Seamless integration with text/image/video workflows in ComfyUI
- 💾 Cached model for faster reuse

## 🛠️ Installation
1. **Copy or clone** this repository into your ComfyUI custom nodes folder:
   ```
   ComfyUI/custom_nodes/ComfyUI-TranslationNode/
   ```
2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
3. **Prepare the model files** (see the next section).
4. Restart ComfyUI and look for **🈯 Translation Node (Offline)** under the *Text* category.

## 🧱 Local Model Setup
This node uses **Facebook’s M2M-100 (418M)** multilingual translation model.

1. **Download the model** manually from Hugging Face: 🔗 https://huggingface.co/facebook/m2m100_418M
2. Create the following folder structure inside your ComfyUI installation:
   ```
   ComfyUI/
   ├── custom_nodes/
   │   └── ComfyUI-TranslationNode/
   └── models/
       └── translation/
           └── facebook/
               └── m2m100_418M/
   ```
3. Place all downloaded files into that final folder (`m2m100_418M/`):
   ```
   pytorch_model.bin
   rust_model.ot
   config.json
   source.spm
   target.spm
   tokenizer_config.json
   special_tokens_map.json
   ```
4. When you launch ComfyUI, you should see this in the console:
   ```
   [TranslationNode] Using local model: models/translation/facebook/m2m100_418M
   ```
✅ Once the model is in place, the node will **never download anything** — it will always load from your local drive.

## 💡 Usage
1. Add the **Translation Node** to your workflow.  
2. Enter any text you want to translate.  
3. Choose a target language (default: `en`).  
4. The source language can be set to `auto` for automatic detection.  
5. Connect the output (`translated_text`) to other nodes — for example, to an image generation prompt.  
6. Enjoy entering prompts in your own language — the node will handle the translation automatically!

## 🧠 Model Details
- **Model:** `facebook/m2m100_418M`  
- **Type:** Multilingual encoder-decoder transformer  
- **Languages supported:** 100+  
- **Size on disk:** ~3.6 GB (pytorch_model.bin ~1.8 GB, rust_model.ot ~1.8 GB)  
- **Framework:** PyTorch via Hugging Face Transformers

## 🔒 Privacy & Security
This node runs entirely **offline**.
- 🧩 All translations are processed locally on your computer.  
- 💾 The model is loaded from `ComfyUI/models/translation/facebook/m2m100_418M`.  
- 🚫 No text, metadata, or user data is ever sent to external servers or APIs.  
- 🔐 Safe to use with confidential or private content.  
- 🔌 Once installed, you can use it **without any internet connection**.

## ⚙️ Requirements
```
transformers>=4.41.0
sentencepiece
torch
langdetect
```

## 👤 Author
Petr Provazník – 2025

## 📄 License
MIT License © 2025  
Created for the ComfyUI community.
