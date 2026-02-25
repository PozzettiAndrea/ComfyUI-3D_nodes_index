# ComfyUI-Gemini

These nodes integrate the Gemini API into ComfyUI, allowing you to send prompts and images to Gemini AI models.

## Features

- **Error Fallback Value**: Specify a fallback value to use if there's an error accessing the Gemini API.
- **Response Type Selection**: Choose between receiving responses in plain `text` or `json` format.
- **Image Support**: Include up to three images(or **batches**) with your prompt to provide visual context.
- **Custom System Instructions**: Set a system instruction to guide the AI's responses.
- **Adjustable Safety Settings**: Control the content filtering level to block inappropriate content.

## Setting Up the Gemini API Key

1. **Obtain API Key**:
   - Sign up for access to the Gemini API through Google Cloud Platform.
   - Create a new API key with permissions to access the Gemini models.
2. **Set the API Key**:
   - **Option 1**: Set it in your environment variables:
     - On Windows:
       ```cmd
       set GOOGLE_API_KEY=your_api_key_here
       ```
     - On Linux/macOS:
       ```bash
       export GOOGLE_API_KEY=your_api_key_here
       ```
   - **Option 2**: Provide it directly in the node's `api_key` input.

## Inputs Explained

- **prompt (STRING)**:
  - Your main question or instruction for the AI.
  - Example: "What are the health benefits of green tea?"
- **safety_settings (CHOICE)**:
  - Controls the filtering of the response content.
  - Options:
    - `BLOCK_NONE`: No filtering.
    - `BLOCK_ONLY_HIGH`: Blocks only high-risk content.
    - `BLOCK_MEDIUM_AND_ABOVE`: Blocks medium and high-risk content.
- **response_type (CHOICE)**:
  - Determines the format of the AI's response.
  - Options:
    - `text`: Plain text response.
    - `json`: Response in JSON format.
- **model (CHOICE)**:
  - Selects the Gemini model to use.
  - Options:
    - `gemma-3-12b-it`: Very small model that you can run locally or remotely on the Google infrastructure.
    - `gemma-3-27b-it`: Medium size model that you can run locally or remotely on the Google infrastructure.
    - `gemini-2.0-flash-lite-001`: Old version of the **very** fast and free model.
    - `gemini-2.0-flash-001`: Old version of the fast and free model.
    - `gemini-2.5-flash`: Latest stable version of the fast and free model.
    - `gemini-2.5-pro`: Latest stable **Pro** model with advanced capabilities.
- **api_key (STRING, Optional)**:
  - Your Gemini API key.
  - Recommended to set via environment variable.
- **proxy (STRING, Optional)**:
  - Proxy server URL if you need to route requests through a proxy. See: [Why use Proxy?](https://visionatrix.github.io/VixFlowsDocs/AdminManual/Installation/proxy_gemini/#why-use-a-proxy)
- **image_1, image_2, image_3 (IMAGE, Optional)**:
  - Images or image batches to include with your prompt.
  - Useful for tasks like image captioning or visual question answering.
- **system_instruction (STRING, Optional)**:
  - Sets a system-level instruction to influence the AI's behavior.
  - Example: "You are a helpful assistant that provides concise answers."
- **error_fallback_value (STRING, Optional, Lazy Input)**:
  - Value to return if an error occurs when accessing Gemini.
  - If not set, the node will raise an exception on error.
- **temperature (FLOAT, Optional, Lazy Input)**:
  - Controls the randomness of the output. Any **negative value** means to use default value for model.
- **num_predict (INT, Optional, Lazy Input)**:
  - The maximum number of tokens to include in a candidate, value `0` means to use default value for model.

![Race and Gender Detection](https://raw.githubusercontent.com/Visionatrix/ComfyUI-Gemini/main/screenshots/race_gender.jpg)
