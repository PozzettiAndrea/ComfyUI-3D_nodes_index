# Dynamic AIO nodes for custom sampling

[!NOTE] You will probably need the v3-improvements ComfyUI branch for this to work. Also, This will only detect v3 nodes, which fortunately are most of ComfyUI's custom sampling nodes.


The "Any" nodes in this repository inspect your nodes use ComfyUI's dynamic combo inputs feature to generate an AIO node that combines the features of *all* of your advanced custom sampling nodes without bloating the node interface.

# How to use

Instantiate one or more of the following nodes:
- Any Guider (All-In-One)
- Any Sampler (All-In-One)
- Any Scheduler (All-In-One)
- Any Noise (All-In-One)

Connect them to CustomSamplingAdvanced as you like.

Use the combo widget to select the actual implementation. The node will dynamically update with the required inputs.

