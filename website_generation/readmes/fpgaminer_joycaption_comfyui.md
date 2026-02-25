# JoyCaption ComfyUI Nodes

Custom ComfyUI Nodes for running JoyCaption inside ComfyUI.

## Usage

The `JoyCaption` node allows you to pick the desired Caption Type, Caption Length, and various additional Extra Options for tweaking the captions.  It takes an Image as input, and will output the Query that was built and sent to the JoyCaption model based on your settings, and the resulting Caption.  This node automatically downloads the JoyCaption model into `LLavacheckpoints`.  The model can be loaded in 8-bit or 4-bit quantization if low memory usage is needed (though quality will degrade).

The `JoyCaption (Custom)` node works much like the `JoyCaption` node but lets you input a custom System Prompt and Query.
