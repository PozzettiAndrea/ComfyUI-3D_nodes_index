# ComfyUI Loop Utilities

This is the [ComfyUI](https://github.com/comfyanonymous/ComfyUI) custom node for creating flows that needs to loop over multiple prompts one by one to generate images from different prompt in a single go.

## Directory Structure
```
Project-Name/
├── .github/                # GA workflow for publishing the ComfyUI registry 
├── workflows/              # Example workflows for your custom node
├── .gitignore              # gitignore file 
├── __init__.py             # Map your custom node display names here 
├── nodes.py                # Your custom node classes  
├── README.md               # README file
├── pyproject.toml          # Metadata file for the ComfyUI registry
└── requirements.txt        # Project dependencies 
```

## Nodes:

### Foreach Prompt
This node has two properties:
1. prompts_string
2. delimiter

Use the prompts_string to include a single large string where each prompt is seperated by delimiter.
Than connect the prompt output parameter as a text to the following node.

The next node with the rest of the flow will be invoked once for each of the prompts_string after split the string by the delimiter.

For example:

prompts_string:
```
This is prompt no. 1
---
This is prompt no. 2
---
This is last prompt no. 3
```

and the delimiter '---', the node will call the following node once with the prompt `This is prompt no. 1`, once with `This is prompt no.2` and once with `This is last prompt no. 3`.

The custom node installation guide below can usually be used for any custom node, you can use it in your README by modifying the repository name and URL.
## Installation

1. git clone repository into `ComfyUI\custom_nodes\`
```
git clone https://github.com/O-oshir/comfy-loop-utilities
```

2. Go to `ComfyUI\custom_nodes\comfy-loop-utilities` and run
```
pip install -r requirements.txt
```

If you are using the portable version of ComfyUI, do this:
```
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\comfy-loop-utilities\requirements.txt
```


