# ComfyUI S3 Save Node

A custom ComfyUI node for saving generated images directly to Cloudflare R2 (or S3-compatible) buckets using boto3, with secure random filename generation and public URL return.

## Features

- Save images to Cloudflare R2/S3 using direct boto3 uploads
- Unique, random 20-character filename generation for each image
- Batch processing of multiple images
- Error handling and status reporting
- WebP format conversion for efficient storage
- Returns JSON with public URLs and status

## Installation

1. Copy this folder to your ComfyUI `custom_nodes` directory:
   ```bash
   cp -r comfy-s3 /path/to/ComfyUI/custom_nodes/
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Restart ComfyUI

## Configuration

The node is configured via environment variables for maximum flexibility. You can set these in your shell or in a `.env` file (if using a loader):

```env
CLOUDFLARE_R2_ENDPOINT_URL= # e.g. https://<account>.r2.cloudflarestorage.com
CLOUDFLARE_ACCESS_KEY_ID=
CLOUDFLARE_SECRET_ACCESS_KEY=
CLOUDFLARE_R2_URL=https://img-dev.fantasy.ai/  # Public base URL for images
CLOUDFLARE_R2_BUCKET=fan-dev
CLOUDFLARE_R2_PREFIX=vik_tests/
```

- **CLOUDFLARE_R2_ENDPOINT_URL**: The endpoint for your R2/S3 storage
- **CLOUDFLARE_ACCESS_KEY_ID**: Your R2/S3 access key
- **CLOUDFLARE_SECRET_ACCESS_KEY**: Your R2/S3 secret key
- **CLOUDFLARE_R2_URL**: The public base URL for accessing images
- **CLOUDFLARE_R2_BUCKET**: The bucket name
- **CLOUDFLARE_R2_PREFIX**: The prefix/path inside the bucket

## Usage

### Node Inputs
- **images**: The image tensor(s) from your ComfyUI workflow

### Node Outputs
- **STRING**: JSON string containing upload results with URLs and status

### Example Workflow
1. Connect your image generation node to the "images" input
2. Run the workflow
3. Get JSON output with public URLs

## Output Format

The node returns a JSON string with the following structure:

```json
[
  {
    "url": "https://img-dev.fantasy.ai/vik_tests/ZFUSJbDRJb2d2ikevexX.webp",
    "status": "success"
  },
  {
    "url": null,
    "status": "failed"
  }
]
```

- Filenames are unique, random 20-character alphanumeric strings (e.g., `ZFUSJbDRJb2d2ikevexX.webp`).
- The URL is constructed from the public base URL, prefix, and filename.

## Security Notes

- All credentials and configuration are handled via environment variables.
- No local image saving is performed; all uploads are in-memory and direct to R2/S3.
- Monitor upload logs for any issues.

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies in `requirements.txt` are installed.
2. **Upload failures**: Check your environment variables, credentials, endpoint, and bucket permissions.
3. **JSON parsing errors**: Verify the output format and ensure the node ran successfully.

### Debug Mode

Enable debug logging by setting the `COMFYUI_DEBUG` environment variable:
```bash
export COMFYUI_DEBUG=1
```

## Node Registration

This node is registered in `__init__.py` using the `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS` dictionaries for ComfyUI.

## License

MIT License - feel free to use and modify as needed. 