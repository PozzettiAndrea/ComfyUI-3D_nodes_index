# ComfyUI Vision LLM Analyzer Node

This repository contains a powerful and versatile custom node for ComfyUI that seamlessly integrates with OpenAI-compatible Large Language Models (LLMs), including multimodal (vision-enabled) models like GPT-4o.

This single node allows you to perform both text generation and image analysis, making it an essential tool for advanced prompt engineering and creative automation.

![Node Preview](https://i.imgur.com/your-image-url.png) <!-- It's a good idea to add a screenshot of your node here -->

## ✨ Features

- **Dual Functionality**: Operates as a standard text-generation LLM node or as a vision-enabled image analyzer.
- **Optional Image Input**: The image input is optional. If an image is provided, the node performs multimodal analysis. If not, it functions as a text-only LLM.
- **Frontend Configuration**: Easily configure the following directly on the node:
    - **API Key**: Securely input your API key.
    - **Base URL**: Customize the API endpoint to use services other than OpenAI (e.g., local LLMs, other providers).
    - **System Role**: Define the behavior and personality of the AI model.
    - **User Prompt**: Provide the main instruction or question.
    - **Model Selection**: Specify the model to use (e.g., `gpt-4o`, `gpt-3.5-turbo`).
- **Seamless Integration**: The text output can be connected to any other ComfyUI node that accepts a string input, such as a prompt for a text-to-image sampler.

## ⚙️ Installation

1.  Navigate to the `custom_nodes` directory in your ComfyUI installation folder:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this GitHub repository into the `custom_nodes` directory:
    ```bash
    git clone https://github.com/Aero-Ex/ComfyUI-Vision-LLM-Analyzer.git
    ```
3.  Install the required dependencies by navigating into the new directory and running pip:
    ```bash
    cd ComfyUI-Vision-LLM-Analyzer/
    pip install -r requirements.txt
    ```
4.  Restart ComfyUI.

The "Vision LLM Analyzer" node will now be available under the "LLM" category when you right-click on the canvas.

## 🚀 How to Use

Once installed, you can add the "Vision LLM Analyzer" node to your workflow.

### Use Case 1: Image Analysis (Multimodal)

1.  Connect an **Image** output from another node (e.g., "Load Image") to the `image` input of the Vision LLM Analyzer node.
2.  Fill in your `api_key`, and confirm the `base_url` is correct for your provider.
3.  Set the `role_prompt` to guide the AI's persona (e.g., "You are a master art critic.").
4.  Write your `user_prompt` to ask a question about the image (e.g., "Describe the artistic style and mood of this image.").
5.  Connect the `STRING` output of this node to another node's text input to use the generated description.

### Use Case 2: Text Generation (Standard LLM)

1.  Leave the `image` input disconnected.
2.  Fill in your `api_key` and `base_url`.
3.  Set the `role_prompt` (e.g., "You are a creative writer.").
4.  Write your `user_prompt` with the text you want the LLM to process (e.g., "Generate three fantasy character concepts with unique backstories.").
5.  Use the `STRING` output for your other nodes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/ComfyUI-Vision-LLM-Analyzer/issues).

## 📄 License

This project is licensed under the MIT License.
