# FastVLM-7B ComfyUI Node

A custom [ComfyUI](https://github.com/comfyanonymous/ComfyUI) node for **Apple’s FastVLM-7B** vision-language model.  
This node lets you pass an **image + instruction** and returns a **generated text response**.
[Please check Apple License before downloading the Model](https://huggingface.co/apple/FastVLM-7B/blob/main/LICENSE)
---

## ✨ Features
- 🔹 Uses [apple/FastVLM-7B](https://huggingface.co/apple/FastVLM-7B) from Hugging Face.  
- 🔹 Accepts **ComfyUI images** (`B,H,W,C` float tensors).  
- 🔹 Converts to **PIL image** internally for model input.  
- 🔹 Text input (`instruction`) with multiline support.  
- 🔹 Output is a **STRING** containing the model’s answer.  
- 🔹 Automatically checks `ComfyUI/models/LLM/FastVLM`:
  - Creates folder if missing.
  - Downloads model into it on first run.  
- 🔹 Works on **GPU (fp16)** or **CPU (fp32)** depending on your system.

---
[support us on Patreon](https://www.patreon.com/c/TB_LAAR)

[Check our TBG Enhanced upscaler and Refiner for ComfyUI at https://github.com/Ltamann/ComfyUI-TBG-ETUR](https://github.com/Ltamann/ComfyUI-TBG-ETUR)



