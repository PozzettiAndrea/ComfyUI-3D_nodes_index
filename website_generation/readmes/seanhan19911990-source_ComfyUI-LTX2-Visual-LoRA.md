
<img width="506" height="239" alt="image" src="https://github.com/user-attachments/assets/b5e17c57-9cd8-4062-9eb4-55e34cf05735" />


# ComfyUI-LTX2-Visual-LoRA
A ComfyUI custom node that filters LTX-2 LoRAs to strip out audio-weight interference, ensuring clean, high-fidelity sound while maintaining visual fine-tuning.


🚀 LTX-2 Visual-Only LoRA Loader
A specialized utility for ComfyUI designed to solve the "noisy audio" problem in LTX-2 generations. By surgically filtering the model weights, this node ensures your videos look incredible without sacrificing sound quality.

✨ What This Node Does
📂 Intelligent Filtering — Scans the LoRA's internal state_dict and identifies weights tied to the audio transformer blocks.

🔇 Audio Noise Suppression — Strips out low-quality or "baked-in" audio data often found in community-trained LoRAs.

🖼️ Visual Preservation — Keeps the visual fine-tuning 100% intact.

💎 Crystal Clear Sound — Forces the model to use its clean, default audio logic instead of the "static" or "hiss" from the LoRA.

🛠️ Why You Need This
Unified Model Fix — Since LTX-2 is a joint audio-video model, LoRAs often accidentally "learn" the bad audio from the training clips. This node breaks that link.

Mix & Match — Use the visual style of a "gritty film" LoRA while keeping the high-fidelity, clean bird chirps or ambient sounds of the base model.

Seamless Integration — A drop-in replacement for the standard LoRA loader in your LTX-2 workflows.


📥 Installation Guide
To install LTX-2 Visual-Only LoRA Loader, follow these steps:

Method 1: Git Clone (Recommended)
Open a terminal or command prompt in your ComfyUI/custom_nodes/ folder.

Run the following command:


git clone https://github.com/seanhan19911990-source/ComfyUI-LTX2-Visual-LoRA.git

Restart ComfyUI.
