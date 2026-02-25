# ComfyUI Sync PVM Node

This custom node allows you to generate personalized video messages (PVM) using audio, video, and multilingual text prompts inside ComfyUI.

## Installation & Usage

After cloning [ComfyUI](https://github.com/comfyanonymous/ComfyUI) and setting up a virtual environment for it, follow these steps:

1. Navigate to the custom nodes directory:  
   `cd /path/to/ComfyUI/custom_nodes/`

2. Clone this repository:  
   `git clone https://github.com/wasilone11/comfyui-pvm-node.git`

3. Install the required dependencies:  
   `pip install -r comfyui-pvm-node/requirements.txt`

4. Go back to the main ComfyUI directory and run:  
   `cd /path/to/ComfyUI/`  
   `python main.py`

5. A link will be printed in the terminal — open it in your browser to access the ComfyUI GUI.

6. In the ComfyUI interface:  
   - On the left sidebar, go to the **Nodes** tab.  
   - Search for **Sync**.  
   - Open the **Sync** node and locate the PVM node.  
   - Click **Run** to generate the output!
   - The output video link will be saved in the output csv under output_url.
   - A separate json file will be saved in the same folder which will have the Job ID's.

---
- Refer to this for an example input.csv: `https://github.com/synchronicity-labs/sync-examples/blob/main/personalized-video-messsging/python/example.csv`.
- For issues or contributions, feel free to open a pull request or create an issue in this repository. Moreover, you can also refer to: `https://github.com/synchronicity-labs/sync-examples/tree/main/personalized-video-messsging/python`

