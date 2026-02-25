# AS_LLM_nodes

This ComfyUI extension provides custom nodes for working with Google Gemini and OpenAI ChatGPT. 

## AS_GeminiCaptioning

### User Guide

The **AS_GeminiCaptioning** node lets you generate a descriptive text prompt from a single image using the Google Gemini API. Supply your image and adjust any optional text fields to tailor the output.

### Inputs

- **IMAGE** (Required)  
  The image you want to describe (e.g., JPEG, PNG). Connect your image input.

- **PROMPT TYPE** (Required)  
  Choose between the preset styles "SD1.5 – SDXL" or "FLUX" to select the base style of the prompt.  
  *If you do not provide a custom reference, the selected style determines which default text is used.*

- **APY KEY PATH** (Required)  
  The file path to your API key for the Google Gemini API.

- **GEMINI MODEL** (Required)  
  The model that will process your request. Possible options include:  
  - Gemini 2.0 Flash  
  - Gemini 2.0 Flash-Lite  
  - Gemini 1.5 Flash  
  - Gemini 1.5 Pro  
  *The default is Gemini 2.0 Flash.*

- **PROMPT LENGTH** (Optional)  
  An approximate word count for the final prompt. If empty, there is no length restriction.

- **PROMPT REFERENCE** (Optional)  
  A sample text prompt format that serves as a reference. If empty, a default reference is used.

- **PROMPT STRUCTURE** (Optional)  
  A guideline for organizing details in the prompt (e.g., building type, materials, location).

- **IGNORE** (Optional)  
  Specific words or concepts to exclude from the prompt.

- **EMPHASIS** (Optional)  
  Words or concepts to emphasize.

- **SAVE TO PATH** (Optional)  
  A directory path for saving the generated text file.

- **TXT NAME** (Optional)  
  Name for the `.txt` file. If empty and a path is provided, defaults to `result.txt`.

### Outputs

- **RESULT PROMPT**  
  The text response from Gemini.

- **REQUEST TEXT**  
  The exact text payload sent to the API.

- **LOG**  
  A log of execution steps and errors.

---

## AS_MultimodalGemini

### User Guide

The **AS_MultimodalGemini** node sends text plus up to three images to the Google Gemini API.

### Inputs

- **TEXT_INPUT** (Required)  
  A text string to be sent along with the images.

- **API_KEY_PATH** (Required)  
  The file path to your Gemini API key.

- **GEMINI MODEL** (Required)  
  - Gemini 2.0 Flash  
  - Gemini 2.0 Flash-Lite  
  - Gemini 1.5 Flash  
  - Gemini 1.5 Pro  
  *Default is Gemini 2.0 Flash.*

- **IMAGE_1**, **IMAGE_2**, **IMAGE_3** (Optional)  
  Up to three images to attach.

### Outputs

- **RESULT**  
  The text returned by Gemini.

- **LOG**  
  A log of steps and errors.

---

## AS_ComfyGPT

### User Guide

The **AS_ComfyGPT** node integrates with OpenAI’s ChatGPT. Provide the path to your API key, choose a model, and enter a prompt. The node returns ChatGPT’s reply.

### Inputs

- **api_key_file** (Required)  
  Path to a file containing your OpenAI API key.

- **model** (Required)  
  Name of the OpenAI model (e.g., "gpt-4", "gpt-3.5-turbo").

- **prompt** (Required)  
  The user prompt text to send to the GPT model.

### Outputs

- **STRING**  
  The response from ChatGPT.

---

## Required Libraries

- **Pillow**  
- **requests**  
- **google-generativeai**  
- **openai**  
