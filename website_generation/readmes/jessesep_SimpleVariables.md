# SimpleVariables

A lightweight ComfyUI node pack for storing and retrieving any data by name across your workflow.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jessesep/SimpleVariables.git
```

Restart ComfyUI and search for **"variable"**.

## Nodes

| Node | Description |
|------|-------------|
| **Set Variable** | Store any data with a name, shows preview on node |
| **Get Variable** | Retrieve data by name, shows preview on node |
| **List Variables** | Show all stored variables on node |
| **Clear Variables** | Clear all stored variables |

## Usage

```
[Load Image] → [Set Variable] (name: "ref")
                     ↓
              value (passthrough)

              Node displays: "ref = Tensor [1, 512, 512, 3]"

... elsewhere ...

[Get Variable] (name: "ref") → value → [Any Node]

              Node displays: "ref = Tensor [1, 512, 512, 3]"
```

## Features

- **Universal** - Works with all data types (Image, Mask, Latent, Model, etc.)
- **On-node preview** - See what's stored directly on the node (type + shape/value)
- **Passthrough** - Set Variable passes data through
- **Debug** - List Variables shows all stored data

## Preview Examples

Preview is shown directly on each node:

| Data Type | On-Node Display |
|-----------|-----------------|
| Image | `my_image = Tensor [1, 512, 512, 3]` |
| String | `prompt = "a beautiful sunset..."` |
| Int | `steps = 20` |
| Model | `my_model = BaseModel` |

## License

MIT License

## Credits

Created by jessesep with Claude (Anthropic).
