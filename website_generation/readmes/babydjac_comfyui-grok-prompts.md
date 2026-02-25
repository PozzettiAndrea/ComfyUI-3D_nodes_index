# 🧠 ComfyUI Grok Prompts

**AI-Powered Prompt Engineering Nodes for ComfyUI using xAI's Grok API.**  
Fine-tune your prompt craft with LLM intelligence, split, recombine, and visualize prompt transformations, all inside ComfyUI.

---

## 🔧 What is this?

**`comfyui-grok-prompts`** is a modular node suite for ComfyUI that uses xAI’s **Grok LLM API** to transform user input into optimized prompts for AI models like **PonyXL** and **Flux**. These nodes intelligently:

- ✂️ Split prompts into subject/scene (`text_l`) and style/mood (`text_g`)
- 🔀 Combine and rewrite them into **perfectly scored** Danbooru-tagged prompts
- 🎥 Output video prompts using **Wan’s Advanced Prompt Formula**
- 💬 Display a UI explanation of how the prompt was refined

---

## 🌈 Live Visual Demos

| Model     | Image | Video Preview |
|-----------|-------|----------------|
| **PonyXL** | ![Pony](https://raw.githubusercontent.com/babydjac/comfyui-grok-prompts/main/media/PonyExample.png) | <video src="https://raw.githubusercontent.com/babydjac/comfyui-grok-prompts/main/media/PonyVideo.mp4" autoplay loop muted playsinline width="320"></video> |
| **Flux**   | ![Flux](https://raw.githubusercontent.com/babydjac/comfyui-grok-prompts/main/media/FluxExample.png) | <video src="https://raw.githubusercontent.com/babydjac/comfyui-grok-prompts/main/media/FluxVideo.mp4" autoplay loop muted playsinline width="320"></video> |

---

## 🧩 Node Packs Included

### 🔹 `PonyXL Grok Prompter`

- 🔤 Takes your prompt and transforms it into:
  - `ponyxl_prompt`: `score_9, score_8_up, rating_mature, 1girl, brunette_hair, long_hair, beautiful_face, detailed_eyes, blue_eyes, full_lips, blush, gigantic_breasts, cleavage, casual_clothing, shopping_mall, indoor, waist_up`
  - `wan_prompt`: `a video of a gorgeous brunette walking through a busy mall, focusing on her face and upper body`

- 💬 Also displays Grok's explanation:  
  _“Combined and cleaned Danbooru tags for clarity, emphasis, and aesthetic scoring. Generated concise video scene prompt from subject + motion.”_

---

### 🔸 `Flux Grok Prompter`

- 🔤 Optimizes prompts for abstract or high-concept visuals (Flux model style):
  - `flux_prompt`: `a close-up view of a stunning brunette woman walking through a bustling mall, surrounded by vibrant shadows and colors`
  - `wan_prompt`: `a video of a brunette woman walking confidently through a mall, with camera focused on her face`

- 💬 Grok's explanation:  
  _“Emphasized human detail and cinematic energy; prompt pruned and rewritten for maximum Flux fluency.”_

---

## 📂 Media Folder Contents

All media live in [`/media`](https://github.com/babydjac/comfyui-grok-prompts/tree/main/media):

| File | Description |
|------|-------------|
| `PonyExample.png` | PonyXL still image output |
| `FluxExample.png` | Flux still image output |
| `PonyVideo.mp4`   | PonyXL video animation |
| `FluxVideo.mp4`   | Flux video animation |

---

## 🎨 UI/Visual Assets

Supporting visuals:

- ![Asset 1](https://github.com/user-attachments/assets/b3e1b7de-aa27-4172-b1b8-eba61548e2d9)
- ![Asset 2](https://github.com/user-attachments/assets/acc0ca68-ad93-41f9-a1be-8d695d141b9d)

---

## 🔐 xAI API Required

To use these nodes, you’ll need an API key from [x.ai](https://x.ai/api). Input your key into the node’s `api_key` field.

---

## 🚀 Use Case Highlights

- Perfect for NSFW image prompting using PonyXL
- Abstract stylized generation with Flux
- Natural-language video scene building for Wan
- Ideal for artists, animators, and prompt engineers wanting more automation and precision

---

## 🫡 Credits

Brought to you by [@babydjac](https://github.com/babydjac)  
Powered by: [ComfyUI](https://github.com/comfyanonymous/ComfyUI) + [xAI’s Grok](https://x.ai/)

---

**Prompt smarter. Generate harder.**
