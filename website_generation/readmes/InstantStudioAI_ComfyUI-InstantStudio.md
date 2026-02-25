# ComfyUI-InstantStudio Node Pack

A collection of nodes to enhance your experience with ComfyUI.

## Nodes in This Pack

### 1. **Upload Images Node**
The `upload_images` node allows you to upload images to the **InstantStudio Toolkit**. It requires:
- **Username**
- **Toolkit Endpoint**
- **API Key**

<img width="708" alt="Screenshot 2024-12-12 at 3 09 39 PM" src="https://github.com/user-attachments/assets/e44619ef-93c2-4747-9990-0cbe303e3135" />


### 2. **HuggingFace Classify Node**
The `classifier` node works with the **HF Transformers Classifier Provider**, a feature provided by the [ComfyUI Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) by **ltdrdata**. This node:
- Utilizes **HuggingFace's Transformers models** for classification.
- Currently supports classifying images as **male** or **female**.
- Enables workflows based on the gender classification of a user's input image.

  <img width="928" alt="Screenshot 2024-12-12 at 2 41 41 PM" src="https://github.com/user-attachments/assets/6b81af77-9477-48bc-9ee9-878bde9f2803" />


### 3. **Moondream Node**
This node is a comfyui node for the moondream visual LLM (https://huggingface.co/vikhyatk/moondream2a)
It is customized based on [ComfyUI-Hangover-Moondream](https://github.com/Hangover3832/ComfyUI-Hangover-Moondream) to meet our needs. This node:
- Utilizes **HuggingFace's Transformers models** for classification.
- Can be used to analyze images and generate text.

---
## Install

To install the ComfyUI-InstantStudio Node Pack:

### Manual Installation
1. Navigate to your `custom_nodes` directory:
   ```bash
   cd custom_nodes
   ```
2. Clone
   ```bash
   git clone https://github.com/InstantStudioAI/ComfyUI-InstantStudio.git
   ```
3. Install Requirements
   ```bash
   cd comfy_instant_studio
   pip install -r requirements.txt
   ```
4. Make sure **ComfyUI-Impact-Pack** is also installed if you want to use the Classifier Node. 

5. Restart ComfyUI
