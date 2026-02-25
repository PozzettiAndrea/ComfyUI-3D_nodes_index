# ComfyUI-PackedPipes

![ComfyUI-PackedPipes](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/images/logo.png)

I decided to share my custom nodes that help organize connections in the ComfyUI workflow by combining multiple links into a single pipeline link. This extension adds two nodes, `Pipe Packer` and `Pipe Unpacker`, to the `utils` category.

* `Pipe Packer` accepts up to 16 connections of any type.
* The `Pipe Unpacker` unpacks all input ports of its `Pipe Packer` into its output ports in the same order.
* Supports rerouters and subgraphs.
* Supports custom output port labels for connected nodes.
* The `Pipe Packer` node supports nested connections from other packers.
* When an input port is connected, the `Pipe Unpacker` node automatically synchronizes with its `Pipe Packer` node.

> [!WARNING]
> Does not support Nodes 2.0 theme.

## Installation

Clone this repository into the `custom_nodes` folder of your ComfyUI installation:
```
git clone https://github.com/id7238/ComfyUI-PackedPipes.git
```

## Examples

### 1. Usage example

![](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/images/workflow_example1.png)

### 2. An example of nested Packers and Unpackers

![](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/images/workflow_example2.png)

### 3. A complex example

This is an example from a modified Wan 2.2 14B I2V workflow template, modified to sequence scenes to create a video longer than 5 seconds. The last frame is passed to the next scene as the first image. The subgraph of the second scene in the workflow can be duplicated as a subsequent scene. Unused scenes other than the first can be bypassed.

[Download the workflow](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/workflows/video_wan2_2_14B_i2v_sequence.json)

![](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/images/workflow_example3-0.png)
[Setup subgraph](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/images/workflow_example3-1-setup.png)
| [First scene subgraph](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/images/workflow_example3-2-scene1.png)
| [Second and subsequent scenes subgraph](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/images/workflow_example3-3-scene2.png)
| [Create Video subgraph](https://raw.githubusercontent.com/id7238/ComfyUI-PackedPipes/docs/assets/images/workflow_example3-4-create_video.png)


