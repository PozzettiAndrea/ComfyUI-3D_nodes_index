# VNTANA ComfyUI Custom Nodes

ComfyUI custom nodes for integrating with the VNTANA 3D content management platform.

## Features

- **Authentication**: Secure credential management with token caching
- **Product Search**: Search and browse products in VNTANA workspaces
- **Render Download/Upload**: Download renders as ComfyUI images and upload generated images
- **3D Model Download/Upload**: Download and upload 3D models with optimization presets
- **Workspace & Pipeline Management**: List available workspaces and optimization pipelines

**New to VNTANA nodes?** Check out the [User Guide](docs/USER_GUIDE.md) for step-by-step tutorials.

## Installation

### Method 1: ComfyUI Custom Nodes (Recommended)

1. Clone or copy this repository to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/VNTANA-3D/VNTANA-comfyui-node.git
   ```

2. Install dependencies:
   ```bash
   cd VNTANA-comfyui-node
   pip install -e .
   ```

3. Restart ComfyUI

### Method 2: Manual Installation

1. Copy the entire `VNTANA-comfyui-node` folder to `ComfyUI/custom_nodes/`
2. Install requirements: `pip install -r requirements.txt`
3. Restart ComfyUI

## Available Nodes

### VNTANACredentials

Configure and validate VNTANA authentication credentials.

**Inputs:**
- `email` (STRING, required): VNTANA account email
- `password` (STRING, required): VNTANA account password
- `organization_uuid` (STRING, required): Organization UUID
- `default_workspace_uuid` (STRING, optional): Default workspace for operations
- `base_url` (STRING, optional): API base URL (default: https://api-platform.vntana.com)

**Outputs:**
- `credentials` (VNTANA_CREDENTIALS): Credential object for other nodes

---

### VNTANASearchProducts

Search for products in a VNTANA workspace.

**Inputs:**
- `credentials` (VNTANA_CREDENTIALS, required)
- `workspace_uuid` (STRING, optional): Override default workspace
- `search_term` (STRING, optional): Search query
- `status` (COMBO: ALL/DRAFT/LIVE_PUBLIC/LIVE_INTERNAL/APPROVED)
- `limit` (INT, default: 10, range: 1-100)

**Outputs:**
- `product_uuids` (STRING list): UUIDs of matching products
- `product_names` (STRING list): Names of matching products
- `count` (INT): Total count of matches

---

### VNTANADownloadRender

Download product renders as ComfyUI images.

**Inputs:**
- `credentials` (VNTANA_CREDENTIALS, required)
- `product_uuid` (STRING, required): Product to download render from
- `workspace_uuid` (STRING, optional)

**Outputs:**
- `image` (IMAGE): ComfyUI image tensor [B,H,W,C]

---

### VNTANAUploadRender

Upload a ComfyUI-generated image as a product render.

**Inputs:**
- `credentials` (VNTANA_CREDENTIALS, required)
- `product_uuid` (STRING, required): Target product
- `image` (IMAGE, required): ComfyUI image to upload
- `workspace_uuid` (STRING, optional)
- `filename` (STRING, default: "render")
- `format` (COMBO: PNG/JPEG/WEBP)

**Outputs:**
- `success` (BOOLEAN)
- `blob_id` (STRING): ID of the uploaded blob

---

### VNTANADownloadModel

Download a 3D model file from VNTANA.

**Inputs:**
- `credentials` (VNTANA_CREDENTIALS, required)
- `product_uuid` (STRING, required)
- `format` (COMBO: GLB/USDZ/FBX/OBJ/STEP)
- `workspace_uuid` (STRING, optional)
- `output_directory` (STRING, optional): Save location

**Outputs:**
- `file_path` (STRING): Path to downloaded file
- `filename` (STRING): Name of the file
- `file_size` (INT): Size in bytes

---

### VNTANAUpload3DModel

Upload a 3D model to VNTANA with optimization.

**Inputs:**
- `credentials` (VNTANA_CREDENTIALS, required)
- `file_path` (STRING, required): Path to 3D model file
- `name` (STRING, required): Product name
- `pipeline_uuid` (STRING, required): Optimization pipeline
- `workspace_uuid` (STRING, optional)
- `optimization_preset` (COMBO: webOptimized/highQuality/mobile/preserveOriginal)
- `description` (STRING, optional)
- `status` (COMBO: DRAFT/LIVE_INTERNAL/LIVE_PUBLIC)

**Outputs:**
- `success` (BOOLEAN)
- `product_uuid` (STRING): Created product UUID
- `conversion_status` (STRING): Processing status

**Optimization Presets:**
- **webOptimized**: Draco compression, 50K polygons, 2K textures
- **highQuality**: No compression, 100K polygons, 4K textures
- **mobile**: Aggressive compression, 25K polygons, 1K textures
- **preserveOriginal**: Minimal processing

---

### VNTANAListWorkspaces

List available workspaces in the organization.

**Inputs:**
- `credentials` (VNTANA_CREDENTIALS, required)

**Outputs:**
- `workspace_uuids` (STRING list)
- `workspace_names` (STRING list)

---

### VNTANAListPipelines

List available optimization pipelines.

**Inputs:**
- `credentials` (VNTANA_CREDENTIALS, required)
- `workspace_uuid` (STRING, optional)

**Outputs:**
- `pipeline_uuids` (STRING list)
- `pipeline_names` (STRING list)

## Example Workflows

### 1. Download and Preview a Render

```
VNTANACredentials → VNTANASearchProducts → VNTANADownloadRender → PreviewImage
```

### 2. Generate and Upload a Render

```
VNTANACredentials ─┬→ VNTANASearchProducts → product_uuid ─┐
                   │                                        │
LoadImage → KSampler → VNTANAUploadRender ←────────────────┘
```

### 3. Upload a 3D Model

```
VNTANACredentials ─┬→ VNTANAListPipelines → pipeline_uuid ─┐
                   │                                        │
                   └→ VNTANAUpload3DModel ←────────────────┘
```

## Configuration

### Getting Your Credentials

1. Log in to your VNTANA account at https://platform.vntana.com
2. Navigate to Organization Settings to find your Organization UUID
3. Navigate to Workspace Settings to find Workspace UUIDs
4. Use your account email and password for authentication

### Security Notes

- Credentials are validated on first use
- Authentication tokens are cached for 5 minutes
- File uploads are validated for size (max 30GB) and type
- Filenames are sanitized to prevent path traversal attacks

## Development

### Running Tests

```bash
pip install pytest
pytest tests/
```

### Linting

```bash
pip install ruff
ruff check .
```

## Requirements

- Python 3.10+
- ComfyUI
- requests >= 2.28.0
- Pillow >= 9.0.0

## License

MIT License - see LICENSE file for details.

## Support

For issues and feature requests, please visit:
https://github.com/VNTANA-3D/VNTANA-comfyui-node/issues

For VNTANA platform documentation:
https://docs.vntana.com
