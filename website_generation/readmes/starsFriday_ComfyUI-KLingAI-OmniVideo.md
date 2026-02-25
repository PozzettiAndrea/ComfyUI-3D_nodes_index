# ComfyUI-KlingAI-OmniVideo 🚀
![ComfyUI Compatible](https://img.shields.io/badge/ComfyUI-Compatible-blue) ![Python](https://img.shields.io/badge/Python-3.12%2B-green)

ComfyUI-KlingAI-OmniVideo is an unofficial ComfyUI node pack for Kling AI’s latest Omni-Video (kling-video-o1) model. It wraps API calls, OSS uploads, and video assembly into standard ComfyUI nodes, supporting text-to-video, multi-image storytelling, start/end-frame control, video editing, and continuation.

## Node Guide
<table>
  <tr>
    <td><img width="720" height="297" alt="Node overview 1" src="https://github.com/user-attachments/assets/db28097f-b1a2-4974-a813-09497c76396b" /></td>
    <td><img width="958" height="637" alt="Node overview 2" src="https://github.com/user-attachments/assets/52b154d8-fdad-4eb7-9c07-124820a45db5" /></td>
  </tr>
</table>

## ✨ Highlights
- Full coverage of the five core Kling Omni modes.
- Automatic OSS relay: uploads images/videos and provides public URLs to the API.
- Native ComfyUI I/O: IMAGE/LATENT (via decode)/AUDIO friendly.
- Prompt helpers: use `<<<image_1>>>` placeholders to precisely reference inputs.

## 🛠️ Installation
Manual (recommended):
1. Go to your ComfyUI custom nodes directory:
   ```bash
   cd /your_path/ComfyUI/custom_nodes/
   ```
2. Clone this repo:
   ```bash
   git clone https://github.com/starsFriday/ComfyUI-KLingAI-OmniVideo.git
   ```
3. Install dependencies:
   ```bash
   cd ComfyUI-KLingAI-OmniVideo
   pip install -r requirements.txt
   ```
4. Restart ComfyUI.

## ⚙️ Configuration (required)
This plugin relies on the Kling AI API and Aliyun OSS (for temporary uploads). Create `config.ini` in this folder (or use the existing one):
```ini
[AUTH]
; Kling AI access/secret keys
; Get them at: https://klingai.kuaishou.com/api
kling_access_key = your_kling_ak
kling_secret_key = your_kling_sk

[OSS]
; Aliyun OSS config (temporary storage for URL access)
; Use a RAM sub-account with RW permission on the bucket
oss_access_key_id = your_aliyun_ak
oss_access_key_secret = your_aliyun_sk
oss_endpoint = https://oss-ap-southeast-1.aliyuncs.com
oss_bucket_name = your_bucket_name
; Optional custom domain (fallbacks to endpoint if empty)
oss_custom_domain = https://your.static.domain.com
```

> The OSS bucket must be public-read or fronted by CDN so Kling servers can fetch your URLs.


## ⚠️ FAQ
- **Input limits**: video duration must be ≤10s, and each side of any input video should be within 720–2560 px; otherwise the API returns errors.  
- **Task Failed**: verify keys in `config.ini` and account balance.  
- **Black output or download errors**: ensure the OSS bucket is public-read or otherwise accessible.  
- **Audio**: outputs include audio; to preserve original audio, combine with nodes like `VHS_LoadVideo`.

## License
MIT License. This package only wraps the API; model rights belong to Kuaishou Kling AI.
