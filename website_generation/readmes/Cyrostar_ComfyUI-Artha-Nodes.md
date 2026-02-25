# ComfyUI-Artha-Nodes
ComfyUI custom nodes for general purpose.

## Installation
1. Clone this repo into ComfyUI `custom_nodes` folder.
2. Install dependencies: `pip install -r requirements.txt`
   or if you use the portable install, run this inside ComfyUI root folder:

  `python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Artha-Nodes\requirements.txt`
  
## Gemini API

You will need a Gemini API key to use the Gemini custom nodes. 
To get your API key, visit the Google AI Studio from the link below.

<a href="https://aistudio.google.com" target="_blank">GOOGLE AI STUDIO</a>

Once you have your API key, it's good practice to place it in the api.json 
file located in the ComfyUI/custom_nodes/ComfyUI-Artha-Nodes folder.
Alternatively, you can enter it directly into the custom node's api_key field, 
but be aware that it will be visible in plain text.

You may also choose to define **GEMINI_API_KEY** as a global variable.

