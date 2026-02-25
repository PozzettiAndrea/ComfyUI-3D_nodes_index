Re-build version of my custom node: [A1rSpace](https://registry.comfy.org/nodes/comfyui_a1rspace)  
Will be public to ComfyUI Registry when it done.  
However, you could downlaod this repo to use it for now, just needs to pay attention to the update.  

# A1RWorkshop  
A1RWorkshop is a custom node for ComfyUI that simplify usese.  

## Function descriptions  
### Embedding Tags
The "Open Embedding Editor" option has been added to the context menu of the model loading node, which can open a window to edit and manage the embedding terms.  
The "Open Embedding Manager" option has been added to the context menu of the canvas, which can open a window to manage embedded terms.  

tips: Using it to embedding models trigger tags, style tags, quality tags, etc. It will bind the embedding to the model. In this way, you can easily switch between different models and shoulden't change text encode anymore.  

### Collectors
There are two new nodes: "Widget Collector" and "Node Collector". Just as the name suggests, they can collect widgets and nodes, respectively.  
They have a "Open Collector" button, toggled it to open the collect mode, then other nodes will append a "Add Widgt/Node to Panel" option to their context menu.  
The "Open Collector" button could hidden when clik the "Hide Switch" button in their context menu.  
The value of widgets which are collected will be syncly updated to the original panel.  

warn: The reorder function of the widget collector is not implemented yet.  

### Seed Control
A random seed node. It hava two buttons: "manural random" and "pull history".  
The "manural random" button will random a seed and update the "control after generate" to fixed.  
The "pull history" button will pull the seed value from the history, it needs the history list lenth is >=2, and update control to fixed value .  
These two buttons will queue a prompt when cliked.  

### Size Canvas
A 2D slider in the "Canvas Size" panel, it will update the width and height size when changed, provids a preset list.  
The range and step of the slider is configable, you can find "Canvas Setting" in the context menu, they are not customizable, but the value range which I provide is enough for most of the use case.  