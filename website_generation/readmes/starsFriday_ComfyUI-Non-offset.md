# ComfyUI-Non-offset

ComfyUI custom nodes focused on fixing pixel shift and spatial misalignment in the qwen-edit series edit models (e.g., qwen-edit-2509 and qwen-edit-2511). V1 targets qwen-edit-2509; V2 targets qwen-edit-2511.

## Examples

<table>
  <tr>
    <th align="left">Prompt: change background to a seaside sunset</th>
    <td align="center"><img width="220" src="https://github.com/user-attachments/assets/6ed8d71b-ba08-4157-81ac-30311c2eabe9" /></td>
    <td align="center"><img width="220" src="https://github.com/user-attachments/assets/15b0996a-f679-4a75-8120-acbae8a651de" /></td>
    <td align="center"><img width="220" src="https://github.com/user-attachments/assets/07f96708-319c-4ebd-9487-cf4e536d1d44" /></td>
    <td align="center"><img width="220" src="https://github.com/user-attachments/assets/995a13ef-d63e-4875-b509-d1029e4b6ece" /></td>
  </tr>
  <tr>
    <th align="left">Prompt: wear a white down jacket, sunglasses, and pink pants</th>
    <td align="center"><img width="220" src="https://github.com/user-attachments/assets/239ff036-a4d3-4591-834d-99596346930b" /></td>
    <td align="center"><img width="220" src="https://github.com/user-attachments/assets/7ec59d1c-8c12-47d9-989a-db8b4fecac31" /></td>
    <td align="center"><img width="220" src="https://github.com/user-attachments/assets/8dfb43d0-1f7b-4bd1-a89b-8547ddccc324" /></td>
    <td align="center"><img width="220" src="https://github.com/user-attachments/assets/f387b0ab-7d99-445f-a179-b784156d77db" /></td>
  </tr>
</table>

## 🚀 Key Features
- CustomSmartResizePad nodes in two variants:  
  - V1 (Standard): zero-padding, mainly for qwen-edit-2509.  
  - V2 (Edge Replicate): recommended edge-pixel replication, mainly for qwen-edit-2511.
- Why V2?  
  - In qwen-edit-2509/2511 tests, traditional black borders caused positional drift (a few to tens of pixels).  
  - Root causes:  
    - Contrast interference: strong edges between pure black padding and the original image disturb positional embeddings.  
    - Attention shift: large zero-valued regions dilute valid features during self-attention.  
  - V2 fix: replicate padding keeps the padding region visually consistent with the original edges, improving coordinate capture and eliminating inpaint misalignment.

## 🛠️ Node
### Smart Resize & Pad V2 (Edge Pixel)
- Resizes the input image proportionally to a target square (e.g., 1024x1024) and fills the short side using edge replication.

#### Inputs
- image: input image tensor.  
- target_size: target square size (default 1024, step of 8 supported).

#### Outputs
- padded_image: the filled image; the model sees a continuous frame instead of black borders.  
- mask: mask of the original region (white = original image, black = padding). It can guide models to focus on “real” pixels.

## 📂 Installation
Go to your `ComfyUI/custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes/
```

Clone this repo (or drop the `.py` files here):

```bash
git clone https://github.com/starsFriday/ComfyUI-Non-offset.git
```

Restart ComfyUI.



## 📝 License
MIT License

## Tips for qwen-edit
For non-square images, keep V2 enabled. At 1024x1024 input, qwen-edit handles bounding boxes and point guidance most reliably.

## Contribution
Found a better padding strategy? Please open an Issue or Pull Request!
