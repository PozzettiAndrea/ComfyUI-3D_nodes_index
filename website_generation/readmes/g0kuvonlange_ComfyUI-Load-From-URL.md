# ComfyUI Load From URL

A **simple** custom node for ComfyUI to load LoRAs and videos directly from a URL. Ideal for users hosting files on a server with publicly accessible URLs.

---

## 🔧 Prerequisites

- Python (for the built‑in downloader)  
- [aria2c](https://aria2.github.io/) (optional, for ultra-fast parallel downloads)

  ```bash
  # On Debian/Ubuntu:
  sudo apt-get update && sudo apt-get install -y aria2

## 🚀 Installation

1. Clone or download this repository into your ComfyUI custom nodes folder:

   ```bash
   git clone https://github.com/g0kuvonlange/ComfyUI-Load-From-URL.git
2. Restart ComfyUI to detect the new nodes.


## ⚙️ Usage

In the ComfyUI canvas, you will find two new nodes under **Loaders**:

1. **Load LoRA from URL**  
2. **Load Video from URL**

Each node supports choosing between:

- **Python** (single-download mode)  
- **aria2c** (high-speed parallel mode)

### Node Parameters

| Parameter       | Type   | Description                                                                 | Default   |
| --------------- | ------ | --------------------------------------------------------------------------- | --------- |
| **URL**         | String | Direct link to the `.safetensors` or video file (e.g. `.mp4`). Must be publicly accessible. | —         |
| **Downloader**  | Enum   | Choose between `auto`, `python` or `aria2c`.                                        | `auto`  |

All files get downloaded and cached in the following directories:

`/ComfyUI/input/url_loras` (for LoRA)  
`/ComfyUI/input/url_videos` (for Video)