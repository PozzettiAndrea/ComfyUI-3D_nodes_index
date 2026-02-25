# ComfyUI Gemini Expanded API Node

This is a Google Gemini API integration node for ComfyUI, supporting text generation and image generation functions. With this node, you can directly use Google's Gemini 2.0 series models in your ComfyUI workflow.
Special Note: Regarding the error [ERROR]API call error: 'NoneType' object has no attribute 'parts', it means that the image or prompt you uploaded violates the "Generative AI Prohibited Use Policy". Please test with general scene or product images first to ensure compliance.

## Updates
2024.3.19: Updated to support multi-image processing.
## Features

- Supports Gemini 2.0 series models (gemini-2.0-flash, gemini-2.0-flash-exp, gemini-2.0-pro)
- Supports text-to-text generation
- Supports image-to-text generation (image understanding)
- Supports text-to-image generation (Note: this functionality is implemented in separate .py files, not directly within this node.)
- Built-in proxy support for convenient use by users in China
- Automatic dependency checking and installation
- Comprehensive error handling and logging

## Installation Method

1. Ensure you have ComfyUI installed.
2. Clone or download this repository into ComfyUI's `custom_nodes` directory:
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/silveroxides/ComfyUI_Gemini_Expanded_API.git
   ```
3. Install dependencies:
   ```
   cd ComfyUI_Gemini_Expanded_API
   pip install -r requirements.txt
   ```
4. Restart ComfyUI.

## How to Use

### 1. Configure API Key

First, you need to obtain a Google Gemini API key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create an API key
3. In ComfyUI, locate and use the `Configure Gemini API Key` node to enter your API key.

### 2. Text Generation

Use the `Expanded Gemini Text/Image` node for text generation:

- Connect the API key configuration node to the `config` input.
- Enter your prompt text in `prompt`.
- Adjust generation parameters (temperature, top_p, top_k, etc.).
- If needed, connect an image to the `input_image` input for image understanding.

### 3. Proxy Settings

If you are in China or other regions requiring a proxy:

1. Set `use_proxy` to `True`.
2. Set `proxy_host` (default is 127.0.0.1).
3. Set `proxy_port` (default is 7890).

## Parameter Description

### API Key Configuration Node

- `api_key`: Google Gemini API key

### Text Generation Node

#### Required Parameters

- `config`: API key configuration
- `prompt`: Prompt text
- `model`: Select model (gemini-2.0-flash, gemini-2.0-flash-exp, gemini-2.0-pro)
- `temperature`: Generation temperature (0.0-1.0), controls the randomness and creativity of the output.
- `top_p`: Nucleus sampling parameter (0.0-1.0)
- `top_k`: Number of candidate tokens to consider (1-100). Higher values mean more diversity.
- `max_output_tokens`: Maximum output tokens (1-8192)
- `include_images`: Whether to include images in the response (True/False)

#### Optional Parameters

- `input_image`: Input image (for image understanding)
- `use_proxy`: Whether to use a proxy (True/False)
- `proxy_host`: Proxy host address
- `proxy_port`: Proxy port

## Output

Text generation node output:
- `text`: Generated text
- `image`: If image generation is enabled, outputs the image.

## Precautions/Notes
- According to Google's "Generative AI Prohibited Use Policy", Gemini API has the following restrictions:
- Must not be used to generate content that violates laws and regulations.
- Must not be used to generate harmful, fraudulent, pornographic, or violent content.
- Must not be used to generate content that infringes on others' privacy or intellectual property rights.
- Image generation may have additional restrictions, and certain types of images might not be generatable.

- Using this node requires a stable network connection or effective proxy settings.
- API requests may be affected by Google server load.
- Large requests may require longer processing times.
- The image generation feature requires a model that explicitly supports it (e.g., `gemini-2.0-flash-exp`).

## Troubleshooting

- If you encounter network connection problems, please check your proxy settings.
- If API requests fail, please check if your API key is valid.
- If dependency installation fails, please manually install the required dependency packages.

## Acknowledgements

Thanks to Google for providing the Gemini API service.
Thanks to [tatookan](https://github.com/tatookan) for creating the original custom node repository for me to expand upon.
