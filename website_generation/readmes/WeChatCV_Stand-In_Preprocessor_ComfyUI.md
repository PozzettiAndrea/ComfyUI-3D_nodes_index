# Stand-In Official Preprocessor ComfyUI Nodes
  <h1>
    <img src="Stand-In.png" width="85" alt="Logo" valign="middle">
    Stand-In
  </h1>

[![Project Page](https://img.shields.io/badge/Project_Page-www.stand--in.tech-green)](https://www.stand-in.tech)
[![Main Repo](https://img.shields.io/badge/Main_Repository-Stand--In-blue)](https://github.com/WeChatCV/Stand-In)

> 🧩 Only images processed with this official preprocessor can fully unleash the power of **Stand-In**.

---

This repository provides a **temporary** ComfyUI node implementation of the Stand-In preprocessor, aiming to correct the misunderstanding of Stand-In’s preprocessing logic in [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper).

We **strongly recommend** using the workflows provided in this repo to ensure proper compatibility and the best identity-preserving performance.

> **Note**: This is a **temporary node**. Features such as KV cache support and advanced attention mechanisms are **not yet implemented**. We are actively developing the **official full-featured ComfyUI nodes** for Stand-In.


## ⚠️ Important Usage Tips

> **Prompt Writing Tip:**  
> If you do **not** wish to alter the subject's facial features, simply use **"a man"** or **"a woman"** without adding extra descriptions of their appearance.  
> Prompts support both **Chinese** and **English** input.  
> The prompt is intended for generating **frontal, medium-to-close-up videos**.

> **Input Image Recommendation:**  
> For best results, use a **high-resolution frontal face image**.  
> There are **no restrictions** on resolution or file extension, as our **built-in preprocessing pipeline** will handle them automatically.

---
We are also actively developing a more flexible version of Stand-In.

---

## 🌐 Project Links

- 📘 **Main Repository**: [WeChatCV/Stand-In](https://github.com/WeChatCV/Stand-In)
- 🏠 **Project Page**: [www.stand-in.tech](https://www.stand-in.tech)

---

## 🚀 Installation
Clone this repository into the `custom_nodes` directory of your ComfyUI installation:

```bash
git clone https://github.com/WeChatCV/Stand-In_Preprocessor_ComfyUI.git
cd Stand-In_Preprocessor_ComfyUI
pip install -r requirements.txt
