# ComfyUI Sync Lipsync Node

This custom node allows you to perform audio-video lip synchronization inside ComfyUI using a simple interface.

## Installation & Usage

After cloning [ComfyUI](https://github.com/comfyanonymous/ComfyUI) and setting up a virtual environment for it, follow these steps:

1. Navigate to the custom nodes directory:  
   `cd /path/to/ComfyUI/custom_nodes/`

2. Clone this repository:  
   `https://github.com/synchronicity-labs/sync-comfyui.git`

3. Install the required dependencies:  
   `pip install -r requirements.txt`

  **IMPORTANT**: If you want to ignore steps 2-3, just run `comfy node install comfyui-sync-lipsync-node` in your `/path/to/ComfyUI/custom_nodes/`

5. Go back to the main ComfyUI directory and run:  
   `cd /path/to/ComfyUI/`  
   `python main.py`

6. A link will be printed in the terminal — open it in your browser to access the ComfyUI GUI.

7. In the ComfyUI interface:  
   - On the left sidebar, go to the **Nodes** tab.  
   - Search for **Sync**. You will find the sync nodes for video input, audio input, API key, generation process, and output. Connect the first three to the generate node as input and output node as output.
   - Input your video, audio, and API key. For audio and video, you can give a url or a local path as an input. The local files should be in the ComfyUI repository that you are using. If you want to load a video or audio from local, connect the input audio/video nodes to LoadVideo/Audio nodes.  
   - Click **Run** to generate the synced output.
   - It will save the video along with the job_id in a json file. You can also give a desired path and video name in the output node.
    **IMPORTANT**: For more information on each node, hover over them and a description will appear.
---

For issues or contributions, feel free to open a pull request or create an issue in this repository.

