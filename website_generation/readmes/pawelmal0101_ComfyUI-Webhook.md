# ComfyUI Webhook Notifier

A simple ComfyUI custom node that sends webhook notifications when images are generated. Perfect for integrating your image generation workflow with external services or your own backend.

## Features

- Sends webhook notifications when images are generated
- Attaches the generated image to the webhook request
- Includes customizable metadata and external ID support
- Saves generated images locally with metadata

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui-webhook-http
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Restart ComfyUI

## Usage

1. Add the "Webhook Image Saver" node to your workflow
2. Connect it to your image generation output
3. Configure the webhook settings:
   - `webhook_url`: Your endpoint that will receive the notification
   - `filename_prefix`: Prefix for saved image files (default: "ComfyUI")
   - `metadata`: Optional JSON metadata to include with the webhook
   - `external_uid`: Optional identifier for tracking generations or sessions

## Webhook Payload

The webhook endpoint will receive a POST request with the following data:

```json
{
    "metadata": "your_custom_metadata",
    "external_uid": "your_tracking_id",
    "images": [
        {
            "filename": "ComfyUI_00001_.png",
            "subfolder": "ComfyUI",
            "type": "output"
        }
    ]
}
```

The generated image will be attached as a file in the request.

## Example Usage

Here's a basic example of how to use the node in your workflow:

1. Connect your image generation output to the "Webhook Image Saver" node
2. Set your webhook URL (e.g., `https://api.yourservice.com/webhook`)
3. Add any custom metadata or tracking IDs
4. Run your workflow - the webhook will be triggered automatically when images are generated

## License

Apache License 2.0
