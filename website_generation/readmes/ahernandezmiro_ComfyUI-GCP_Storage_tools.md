# ComfyUI Custom Nodes for GCP

This repository contains a module with two custom nodes for [ComfyUI](https://github.com/ComfyUI/ComfyUI) that enable seamless interaction with Google Cloud Platform (GCP). These nodes allow you to:

1. **Read Images from GCP**: Fetch images from a GCP bucket.
2. **Write Images to GCP**: Upload images to a GCP bucket.

Both nodes support authentication using your GCP credentials file in JSON format.

---

## Features

- Specify the bucket name and the image file name and path to read/write from.
- Authentication via GCP credentials file.

---

## Installation

1. Clone this repository into your `custom_nodes` directory within your ComfyUI installation:
   ```bash
   git clone https://github.com/ahernandezmiro/ComfyUI-GCP_Storage_tools /path/to/ComfyUI/custom_nodes/gcp_nodes
   ```

2. Install the required dependencies:
   ```bash
   pip install google-cloud-storage
   ```

3. Restart ComfyUI.

---

## Usage

1. **Prepare Your GCP Credentials**
   - Obtain your GCP credentials in JSON format from the [GCP Console](https://console.cloud.google.com/).
   - Save the credentials file locally on your system.

2. **Set the Credentials Directory**
   - Each node requires the full path to your GCP credentials file. This can be specified in the node's input fields.

3. **Use the Nodes in ComfyUI**
   - Add the "Read Images from GCP" or "Write Images to GCP" node to your workflow.
   - Configure the required fields such as bucket name, file name/path, and credentials file directory.

---

## Example Workflow

### Reading an Image from GCP
1. Add the "Read Images from GCP" node.
2. Configure the following:
   - **Bucket Name**: Your GCP bucket name.
   - **File Path**: Path to the image file within the bucket.
   - **File Name**: Name of the image file within the bucket path.
   - **Credentials File Path**: Full path to your GCP credentials JSON file.
3. Connect the node to your workflow to fetch and use the image.

### Writing an Image to GCP
1. Add the "Write Images to GCP" node.
2. Configure the following:
   - **Bucket Name**: Your GCP bucket name.
   - **Destination File Path**: Path where the image should be stored in the bucket.
   - **File Name**: Name of the image file to be stored in the bucket.
   - **Credentials File Path**: Full path to your GCP credentials JSON file.
3. Connect the node to your workflow to upload images to GCP.

---

## Requirements

- Python 3.7+
- `google-cloud-storage` Python library
- GCP account with access to a storage bucket

---

## Troubleshooting

### Missing or Incorrect Credentials
- Ensure your GCP credentials file is in JSON format.
- Verify the file path specified in the node's input.

### Permission Errors
- Ensure your GCP account has the appropriate permissions for the bucket.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality of these nodes.

---

## Acknowledgments

- Built with [ComfyUI](https://github.com/ComfyUI/ComfyUI)
- Powered by [Google Cloud Storage](https://cloud.google.com/storage)
