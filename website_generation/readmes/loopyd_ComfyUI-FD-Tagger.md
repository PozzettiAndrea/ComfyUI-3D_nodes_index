# ComfyUI-FD-Tagger
## E621 image interrogation and auto-captioning

A [ComfyUI](https://github.com/comfyanonymous/ComfyUI) extension allowing the interrogation of Furry Diffusion tags from images using JTP tag inference.

> **NSFW Content Warning**: This ConfyUI extension can be used to classify or may mistakenly classify content as NSFW (obscene) contnet.  Please refrain from using this extension if you are below the general age of consent in your jurisdication.

**Based on:**
- [RedRocket/JointTaggerProject](https://huggingface.co/RedRocket/JointTaggerProject) - The model this custom extension runs on.
- [pythongosssss/ComfyUI-WD14-Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger) - Where this repository was forked from.

**All models created by:**
- [RedRocket](https://huggingface.co/RedRocket)

## Automatic Installation

Use the [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) extension to search for `ComfyUI-FD-Tagger`.  Download the extension by tapping "Try Install", and then restart your ComfyUI instance.

## Manual Installation

1. Open a **Command Prompt** or **Terminal Application** of your choice, then navigate to your ComfyUI ``custom_nodes`` folder:
    
    - **Windows Portable installation**:
    ```
    cd C:\ComfyUI_windows_portable\ComfyUI\custom_nodes\
    ```

    - **Manual/non-Windows installation**:
    ```
    cd /home/saber7ooth/ComfyUI/custom_nodes
    ```
2.  Clone the repository in the folder.
    ```
    git clone https://github.com/loopyd/ComfyUI-FD-Tagger.git
    ```

3. Change to the `ComfyUI-FD-Tagger` folder you just created by cloning the repository:

    - **Windows Portable installation**:
    ```
    cd C:\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-FD-Tagger
    ```
    - **Manual/non-Windows installation**
    ```
    cd /home/saber7ooth/ComfyUI/custom_nodes/ComfyUI-FD-Tagger
    ```
4. Install the python dependencies:

    - **Windows Portable installation**:
    ```
    ../../../python_embeded/python.exe -s -m pip install -r requirements.txt
    ```
    - **Manual/non-Windows installation**:
    ```
    pip install -r requirements.txt
    ```

5. You're now free to start your ComfyUI instance as you normally do.

## Quick interrogation Feature

Quick interrogation of images is also available on any node that is displaying an image, e.g. a `LoadImage`, `SaveImage`, `PreviewImage` node.  

Simply right click on the node (or if displaying multiple images, on the image you want to interrogate) and select `FDTagger` from the menu.

Default settings used for this are in the `settings` section of `config.json`.