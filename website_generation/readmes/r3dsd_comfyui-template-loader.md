# Comfyui-Template-Loader
Easily Load Your Frequently Used Prompts in ComfyUI

With ComfyUI Template Loader, managing and reusing your favorite prompts has never been simpler. Save time and streamline your workflow by loading your go-to templates with just a few clicks!

# Features
- Load Prompt Templates from Files
- Easy to use

# Installation
```bash
git clone https://github.com/r3dsd/comfyui-template-loader.git
```
# Usage
1. **Create a Template File**
    - Place your template file in the following directory: `custom_nodes/comfyui-template-loader/template`
    - Make sure the file has a `.json` extension.

2. **Template File Format**
    - template file should follow this structure:
    ```json
    {
        "Key1": "Prompt1, Prompt2, Prompt3",
        "Key2": "Prompt1, Prompt2, Prompt3",
        ...
    }
    ```

3. **Done!**
    - That's it! Now you can use the TemplateLoader Node in your workflow.

# Nodes
TemplateLoader
- Source: The file Name of the Template File
- Template: The Key of the Template

return: The String of the Template