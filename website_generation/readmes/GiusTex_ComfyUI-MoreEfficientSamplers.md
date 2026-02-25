# ComfyUI-MoreEfficientSamplers
A couple more advanced samplers based on efficiency-nodes comfyui.

For who wants more nodes packed together.

### Updates:
- Added `Sampler Custom UltraAdvancedPlus (Efficient)`, more info below.

<img width="1788" height="696" alt="Nodes example" src="https://github.com/user-attachments/assets/e56a2a69-15ec-4c9a-bf25-129d52ad651d" />

<img width="297" height="613" alt="Sampler Custom Advanced (Eff)" src="https://github.com/user-attachments/assets/44271998-3896-4788-ba9d-e11cc7c39157" />

A simple edit of the native sampler custom to let it render a preview while still generating the image/video.

<img width="333" height="615" alt="Sampler Custom Ultra Advanced (Eff)" src="https://github.com/user-attachments/assets/c2d84fe0-0ca4-49cf-8df2-afbfa3686f7e" />

- An edit of efficiency-nodes's ksampler adv. (eff.) to let it accept custom samplers and schedulers (sigmas), very useful when paired with the `flowmatch scheduler`, from [here](https://github.com/BigStationW/flowmatch_scheduler-comfyui), useful with video models using lightx loras.
- It can also slice internally the sigmas if you use a refiner (example: first 4 steps, 4 sigmas; 2 steps later for the refiner, last 2 sigmas), without the need for an external node (like comfyui `split sigmas` node).

<img width="286" height="495" alt="Sampler Custom UltraAdvancedPlus Efficient" src="https://github.com/user-attachments/assets/37d890ec-95ff-4b0f-bce5-8576a3742284" />

- Same as the `UltraAdvanced` node except it accepts a guider too. Thought for my [ttm custom node](https://github.com/GiusTex/ComfyUI-Wan-TimeToMove), but you can use it for other sampling processes requiring a guider.
- Like the above node, this too can slice internally the sigmas.

### Download
To install ComfyUI-MoreEfficientSamplers, follow these steps:
- Go in the ComfyUI `custom_nodes` folder, then download the repository or clone it here: `git clone https://github.com/GiusTex/ComfyUI-MoreEfficientSamplers.git`.
- Restart ComfyUI.
