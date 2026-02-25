# ComfyUI-UmeAiRT-Sync 🔄

**The intelligent loader for UmeAiRT Workflows.**

This custom node automatically installs, organizes, and updates the professional workflow collection by **[UmeAiRT](https://github.com/UmeAiRT/ComfyUI-Workflows)** directly into your ComfyUI.

## ✨ Features

* **🚀 Zero Maintenance:** No need to manually download JSON or PNG files anymore.
* **🔄 Auto-Update:** Checks for new versions at every ComfyUI startup. If UmeAiRT releases a new workflow (e.g., for a new model like WAN or LTXV), you get it automatically.
* **📂 Clean Organization:** Installs workflows cleanly into `ComfyUI/user/default/workflows/UmeAiRT/`.
* **✅ Native Integration:** Accessible directly via the standard **"Load"** button, the **"Workflows"** menu, or the new **Library/Templates** interface.

## 📥 Installation

### Method 1: Via ComfyUI Manager (Recommended)
1.  Open **ComfyUI Manager**.
2.  Click **"Install via Git URL"**.
3.  Paste the URL of this repository: `https://github.com/UmeAiRT/ComfyUI-UmeAiRT-Sync`
4.  Click **Install** and **Restart ComfyUI**.

### Method 2: Manual Installation
1.  Navigate to your `ComfyUI/custom_nodes/` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/UmeAiRT/ComfyUI-UmeAiRT-Sync.git
    ```
3.  Restart ComfyUI.

## ⚙️ How it works

1.  **On Startup:** The node checks the online version (`version.txt`) against your local installation.
2.  **Sync:** If a new version is detected, it automatically downloads the latest pack from the source repository.
3.  **Ready:** You will see a message in your console: `✨ UmeAiRT: Successfully updated to vX.X!`.

## 📋 Content

By installing this sync node, you get access to the full collection hosted [here](https://github.com/UmeAiRT/ComfyUI-Workflows), organized by categories:

* **Generative Models:**
    * **Flux** 
    * **SDXL** 
    * **Hidream**
    * **Qwen** 
    * **Z-Image** 
* **Video Models:**
    * **LTXV** (Lightricks)
    * **WAN** (WanVideo)
* **Utilities & Enhancement:**
    * **Tools** (General utility nodes and helpers)

---
*Created by [UmeAiRT](https://civitai.com/user/UmeAiRT). Licensed under MIT.*
