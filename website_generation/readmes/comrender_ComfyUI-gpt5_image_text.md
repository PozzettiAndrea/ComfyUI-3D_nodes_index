# ComfyUI OpenAI GPT-5 & Image Analysis Node
<img width="400" height="297" alt="image" src="https://github.com/user-attachments/assets/93581a1c-f9d8-4fdc-b9ca-61a2bd8dd8cc" />

A powerful custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that integrates OpenAI's latest multimodal models. This node allows you to use **GPT-5**, **GPT-4.1**, and **o1** series models to analyze images, generate captions, or perform complex reasoning tasks directly within your ComfyUI workflows.

## ✨ Features

* **Latest Model Support**: Includes support for the **GPT-5 family** (5.2, Pro, Mini, Nano) and **GPT-4.1**.
* **Reasoning Model Logic**: Automatically handles the differences between standard models and "Reasoning" models (GPT-5/o1):
    * Switches between `max_tokens` and `max_completion_tokens` automatically.
    * Disables `temperature` for reasoning models to prevent API errors.
* **Multimodal Input**: Accepts images and text prompts simultaneously.
* **Cost Efficiency**: Includes "Mini" and "Nano" model variants for faster, cheaper inference.

## 🚀 Supported Models

### GPT-5 Series (Reasoning & Agents)
* **GPT-5.2**: Best for coding and agentic tasks.
* **GPT-5.2 Pro**: High-precision reasoning.
* **GPT-5 Mini**: Cost-efficient reasoning.
* **GPT-5 Nano**: Fastest, most lightweight model.

### GPT-4 Series
* **GPT-4.1**: Latest standard flagship.
* **GPT-4o**: Omni model (great for general image understanding).
* **GPT-4o Mini**: Fast and cheap standard model.

### o1 Series
* **o1-preview** / **o1-mini**: Previous generation reasoning models.

## 📦 Installation

1.  Navigate to your ComfyUI custom nodes directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone [https://github.com/your-username/ComfyUI-OpenAI-GPT5.git](https://github.com/your-username/ComfyUI-OpenAI-GPT5.git)
    ```
3.  Install the required dependencies:
    ```bash
    cd ComfyUI-OpenAI-GPT5
    pip install -r requirements.txt
    ```
4.  Restart ComfyUI.

## ⚙️ Usage

1.  **Add the Node**: Right-click -> `openai` -> `analysis` -> `GPT5 Image & Text`.
2.  **API Key**: Paste your OpenAI API Key into the `openai_key` widget.
3.  **Connect Image (Optional)**: Connect a generic image output to the `image` input slot.
4.  **Select Model**: Choose your desired model from the dropdown.

### Parameter Guide

| Parameter | Description |
| :--- | :--- |
| **model** | Select the specific OpenAI model (e.g., `gpt-5.2`, `gpt-4o`). |
| **prompt** | The main instruction or question for the AI (e.g., "Describe this image"). |
| **system_prompt** | Sets the behavior of the assistant (e.g., "You are a creative writer"). |
| **temperature** | Controls randomness. **Note:** Ignored for GPT-5 and o1 models (defaults to 1). |
| **max_tokens** | Output limit for standard models (GPT-4o, GPT-4.1). |
| **max_completion_tokens** | Output limit for **Reasoning models** (GPT-5, o1). |

## ⚠️ Important Notes

* **Reasoning Models (GPT-5 / o1)**: These models do not support the `temperature` parameter. The node automatically ignores your temperature setting when these models are selected to prevent API errors.
* **Token Limits**: If you are using a Reasoning model and the output gets cut off or fails silently, try increasing `max_completion_tokens`.

## 📄 License

MIT License
