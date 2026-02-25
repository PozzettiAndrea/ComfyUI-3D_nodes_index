# Video Output Bridge

A tiny ComfyUI custom node built to unblock RunPod's [`worker-comfyui`](https://github.com/runpod-workers/worker-comfyui)
deployments. It converts `VHS_VideoCombine` outputs into the standard `images`
payload so serverless runners (RunPod, Modal, etc.) can pick up rendered
MP4/WebP files automatically.

## Why?

Some providers only inspect the `images` field in the workflow history when
collecting artifacts. `VHS_VideoCombine` writes its metadata under `gifs`, which
means otherwise successful jobs return `success_no_images`. This node simply
maps those filenames back into the `images` list without touching the actual
video files.

## Installation for RunPod Serverless Endpoints

Add this to your Dockerfile to install the node when building your custom RunPod worker image:

```dockerfile
FROM runpod/worker-comfyui:<version>-base

# Install custom nodes required for video generation workflows
# Node names from https://registry.comfy.org
RUN comfy node install video-output-bridge
```

This ensures the bridge is available in your serverless endpoint before any workflows execute.

## Usage

1. **In your ComfyUI workflow:**
   - Connect the `VHS_FILENAMES` output from `VHS_VideoCombine` to the `filenames` input on `VideoOutputBridge`
   - Set the `label` parameter (optional) to customize the output filename prefix
   - Ensure `VideoOutputBridge` is marked as an output node

2. **Workflow execution:**
   - The node will map video filenames into the `images` array in the workflow history
   - RunPod's S3 uploader will automatically detect and upload these files

## RunPod Worker Configuration

If you are using RunPod's `worker-comfyui`, make sure the worker is configured
to upload artifacts to your S3 bucket; otherwise the registry sees the filenames
but nothing is exported. Follow the environment variable guide in the official
[Configuration Guide](https://github.com/runpod-workers/worker-comfyui/blob/main/docs/configuration.md)
to set the required S3 bucket, access key, and upload toggles.

**Required environment variables:**
- `BUCKET_ENDPOINT_URL` - Your S3-compatible storage endpoint
- `BUCKET_ACCESS_KEY_ID` - S3 access key
- `BUCKET_SECRET_ACCESS_KEY` - S3 secret key

**Free S3-compatible storage:**
[Cloudflare R2](https://developers.cloudflare.com/r2/) offers 10GB storage and 1 million Class A operations per month for free, making it perfect for video output hosting without egress fees.
