# ComfyUI-NanoB-Edit-Gemini

This custom node facilitates direct interaction with the **Google Gemini API** (supporting **Gemini 3 Pro** and **Gemini 2.5 Flash**) for advanced image editing tasks within ComfyUI. It features parallel request handling to generate multiple variations efficiently.

### 💡 Why this Node?
Google's infrastructure can be complex to navigate—specifically the distinctions between Vertex AI/Gemini. Naming conventions are often inconsistent (e.g., `gemini-3-pro-image-preview` vs. "Nano Banana Pro"), and straightforward documentation for implementing these specific API endpoints is scarce. This node aims to bridge that gap by providing a simple, working implementation.

---

## Key Features

* **Multi-Model Support:** Compatible with Gemini 3 Pro and Gemini 2.5 Flash.
* **Parallel Processing:** Handles parallel requests to generate multiple image variations simultaneously.
* **Debug Mode:** Includes a debug option to view the exact input sent to Gemini directly in the ComfyUI terminal/console.
* **Flexible Auth:** Supports both direct API key input (UI) and Environment Variables (Recommended).

---

## ⚠️ Security & Best Practices

**Important:** While this node allows you to enter your API key directly into the UI widget, **it is highly recommended to use Environment Variables.**

> [!WARNING]
> **Do not publish your workflows or embed workflows into final images with your API key entered in the node's text box.**
> If you share a workflow with the key inside, your API usage will be disclosed to third parties. Keep the UI text box empty and use the setup steps below.

---

## 🛠️ Setup Instructions

### 1. Set the Environment Variable
To keep your API key secure, set the `GEMINI_API_KEY` on your system.

#### **Windows**
1.  Search for **"Edit the system environment variables"** in the Start menu.
2.  Click **Environment Variables** -> **New**.
3.  **Variable Name:** `GEMINI_API_KEY`
4.  **Variable Value:** `your_actual_api_key_here`
5.  *Note: You must restart ComfyUI (and the console) after setting this for changes to take effect.*

#### **Linux / macOS**
Add the export command to your shell profile (`.bashrc`, `.zshrc`, etc.) or your launch script:
```bash
export GEMINI_API_KEY="your_actual_api_key_here"
