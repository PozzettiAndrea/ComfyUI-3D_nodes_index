# ComfyUI Upload to BASE Node

A custom [ComfyUI](https://github.com/comfyanonymous/ComfyUI) node that lets you upload generated media directly to your [BASE](https://getbase.app) account — no manual downloads or re-uploads needed.

---

## 🚀 Features

- Upload static images or MP4 videos from a ComfyUI workflow to your BASE account
- Supports direct upload of browser-compatible MP4 video files
- Optionally specify a folder ID to organize uploads
- Secure uploads via personal API key
- Streamlines creative workflow between ComfyUI and BASE

---

## 🧩 Installation

1. Clone this repo into your ComfyUI `custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/babe-and-spencer-enterprises/base-comfyui-node.git
   ```

2. Restart ComfyUI.

3. The node will appear under the **BASE** category in the node menu as `Upload to BASE`.

---

## 🔐 Generate Your API Key

1. Log in at [go.getbase.app](https://go.getbase.app)
2. Go to **Settings → Integrations**
3. Click **Generate API Key**
4. Copy and paste this key into the `api_key` input of the node in ComfyUI

This key securely links your uploads to your BASE account.

![Generate API Key Screenshot](https://go.getbase.app/assets/assets/base_copyapikey.png)

---

## 🛠️ Node Inputs

| Input            | Description                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `image`          | (Optional) A single image to upload (connect from a `VAEDecode` node). Ignored if `video` is provided.                                  |
| `video`          | (Optional) A video file to upload as browser-compatible MP4. Takes precedence over `image`.                                             |
| `api_key`        | Your personal BASE API key (see above).                                                                                                  |
| `filename_prefix`| (Optional) Prefix for the saved file name. May include formatting variables like `%date:yyyy-MM-dd%`. Defaults to `"ComfyUI"`.         |
| `folder_id`      | (Optional) The ID of a folder in your BASE account to store the image/video under. Right-click a folder in BASE to copy its ID.         |

**At least one of `image` or `video` must be provided.**

---

## 📦 Node Behavior

This is an output node in ComfyUI. It performs an upload as a side effect and does not return any value to the graph.

- If `video` is provided, the node uploads a browser-compatible MP4 video to your BASE account.
- Otherwise, a static PNG image is uploaded.

---

## 💡 Example Workflow

Place this node at the end of your workflow as an output node. Example use cases:

- **Static image upload:** Connect a single image (e.g., from `VAEDecode`) to `image` input to upload a PNG.
- **Video upload:** Connect a video file to the `video` input to upload it as an MP4.

Provide your BASE API key and (optionally) a folder ID. The node will upload the file to your BASE account as a side effect; it does not return any value to the graph.

You can customize the file naming by setting the `filename_prefix` input. This helps keep your uploads organized by including date or node values.

![Example Workflow Screenshot](https://go.getbase.app/assets/assets/vae_decode.png)

---

## 📁 Repository Structure

```
base-comfyui-node/
├── base_upload_node.py   # The custom node logic
├── __init__.py           # Node registration
├── README.md             # This file
├── LICENSE               # MIT License
├── .gitignore            # Python-specific ignores
```

---

## 🤝 License

This project is licensed under the [MIT License](LICENSE). Use freely with attribution.
