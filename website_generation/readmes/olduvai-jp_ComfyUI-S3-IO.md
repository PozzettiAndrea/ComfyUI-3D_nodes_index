# ComfyUI-S3-IO

S3-backed input/output nodes for ComfyUI. It lets you browse/load images and videos from an S3 (or S3-compatible)
bucket, upload local input files to S3, and push outputs back to S3 automatically.

## Features

- Load images and videos directly from S3 input prefixes.
- Upload local input files (and pasted/dragged files) to S3 on demand.
- Save image outputs and video renders back to S3 output prefixes.
- Optional custom S3 endpoint for MinIO/compatible storage.
- Thumbnail generation for fast image previews.
- Light caching for downloaded objects.

## Installation

1. Clone or copy this folder into your ComfyUI custom nodes directory:
   `ComfyUI/custom_nodes/ComfyUI-S3-IO`
2. Install dependencies in your ComfyUI Python environment:
   `python -m pip install -r requirements.txt`
3. Set the required environment variables (see below) and start ComfyUI.

## Configuration

Required:

- `S3IO_ACCESS_KEY_ID`
- `S3IO_SECRET_ACCESS_KEY`
- `S3IO_BUCKET`

Optional:

- `S3IO_ENDPOINT_URL` (for MinIO or other S3-compatible endpoints)
- `S3IO_REGION`
- `S3IO_INPUT_PREFIX` (default: empty)
- `S3IO_OUTPUT_PREFIX` (default: empty)
- `S3IO_THUMB_PREFIX` (default: `thumbs`)

Legacy environment prefix `S3_` is also supported (e.g., `S3_ACCESS_KEY_ID`).

Example:

```bash
export S3IO_ACCESS_KEY_ID="AKIA..."
export S3IO_SECRET_ACCESS_KEY="..."
export S3IO_BUCKET="comfy-bucket"
export S3IO_ENDPOINT_URL="https://s3.example.com"
export S3IO_REGION="us-east-1"
export S3IO_INPUT_PREFIX="inputs"
export S3IO_OUTPUT_PREFIX="outputs"
export S3IO_THUMB_PREFIX="thumbs"
```

## Nodes

### Load Image from S3

- Lists files from `S3IO_INPUT_PREFIX` with image extensions.
- If the selected file exists locally (ComfyUI input directory), it is uploaded to S3 and used.
- Otherwise the file is downloaded to a local cache and loaded.

### Save Image to S3

- Saves the image locally (same as the stock node) and uploads to `S3IO_OUTPUT_PREFIX`.
- Ensures unique filenames on S3 (adds ` (n)` suffixes if needed).
- `filename_prefix` supports the standard replacements (`%date:yyyy-MM-dd%`, `%OtherNode.widget%`, etc.) just like the stock Save nodes.

### Load Video (Upload) from S3

- Lists files from `S3IO_INPUT_PREFIX` with video extensions.
- Same upload/download behavior as the image node.
- Uses the vendorized VideoHelperSuite load path.

### Video Combine to S3

- Extends VideoHelperSuite output and uploads all generated files to `S3IO_OUTPUT_PREFIX`.
- Adds UI download entries so ComfyUI can prompt for downloads.
- `filename_prefix` accepts the same replacements (`%date:...%`, `%SomeNode.widget%`) as `VHS_VideoCombine`.

Example prefix:

```
%date:yyyyMMdd%/run_%PositivePrompt.text%
```

This saves under a date-based subfolder and inserts another node's widget value, matching the behavior of the built-in save nodes.

## UI Upload/Download Integration

- Adds upload buttons and drag-and-drop/paste support for `Load Image from S3` and `Load Video (Upload) from S3`.
- Adds a delete button to remove the currently selected S3 input file (with confirmation prompt).
- Also hooks into `VHS_LoadVideo` / `VHS_LoadVideoFFmpeg` if those nodes exist.
- If `comfyuiDL` is available, output downloads are requested automatically.

## Notes

- S3 listings are refreshed when you use ComfyUI's Refresh (Refresh Node Definitions).
- Download cache lives under ComfyUI temp as `temp/s3-io/...` and respects S3 ETag changes.
- Thumbnails are stored in `S3IO_THUMB_PREFIX` as `.jpg` (max 256px).
- Image previews fetch S3 thumbnails (or originals) into `temp` when the file is not present locally.
- Video previews fetch S3 files into `temp` when the file is not present locally.
