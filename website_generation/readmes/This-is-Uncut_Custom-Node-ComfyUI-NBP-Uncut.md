# Custom-Node-ComfyUI-NBP-Uncut

Node to use NBP with custom API key to improve data privacy control.
The node is, once installed available in comfy node tree under "UncutNodes"

# Install

In comfy manager, go to Custom Nodes Manager
In lower right corner click "Install via Git URL"
Paste the git url and confirm.
restart comfy.

OR

Git clone the repository into your comfyUI/custom_nodes folder

If you get error message when starting comfy, or not getting high resolution output, try to:
from inside the cloned folder with venv activated:
"pip install -r requirements.txt"
or specifically: 
"pip install --upgrade google-genai" 
start/restart ComfyUI server.

# Use

First use you will have to supply local network IP address to gain access to VertexAI APIkey. This is supplied through internal channels.
There might be a need to retry first generation to fetch key.
