# mc_qwen
comfyui node TextEconder for qwen image edit with internal lanczos rescale  instead of area rescale.

Install Via ComfyUI Manager.

Manual Installation:

```bash
# Navigate to ComfyUI's custom_nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/tester4488/mc_qwen.git
```

You can find in:

MC nodi/qwen

based on
https://huggingface.co/Phr00t/Qwen-Image-Edit-Rapid-AIO/blob/main/fixed-textencode-node/nodes_qwen.py




![Immagine 2025-11-08 171335](https://github.com/user-attachments/assets/b3d9b842-443d-46f6-9f18-0d179283c437)

and after reading this post:

https://www.reddit.com/r/comfyui/comments/1nxrptq/how_to_get_the_highest_quality_qwen_edit_2509/?chainedPosts=t3_1or205v

<img width="1006" height="348" alt="immagine" src="https://github.com/user-attachments/assets/d3dbf728-e23c-4926-a120-067724470d5a" />



2025/11/10
Adding image_qwen_image_edit-AIO-v001.json workflow:

<img width="581" height="679" alt="immagine" src="https://github.com/user-attachments/assets/4593cf32-3852-4508-a346-5e6cbde6616c" />

adding image_qwen_image_edit-AIO-3loras-001.json workflow with Multiples angles and Light restoration loras.

<img width="924" height="729" alt="immagine" src="https://github.com/user-attachments/assets/26f3bb7b-1a86-4677-8378-9783abfa85e5" />

adding a wokflow with the subgraph nodes and Camera Control Prompt Generator node.

<img width="503" height="398" alt="immagine" src="https://github.com/user-attachments/assets/1f2a1388-fbdf-4fd5-af40-e4c3137d3ff7" />
<img width="512" height="586" alt="immagine" src="https://github.com/user-attachments/assets/bf597943-7767-431c-9f7b-0474c0035181" />


