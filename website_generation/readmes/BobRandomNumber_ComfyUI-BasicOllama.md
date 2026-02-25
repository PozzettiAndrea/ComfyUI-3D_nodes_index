# ComfyUI-BasicOllama

A simplified node that provides access to Ollama. It allows you to send prompts, system prompts, and images to your Ollama instance and receive text-based responses.

## ⚠️ Requirements

**You must have Ollama installed and running on your local machine for this node to function.** You can download it from [https://ollama.com/](https://ollama.com/).

## 🚀 Features

* **Direct Ollama Integration:** Seamlessly connect to your local Ollama instance.
* **Automatic Image Detection:** The node automatically detects if an image is connected and sends it to Ollama for multimodal analysis.
* **System Prompt Support:** Utilize the `system` parameter in the Ollama API for more control over model behavior.
* **Dynamic Prompt Templates:** Easily load your own system prompts from `.txt` files in the `prompts` directory.
* **Dynamic Image Inputs:** Start with one image input, and automatically add more as you connect them.
* **Easy Configuration:** Quickly set up your Ollama URL via a `config.json` file.

![](https://github.com/BobRandomNumber/ComfyUI-BasicOllama/blob/main/BasicOllama.png)

## 📦 Installation

1. **Clone the Repository:**
   Navigate to your `ComfyUI/custom_nodes` directory and clone this repository:
&nbsp;
```bash
    git clone https://github.com/BobRandomNumber/ComfyUI-BasicOllama.git
```

2. **Install Dependencies:**
   Navigate to the newly cloned directory and install the required packages:
&nbsp;
```bash
    cd ComfyUI-BasicOllama
```
```bash
    pip install -r requirements.txt
```

3. **Restart your ComfyUI instance to load the new custom node.**

## ✨ Usage

The `BasicOllama` node can be found under the `Ollama` category in the ComfyUI menu. Connect optional image/s to the `image` inputs to have it automatically included in your prompt if desired.

### Inputs

| Name                   | Type      | Description                                                                                                                                                             |
| ---------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prompt`               | `STRING`  | The main text prompt to send to the Ollama model.                                                                                                                       |
| `ollama_model`         | `COMBO`   | A list of available Ollama models on your local instance.                                                                                                               |
| `keep_alive`           | `INT`     | The duration (in minutes) that the Ollama model should remain loaded in memory after the request is complete.                                                           |
| `saved_sys_prompt`     | `COMBO`   | A dropdown list of saved system prompts from the `.txt` files in the `prompts` directory. This is used as the system prompt by default.                                 |
| `use_sys_prompt_below` | `BOOLEAN` | If checked (`True`), the `system_prompt` text box below will be used instead of the dropdown selection. If unchecked (`False`), the `saved_sys_prompt` dropdown is used. |
| `system_prompt`        | `STRING`  | A multiline text box for a custom, one-off system prompt. This is only active when `use_sys_prompt_below` is checked.                                                     |
| `image`                | `IMAGE`   | An optional image input for multimodal models. The node starts with one image input, and connecting an image to it will create a new input, allowing for any number of images. |

### Outputs

| Name   | Type     | Description                               |
| ------ | -------- | ----------------------------------------- |
| `text` | `STRING` | The text-based response from the Ollama model. |

## ✍️ Adding Custom System Prompts

You can easily add your own reusable system prompts to the `saved_sys_prompt` dropdown menu.

1. Navigate to the `ComfyUI-BasicOllama/prompts` directory.
2. Create a new text file (e.g., `my_prompt.txt`).
3. Write your system prompt inside this file. For example, if you want a system prompt for generating JSON, the content of the file could be:

&nbsp;   ```
    You are a helpful assistant that only responds with valid, well-formatted JSON.
    ```

4. Save the file.
5. Refresh your ComfyUI browser window.

The name of your file (without the `.txt` extension) will now appear as an option in the `saved_sys_prompt` dropdown. In the example above, you would see `my_prompt` in the list.

## ⚙️ Configuration

By default, the `BasicOllama` node will attempt to connect to your Ollama instance at `http://localhost:11434`.

If your Ollama instance is running on a different URL/port, you can change it by editing the `config.json` file located in the `ComfyUI-BasicOllama` directory:

```json
{
  "OLLAMA_URL": "http://your-ollama-url:11434"
}
```

## 🙏 Attribution

A special thank you to [@al-swaiti](https://github.com/al-swaiti) for creating the original [ComfyUI-OllamaGemini](https://github.com/al-swaiti/ComfyUI-OllamaGemini) whose Ollama node served as the foundation and inspiration for this.
This project is licensed under the [MIT License](LICENSE).

