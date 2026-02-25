# ComfyUI Attome S3 Nodes

Custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that enable seamless loading and saving of media files (images, videos, audio, text) directly from/to AWS S3 or S3-compatible storage services.

![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Nodes-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

- **Optional S3 Config** - Use `env.txt` defaults or override with config node when needed
- **Environment Configuration** - Load default S3 credentials from `env.txt` file (cached for performance)
- **Smart S3 Key Handling** - Returns proper empty resources (512×512 images, 1024-sample audio) when s3_key is empty
- **Automatic File Extensions** - File extensions auto-match selected format (PNG/JPEG/WEBP, WAV/MP3, etc.)
- **Metadata Control** - Optional workflow metadata embedding in images
- **Batch Saving** - Save multiple images/files at once with automatic numbering (`output_1.png`, `output_2.png`, etc.)
- **Dynamic Filenames** - Use placeholders like `%date%`, `%time%`, `%random%` in your file paths
- **List Output** - All save nodes return a list of S3 URIs for easy downstream processing
- **Image Operations** - Load/Save PNG, JPEG, WEBP with quality settings
- **Video Operations** - Load/Save MP4 with frame extraction options
- **Audio Operations** - Load/Save WAV, MP3, FLAC, OGG formats
- **Text Operations** - Load/Save text files with encoding support
- **S3-Compatible** - Works with AWS S3, Rustfs, MinIO, DigitalOcean Spaces, Backblaze B2, etc.


## Nodes

| Node | Description |
|------|-------------|
| **Attome S3 Config** | Configure AWS credentials, region, bucket, and optional endpoint URL |
| **Attome S3 Load Image** | Load image from S3, outputs IMAGE + MASK tensors |
| **Attome S3 Save Image** | Save image to S3 (PNG/JPEG/WEBP, configurable quality) |
| **Attome S3 Load Video** | Load video from S3, outputs frames as IMAGE batch + FPS |
| **Attome S3 Save Video** | Save image batch as video to S3 (configurable FPS/codec) |
| **Attome S3 Load Audio** | Load audio from S3, outputs AUDIO dict |
| **Attome S3 Save Audio** | Save audio to S3 (WAV/MP3/FLAC/OGG) |
| **Attome S3 Load Text** | Load text file from S3 |
| **Attome S3 Save Text** | Save text content to S3 |

<img width="1016" height="748" alt="image" src="https://github.com/user-attachments/assets/0aa82b3c-2556-4894-a65d-05765bbcc6d1" />


## Installation


### Method 1: Portable ComfyUI (Windows)

```bash
cd ComfyUI_windows_portable\ComfyUI\custom_nodes
git clone https://github.com/attome-ai/Comfyui_Attome_S3.git
cd Comfyui_Attome_S3
..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
```

## Requirements

- Python 3.10+
- ComfyUI
- boto3
- Pillow (usually pre-installed with ComfyUI)
- torch (usually pre-installed with ComfyUI)
- numpy (usually pre-installed with ComfyUI)
- torchaudio (for audio operations)
- opencv-python (for video operations)

## Usage

### Basic Workflow

**Option 1: Use env.txt (Recommended for single environment)**

1. Edit `env.txt` with your credentials (see [Using env.txt](#using-envtxt-for-default-configuration))
2. Use any Load/Save node directly - no config node needed!
3. Specify the S3 key (path) for your file

**Option 2: Use Config Node (For multiple environments or overrides)**

1. Add **Attome S3 Config** node
2. Enter your AWS credentials:
   - `aws_access_key_id`: Your AWS access key
   - `aws_secret_access_key`: Your AWS secret key
   - `region_name`: AWS region (e.g., `us-east-1`)
   - `bucket_name`: Your S3 bucket name
   - `endpoint_url`: (Optional) Custom endpoint for S3-compatible services
3. Connect the `s3_config` output to any Load/Save node
4. Specify the S3 key (path) for your file

### Example: Load Image from S3

**Without Config Node (using env.txt):**
```
[Attome S3 Load Image] --> [Your Workflow]
         |
         +-- s3_key: "images/input.png"
```

**With Config Node:**
```
[Attome S3 Config] --> [Attome S3 Load Image] --> [Your Workflow]
                             |
                             +-- s3_key: "images/input.png"
```

### Example: Save Generated Image to S3

```
[Your Workflow] --> [Attome S3 Save Image] <-- [Attome S3 Config]
                            |
                            +-- s3_key: "outputs/result.png"
                            +-- format: "PNG"
                            +-- quality: 95
                            +-- save_metadata: true (or false)
```

### Workflow Metadata Control

The **save_metadata** parameter controls whether ComfyUI workflow information is embedded in saved files:

**✅ `save_metadata: true` (Default)**
- Embeds complete workflow data (nodes, connections, parameters) in file metadata
- Allows recovery of the exact workflow that generated the file
- **Perfect for debugging and testing workflows**
- Slightly larger file size due to embedded JSON

**❌ `save_metadata: false`**
- Saves clean files without any workflow information
- Smaller file sizes
- No exposed workflow data when sharing publicly
- **Perfect for production outputs**

**Format-Specific Implementation:**

| Format | Metadata Storage Method | Notes |
|--------|------------------------|-------|
| **PNG Images** | PNG text chunks (`pnginfo`) | Standard method, works with all PNG viewers |
| **MP4 Videos** | MP4 metadata tags (`©cmt`, `desc`) | Requires `mutagen` library (optional) |
| **MP3/FLAC Audio** | ID3/Vorbis comment tags | Requires `mutagen` library (optional) |
| **Text Files** | Comment header (`# ComfyUI Workflow...`) | Prepended as comments at file start |
| **JPEG/WEBP/WAV/OGG** | Not supported | Metadata will be silently skipped |

**Use Cases:**
- **Development/Testing**: Keep `save_metadata: true` to easily recover and debug workflows
- **Production/Sharing**: Set `save_metadata: false` for clean, compact files
- **Public APIs**: Disable to prevent exposing your workflow logic

**Optional Dependency:**
```bash
pip install mutagen  # For video/audio metadata support
```

### Using with S3-Compatible Services

For MinIO, DigitalOcean Spaces, Backblaze B2, or other S3-compatible services, set the `endpoint_url` parameter:

| Service | Endpoint URL Example |
|---------|---------------------|
| MinIO | `http://localhost:9000` |
| DigitalOcean Spaces | `https://nyc3.digitaloceanspaces.com` |
| Backblaze B2 | `https://s3.us-west-000.backblazeb2.com` |
| Cloudflare R2 | `https://<account_id>.r2.cloudflarestorage.com` |


### Using env.txt for Default Configuration

You can use the `env.txt` file in the plugin directory to set default values for the S3 Config node. This is useful for avoiding repeated credential entry.

1. Edit `env.txt` in the plugin directory with your credentials:

```
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
REGION_NAME=us-east-1
BUCKET_NAME=your_bucket_name_here
ENDPOINT_URL=
```

2. Restart ComfyUI - all S3 nodes will now use these as defaults automatically (no config node required!)

**Benefits:**
- ✅ No need to wire config nodes in every workflow
- ✅ Cached in memory - only reads file once per session
- ✅ Can still override with config node when needed


### Empty S3 Key Behavior

All load nodes intelligently handle empty `s3_key` values:

- **Empty Image**: Returns 512×512 black image (prevents division errors in nodes like IPAdapter)
- **Empty Video**: Returns single 512×512 black frame
- **Empty Audio**: Returns 1024-sample silent audio
- **Empty Text**: Returns empty string

This allows optional S3 resources in workflows without errors.

### Automatic File Extension Matching

Save nodes automatically adjust file extensions to match your format selection:

```
Path: "output"  + Format: WEBP  = Saved as: "output.webp"
Path: "output.png"  + Format: JPEG  = Saved as: "output.jpg"
```

**Supported Formats:**
- Images: PNG, JPEG (.jpg), WEBP
- Audio: WAV, MP3, FLAC, OGG
- Video: MP4 (always)


## Troubleshooting

### "No module named 'boto3'"

```bash
pip install boto3
```

### "No module named 'cv2'" (Video nodes)

```bash
pip install opencv-python
```

### "No module named 'torchaudio'" (Audio nodes)

```bash
pip install torchaudio
```

### "Access Denied" errors

1. Verify your AWS credentials are correct
2. Check the IAM user has the required S3 permissions
3. Ensure the bucket name and region are correct
4. For S3-compatible services, verify the endpoint URL

### Nodes not appearing in ComfyUI

1. Restart ComfyUI completely
2. Check the console for import errors
3. Verify all dependencies are installed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - The amazing node-based Stable Diffusion UI
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK for Python

## Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search [existing issues](https://github.com/attome-ai/ComfyUI_Attome_S3/issues)
3. Open a new issue with:
   - ComfyUI version
   - Python version
   - Full error message
   - Steps to reproduce
