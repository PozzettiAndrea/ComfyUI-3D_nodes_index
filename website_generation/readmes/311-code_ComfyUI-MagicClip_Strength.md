# 🎨🖼️ ComfyUI MagicClip_Strength for SDXL 🖼️🎨

![Magic Clip Strength](https://github.com/311-code/ComfyUI-MagicClip_Strength/blob/main/magic_clip_strength.png?raw=true)

<p align="center">
  <a href="https://ko-fi.com/311_code"><img src="https://img.shields.io/badge/Support%20Me-Ko--Fi-red?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support me on Ko-Fi"></a>
</p>

## 🎨 Regular Clip Text Encode (ZZzzz)
![Regular Clip Text Encode](https://github.com/311-code/ComfyUI-MagicClip_Strength/blob/main/default_clip_text_encode.png?raw=true)

## ✨ Introduction

This project allows you to adjust SDXL's two text encoder's strengths individually for `clip_g` (ViT-bigG) and `clip_l` (CLIP-ViT-L) within **ComfyUI**. (And other adjustments)

## 🔧 Features

- 🎯 **Clip Text Encoding**: Adjust `clip_g` (global) and `clip_l` (local) strengths for better text-to-image alignment.
- 🖼️ **Enhanced Layer_idx values**: Specify positive `layer_idx` values. (ComfyUI usually just only supports negative values.) You can mix and match with + and - values on positive and negative prompt.

## 🛠️ Installation Instructions

1. **Download ZIP and Extract**:
    - Download the ZIP and extract it to:
      ```
      /ComfyUI/custom_nodes/ComfyUI-MagicClip_Strength
      ```
2. **Or Clone the Repository**:
    - Clone the repository directly into your ComfyUI custom nodes directory:
      ```sh
      git clone https://github.com/311-code/ComfyUI-MagicClip_Strength
      ```

3. **Find the Node**:
    - In **ComfyUI**, type `SDXL` to find the node labeled:
      ```
      311_code SDXL Clip Text Encode
      ```

> **No `requirements.txt` file is needed.**

## 💡 How to Use

- After installation, use the node to adjust Clip strength directly in your workflows.
- For more refined control over SDXL models, experiment with `clip_g` and `clip_l` strengths and positive and negative values, layer_idx, and size_cond_factor. (as shown in example image)
- PS. I also highly trying out a 'saveclip' node on your favorite SDXL checkpoint, then use the newly saved custom clip_l in dualclip loader to mix and match clip_l with various models. (use this node and adjust strength)

Please note that using all positive layer_idx values for both the positive and negative prompts can be hit or miss. For example, here is the default ComfyUI purple galaxy glass bottle prompt with values +8 for pos/neg prompts. I recommend either mixing positive and negative values or using only negative values for better prompt adherence.
<img src="https://github.com/311-code/ComfyUI-MagicClip_Strength/blob/main/comfy_default_w_dual_positive_layer_idx.png?raw=true" alt="Dual + layer_idx" width="75%">

## 💖 Support Me

Creating and maintaining this project takes time and effort. If you find it helpful, consider supporting me:

<p align="center">
  <a href="https://ko-fi.com/311_code" target="_blank"><img src="https://img.shields.io/badge/Support%20Me-Ko--Fi-red?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support me on Ko-Fi"></a>
</p>

## 🤝 Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
