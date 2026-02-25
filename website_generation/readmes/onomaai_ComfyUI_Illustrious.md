# ComfyUI Illustrious

A lightweight ComfyUI extension that lets you **drag, drop, and wire Illustrious XL API endpoints right inside your graph** no boilerplate, no cURL copy pasting, and no lost creative flow.

> **Supported models:** every production checkpoint we host (v0.1 → v3.5)  
> **Max resolution:** 2048 × 2048  
> **Extras:** Stardust accounting, multithreaded batching (up to 10 images), **Tag Booster**, **Mood Enhancer**

---

## ✨ Why Yet Another Node?

Illustrious XL was designed for large, high resolution canvases and crisp natural language alignment but that power is useless if artists have to paste cURL commands into a terminal.  
ComfyUI is our favorite node based playground, so we wrapped the Illustrious endpoints in nodes that:

- **Hide** the messy parts (auth headers, error handling, threading)
- **Surface** only the controls you care about (resolution, sampler, seed, CFG scale, etc.)
- **Live** natively in your graph drag, drop, wire, done.

---

## 📦 Installation

### Git clone (CLI)

```bash
git clone https://github.com/OnomaAI/ComfyUI_Illustrious.git custom_nodes/ComfyUI_Illustrious
```

### ComfyUI‑Manager (GUI)

1. Open **ComfyUI‑Manager → Install via Git URL**
2. Paste `https://github.com/OnomaAI/ComfyUI_Illustrious.git`
3. Click **Install**

---

## 🔑 Account Setup

1. Log into the **Illustrious dashboard**
2. **My Profile → API Key → Create API Key**
3. Create `custom_nodes/ComfyUI_Illustrious/.env` and add:

   ```ini
   ILLUSTRIOUS_API_KEY=<YOUR_ACCESS_TOKEN>
   ```

4. Restart ComfyUI the nodes will auto detect your key.

---

## 🧩 Node Overview

All Illustrious blocks appear under the **Illustrious** category in your node palette:

![Node overview](https://illustrious-prod.s3.ap-northeast-2.amazonaws.com/blog/2025-05-14T06:54:07.240Z/image1.jpg)

---

## 🎨 Usage

### Illustrious-Generator

1. Add a **Generator** node to your graph.
2. Configure:
   - **Model** (v0.1 → v3.5)
   - **Resolution** (≤ 2048 × 2048)
   - **Sampler**, **Seed**, **CFG Scale**, etc.
3. **Batch generation** (multithread):
   - Set **`n_requests`** to 2–10 (concurrent images)
   - Set **Seed** to `-1`
   - Set **control_after_generate** to `fixed`
4. Connect a **Save Image** node or your own chain to capture images _and_ Stardust usage/balance.

![Generator example](https://illustrious-prod.s3.ap-northeast-2.amazonaws.com/blog/2025-05-14T06:53:55.203Z/image2.jpg)

👉 **Full argument reference:** <https://illustrious-xl.ai/docs/text-to-image>

---

### Illustrious-TagBooster

Wire **TagBooster → Generator → Save Image** to expand a short idea into a detailed prompt automatically.

![TagBooster example](https://illustrious-prod.s3.ap-northeast-2.amazonaws.com/blog/2025-05-14T06:53:43.186Z/image3.jpg)

👉 **Docs:** <https://illustrious-xl.ai/docs/text-enhance/tag-booster>

---

### Illustrious-MoodEnhancer

Insert **MoodEnhancer** wherever you need a colorful, scene ready rewrite perfect for Illustrious’s expressive branches.

![MoodEnhancer example](https://illustrious-prod.s3.ap-northeast-2.amazonaws.com/blog/2025-05-14T06:53:32.795Z/image4.jpg)

👉 **Docs:** <https://illustrious-xl.ai/docs/text-enhance/mood-enhancer>

---

## 📚 Documentation

- **Overview:** <https://illustrious-xl.ai/docs/overview>
- **ILXL Text‑to‑Image:** <https://illustrious-xl.ai/docs/text-to-image>
- **Tag Booster:** <https://illustrious-xl.ai/docs/text-enhance/tag-booster>
- **Mood Enhancer:** <https://illustrious-xl.ai/docs/text-enhance/mood-enhancer>

---

Made with ❤️ by **OnomaAI** · [Illustrious XL](https://illustrious-xl.ai) · [GitHub](https://github.com/OnomaAI/ComfyUI_Illustrious) · [Huggingface](https://huggingface.co/OnomaAIResearch)
