# Comfyui Dynamic Params Node

Comfyui custom nodes that support dynamic parameter addition and deletion
Click the add button to add parameters with a specified name, type, value, description, and modify their values, while generating corresponding outputs. The added parameters and corresponding outputs can be deleted

## Nodes

![Image](https://github.com/user-attachments/assets/2bd391dd-0fc1-48d2-8582-99b9d3c9236c)

![Image](https://github.com/user-attachments/assets/aab153ce-ffd0-4cca-babd-391976ff0f15)

![Image](https://github.com/user-attachments/assets/859d432c-920b-4500-b13b-948c1507cc38)

## Installation

1. Navigate to your ComfyUI custom nodes directory:

```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:

```bash
git clone https://github.com/erehr/comfyui_erenodes.git
```

3. Restart ComfyUI

## Features

### Dynamically add parameters

You can specify the name, type, value, description, and modify the value of the added parameter

### Generate corresponding output

Each added dynamic parameter needs to have a corresponding output

### Delete added parameters and corresponding output

All dynamic parameters added and corresponding output to the node can be deleted

### The values of dynamically added parameters are prioritized to be taken from the input

If the dynamic parameter is connected to the output of another node, its value is taken from the output of the connected node. If it is not connected to another node, its own added and modified value is taken;

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
