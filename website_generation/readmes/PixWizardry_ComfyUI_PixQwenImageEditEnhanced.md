# Pix Qwen Image Edit (5 Images) 🐋

An enhanced Vision-Language Model (VLM) conditioning node for ComfyUI. This node is a powerful upgrade to the native `TextEncodeQwenImageEditPlus`, by ComfyUI, specifically designed for the **Qwen-Image** series.

It allows you to feed up to 5 reference images into the AI's "context window," giving you unprecedented control and complex image editing.

---

## 🚀 Key Improvements Over Native Node

| Feature | Native ComfyUI Node | Pix Qwen Enhanced |
| :--- | :--- | :--- |
| **Image Slots** | 3 Images | **5 Images** |
| **System Prompt** | Hardcoded (Hidden) | **Fully Editable in UI** |
| **Assistant Priming** | None (Auto) | **Custom AI Response Starting** |
| **Token Tracking** | None | **Live UI Counter (Image + Txt)** |
| **Debug Outputs** | None | **Raw Prompt + Token Math String** |

---

## 🛠 Features Explained

### 1. Customizable System Instruction
The ComfyUI native node hides the instruction that tells the AI to "maintain consistency." 
In this node, the **SYSTEM_INSTRUCTION** is exposed.
*   **Consistency Mode (Default):** Use the default text to keep faces and clothes the same. Citing Qwen Techincal Paper.
*   **Creative Mode:** Remove the "maintain consistency" clause to let the AI be more imaginative with your reference images.

### 2. Assistant Priming
Control the "mood" of the AI. By typing in the **ASSISTANT_PRIMING** box, you are writing the first few words of the AI's response.
*   *Example:* Typing "A hyper-realistic 8k photo" forces the model to generate in that style immediately after reading your prompt.

### 3. Live Token Analytics
The node includes a word-wrapped display at the bottom that calculates your **Context Window** usage:
*   **Images (Image Tokens):** Each image consumes ~720-740 tokens (normalized to 384x384).
*   **Txt (Text Tokens):** The cost of your System Prompt, User Prompt, and Chat tags.
*   **Grand Total:** Monitor how much of the 32k context window you are using within this node.

---

## 💡 Bypass Logic & Best Practices

This node is designed to handle "Bypass" states intelligently. Whether you are saving VRAM or setting up a Negative Prompt, here is how the logic works:

### 🟢 Scenario 1: Bypassing the VAE Only
If you connect images but **disconnect/bypass the VAE input**:
*   **Result:** The model enters **"Concept Mode."** It "sees" the image via the low-res Vision Encoder (384px) but does not receive high-res "Reference Latents."
*   **Benefit:** Lower VRAM usage.
*   **CON:** Poor Outputs

### 🟡 Scenario 2: Bypassing Specific Images
If you have a `Load Image` node connected but **Bypass (Ctrl+B)** that image node:
*   **Result:** The node detects the "Empty Tensor" (0 pixels) and **completely removes** the reference (e.g., "Picture 3") from the prompt.
*   **Benefit:** No "Ghost Data." The AI won't get confused by trying to look at an image that isn't there.

### 🔴 Scenario 3: The "Negative Prompt" Strategy (Lightning Loras)
When setting up your **Negative Conditioning**, you should bypass **ALL** images and the VAE.
*   **How to do it:** Use a second copy of this node for your negative input. Or Use the native ComfyUI node. Leave all image slots empty and the VAE disconnected.
*   **The Logic:** You want the **Positive** conditioning to have visual data, but the **Negative** conditioning to be "Blind" (Text-only). 
*   **The Benefit:** 
    1.  **VRAM Savings:** You aren't calculating all images (Ex. 5 pos + 5 neg), instead only 5 pos images.
    2.  **Cleaner Steering:** By using text-only negatives (e.g., "blurry, low quality"), the model knows exactly what to avoid without being distracted by visual references.

---

## 📦 Installation

1. Git clone this repo
2.  Restart ComfyUI.
3.  Add the custom node to your workflow "🐋 Pix Qwen Image Edit (5 Images)"

## 🔗 Requirements
*   Standard ComfyUI installation.
---

## 📜 Credits & Acknowledgments

*   **[ComfyUI](https://github.com/comfyanonymous/ComfyUI):** For the original `TextEncodeQwenImageEdit` foundation and the core conditioning logic.
*   [Scale Image to Total Pixels Adv](https://github.com/BigStationW/ComfyUi-Scale-Image-to-Total-Pixels-Advanced)
*   **[Qwen Team:](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)** For the underlying Qwen-Image/Qwen2.5-VL model architectures.
  ```bibtex
@misc{wu2025qwenimagetechnicalreport,
      title={Qwen-Image Technical Report}, 
      author={Chenfei Wu and Jiahao Li and Jingren Zhou and Junyang Lin and Kaiyuan Gao and Kun Yan and Sheng-ming Yin and Shuai Bai and Xiao Xu and Yilei Chen and Yuxiang Chen and Zecheng Tang and Zekai Zhang and Zhengyi Wang and An Yang and Bowen Yu and Chen Cheng and Dayiheng Liu and Deqing Li and Hang Zhang and Hao Meng and Hu Wei and Jingyuan Ni and Kai Chen and Kuan Cao and Liang Peng and Lin Qu and Minggang Wu and Peng Wang and Shuting Yu and Tingkun Wen and Wensen Feng and Xiaoxiao Xu and Yi Wang and Yichang Zhang and Yongqiang Zhu and Yujia Wu and Yuxuan Cai and Zenan Liu},
      year={2025},
      eprint={2508.02324},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2508.02324}, 
}
```


---
*Developed by PixWizardry. Built on reverse-engineered research for the ComfyUI community.*
