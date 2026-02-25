# ComfyUI-lethris-dia2



🗣️ **Dia2 TTS Generator** & 💬 **Dia2 Captions Generator** for ComfyUI



---



![Dia2 Workflow Example](Examples/Dia2_TTS_and_Caption_Generators.png)



Generate high-quality text-to-speech and captions inside **ComfyUI** with ease. Supports multiple speakers, punctuation-aware sentence grouping, and multiple caption formats.



---



## Features



- 🎙️ Generate TTS audio using Dia2-2B  

- 👥 Multi-speaker support: `[S1]`, `[S2]`  

- 💬 Generate captions in **SRT**, **SSA/ASS**, and **VTT** formats  

- 📝 Per-word, sentence, or advanced grouping (respects punctuation and parentheses)  

- 🧩 Optional voice cloning with example samples (`Voice_Sample_S1.wav`, `Voice_Sample_S2.wav`)  



---
## 📦 Install via ComfyUI Manager (Recommended 🎉)

The node is now officially listed in **ComfyUI Manager**!

To install:

1. Launch **ComfyUI** and open **Manager** (via sidebar or `custom_nodes` menu).
2. Go to the **Install Custom Nodes** tab.
3. Search for: `"Dia2 TTS & Captions Generators for ComfyUI`
4. Click **Install**
5. Restart ComfyUI — you're ready to go!

## 🛠️ Manual Installation (if needed)

Clone this repo into your ComfyUI `custom_nodes` folder:

```bash
  git clone https://github.com/lord-lethris/ComfyUI-lethris-dia2.git
  cd ComfyUI-lethris-dia2
  pip install -r requirements.txt
```

Restart ComfyUI after installation.

✅ After installation, you should see:
- 🗣️ Dia2 TTS Generator
- 💬 Dia2 Captions Generator

## Model & Tokenizer Installation

⚡ GPU Users: Dia2 requires CUDA 12.8 or higher.
Make sure your NVIDIA drivers and PyTorch installation are compatible.
CPU mode works but is slower.

1) Dia2 Model & Tokenizer

- Download the Dia2-2B model & tokenizer from:
  https://huggingface.co/nari-labs/Dia2-2B/tree/main

| FILE                  | Description |
|-----------------------------|-------------|
| [model.safetensors](https://huggingface.co/nari-labs/Dia2-2B/resolve/main/model.safetensors?download=true)            | Dia2-2B model / weights file |
| [tokenizer.json](https://huggingface.co/nari-labs/Dia2-2B/resolve/main/tokenizer.json?download=true)            | tokenizer |

- Rename the weights file to:
  Dia2-2B.safetensors

- Place the model and tokenizer files in:
  /models/Dia2/


---



## Usage in ComfyUI

### 1. Drag in the nodes

- 🗣️ **Dia2 TTS Generator** → converts your text prompt into audio and generates word-level timestamps.  
- 💬 **Dia2 Captions Generator** → converts timestamps into captions in multiple formats.

### 2. Using the Dia2 TTS Generator

- Enter your **prompt** in the text box. You can use multiple lines for multiple speakers.  
- Optional: supply **voice samples** for S1 and S2 to mimic the voices.  
- **Seed**: set a fixed seed for reproducible audio.  
- **Model & Tokenizer**: select the Dia2-2B model and corresponding tokenizer.  
- **Device & Dtype**: choose GPU (CUDA) or CPU. GPU is faster; CPU works but slower.  
- **Output Format**: select `wav`, `flac`, or `mp3`.  
- **CFG / Temperature / Top-K**: tweak text and audio generation parameters to control randomness and style.  

#### Special Tokens / Actions

Dia2 supports a variety of expressive tokens in your prompt:

```
[S1], [S2], (laughs), (applause), (audience cheers), (coughs), (sings), (barks), (screams), (phone ringing), (groans), (thunder), (whispers), (explosion), (car engine sound), (beatboxing), (sighs)
```

- `[S1]` / `[S2]` → switches speaker lines  
- `(laughs)` → inserts laughter  
- `(applause)` → inserts applause  
- `(sighs)` → adds sigh  
- `(audience cheers)` → crowd cheering  
- …and many more, see the full token list in the project.

Use these tokens inline in your text to simulate real-world dialogue or sound effects.

### 3. Generating Captions

- Drag in the 💬 **Dia2 Captions Generator** and connect the **timestamps_json** output from the TTS node.  
- **Caption Modes**:  
  - **Per Word** → each word gets its own timestamped caption.  
  - **Sentence** → groups words into sentences based on punctuation.  
  - **Sentence Advanced** → intelligently groups words respecting punctuation and parentheses.  
- **Caption Formats**: choose **SRT**, **SSA/ASS**, or **VTT**.  
- Captions are automatically saved to `output/captions`, with unique filenames to prevent overwrites.

---

## Example Workflow



- Workflow JSON: [Examples/Dia2_TTS_and_Caption_Generators.json](Examples/Dia2_TTS_and_Caption_Generators.json)

- Example image: [Examples/Dia2_TTS_and_Caption_Generators.png](Examples/Dia2_TTS_and_Caption_Generators.png)

- Voice samples: [Voice/Voice_Sample_S1.wav](Voice/Voice_Sample_S1.wav), [Voice/Voice_Sample_S2.wav](Voice/Voice_Sample_S2.wav)



These show how to set up multi-speaker prompts and caption generation.



---



## Notes



- Always place your Dia2 model in the `/models/Dia2/` folder for proper usage.  

- If weights are found in `diffusion_models`, the node will warn you but can still load them.  

- ⚡ **GPU Users:** Dia2 requires CUDA 12.8 or higher. Make sure your NVIDIA drivers and PyTorch installation are compatible with CUDA 12.8+ for GPU acceleration. CPU mode works but is slower.


---



## Credits



Massive thanks to **[nari-labs](https://huggingface.co/nari-labs)** for an absolutely smashing job on Dia2! 🎉
