# traumakom Prompt Generator – ComfyUI Node

A powerful custom node for ComfyUI that generates rich, dynamic prompts based on modular JSON worlds — with color realm control (RGB / CMYK), LoRA triggers, optional AI-based prompt enhancement, and a modular **Identity Mixer** to build consistent characters from reusable traits.

> Created with passion by traumakom  
> Powered by Dante 🐈‍⬛, Helly 🐺, and Lily 💻

## Main Nodes

### - Prompt Generator (main Node)

<img width="479" height="1075" alt="image" src="https://github.com/user-attachments/assets/51e5b580-f621-452c-938f-946cb633a577" />


### - Identity Mixer


<img width="479" height="808" alt="image" src="https://github.com/user-attachments/assets/466a2a43-8f49-46c7-b85e-698337b580de" />


### - Connection Example


<img width="1035" height="1105" alt="image" src="https://github.com/user-attachments/assets/113f3169-3a39-4f48-bc7f-f28aacff7b0e" />


## 🌟 Features

### PromptCreator Core
- 🔮 Dynamic prompt generation from modular **JSON worlds**
- 🎨 `COLOR_REALM` support for **RGB / CMYK** palette-driven aesthetics
- 🧩 LoRA trigger integration (e.g., `Realistic`, `Detailed Hands`)
- 🧠 Optional AI enhancer (OpenAI / Cohere / Gemini / Ollama / llama.cpp) to rewrite or enrich prompts
- 📁 Reads world data from `/JSON_DATA`
- 🧪 Debug messages + error handling for smoother workflows
- 🔄 Reload JSON worlds without restarting ComfyUI

### ✅ Identity Mixer (NEW)
- 🧬 Modular identity generation via reusable traits
- ♻️ Trait library (`TRAITS`) + curated presets (`PRESETS`)
- 🎲 Randomized or fixed identity attributes
- 📴 Optional ethnicity exclusion (`None`)
- 🧷 Identity signature output for dataset consistency
- 🧼 Explicit trait syntax (e.g. `lavender hair`, `emerald eyes`) to avoid semantic bleed

---

## 📦 Installation

### Using ComfyUI Manager
1. Open ComfyUI → Manager
2. Install from URL
3. Paste the GitHub repository URL

### Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/PromptCreatorNode.git
```

---

## 📁 Folder Structure

```
ComfyUI/
├── custom_nodes/
│   └── PromptCreatorNode/
│       ├── PromptCreatorNode.py
│       ├── IdentityMixerNode.py
├── JSON_DATA/
│   └── *.json
├── identity.json
├── identities.json
├── api_keys.txt
```

---

## ⚙️ Usage

### PromptCreator
1. Select a JSON world
2. Enable AI enhancer (optional)
3. Generate prompt
4. Connect to CLIPTextEncode

### Identity Mixer
1. Select traits or presets
2. Use random or fixed values
3. Output identity string + signature
4. Append to prompt or dataset captions

---

## 🌈 identity.json Structure

### TRAITS
Reusable identity components:
```json
{
  "TRAITS": {
    "hair_color": ["lavender hair", "cobalt-blue hair"],
    "eyes_color": ["emerald eyes", "icy gray eyes"],
    "ethnicity": ["None", "Mediterranean", "East Asian"]
  }
}
```

### PRESETS
Optional curated identities:
```json
{
  "PRESETS": {
    "Kira_Goth": {
      "hair_color": ["cobalt-blue hair"],
      "expression_base": ["quiet intensity"],
      "ethnicity": ["None"]
    }
  }
}
```

---

## 🧪 AI Enhancement

Supports OpenAI, Cohere, and Gemini.  
API keys must be placed in `api_keys.txt`.

---

## ☕ Support

If you enjoy this project, consider supporting it on Ko-Fi.

---

## 📜 License

Free to use and remix.  
Star the repo if you like it ⭐
