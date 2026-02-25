# ComfyUI Reve API Integration Node

A unified ComfyUI custom node that integrates all Reve API endpoints (Create, Edit, Remix) into a single, dynamic node with operation-specific inputs and seamless operation switching.

<img width="1447" height="727" alt="image" src="https://github.com/user-attachments/assets/e2385531-c9fd-43e7-b924-dd07c66aecad" />


## ✅ Current Status

**The Reve API is now working!** This integration has been updated with the correct API endpoints and is fully functional.

The API uses the endpoints `/v1/image/create`, `/v1/image/edit`, and `/v1/image/remix`. Authentication works with API keys in the format `papi.xxxxx`.

## Features

- **Unified Interface**: Single node handles all three operations (Create, Edit, Remix)
- **Dynamic Inputs**: Show/hide parameters based on selected operation type
- **Consistent Outputs**: Standardized output format across all operations
- **Error Handling**: Comprehensive error management with operation-specific context
- **Credit Tracking**: Integrated credit monitoring and usage tracking
- **Verbose Logging**: Optional detailed logging for debugging and monitoring API interactions

## Operations

### Create
Generate images from text prompts.
- **Cost**: 18 credits per generation
- **Inputs**: prompt, aspect_ratio, version, output_format

### Edit
Modify existing images with text instructions.
- **Cost**: 30 credits per edit
- **Inputs**: prompt, reference_image, version, output_format

### Remix
Combine multiple images with text guidance.
- **Cost**: 30 credits per remix
- **Inputs**: prompt, reference_images (1-4), aspect_ratio, version, output_format

## Installation

1. Clone or download this repository to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/lum3on/ComfyUI_Reve-API.git
   ```

2. Install dependencies:
   ```bash
   cd ComfyUI_Reve-API
   pip install -r requirements.txt
   ```

3. Restart ComfyUI

## Usage

1. Add the "Reve API (Create/Edit/Remix)" node to your workflow
2. Enter your Reve API key in the api_key field
3. Select the desired operation from the dropdown
4. Configure parameters based on the operation:
   - **Create**: Enter prompt and select aspect ratio
   - **Edit**: Connect reference image and enter editing instructions
   - **Remix**: Connect reference images (1-4) and enter combination prompt
5. Execute the workflow

## Outputs

The node provides five outputs:
- **image**: Generated/edited image tensor
- **metadata**: JSON string with operation details
- **request_id**: Unique identifier for the API request
- **credits_used**: Number of credits consumed
- **credits_remaining**: Remaining credit balance

## API Key Management

Your Reve API key is entered directly in the node's api_key field. The key is required for all operations and should be in the format `papi.xxxxx`.

## Verbose Logging

The node includes an optional verbose logging feature that provides detailed information about API interactions, performance metrics, and debugging information.

### Enabling Verbose Logging

1. In the node interface, set the `verbose_logging` parameter to `True`
2. Check the ComfyUI console for detailed log output

### What Gets Logged

When verbose logging is enabled, the following information is logged to the console:

- **Operation Start**: Details about the operation being performed
- **Request Parameters**: Information about the API request (without sensitive data)
- **API Response**: Request ID, credits used/remaining, processing time
- **Performance Metrics**: Total processing time, API call time, image processing time
- **Error Details**: Detailed error information when operations fail

### Example Verbose Output

```
2025-09-16 12:38:26,317 - nodes.reve_api_node.verbose - INFO - 🚀 Starting Reve API CREATE operation
{
  "prompt_length": 21,
  "operation": "create",
  "version": "latest",
  "aspect_ratio": "16:9",
  "output_format": "png"
}

2025-09-16 12:38:28,842 - nodes.reve_api_node.verbose - INFO - 🔍 Reve API CREATE Operation Complete
{
  "operation": "create",
  "request_id": "req-abc123",
  "credits_used": 18,
  "credits_remaining": 482,
  "processing_time_seconds": 2.5,
  "success": true
}

2025-09-16 12:38:28,845 - nodes.reve_api_node.verbose - INFO - ✅ Reve API CREATE operation completed successfully
{
  "total_processing_time_seconds": 2.528,
  "api_call_time_seconds": 2.5,
  "image_processing_time_seconds": 0.028
}
```

### Benefits of Verbose Logging

- **Debugging**: Identify issues with API calls or image processing
- **Performance Monitoring**: Track processing times and optimize workflows
- **Credit Tracking**: Monitor credit usage across operations
- **Audit Trail**: Keep detailed records of API interactions
- **Troubleshooting**: Get detailed error information for support

### Note on Performance

Verbose logging has minimal performance impact when disabled (default). When enabled, it adds negligible overhead for logging operations.

## Error Handling

The node provides detailed error messages for common issues:
- Invalid API key
- Insufficient credits
- Content policy violations
- Rate limiting
- Network errors

## Requirements

- ComfyUI
- Python 3.8+
- PyTorch (included with ComfyUI)
- Pillow (included with ComfyUI)
- requests
- numpy (included with ComfyUI)

## Troubleshooting

### Node doesn't appear in ComfyUI
- Check that all dependencies are installed
- Verify the node is in the correct custom_nodes directory
- Check ComfyUI console for error messages

### API errors
- Verify your API key is correct
- Check your credit balance
- Ensure images meet size requirements (max 10MB for edit, 5MB each for remix)

### Image conversion errors
- Ensure input images are valid ComfyUI image tensors
- Check image dimensions are reasonable (512x512 to 2048x2048 recommended)

## Support

For issues related to:
- **Node functionality**: Check the GitHub repository issues
- **Reve API**: Contact Reve API support
- **ComfyUI integration**: Check ComfyUI documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog

### v1.2.0
- **CHANGED**: API key is now required in the node interface - no more environment variable setup needed
- **REMOVED**: Environment variable fallback for API key (REVE_API_KEY)
- **IMPROVED**: Simplified setup process - users just paste their API key directly in the node
- **ENHANCED**: Better API key validation with clear error messages

### v1.1.1
- **FIXED**: HTTP 400 error in edit operation by using correct `edit_instruction` parameter
- **REMOVED**: Unsupported `aspect_ratio` parameter from edit operation
- **IMPROVED**: Error handling to show detailed API error messages instead of generic HTTP codes
- **ENHANCED**: Debugging capabilities with better error message extraction

### v1.1.0
- **NEW**: Verbose logging functionality for debugging and monitoring
- **CHANGED**: Simplified node outputs to only return image and metadata
- **ENHANCED**: Credit tracking and performance metrics now available via verbose logging
- **IMPROVED**: Better structured metadata output with JSON formatting

### v1.0.0
- Initial release
- Unified node supporting Create, Edit, and Remix operations
- Dynamic input system
- Comprehensive error handling
- Credit tracking and monitoring
