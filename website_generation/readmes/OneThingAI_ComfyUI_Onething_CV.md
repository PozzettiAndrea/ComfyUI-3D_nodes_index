# ComfyUI OneThing CV Node

This custom node for ComfyUI allows you to get detailed text descriptions of images using the OneThing AI Vision API. The node integrates with OneThing AI's powerful vision models to provide detailed descriptions of image content.

## Features

- Upload and process images in ComfyUI
- Get detailed descriptions of image content using OneThing AI's Vision API
- Configurable model selection and parameters
- Built-in retry mechanism for robust API communication
- Easy integration with existing ComfyUI workflows

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/OnethingAI/ComfyUI_Onething_CV.git
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Obtain an API key from OneThing AI
2. In ComfyUI, you'll find a new node called "OneThingAI Image Understanding" under the "OneThingAI/CV" category
3. Connect an image output to the node's image input
4. Configure the node parameters (see Parameters section below)
5. Run the workflow to get the image description

## Parameters

### Required Parameters

- `image`: The input image to be described (IMAGE type)
- `api_key`: Your OneThing AI API key (STRING type)
- `model`: The model to use for image understanding (default: "gpt4o")
- `retries`: Number of retry attempts for API calls (default: 3, range: 0-5)
- `timeout`: API request timeout in seconds (default: 20, range: 5-100)
- `max_tokens`: Maximum number of tokens in the response (default: 500, range: 100-10000, step: 100)

## Output

- `STRING`: A detailed description of the image content

## Example Workflow

1. Load Image Node -> OneThingAI Image Understanding Node
2. Configure the parameters:
   ```
   api_key: "your-api-key-here"
   model: "gpt4o"
   retries: 3
   timeout: 20
   max_tokens: 500
   ```
3. The node will return a detailed description of the image content

## Error Handling

The node includes robust error handling:
- Automatic retries for failed API calls
- Exponential backoff strategy
- Timeout protection
- Detailed error messages

Common error status codes that trigger retries:
- 429: Too Many Requests
- 500: Internal Server Error
- 502: Bad Gateway
- 503: Service Unavailable
- 504: Gateway Timeout

## Notes

- Make sure to keep your API key secure and never share it publicly
- The API has rate limits, please check OneThing AI's documentation for details
- The node requires an active internet connection to work
- Larger max_tokens values will result in longer, more detailed descriptions but may take more time to process
- The retry mechanism helps handle temporary API issues automatically
- If you encounter persistent errors, try:
  1. Increasing the timeout value
  2. Checking your API key
  3. Verifying your internet connection
  4. Ensuring the image is in a supported format

## Support

If you encounter any issues or have questions:
1. Check the error message returned by the node
2. Verify your API key and parameters
3. Check OneThing AI's API status and documentation
4. Open an issue in the GitHub repository

## License

This project is licensed under the MIT License - see the LICENSE file for details. 