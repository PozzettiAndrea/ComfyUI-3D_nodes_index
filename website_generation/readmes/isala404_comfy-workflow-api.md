# ComfyUI Workflow API

HTTP API for ComfyUI with webhook-based workflow execution. Submit workflows via HTTP, receive real-time progress updates and outputs at your callback URL.

## Installation

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/isala404/comfy-workflow-api.git
pip install -r comfy-workflow-api/requirements.txt
```

## Use Cases

- **Backend Integration**: Run ComfyUI as a headless service behind your application
- **Batch Processing**: Submit multiple workflows and receive results asynchronously
- **Distributed Systems**: Decouple workflow submission from result handling
- **Mobile/Web Apps**: Trigger image generation from any HTTP client

## How It Works

```
Client                          ComfyUI                         Your Server
  │                                │                                │
  ├─── POST /api/webhook ─────────►│                                │
  │    (workflow + callback_url)   │                                │
  │                                │                                │
  │◄── {request_id, prompt_id} ────┤                                │
  │                                │                                │
  │                                ├── workflow.progress ──────────►│
  │                                ├── workflow.progress ──────────►│
  │                                ├── ...                          │
  │                                │                                │
  │                                ├── multipart (files) ──────────►│
  │                                │                                │
```

## Quick Start

### 1. Create a workflow using webhook nodes

Use **WebhookReceiver** → **WebhookTransformer** → **WebhookSend** to read inputs from HTTP and send outputs back:

```
                    ┌─► WebhookTransformer ──► CLIPTextEncode ──┐
WebhookReceiver ────┤   (extracts "prompt")                     ├──► KSampler ──► WebhookSend
                    └─► WebhookTransformer ──► VAEEncode ───────┘
                        (extracts "image")
```

### 2. Submit via HTTP

```bash
# Image-to-image example
curl -X POST http://localhost:8188/api/webhook \
  -F "workflow=@workflow.json" \
  -F "callback_url=http://your-server.com/webhook" \
  -F "prompt=turn it into a watercolor painting" \
  -F "image=@input.png"
```

### 3. Receive at your callback

Your server receives:
- **Progress events** (JSON): `{"event": "workflow.progress", "progress": {"value": 5, "max": 20}}`
- **Output files** (gzip multipart): Images, audio, video, etc.

## Nodes

### WebhookReceiver

Entry point for webhook workflows. Reads request configuration from the HTTP call.

| Output | Type | Description |
|--------|------|-------------|
| webhook_context | WEBHOOK_CONTEXT | Context for other webhook nodes |

### WebhookTransformer

Extracts a field from the HTTP request. Connects to any input type.

| Input | Description |
|-------|-------------|
| webhook_context | From WebhookReceiver |
| field | Field name to extract (e.g., "prompt") |
| default_value | Optional fallback if field missing |

| Output | Type | Description |
|--------|------|-------------|
| value | * (wildcard) | Extracted value, auto-typed |

**Type inference**: Strings are converted to INT, FLOAT, BOOLEAN when applicable. File uploads become IMAGE, AUDIO, VIDEO, MESH, or LATENT based on content type.

### WebhookSend

Sends outputs to the callback URL. Supports 5 output fields.

| Input | Description |
|-------|-------------|
| webhook_context | From WebhookReceiver |
| field_1..5 | Any ComfyUI type (IMAGE, AUDIO, STRING, etc.) |
| field_1..5_name | Names for each output |

**Encoding**: IMAGE→PNG, AUDIO→FLAC, VIDEO→MP4, MESH→GLB, LATENT→safetensors

## API Reference

### POST /api/webhook

| Field | Required | Description |
|-------|----------|-------------|
| workflow | Yes | Workflow JSON |
| callback_url | Yes | URL to receive events/outputs |
| auth_header | No | Auth header name |
| auth_value | No | Auth header value |
| timeout | No | HTTP timeout (default: 60s) |
| max_retries | No | Retry attempts (default: 3) |
| *custom fields* | No | Any field accessible via WebhookTransformer |

**Response:**
```json
{"request_id": "...", "prompt_id": "...", "status": "queued"}
```

### GET /api/webhook/status/{request_id}

Check request status.

### DELETE /api/webhook/{request_id}

Cancel a queued/running workflow.

## Webhook Events

| Event | Content-Type | Description |
|-------|--------------|-------------|
| workflow.started | application/json | Execution began |
| workflow.progress | application/json | Step progress (throttled 500ms) |
| workflow.completed | multipart/form-data (gzip) | Output files + metadata |
| workflow.error | application/json | Execution failed |

**Note**: Completion payload is gzip compressed. Decompress before parsing.

## Example

**workflow.json** (see `example_workflow.json`):
```json
{
  "10": {
    "class_type": "WebhookReceiver",
    "inputs": {"debug": true}
  },
  "11": {
    "class_type": "WebhookTransformer",
    "inputs": {"field": "prompt", "webhook_context": ["10", 0]}
  },
  "6": {
    "class_type": "CLIPTextEncode",
    "inputs": {"text": ["11", 0], "clip": ["4", 1]}
  },
  "...": "... rest of workflow ...",
  "12": {
    "class_type": "WebhookSend",
    "inputs": {"webhook_context": ["10", 0], "field_1": ["8", 0]}
  }
}
```

**Python client** (see `example_client.py`):
```python
import requests, json

# Load image for img2img
image_data = open("input.png", "rb").read()

response = requests.post(
    "http://localhost:8188/api/webhook",
    files={
        "workflow": (None, json.dumps(workflow), "application/json"),
        "callback_url": (None, "http://localhost:5001/webhook"),
        "prompt": (None, "make it look like a painting"),
        "image": ("input.png", image_data, "image/png"),
    }
)
```

## Testing

```bash
# Terminal 1: Start ComfyUI
python main.py

# Terminal 2: Run example client (image-to-image)
cd custom_nodes/comfy-workflow-api
python example_client.py sample_input.png "turn it into a watercolor painting"
```

A sample image (`sample_input.png`) is included in the repo for testing.

## License

MIT
