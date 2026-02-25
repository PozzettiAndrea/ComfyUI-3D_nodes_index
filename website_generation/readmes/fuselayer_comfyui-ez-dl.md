# Fork of ciri/comfyui-model-downloader 

With the following improvements:

- **Ability to cancel download** at any time (automatically deletes incomplete file)
- **Automatic file path scanning** so you can download to the correct directories when the node runs
- **Added overwrite toggle for Civitai downloader**
- **Civarchive (formerly civitaiarchive) support added v 1.0.1**
- **Generalized URL parsing**. Can take huggingface or civitai URLs in full, and in various other forms. Basically any valid link to a model, api, page, or otherwise *should* work.
  - Any of the following will work for Civitai:
     - `https://civitai.com/models/1234567?modelVersionId=2345678`
     - `2345678`
     - `https://civitai.com/api/download/models/2345678?type=Model&format=SafeTensor`
     - `https://civitai.com/api/download/models/2345678`
  - and for Huggingface:
     - `https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V2.0.safetensors`
     - `https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V2.0.safetensors?download=true`
     - `https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V2.0.safetensors`
     -  `lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V2.0.safetensors`

## Model Downloader for ComfyUI

<div align="center">
    <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://github.com/ciri/comfyui-model-downloader/blob/main/assets/logo.svg?raw=true">
    </picture>
</div>


## Introduction
This project provides an improved experimental model downloader node for ComfyUI, designed to simplify the process of downloading and managing models in environments with restricted access or complex setup requirements. It aims to enhance the flexibility and usability of ComfyUI by enabling seamless integration and management of machine learning models.

## Features
- **Easy Model Downloading**: Simplify the process of downloading models directly within the ComfyUI environment.
- **Repositories**: Currently supports hugging face and CivitAI.
- **User-friendly**: Designed with a focus on ease of use, making model management accessible to users of all skill levels.

## Available Nodes

### HF Downloader
<img width="778" height="525" alt="image" src="https://github.com/user-attachments/assets/a869c34d-03ec-4e5e-b5b7-85d6b08922ac" />


Parameters:

* model_url: Hugging Face repo ID or URL
* filename: filename to download from the repository
* save_dir: destination directory
* overwrite: overwrite existing file if it exists

### CivitAI Downloader
<img width="745" height="594" alt="image" src="https://github.com/user-attachments/assets/35482d5b-a1af-4bf4-a37e-e07de1eeb09c" />


Parameters:
* model_url: CivitAI model ID or URL
* token_id: CivitAI token ID
* save_dir: destination directory


## Better paths 

<img width="867" height="788" alt="image" src="https://github.com/user-attachments/assets/fcd78de3-be5f-4f76-a0b4-43d2d33b73c5" />


## Auto Model Finder (Experimental)

![Auto](assets/auto-downloader.png?raw=true)

Automatically searches for known files (e.g., .safetensors, .ckpt, etc) files in your canvas and looks for repositories containing them on Hugging Face. Ideally, you should use this together with the HF Downloader node to automatically download any missing models.

Troubleshooting: this node is experimental and may not work as expected. If it doesn't work, try removing the node and adding it again.

## Installation

### Via Git Clone

Clone the repository or download the extension directly into your ComfyUI project's `custom_nodes` folder:

```
git clone https://github.com/fuselayer/model-downloader-comfyui.git
```

## Usage
To use the model downloader within your ComfyUI environment:
1. Open your ComfyUI project.
2. Find the `HF Downloader` or `CivitAI Downloader` node.
3. Configure the node properties with the URL or identifier of the model you wish to download and specify the destination path.
4. Execute the node to start the download process.
5. To avoid repeated downloading, make sure to bypass the node after you've downloaded a model.

Roadmap (tentative)
- [ ] Unify nodes
- [ ] Generalize input parsing to accomodate path separators for lists of models
- [ ] Implement resume partial download in case of failure
- [ ] Remove debugging code
  


## Contributing
Contributions are welcome! Please:

* Fork the repository
* Create a feature branch
* Submit a pull request

## Support
For support, questions, or contributions, please open an issue on the GitHub repository page. Contributions are welcome!

## License


GNU Affero General Public License v3.0













