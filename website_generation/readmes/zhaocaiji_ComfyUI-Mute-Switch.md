# ComfyUI Mute Switch (Dynamic)

A smart logic switch for ComfyUI that physically **MUTES** upstream nodes to save GPU/CPU resources, featuring dynamic inputs and auto-cleanup.

Unlike a standard "Bypass" (which passes data through), this node sets the upstream execution mode to **Mute (Never)**. This allows ComfyUI to completely skip processing entire branches of your workflow, saving time and VRAM.

## Features

* **True Resource Saving**: Mutes unconnected or disabled branches preventing execution.
* **Dynamic Inputs**: Automatically adds new input slots as you connect them.
* **Auto-Cleanup**: Automatically removes unused slots and reorders inputs when links are removed.
* **Odd/Even Logic**: Controlled by an integer input (1=On, 2=Off).
* **Invert Toggle**: Easily flip the logic without changing the input number.
* **Zero-Output**: Acts as a workflow sink (Output Node), no extra output sockets needed.

## Installation

1.  Clone this repository into your `ComfyUI/custom_nodes/` folder:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ComfyUI-Mute-Switch.git](https://github.com/YOUR_USERNAME/ComfyUI-Mute-Switch.git)
    ```
2.  Restart ComfyUI.

## Usage

1.  **Add Node**: Search for `Mute Switch`.
2.  **Control**: Connect an `Int` or `Primitive` node to the `control_value` widget.
    * **Odd Numbers (1, 3...)**: Inputs are **Active**.
    * **Even Numbers (0, 2...)**: Inputs are **Muted**.
3.  **Invert**: Use the `invert` switch in the node widget to flip the logic (Odd=Mute, Even=Active).
4.  **Connect**: Drag your workflow branches (e.g., the output of a specialized module) into `input_1`. A new `input_2` will automatically appear.

## Why use this?

Standard boolean switches in ComfyUI often calculate *both* branches before discarding one. This node uses frontend JavaScript to act on the graph before execution starts, ensuring the disabled branch never even loads into memory.