# ComfyUI-Azure-Blob-Storage

## Description

ComfyUI-Azure-Blob-Storage integrates [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/) within [ComfyUI](https://github.com/comfyanonymous/ComfyUI). This open-source project offers custom nodes that make it easy to load and save images, videos, and checkpoint models directly from Azure blob containers through the ComfyUI graph interface.

Find ```ComfyUI-Azure-Blob-Storage``` authored by ```l20richo``` and proceed with its installation.

## Getting Started
1. Install by either : 
    - search for ```ComfyUI-Azure-Blob-Storage``` authored by ```l20richo``` and proceed with its installation.
    - Clone this repo into custom_nodes in Comfy UI 

2. Setup the variable
Set up your `.env` file 
    - Copy `.env.example` into `.env` and 

    ```
    AZURE_STORAGE_ACCOUNT_NAME = ""
    AZURE_STORAGE_CONNECTION_STRING = ""
    AZURE_STORAGE_CONTAINER_NAME = ""
    BLOB_INPUT_DIR = ""
    BLOB_OUTPUT_DIR = ""
    ```
    - Visit (https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string) for more informations about these credentials



## Features 
ComfyUI nodes to:
- [x] standalone download/upload file from/to Azure Blob Storage buckets
- [x] load/save image from/to Amazon Azure Blob Storage buckets
- [x] save VHS (VideoHelperSuite) video files to Azure Blob Storage buckets
- [x] install ComfyUI-Azure-Blob-Storage from [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- [ ] load checkpoints from Azure Blob Storage buckets
- [ ] load video from Azure Blob Storage buckets
## Credits
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [ComfyS3](https://github.com/TemryL/ComfyS3.git)
