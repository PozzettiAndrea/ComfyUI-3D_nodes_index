ComfyUI - Info Utils
=============================================================================

Collection of custom nodes for ComfyUI that facilitate simpler information
providing and gathering, such as Show Text and Token Counter nodes.

Install
-----------------------------------------------------------------------------

**Option 1**

Install via [ComfyUI-Manager][1].

**Option 2**

Clone the repository into your ComfyUI custom_nodes directory.
```text
git clone https://github.com/exectails/comfyui-et_infoutils
```

Nodes
-----------------------------------------------------------------------------

### Token Counter

A passthrough text node that takes a string, counts the tokens in it,
and displays the amount in a text box on the node. The original string
is returned as is, so the node can be plugged in between a text provider
and an encoder.

Note that in case of list inputs (such as multiple prompts from a dynamic
prompt node), the counter counts only one of the strings. Should the prompt
lengths vary wildly, the counter might not be reliable.

### Text Box

A primitive string node that provides a multiline text box for longer
text inputs.

### Show Data

A node primarily intended for debugging that takes an arbitrary input
and displays it in string format.

### Inspect Text

A node primarily intended for debugging that takes a string input,
displays it, and passes it through to its output for further processing.

### Present Image

A node that takes images and displays them, with a toggle for saving them
at a configurable path. It essentially merges the Preview and Save Image
nodes, while giving control over the save path and adding a simpler way
to toggle saving on and off.


[1]: https://github.com/ltdrdata/ComfyUI-Manager
