# ComfyUI Custom Node: Prompt List JSON

This repository provides a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows managing positive and negative prompts in a structured JSON format. The node supports creating new prompt lists, random prompt selection, and logging prompt details to the console for seamless integration into your workflow.

## Features

- 📂 **JSON-based prompt management**: Prompts are stored in individual JSON files for easy editing and retrieval.
- 🔄 **Add or update prompts**: Supports creating new prompt lists, updating existing prompts, and overwriting as needed.
- 🎲 **Random prompt selection**: Choose a random prompt from an existing list with ease.
- 🖥️ **Console logging**: Optionally logs prompt details with formatted outputs for debugging or verification.
- 🛠️ **Automatic file management**: Ensures required directories and files are created automatically.

## Installation

1. Clone or download this repository to your ComfyUI custom node directory:
   ```bash
   git clone https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON.git
   ```
2. Restart ComfyUI to load the custom node.

#### Alternative Method (ComfyUI manager)

1. Install using the ComfyUI manager.

![ComfyUI manager](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON/blob/master/images/manager.png)

#### Alternative Method (comfy-cli)
1. Install comfy-cli ([read docs](https://docs.comfy.org/comfy-cli/getting-started))
   ```bash
   install comfy-cli
   ```
2. Install custome node
   ```bash
   comfy node registry-install comfyui_prompt_list_json
   ```

## Usage

![Node in menu](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON/blob/master/images/node_in_menu.png)

### Node Inputs

- **Prompt List**: Select an existing prompt list or create a new one.
- **New List Name**: Specify the name for a new list (used when creating a new list).
- **Prompt Name** (required): A unique name for the prompt.
- **Positive Prompt** (required for new prompts): The positive description of the prompt.
- **Negative Prompt** (optional): The negative description of the prompt.
- **Random** (boolean, default `False`): Enable random selection of prompts from the list.
- **Overwrite** (boolean, default `False`): Whether to overwrite an existing prompt with the same name.
- **Console Log** (boolean, default `False`): Prints prompt details to the console for debugging.

### Node Outputs

- **Positive Prompt**: The saved or retrieved positive prompt.
- **Negative Prompt**: The saved or retrieved negative prompt.
- **Full List**: The entire prompt list as a JSON string.

### Example Workflow

1. Add or update a prompt with the following inputs:
   - **Prompt List**: `test.json`
   - **New List Name**: `test`
   - **Prompt Name**: `girl on helmet`
   - **Positive Prompt**: `concept art Girl in black thin, oily latex, black motorcycle helmet, black glass on helmet, pours a bucket of yellow paint on himself, paint dripping down his body, yellow silk long scarf, sexy, dynamics. Black mirrors in the background, reflections. digital artwork, illustrative, painterly, matte painting, highly detailed`
   - **Negative Prompt**: `photo, photorealistic, realism, ugly`
   - **Overwrite**: `True`
   - **Console Log**: `True`
   - **Random**: `True`

![Node_prev_list](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON/blob/master/images/node_prev_list.png)

2. The prompt will be saved to the specified JSON file, and its details will appear in the console if logging is enabled.

![log](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON/blob/master/images/log.png)

### File Structure

Prompts are stored in individual JSON files in the following format:
```json
{
    "SunsetScene": {
        "positive": "A breathtaking sunset over the mountains",
        "negative": "Low quality, blurry"
    }
}
```

### Adding Prompts Programmatically

You can also use this node programmatically. Here's an example:
```python
from your_module import ComfyUI_Prompt_JSON

manager = ComfyUI_Prompt_JSON()
positive, negative, full_list = manager.process(
    **{
        "Prompt List": "New List",
        "New List Name": "NaturePrompts",
        "Prompt Name": "SunsetScene",
        "Positive Prompt": "A breathtaking sunset over the mountains",
        "Negative Prompt": "Low quality, blurry",
        "Random": False,
        "Overwrite": True,
        "Console Log": True
    }
)
```

### Error Handling

- Raises a `ValueError` if a required field (e.g., `Prompt Name` or `Positive Prompt`) is missing.
- Displays detailed error messages for debugging in the console.

![Error prompt name](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON/blob/master/images/node_err1.png)
![Error positive prompt](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON/blob/master/images/node_err2.png)
![Error New List Name](https://github.com/TKRLAB/ComfyUI_Prompt_List_JSON/blob/master/images/node_err3.png)

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

---

Enjoy using the **Prompt List JSON** node with ComfyUI! 🎨
