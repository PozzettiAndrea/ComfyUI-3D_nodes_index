# ComfyUI-GCP-Storage

## Description:

A custom node for ComfyUI to save a image to your Google Cloud Platform Storage Bucket.

## Installation:

Use `git clone https://github.com/Fantaxico/ComfyUI-GCP-Storage.git` in your ComfyUI custom nodes directory

## Usage

Requires a `config.json` file that has `{ "gcp_service_json_path": "xxx" }` set to your Service Account json file path (for reference see https://cloud.google.com/iam/docs/keys-create-delete).

Add the node to your workflow and enter a file name and your bucket name.

The node saves your image locally in `comfyUi/outputs` and then uploads it to GCP.
