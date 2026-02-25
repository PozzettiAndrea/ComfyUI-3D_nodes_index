# Orpheus TTS for ComfyUI (via LM Studio)

A custom node for ComfyUI that generates high-quality, natural-sounding speech using Orpheus TTS models running in LM Studio.

I tried all the other Orpheus nodes for ComfyUI, and they were either slow (2+min for 15s), or I couldn't get them to install right.  Unlike those, this doesn't try to run the LLM model with all the different settings via some cli thing, I just rely on LM Studio where you can handle all the loading there.  I got this to be as fast as I could, about 0.5x realtime on a RTX3090.  Voices sound so good.


![Workflow Diagram](./example_workflows/OrpheusTTSLMStudioExample.png)


And now for your regularly scheduled LLM generated readme:

This node is designed for performance and user experience, featuring a highly-responsive, parallelized workflow. It streams audio tokens from LM Studio while decoding them into sound in a separate thread, ensuring your ComfyUI interface remains smooth. The state-of-the-art progress bar intelligently displays the real-time progress of the entire operation, not just one part of it.

 
*(Note: You will need to replace this with an actual screenshot of the node in your workflow.)*

## ✨ Features

*   **High-Quality Speech Generation:** Leverages the power of Orpheus TTS foundation models for expressive and natural voice output.
*   **Seamless LM Studio Integration:** Connects directly to your local LM Studio server, allowing you to use any compatible Orpheus model you have downloaded.
*   **🚀 Blazing-Fast Parallel Processing:** The node fetches audio tokens from the LLM and decodes them into audio simultaneously, maximizing performance and reducing wait times.
*   **Full Control:** All standard LLM inference parameters (`temperature`, `top_p`, `seed`, etc.) are exposed for fine-tuning your results.


## ✅ Requirements

1.  **ComfyUI:** A working installation of ComfyUI.
2.  **LM Studio:** The LM Studio application installed and running.
3.  **An Orpheus Model:** You must have an Orpheus-compatible GGUF model downloaded in LM Studio.
    *   We recommend starting with `isaiahbjork/orpheus-3b-0.1-ft-Q4_K_M-GGUF`. You can search for and download this directly from the LM Studio app.
4.  **Python Dependencies:** This node requires the `lmstudio` and `transformers` Python libraries.

## ⚙️ Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/phazei/ComfyUI-OrpheusTTS-LMStudio.git
    ```
    *(Note: Replace the URL with your actual repository URL after publishing.)*
3.  Install the required Python packages:
    ```bash
    cd ComfyUI-OrpheusTTS-LMStudio 
    pip install -r requirements.txt
    ```
    *(You should create a `requirements.txt` file in your repo with the following content:)*
    ```
    lmstudio>=0.2.20
    transformers
    torch
    numpy
    ```
4.  Restart ComfyUI.

## 🚀 Setup & Usage

### 1. In LM Studio

1.  **Download Model:** In LM Studio, search for and download an Orpheus model (e.g., `orpheus-3b-0.1-ft`).
2.  **Load Model:** Select the model to load it.
3.  **Start Server:** Navigate to the "Local Server" tab (the `<->` icon) and click **Start Server**. This is the crucial step that allows ComfyUI to communicate with the model.

### 2. In ComfyUI

1.  **Add the Node:** Right-click on your graph, select "Add Node," and find the **OrpheusTTS/LM Studio > Orpheus TTS (LM Studio)** node.
2.  **Enter Your Text:** Type the text you want to convert to speech in the `text` field.
3.  **Select a Voice:** Choose one of the built-in English voices from the `voice` dropdown.
4.  **Set the Model Key (Optional but Recommended):**
    *   The `model_key` field tells the node which specific model to use in LM Studio.
    *   To find the key, look at the top of your LM Studio server window. It will show the path-like identifier for the loaded model (e.g., `orpheus-3b-0.1-ft`).
    *   Copy this identifier and paste it into the `model_key` field. If you leave it blank, the node will use whichever model is currently loaded in LM Studio by default.
5.  **Generate:** Queue the prompt. The node will connect to LM Studio, generate the audio, and output an `AUDIO` artifact that can be used with video nodes or saved.

## Troubleshooting

*   **Node not appearing:** Ensure you have restarted ComfyUI after installation.
*   **Connection Errors:**
    *   Verify that the LM Studio server is running.
    *   Check that your system's firewall is not blocking the connection on the port LM Studio is using (usually 1234).
*   **Slow Performance:** Enable the `debug` flag on the node and check the logs in your console. The performance timers will show you whether the slowdown is happening during the LLM phase or the SNAC decoding phase.

## License

This project is licensed under the Apache 2.0 License