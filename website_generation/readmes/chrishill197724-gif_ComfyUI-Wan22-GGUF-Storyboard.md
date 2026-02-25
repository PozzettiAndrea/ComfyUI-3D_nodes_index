# Wan2.2 Storyboard: First-Mid-Mid-Last (GGUF 5B)

An optimized storyboard-based latent generator for **Wan 2.2**. This node is specifically designed for users with **Low VRAM (8GB)** running the **5B GGUF** models who want precise control over video composition.



## 🌟 Key Features
- **Low VRAM Optimized:** Built-in memory management including Tiled VAE support and proactive cache clearing to fit 768x1280 video on 8GB cards (like the 3060 Ti).
- **Storyboard Logic:** Place up to 4 key images (Start, Middle 1, Middle 2, and End) to dictate the flow of your video.
- **Wan 2.2 Native Math:** Automatically handles the strict $(4n + 1)$ frame alignment required by the Wan 2.2 architecture to prevent VAE crashes.
- **Stable Timing:** Generates consistent frame counts based on your desired seconds and FPS.

## 🚀 Installation

1. Navigate to your ComfyUI `custom_nodes` folder.
2. Create a new folder named `ComfyUI-Wan22-GGUF-Storyboard`.
3. Place `wan_storyboard_node.py` and `__init__.py` inside that folder.
4. Restart ComfyUI.
5. 
## 📁 Example Workflow
Download the [workflow.json](./workflow.json) file and drag it into ComfyUI to get started instantly with our recommended settings!
## ⚠️ Important: Manual FPS Sync
Because this node acts as the "Director" for your latent frames, **you must manually match the FPS** settings.

> **Crucial Step:** Ensure the `fps` value in the **Wan2.2 Storyboard** node is set to the **exact same number** as your video saving node (e.g., `Create Video` or `Video Combine`). 
> 
> *If these do not match, your video will appear choppy, sped up, or stuttered.*



## 🛠 Usage Guide

### 1. The Storyboard Slots
- **Start Image:** Locks the very first frame of your video.
- **Middle 1 & 2:** The node calculates the mathematical "center" of your video length and places these images there to guide the motion.
- **End Image:** Locks the final frame, ensuring the AI completes the intended movement.

### 2. Recommended Settings for 8GB VRAM
For the cleanest results on a mid-range card, we recommend:
- **Resolution:** 768 x 1280 (Vertical)
- **FPS:** 24
- **Length:** 5.0 to 7.0 Seconds
- **CFG:** 6.0
- **Steps:** 35 (using WanVideoNAG for clarity)

## 🤝 Acknowledgments
Built for the ComfyUI community to make high-end video generation accessible on consumer-grade hardware.
