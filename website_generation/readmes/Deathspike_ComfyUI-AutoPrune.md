# ComfyUI-AutoPrune

A slightly cursed ComfyUI _custom node_ that creates pruned copies of images without ComfyUI metadata.

## 🤨 What the hell does that-

_AutoPrune_ abuses the ComfyUI _custom node_ system to start a background thread that watches your output image directory. Whenever ComfyUI saves a new image, _AutoPrune_ automatically creates a **pruned copy without metadata**. Your original image is left completely untouched. _AutoPrune_ just gives you a clean copy that's ready to share online without accidentally leaking how you made it. There's nothing to add to your workflow, no settings to tweak, and no buttons to press.

## 🛠️ Okay! How do I install this thing?

Good question! You can install in two ways:

### Option 1 - ComfyUI Manager (Recommended)

1. Open **ComfyUI Manager**.
2. Go to **Custom Nodes Manager**.
3. Search for **AutoPrune** by **Deathspike**.
4. Click **Install** and choose **latest**.
5. Restart ComfyUI.

### Option 2 - Manual Installation

1. Open **Command Prompt** (_Windows_) or **Terminal** (_macOS/Linux_).
2. Navigate to your **custom_nodes** directory: `cd /path/to/comfyui/custom_nodes`
3. **Clone** this repository: `git clone https://github.com/Deathspike/ComfyUI-AutoPrune`
4. Restart ComfyUI.

> [!WARNING]
> _AutoPrune_ will create pruned copies for **all images currently in your output directory**.

## 🌐 Community

If you enjoy _AutoPrune_, check out more of my work:

* 👉 _Civitai_: https://civitai.com/user/Deathspike
* 🛠️ _GitHub_: https://github.com/Deathspike

Got questions or want to show off something you made with _AutoPrune_?

* 💬 Join our anime [Discord](https://discord.gg/zSR5FcYWWE). I’m **@Deathspike**, and I’d love to hear from you!
