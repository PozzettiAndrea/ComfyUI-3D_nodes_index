# ComfyUI Cloud Storage Extension

This extension adds cloud storage support to ComfyUI, allowing you to save and load images, masks, and videos directly from cloud storage services. Currently supports Aliyun OSS and AWS S3.

## Features

- **Cloud Storage Support**
  - Aliyun OSS
  - AWS S3
  - Extensible architecture for future storage providers

- **Available Nodes**
  - `Save Image To Cloud`: Save images to cloud storage
  - `Load Image From Cloud`: Load images from cloud storage
  - `Load Mask From Cloud`: Load image masks from cloud storage
  - `Load Video From Cloud`: Load and process videos from cloud storage

## Installation

1. Install the required dependencies:
   ```bash
   pip install oss2  # For Aliyun OSS
   pip install boto3 # For AWS S3
   ```

2. Clone this repository into your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/yourusername/ComfyUI-CloudStorage
   ```

## Node Documentation

### Save Image To Cloud
Saves images to cloud storage with optional metadata.

**Inputs:**
- `images`: Images to save
- `storage_type`: Storage service type ('oss' or 's3')
- `endpoint`: Storage service endpoint
- `bucket`: Storage bucket name
- `access_key_id`: Access key ID
- `access_key_secret`: Access key secret
- `filename_prefix`: Prefix for generated filenames
- `prefix`: Storage path prefix

**Optional:**
- `region`: Region for S3 storage (default: us-east-1)

**Outputs:**
- `urls`: Semicolon-separated list of uploaded image URLs

### Load Image From Cloud
Loads images from cloud storage.

**Inputs:**
- `storage_type`: Storage service type
- `endpoint`: Storage service endpoint
- `bucket`: Storage bucket name
- `access_key_id`: Access key ID
- `access_key_secret`: Access key secret
- `file_key`: File path in storage

**Optional:**
- `region`: Region for S3 storage

**Outputs:**
- `IMAGE`: Loaded image tensor
- `MASK`: Image mask tensor

### Load Mask From Cloud
Loads image masks from cloud storage with channel selection.

**Inputs:**
- Same as Load Image From Cloud, plus:
- `channel`: Color channel to use as mask (alpha/red/green/blue)

**Outputs:**
- `MASK`: Selected channel mask tensor

### Load Video From Cloud
Loads and processes videos from cloud storage.

**Inputs:**
- Same as Load Image From Cloud, plus:
- `force_rate`: Force specific frame rate (0 for original)
- `custom_width`: Custom width (0 for original)
- `custom_height`: Custom height (0 for original)
- `frame_load_cap`: Maximum number of frames to load
- `skip_first_frames`: Number of frames to skip from start
- `select_every_nth`: Select every nth frame

**Optional:**
- `vae`: VAE model for latent conversion
- `format`: Output format (default/latent)

**Outputs:**
- `IMAGE`: Video frames tensor
- `frame_count`: Number of frames
- `audio`: Audio data (if available)
- `video_info`: Video metadata

## Configuration Examples

### Aliyun OSS
```python
{
    "storage_type": "oss",
    "endpoint": "oss-cn-beijing.aliyuncs.com",
    "bucket": "your-bucket",
    "access_key_id": "your-access-key-id",
    "access_key_secret": "your-access-key-secret",
    "prefix": "comfyui/"
}
```

### AWS S3
```python
{
    "storage_type": "s3",
    "endpoint": "https://s3.amazonaws.com",  # Optional for standard S3
    "bucket": "your-bucket",
    "access_key_id": "your-access-key-id",
    "access_key_secret": "your-access-key-secret",
    "region": "us-east-1",
    "prefix": "comfyui/"
}
```

## Security Considerations

1. Never commit your cloud storage credentials to version control
2. Use appropriate bucket policies and access controls
3. Consider using temporary credentials or role-based access
4. Ensure your storage buckets are properly configured for public/private access

## Error Handling

The extension includes comprehensive error handling for:
- Invalid credentials
- Network issues
- File access problems
- Invalid file formats
- Storage service errors

Error messages are descriptive and include specific details to help troubleshoot issues.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.
