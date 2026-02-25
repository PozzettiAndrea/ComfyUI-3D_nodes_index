# ComfyUI LoRA Uploaders

Upload your LoRA models to Hugging Face Hub and ModelScope directly from ComfyUI.

**Version: v0.2.0**

## Quick Start

### Installation

1. Clone into ComfyUI's custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/vioaki/ComfyUI-HuggingFaceLoraUploader.git
```

2. Install dependencies:
```bash
cd ComfyUI-HuggingFaceLoraUploader
pip install -r requirements.txt
```

3. Restart ComfyUI

### Get Your Access Token

- **Hugging Face**: Settings → Access Tokens (requires write permission)
- **ModelScope**: Personal Center → Access Tokens

## Usage

### Upload to Hugging Face

1. Add node: Right-click → Add Node → Uploaders/HuggingFace → Hugging Face LoRA Uploader
2. Fill in required fields:
   - **lora_name**: Select your local LoRA file
   - **hf_token**: Your Hugging Face access token
   - **repo_id**: Target repository (format: `username/repo_name`)
   - **commit_message**: Describe this upload
3. Run workflow

### Upload to ModelScope

1. Add node: Right-click → Add Node → Uploaders/ModelScope → ModelScope LoRA Uploader (HTTP)
2. Fill in required fields:
   - **lora_name**: Select your local LoRA file
   - **modelscope_token**: Your ModelScope access token
   - **repo_id**: Target repository (format: `username/model_name`)
   - **commit_message**: Describe this upload
   - **visibility_str**: `public` or `private`
3. Run workflow

## Key Features

- **Auto-Detection**: Automatically finds LoRA files in your ComfyUI directories
- **Auto-Create Repos**: Creates repositories if they don't exist
- **Custom Paths**: Upload to specific folders within repositories
- **Status Feedback**: See upload results directly in ComfyUI

## Important Notes

### Security Warning
Access tokens are saved in plain text in your workflow JSON files. Do not share workflow files containing tokens publicly.

### Optional Settings

Both uploaders support:
- **path_in_repo**: Upload to a subfolder (e.g., `loras/`)
- **create_repo_if_not_exists**: Auto-create repository (default: enabled)
- **private_repo** (HF) / **visibility_str** (ModelScope): Set repository privacy

ModelScope additional options:
- **chinese_name**: Chinese display name for your model
- **license_str**: Choose a license (Apache 2.0, MIT, etc.)
- **revision**: Target branch (default: `master`)

## Troubleshooting

**Nodes not appearing?**
- Verify `huggingface-hub` and `modelscope` are installed
- Check ComfyUI console for errors

**Upload failed?**
- Confirm your token has write permissions
- Check repository ID format
- Verify internet connection
- See ComfyUI console for detailed error messages

**Large files taking long?**
- This is normal - be patient during upload

## Technical Details

- **ModelScope v0.2.0** uses HTTP API (no Git configuration needed)
- Automatically generates `configuration.json` and `README.md` for ModelScope uploads
- Cleans up temporary files after upload
