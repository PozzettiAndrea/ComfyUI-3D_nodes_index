# ComfyUI-JMESPath

A ComfyUI node that runs a [JMESPath](https://jmespath.org) query against input JSON and outputs the result.

![A screenshot showing usage of the node.](docs/workflow.png)

## Installation

### ComfyUI-Manager

- Open the Manager
- Pick "Custom Nodes Manager"
- Search for "ComfyUI-JMESPath"
- Install the latest version
- Restart ComfyUI

### Comfy-Cli

- Run `comfy node install comfyui-jmespath`
- Restart ComfyUI

### Manual

Run the following commands in the terminal:

```shell
cd custom_nodes
git clone https://github.com/Gremlation/ComfyUI-JMESPath
pip install -r ComfyUI-JMESPath/requirements.txt
```

Then restart ComfyUI.
