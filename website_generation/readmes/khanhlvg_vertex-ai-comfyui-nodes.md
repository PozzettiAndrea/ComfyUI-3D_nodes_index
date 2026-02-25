> **Disclaimer:** This is a personal project and is not an official Google product.

# \[Unofficial\] Vertex AI Custom Nodes for ComfyUI

Custom nodes for ComfyUI that provide access to Google Cloud's Vertex AI generative models, including:

*   **Gemini API**: For advanced language and multimodal tasks.
*   **Imagen API**: For high-quality image generation and editing.
*   **Veo API**: For state-of-the-art video generation.
*   **Chirp API**: For speech-to-text and text-to-speech.
*   **Lyria API**: For music generation.

## Quick Installation

You can install ComfyUI and the Vertex AI custom nodes with a single command. This script will check for dependencies, clone the necessary repositories, and guide you through the authentication process.

```bash
bash <(curl -s https://raw.githubusercontent.com/khanhlvg/vertex-ai-comfyui-nodes/main/scripts/install.sh)
```

Then run ComfyUI.

```bash
cd ComfyUI
source venv/bin/activate
python main.py
```

## Manual Setup

Before using these custom nodes, you need to set up your environment to authenticate with Google Cloud.

1.  **Install the gcloud CLI:**

    Follow the official instructions to install the Google Cloud CLI for your operating system: [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)

2.  **Authenticate with Application Default Credentials (ADC):**

    Once the gcloud CLI is installed, you need to authenticate your local environment. Run the following command in your terminal:

    ```bash
    gcloud auth application-default login
    ```

    This will open a browser window for you to log in to your Google account and grant the necessary permissions.

3.  **Set Environment Variables:**

    You need to set the following environment variables in your terminal session before launching ComfyUI. Replace `your-gcp-project-id` and `your-gcp-location` with your actual Google Cloud project ID and desired location (e.g., `us-central1`).

    ```bash
    export GOOGLE_CLOUD_PROJECT=your-gcp-project-id
    export GOOGLE_CLOUD_LOCATION=your-gcp-location
    ```

    To make these variables persistent across terminal sessions, you can add these lines to your shell's startup file (e.g., `~/.bashrc`, `~/.zshrc`).

Once you have completed these steps, you can start ComfyUI, and the Vertex AI custom nodes will be able to access the APIs.

## Running Unit Tests

To run the unit tests, run the following command:

```bash
python -m unittest discover
```
