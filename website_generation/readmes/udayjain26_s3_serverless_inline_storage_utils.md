# S3 Serverless-Inline Storage Utils

Upload images and videos to S3 directly from ComfyUI workflows. Load checkpoints by filename. No environment variables needed - all credentials go directly in the nodes.

## Installation

1. Install via ComfyUI-Manager or clone to `ComfyUI/custom_nodes`
2. Restart ComfyUI
3. Look for nodes in "S3 Serverless Storage" category

## Nodes

**S3 Image Upload** - Upload images as WebP files
- Put your S3 credentials directly in the node
- Images automatically convert to WebP format
- Clean filenames: `test123` becomes `test123.webp`

**S3 Video Upload** - Upload video files  
- Same inline credentials approach
- Keeps original video format
- Clean filenames: `myvideo` with `clip.mp4` becomes `myvideo.mp4`

**S3 Image Load** - Download images from S3 URLs
- Works with public URLs and signed URLs
- No credentials needed for public files

**String Checkpoint Loader** - Load checkpoints by filename
- Load any safetensors/checkpoint file from the checkpoints directory
- Provide filename as string input instead of dropdown selection
- Example: `model.safetensors` or `checkpoint.ckpt`

## Usage

### For AWS S3:
- bucket_name: your bucket name
- access_key_id: your access key  
- secret_access_key: your secret key
- region: your AWS region
- endpoint_url: leave empty

### For Supabase:
- bucket_name: your bucket name
- access_key_id: your supabase S3 key
- secret_access_key: your supabase S3 secret  
- region: us-east-1
- endpoint_url: https://yourproject.supabase.co/storage/v1/s3

### For other S3-compatible services:
Fill in your service's S3 endpoint URL.

### For String Checkpoint Loader:
- ckpt_filename: Just the filename (e.g., `model.safetensors`)
- File must exist in your ComfyUI checkpoints directory

## Security Note

Don't share workflows with your credentials filled in. Clear the credential fields before sharing workflow files with others.

