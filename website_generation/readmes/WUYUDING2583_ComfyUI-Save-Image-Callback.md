# Save Image With Callback

A custom ComfyUI node that extends the Save Image node with callback functionality.

## Overview

This node enables integration between ComfyUI and external services by adding callback capabilities to the image saving process. When an image is saved, the node automatically call your webhook with your specified URL with custom data.

## Use Cases

- Integration with external image storage services
- Automated post-processing workflows
- Real-time notifications when images are generated
- Custom image handling pipelines

## Installation

1. Clone this repository to your `ComfyUI/custom_nodes` directory
2. Restart ComfyUI
3. The node will appear in your node list as "Save Image With Callback"

## Usage

1. Add the "Save Image With Callback" node to your workflow
2. Export your workflow as an API
3. When calling the ComfyUI API, structure your request body as follows:
4. When the image is saved, the node will call your webhook with your specified URL with callback_data.

```json
{
    "prompt": prompt_data,
    "extra_data": {
        "extra_pnginfo": {
            "callback_data": {
                "callback_url": "http://your_callback_url",
                "custom_field1": "value1",
                "custom_field2": "value2"
            }
        }
    }
}
```

### Parameters

- `prompt_data`: Your exported ComfyUI workflow prompt
- `callback_url`: The URL that will be called after image saving
- Additional fields in `callback_data` will be included in the callback request
