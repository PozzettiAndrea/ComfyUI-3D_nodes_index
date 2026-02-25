# ComfyUI GCP Cloud Storage Integration

This custom node package provides seamless integration between ComfyUI and Google Cloud Platform (GCP) Cloud Storage, enabling you to run ComfyUI without relying on instance disk storage.
decouple your storage needs from local disks by leveraging GCP's scalable and reliable Cloud Storage service. Models can be saved and loaded directly from Cloud Storage, while outputs and temporary files are automatically synced. 

# Tips & Tricks:
- Initial model loading may take time depending on your network speed and model size.
- The model file is cached locally after the first download, so subsequent uses will be faster.
- To save the output to Cloud storage, use the "GCP Storage Upload Image" node in your workflow.
- File saving supports 2 different naming formats to keep the naming unique and organized. Save it with a timestamp or with ComfyUI's standard naming with incremental numbers.
- "GCP Storage Upload Image" node requires user to pick the file naming format, timestamp or ComfyUI standard naming. * You will encounter error if you leave it blank.*

## Features

- 🚀 **Transparent Storage**: Automatically sync files between local cache and Cloud Storage
- 📁 **Smart Caching**: Only download files when needed, cache locally for performance
- 🔄 **Bidirectional Sync**: Upload outputs and download models/inputs automatically
- 🎛️ **Node Integration**: Custom nodes for explicit Cloud Storage operations
- ⚙️ **Easy Setup**: Automated setup script for GCP configuration
- 📈 **Scalable**: Remove dependency on instance persistent storage

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   ComfyUI       │    │  Storage Manager │    │ GCP Cloud       │
│   Instance      │◄──►│   (Middleware)   │◄──►│ Storage         │
│                 │    │                  │    │                 │
│ ┌─────────────┐ │    │ ┌──────────────┐ │    │ ┌─────────────┐ │
│ │Local Cache  │ │    │ │Path Mapping  │ │    │ │   Buckets   │ │
│ │- models/    │ │    │ │- models/ →   │ │    │ │ - models/   │ │
│ │- temp/      │ │    │ │  gs://bucket │ │    │ │ - outputs/  │ │
│ │- cache/     │ │    │ │- outputs/ →  │ │    │ │ - inputs/   │ │
│ └─────────────┘ │    │ │  gs://bucket │ │    │ │ - user/     │ │
└─────────────────┘    │ └──────────────┘ │    │ └─────────────┘ │
                       └──────────────────┘    └─────────────────┘
```

## Quick Start

### 1. Automatic Setup

Run the automated setup script:

```bash
cd /home/prawegko/ComfyUI/custom_nodes/comfyui-gcp-storage/
./setup_gcp_storage.sh
```

This script will:
- Create a GCP Cloud Storage bucket
- Set up service account and permissions
- Generate credentials
- Install Python dependencies
- Create environment configuration

### 2. Manual Setup

If you prefer manual setup:

#### Install Dependencies
```bash
pip install google-cloud-storage google-auth google-auth-oauthlib google-auth-httplib2
```

#### Set Environment Variables
```bash
export GCP_PROJECT_ID="your-project-id"
export GCP_STORAGE_BUCKET="your-bucket-name"
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

#### Create Cloud Storage Bucket
```bash
gsutil mb gs://your-bucket-name
gsutil -m cp -r /dev/null gs://your-bucket-name/models/
gsutil -m cp -r /dev/null gs://your-bucket-name/outputs/
gsutil -m cp -r /dev/null gs://your-bucket-name/inputs/
gsutil -m cp -r /dev/null gs://your-bucket-name/user/
gsutil -m cp -r /dev/null gs://your-bucket-name/workflows/
```

### 3. Upload Existing Models

Transfer your existing models to Cloud Storage:

```bash
gsutil -m cp -r ./models/* gs://your-bucket-name/models/
```

### 4. Restart ComfyUI

Restart ComfyUI to load the new nodes and storage manager.

## Usage

### Automatic Mode (Recommended)

Once configured, the storage manager automatically:

1. **Downloads models** from Cloud Storage when ComfyUI needs them
2. **Uploads outputs** to Cloud Storage when generated
3. **Caches files locally** for performance
4. **Syncs changes** bidirectionally

No changes to your workflows are needed!

### Manual Node Usage

Use the custom nodes for explicit control:

#### GCP Storage Upload Image
- Upload generated images directly to Cloud Storage
- Configurable paths, formats, and quality

#### GCP Storage Download Image  
- Download images from Cloud Storage into workflows
- Supports gs:// URLs

#### GCP Storage Upload/Download Model
- Explicitly manage model files in Cloud Storage
- Useful for dynamic model loading

#### GCP Storage List Files
- List files in Cloud Storage buckets
- Browse available models and assets

#### Transfering existing model file to GCP Cloud Storage
- Use `gsutil` command line tool to upload existing model files to your Cloud Storage bucket.

```bash
gsutil -m cp -r ./models/* gs://your-bucket-name/models/
```
- You can also use the python script to handle selective migrate of model files when transferring larger number of model files. Due to large size of model files, it is recommended to use `gsutil` command line tool for faster transfer.
- To migrate the model file with selective_python.py script, run the following command:
```bash
python selective_python.py --source ./models/checkpoints/<safetensor model file> --destination gs://your-bucket-name/models/

```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GCP_PROJECT_ID` | Your GCP project ID | Yes |
| `GCP_STORAGE_BUCKET` | Cloud Storage bucket name | Yes |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account JSON key | Yes* |
| `GCP_CREDENTIALS_JSON` | Service account JSON as string | Yes* |

*Either `GOOGLE_APPLICATION_CREDENTIALS` or `GCP_CREDENTIALS_JSON` is required.

### Path Mappings

Default mappings from local paths to Cloud Storage:

```python
{
    "./models/": "models/",
    "./output/": "outputs/", 
    "./input/": "inputs/",
    "./user/": "user/",
    "./saved_workflows/": "workflows/",
    "./temp/": None  # Keep local only
}
```

### Bucket Structure

Recommended Cloud Storage bucket organization:

```
gs://your-bucket-name/
├── models/
│   ├── checkpoints/
│   ├── loras/
│   ├── vae/
│   └── ...
├── outputs/
│   ├── images/
│   └── videos/
├── inputs/
│   └── user_uploads/
├── user/
│   └── user_data/
└── workflows/
    └── saved_workflows/
```

## Authentication

### Service Account (Recommended)

1. Create a service account with Storage Admin role
2. Download the JSON key file
3. Set `GOOGLE_APPLICATION_CREDENTIALS` environment variable

### Application Default Credentials

For GCP Compute Engine instances with attached service accounts:

```bash
gcloud auth application-default login
```

### Custom Credentials

Set credentials as environment variable:

```bash
export GCP_CREDENTIALS_JSON='{"type": "service_account", ...}'
```

## Performance Optimization

### Caching Strategy

- **Smart Downloads**: Files only downloaded when accessed
- **Local Cache**: Frequently used files cached locally
- **Timestamp Checking**: Avoid unnecessary downloads
- **Temp Files**: Temporary files stay local

### Batch Operations

Use the storage manager for batch sync:

```python
from gcp_storage_manager import storage_manager

# Sync entire model directory
storage_manager.sync_directory('./models/', direction='download')

# Upload all outputs
storage_manager.sync_directory('./output/', direction='upload')
```

## Monitoring and Logging

Enable detailed logging:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

Monitor operations:
- Download/upload activities logged
- Cache hit/miss information
- Error handling and retries

## Troubleshooting

### Common Issues

#### Authentication Error
```
google.auth.exceptions.DefaultCredentialsError
```
**Solution**: Verify `GOOGLE_APPLICATION_CREDENTIALS` points to valid JSON key file.

#### Permission Denied
```
403 Forbidden
```
**Solution**: Ensure service account has Storage Admin role on the bucket.

#### Bucket Not Found
```
404 Not Found
```
**Solution**: Verify bucket name and ensure it exists in your project.

#### Import Error
```
ModuleNotFoundError: No module named 'google.cloud'
```
**Solution**: Install dependencies:
```bash
pip install google-cloud-storage
```

### Debug Mode

Enable debug logging for detailed troubleshooting:

```bash
export COMFYUI_GCP_DEBUG=true
```

### Test Configuration

Verify your setup:

```python
from gcp_storage_manager import get_storage_status
print(get_storage_status())
```

## Migration Guide

### From Local Storage

1. **Backup existing data**:
   ```bash
   tar -czf comfyui-backup.tar.gz models/ output/ input/ user/ saved_workflows/
   ```

2. **Run setup script**:
   ```bash
   ./setup_gcp_storage.sh
   ```

3. **Upload existing files**:
   ```bash
   gsutil -m cp -r models/* gs://your-bucket-name/models/
   gsutil -m cp -r output/* gs://your-bucket-name/outputs/
   gsutil -m cp -r input/* gs://your-bucket-name/inputs/
   ```

4. **Test the setup**:
   ```bash
   # Clear local cache and test download
   rm -rf models/*
   # Start ComfyUI - models should download automatically
   ```

### From Other Cloud Providers

Use `gsutil` to transfer from other cloud storage:

```bash
# From AWS S3
gsutil -m cp -r s3://source-bucket/* gs://target-bucket/

# From Azure
gsutil -m cp -r az://source-container/* gs://target-bucket/
```

## Security

### Best Practices

1. **Use Service Accounts**: Don't use personal credentials in production
2. **Minimal Permissions**: Grant only necessary Storage permissions
3. **Rotate Keys**: Regularly rotate service account keys
4. **Network Security**: Use VPC and private Google Access if needed
5. **Bucket Policies**: Configure bucket-level IAM policies

### Recommended IAM Roles

- `roles/storage.objectAdmin` - For read/write access to objects
- `roles/storage.legacyBucketReader` - For listing bucket contents

## Cost Optimization

### Storage Classes

- **Standard**: For frequently accessed files (models, active outputs)
- **Nearline**: For files accessed less than once per month
- **Coldline**: For archival of old outputs
- **Archive**: For long-term backup

### Lifecycle Policies

Set up automatic lifecycle management:

```bash
gsutil lifecycle set lifecycle.json gs://your-bucket-name
```

Example `lifecycle.json`:
```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30, "matchesPrefix": ["outputs/"]}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365, "matchesPrefix": ["temp/"]}
      }
    ]
  }
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the same license as ComfyUI.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review logs for error details
3. Create an issue with detailed information
4. Include configuration (without sensitive data)

---

**Note**: This integration is designed for production use on GCP. Ensure you understand GCP pricing and have appropriate monitoring in place.