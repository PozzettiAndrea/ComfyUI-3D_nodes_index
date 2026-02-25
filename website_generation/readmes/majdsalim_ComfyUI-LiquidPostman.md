# Liquid Postman (Gemini Image)

A ComfyUI custom node for image generation using the Google Gemini API. Supports text prompts, image editing, PDF/DOCX file input, and search grounding.

## Installation

### ComfyUI Manager
Search for **"Liquid Postman"** in ComfyUI Manager and click Install.

### CLI
```bash
comfy node install comfyui-liquidpostman
```

### Manual
Clone this repository into your ComfyUI `custom_nodes` folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/majdsalim/ComfyUI-LiquidPostman.git
pip install requests Pillow
```

## Setup

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Add the **Liquid Postman (Gemini Image)** node to your workflow (found under `google/gemini`)
3. Paste your API key into the `api_key` field

## Inputs

| Input | Type | Default | Description |
|---|---|---|---|
| `api_key` | STRING | `""` | Your Gemini API key (required) |
| `prompt` | STRING | `""` | Text prompt for image generation |
| `model` | STRING | `gemini-3-pro-image-preview` | Gemini model to use |
| `seed` | INT | `42` | Random seed (-1 to disable) |
| `aspect_ratio` | ENUM | `1:1` | Output aspect ratio (1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9) |
| `resolution` | ENUM | `1K` | Output resolution (1K, 2K, 4K) |
| `response_modalities` | ENUM | `IMAGE` | `IMAGE` or `IMAGE+TEXT` |
| `system_prompt` | STRING | *(built-in)* | System instruction for the model |
| `search_grounding` | BOOLEAN | `false` | Enable Google Search grounding |
| `files` | STRING | `""` | PDF/DOCX file paths or folder paths (comma or newline separated) |
| `debug` | BOOLEAN | `false` | Print request/response details to console |
| `images` | IMAGE | *(optional)* | Input images for editing or reference |

## Outputs

| Output | Type | Description |
|---|---|---|
| `image` | IMAGE | Generated image(s) as a tensor batch |
| `text` | STRING | Text response from the model (when using IMAGE+TEXT mode) |

## Features

### Image Generation
Enter a text prompt to generate images with Gemini.

### Image Editing
Connect input images to the `images` pin. All images are uploaded via the Gemini Files API, so there is no file size limit.

### File Input (PDF / DOCX)
Provide file paths in the `files` field. You can:
- List individual file paths separated by commas or newlines
- Provide a folder path to automatically include all `.pdf` and `.docx` files in that folder

```
C:\docs\report.pdf, C:\docs\brief.docx
C:\docs\project_files
```

### Search Grounding
Enable `search_grounding` to let Gemini use Google Search for up-to-date information when generating images.

### Debug Mode
Enable `debug` to print the full API request body and response metadata to the ComfyUI console.

## License

MIT
