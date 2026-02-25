# 🍒 ComfyUI-CherryPicker

A workflow-friendly "Studio" node for ComfyUI that allows you to manually save images to a specified folder with a single click.

### 🚀 Why use this?
In standard ComfyUI, saving an image usually requires "Queueing" the whole prompt. If you have multiple samplers (like a Base Pass + Detailers) on **Random Seeds**, re-executing just to save one image will change the results. 

**CherryPicker** solves this by adding a physical **"Save Image Now"** button to the node. You generate until you see a winner, click the button, and it's instantly saved to your specified directory—no re-sampling required.

### 🛠️ Installation
1. **Via ComfyUI-Manager (Recommended):** Search for `Cherry Picker` and click install.
2. **Manual:** Clone this repo into your `custom_nodes` folder:
   ```bash
   git clone https://github.com/malfyz/ComfyUI-CherryPicker.git

⚙️ How to Use
* images: Connect any image output (Base, Detailer, or Final).
* save_path: The full path to your "Keepers" folder (e.g., D:/Uffie_Project/Keepers).
* filename_prefix: The name to start your files with (e.g., Uffie_Shot).
* The Button: Once an image is displayed in the preview, click "Save Image Now" to commit it to disk.
* There is an autosave toggle so the node can operate as a normal 'Save Image' node as needed.

🌟 Features
* Zero Reruns: Saves the current state of the node instantly.
* Seed Independent: Keep your samplers on 'Randomize' and only save the "Golden Shots."
* Custom Directories: Easily organize different "shoots" into different folders.
