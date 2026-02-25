# ComfyUI OSS Upload Plugin

A ComfyUI plugin for uploading generated images and videos to Alibaba Cloud OSS (Object Storage Service).

## Features

- **Image Upload Node**: Upload ComyUI generated images to OSS
- **Video Upload Node**: Upload videos (compatible with VideoHelperSuite) to OSS
- **Audio Upload Node**: Upload audio files to OSS
- **Automatic Retry**: Automatically retries uploads up to 10 times on failure
- **Random Filename Generation**: Option to generate random filenames with timestamp
- **Custom Filename**: Option to specify custom filenames
- **Configurable OSS Settings**: Support for custom endpoint, bucket, access keys, and paths

## Installation

1. Copy the `ComfyUI-OSS-Upload` folder to your ComfyUI `custom_nodes` directory
2. Install required dependencies:
   ```bash
   pip install oss2
   ```

## Usage

### Image Upload Node (OSS Image Uploader)

**Inputs:**
- `image`: IMAGE type from ComfyUI
- `endpoint`: OSS endpoint (e.g., https://oss-cn-hangzhou.aliyuncs.com)
- `bucket`: OSS bucket name
- `access_key`: Access Key ID
- `access_secret`: Access Key Secret
- `path`: OSS storage path (e.g., comfyui/images)
- `random_filename`: Boolean to enable/disable random filename generation
- `filename`: Custom filename (used when random_filename is False)

**Output:**
- `url`: Complete URL of the uploaded file on OSS

### Audio Upload Node (OSS Audio Uploader)

**Inputs:**
- `audio`: AUDIO type from ComfyUI
- `endpoint`: OSS endpoint (e.g., https://oss-cn-hangzhou.aliyuncs.com)
- `bucket`: OSS bucket name
- `access_key`: Access Key ID
- `access_secret`: Access Key Secret
- `path`: OSS storage path (e.g., comfyui/audio)
- `random_filename`: Boolean to enable/disable random filename generation
- `filename`: Custom filename (used when random_filename is False)

**Output:**
- `url`: Complete URL of the uploaded file on OSS

### Video Upload Node (OSS Video Uploader)

**Inputs:**
- `video`: VHS_FILENAMES type from VideoHelperSuite VideoCombine node
- `endpoint`: OSS endpoint (e.g., https://oss-cn-hangzhou.aliyuncs.com)
- `bucket`: OSS bucket name
- `access_key`: Access Key ID
- `access_secret`: Access Key Secret
- `path`: OSS storage path (e.g., comfyui/videos)
- `random_filename`: Boolean to enable/disable random filename generation
- `filename`: Custom filename (used when random_filename is False)

**Output:**
- `url`: Complete URL of the uploaded file on OSS

## Random Filename Format

When random filename is enabled, files are named with the format:
```
{timestamp}_{random_string}.{extension}
```
Example: `20241210_143052_a3k9m2p7.png`

## Example Workflow

1. Generate an image using ComfyUI nodes
2. Connect the IMAGE output to the OSS Image Uploader node
3. Configure your OSS credentials and settings
4. Run the workflow
5. The node will output the complete OSS URL of the uploaded file

## Security Notes

- Keep your OSS access keys secure
- Consider using STS tokens for production use
- Set appropriate bucket permissions
- Use HTTPS endpoints for secure uploads

## Compatibility

- Tested with ComfyUI
- Compatible with VideoHelperSuite for video uploads
- Supports common image formats: PNG, JPG, JPEG, WebP
- Supports common video formats: MP4, AVI, MOV, WebM, MKV
- Supports common audio formats: WAV, MP3, FLAC
