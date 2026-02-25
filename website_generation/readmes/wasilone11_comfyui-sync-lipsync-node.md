# ComfyUI Sync Lipsync Node

This custom node allows you to perform audio-video lip synchronization inside ComfyUI using a simple interface.

## Installation & Usage

After cloning [ComfyUI](https://github.com/comfyanonymous/ComfyUI) and setting up a virtual environment for it, follow these steps:

1. Navigate to the custom nodes directory:  
   `cd /path/to/ComfyUI/custom_nodes/`

2. Clone this repository:  
   `git clone https://github.com/wasilone11/comfyui-sync-lipsync-node.git`

3. Install the required dependencies:  
   `pip install -r comfyui-sync-lipsync-node/requirements.txt`

4. Go back to the main ComfyUI directory and run:  
   `cd /path/to/ComfyUI/`  
   `python main.py`

5. A link will be printed in the terminal — open it in your browser to access the ComfyUI GUI.

6. In the ComfyUI interface:  
   - On the left sidebar, go to the **Nodes** tab.  
   - Search for **Sync**. You will find three sync nodes; one for input, one for generation and one for output. Connect them to each other.
   - Input your video, audio, and API key. For audio and video, you can give a url or a local path as an input. The local files should be somewhere in the ComfyUI repository that you are using.  
   - Click **Run** to generate the synced output!

---

For issues or contributions, feel free to open a pull request or create an issue in this repository.

