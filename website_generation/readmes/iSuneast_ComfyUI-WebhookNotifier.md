# ComfyUI-WebhookNotifier

Webhook notification plugin for ComfyUI, used to send webhook notifications when workflow execution is completed.

## Features

- Automatically sends webhook notifications after workflow execution
- Supports custom JSON data in notifications
- Provides two nodes:
  - `Webhook Notifier`: connects to an `IMAGE` output as trigger
  - `Webhook Notifier (Any)`: accepts any input type as trigger (IMAGE, STRING, LATENT, VHS_FILENAMES, etc.)

## Installation

1. Clone this repository to ComfyUI's `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/iSuneast/ComfyUI-WebhookNotifier.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Restart ComfyUI service

## Usage

The plugin provides two Webhook Notifier nodes:

### Webhook Notifier

Connects to an `IMAGE` output to send notifications when image generation is complete.

Parameters:
- `images`: Trigger input (required, connects to an `IMAGE` output; the data is **not** read or sent, only used as a trigger)
- `webhook_url`: Webhook URL address (required, default is "https://example.com/webhook")
- `additional_info`: Additional information in JSON format (optional, default is empty)

### Webhook Notifier (Any)

Accepts any input type to send notifications when execution is complete.

Parameters:
- `any_input`: Trigger input (required, accepts any type such as IMAGE, STRING, LATENT, VHS_FILENAMES, etc.; the data is **not** read or sent, only used as a trigger)
- `webhook_url`: Webhook URL address (required, default is "https://example.com/webhook")
- `additional_info`: Additional information in JSON format (optional, default is empty)

## Webhook Notification Format

The WebhookNotifier node sends the contents of the `additional_info` parameter as the JSON payload. **Note that the input data itself is not included in the webhook payload**. The node only requires the `any_input` connection to trigger the notification when execution is complete.

For example, if you provide the following in the additional_info field:

```json
{
  "status": "completed",
  "custom_field1": "Custom value 1",
  "custom_field2": "Custom value 2"
}
```

This exact JSON will be sent to the webhook URL. If the additional_info field is left empty or contains invalid JSON, an empty JSON object `{}` will be sent.

## Example

- **Webhook Notifier**: Connect an image output to the `images` input, set your webhook URL, and optionally provide additional information in JSON format.
- **Webhook Notifier (Any)**: Connect any output (IMAGE, STRING, LATENT, VHS_FILENAMES, etc.) to the `any_input`, set your webhook URL, and optionally provide additional information.

When the upstream node completes execution, the webhook will send a POST request to the specified URL with your custom data.

## Debugging

The node prints debug information to the console, including whether the webhook notification was sent successfully:
- "Webhook notification started in background" when the webhook thread is started
- "Webhook notification successful: [status code]" for successful requests
- "Webhook notification failed: [status code] - [response text]" for failed requests
- "Error sending webhook: [error message]" for exceptions
- "Error preparing webhook: [error message]" if there are errors before sending

## License

MIT

## Contributions

Issues and pull requests are welcome!