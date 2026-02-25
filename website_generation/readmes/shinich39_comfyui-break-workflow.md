# comfyui-break-workflow

Break the execution, save the incompleted image then continue later.

## Usage  

- Add node > utils > Break

#### Break

- KSampler - VAE Decode - Save Image(Save the incompleted image)  
- KSampler - Break - KSampler(Will be skipped) - ...
- KSampler - Break - KSampler(Will be skipped) - Break - KSampler(Execution required twice) - ...  

#### Continue

Drag and Drop the incompleted image on ComfyUI and Run workflow.

#### Continue multiple images

Drag and Drop the incompleted images on Break node.  
Images will be added to the queue and run workflow with the skipped nodes.  

## Acknowledgements

- [JSON5](https://json5.org/)