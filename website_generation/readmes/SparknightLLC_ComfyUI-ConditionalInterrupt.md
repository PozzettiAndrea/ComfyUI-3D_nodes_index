# ComfyUI-ConditionalInterrupt

A node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that terminates the workflow processing if `proceed` is set to False. More convenient than manually bypassing a bunch of nodes.

This is a restructured version of the `SRL Conditional Interrupt` node from the [srl-nodes](https://github.com/seanlynch/srl-nodes/tree/main) pack. Thank you to @seanlynch for his original work.

My take on this function has the following differences:

- It does not require an additional input node for the termination conditional; you can simply toggle `proceed` in the UI, saving space in your workflow
- The conditional logic is flipped; True means proceed, False means terminate
- Additional `delay_helper` input for control over processing order
- The srl-nodes pack contains a different node that allows execution of arbitrary code--a potential security risk--whereas this repo is not bundled with any other nodes

### Inputs

- `input`: Passthrough any data for processing
- `proceed`: Determines whether to terminate the workflow
- `delay_helper` (optional, experimental): Additional input of any type that might help with postponing the execution of Conditional Interrupt if you find it's activating too early