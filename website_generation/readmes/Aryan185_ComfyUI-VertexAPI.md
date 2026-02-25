# ComfyUI-VertexAPI

A collection of powerful custom nodes for ComfyUI that connect your local workflows to Google's Vertex AI models. Use Google's Gemini, Imagen, and Veo models directly within ComfyUI using your Google Cloud Vertex AI credentials.

## Key Features

*   **Gemini Chat (Vertex AI):** Google's powerful multimodal AI via Vertex AI. Ask questions about an image, generate detailed descriptions, or create prompts for other models. Supports thinking budget controls.
*   **Gemini Segmentation (Vertex AI):** Generate segmentation masks for objects in an image using Gemini on Vertex AI.
*   **Google Imagen Edit (Vertex AI):** Perform advanced image editing, inpainting, outpainting, and background swapping using Imagen on Google's Vertex AI platform.
*   **Google Imagen Generator (Vertex AI):** Create images with Google's Imagen models via Vertex AI.
*   **Nano Banana (Vertex AI):** A creative image generation node using a specialized Gemini model on Vertex AI.
*   **Veo Text-to-Video (Vertex AI):** Generate high-quality video clips from text prompts using Google's Veo model via Vertex AI.
*   **Gemini TTS (Vertex AI):** Create speech from text using Google's Gemini models via Vertex AI.
*   **Gemini Diarisation (Vertex AI):** Perform speaker diarization on audio files using Gemini on Vertex AI.

---

## 🚀 Installation

1.  Navigate to your ComfyUI installation directory.
2.  Go into the `custom_nodes` folder:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
3.  Clone this repository:
    ```bash
    git clone https://github.com/Aryan185/ComfyUI-VertexAPI.git
    ```
4.  Install the required Python packages:
    ```bash
    cd ComfyUI-VertexAPI
    pip install -r requirements.txt
    ```
5.  **Restart ComfyUI.**

---

## 🔑 Prerequisites: Vertex AI Setup

Most nodes in this collection require Google Cloud Vertex AI credentials to function.

You will need:
1.  **Google Cloud Project ID:** The ID of your Google Cloud project.
2.  **Location:** The region where your resources are located (e.g., `us-central1`).
3.  **Service Account JSON:** A path to your Google Cloud service account JSON key file. Ensure the service account has the necessary permissions (e.g., Vertex AI User).

---

## 📚 Node Guide

### Gemini Chat (Vertex AI)

A versatile node for text generation and image analysis using Vertex AI.

*   **Category:** `text/generation`
*   **Inputs:**
    *   `prompt`: The text prompt.
    *   `project_id`: Your Google Cloud Project ID.
    *   `location`: Google Cloud location (default: `us-central1`).
    *   `service_account`: Path to your service account JSON file.
    *   `model`: The Gemini model to use (e.g., `gemini-2.5-pro`).
    *   `image` (Optional): Input image for analysis.
    *   `thinking`: Enable thinking process.
    *   `thinking_budget`: Token budget for thinking.
*   **Output:**
    *   `response`: The generated text.

### Gemini Segmentation (Vertex AI)

Generate segmentation masks using Gemini on Vertex AI.

*   **Category:** `image/generation`
*   **Inputs:**
    *   `image`: Source image.
    *   `segment_prompt`: Description of objects to segment.
    *   `project_id`, `location`, `service_account`: Vertex AI credentials.
    *   `model`: Gemini model to use.
*   **Output:**
    *   `mask`: Segmentation mask.

### Google Imagen Edit (Vertex AI)

Advanced image editing using Imagen on Vertex AI.

*   **Category:** `image/edit`
*   **Inputs:**
    *   `image`: Source image.
    *   `mask`: Mask defining the edit area.
    *   `prompt`: Description of the edit.
    *   `project_id`, `location`, `service_account`: Vertex AI credentials.
    *   `edit_mode`: Inpaint insertion, removal, outpainting, or background swap.
*   **Output:**
    *   `edited_images`: The edited image(s).

### Google Imagen Generator (Vertex AI)

Generate images using Google's Imagen models via Vertex AI.

*   **Category:** `image/generation`
*   **Inputs:**
    *   `prompt`: Image description.
    *   `project_id`, `location`, `service_account`: Vertex AI credentials.
    *   `model`: Imagen model to use (e.g., `imagen-3.0-generate-001`).
    *   `negative_prompt` (Optional): What to avoid in the image.
    *   `aspect_ratio`, `image_size`, `guidance_scale`, `seed`: Generation controls.
*   **Output:**
    *   `images`: Generated image(s).

### Nano Banana (Vertex AI)

Creative image generation using Gemini on Vertex AI.

*   **Category:** `image/generation`
*   **Inputs:**
    *   `project_id`, `location`, `service_account`: Vertex AI credentials.
    *   `model`: Gemini model (e.g., `gemini-3-pro-image-preview`).
    *   `prompt` (Optional): Text prompt.
    *   `image_1` to `image_5` (Optional): Source images.
*   **Output:**
    *   `image`: Generated image.

### Veo Text-to-Video (Vertex AI)

Generate video clips using Veo on Vertex AI.

*   **Category:** `video/generation`
*   **Inputs:**
    *   `prompt`: Video description.
    *   `project_id`, `location`, `service_account`: Vertex AI credentials.
    *   `model`: Veo model (e.g., `veo-2.0-generate-001`).
*   **Output:**
    *   `frames`: Generated video frames.

### Gemini TTS (Vertex AI)

Generate speech from text using Gemini on Vertex AI.

*   **Category:** `audio/generation`
*   **Inputs:**
    *   `text`: Text to convert to speech.
    *   `project_id`, `location`, `service_account`: Vertex AI credentials.
    *   `model`: Gemini TTS model.
    *   `voice_id`: Voice selection.
*   **Output:**
    *   `audio`: Generated audio.

### Gemini Diarisation (Vertex AI)

Speaker diarization using Gemini on Vertex AI.

*   **Category:** `audio`
*   **Inputs:**
    *   `audio`: Input audio.
    *   `num_speakers`: Number of speakers to detect.
    *   `project_id`, `location`, `service_account`: Vertex AI credentials.
    *   `model`: Gemini model.
*   **Output:**
    *   `speaker_1` to `speaker_4`: Audio tracks for separated speakers.

##  Acknowledgements

*   The [ComfyUI](https://github.com/comfyanonymous/ComfyUI) team.
*   Google for Vertex AI and the incredible Gemini, Imagen, and Veo models.
