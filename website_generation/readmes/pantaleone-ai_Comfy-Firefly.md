# ComfyUI Adobe Firefly Node (Beta)

This is a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to generate images using **Adobe Firefly Services API (v3)** directly within your workflows.

## ✨ Features

* **Text to Image Generation**: seamless connection to Adobe Firefly v3.
* **Auto-Authentication**: Automatically handles token exchange and caching using your Client ID and Secret.
* **Native ComfyUI Format**: Outputs standard `IMAGE` tensors.

## 🛠️ Installation

1.  Navigate to your ComfyUI `custom_nodes` directory.
2.  Clone this repository or place the `ComfyUI-Adobe-Firefly` folder there.
3.  Install requirements: `pip install -r requirements.txt`
4.  Restart ComfyUI.

## 🔑 Getting Adobe Credentials

1.  Go to the [Adobe Developer Console](https://developer.adobe.com/console/home).
2.  Create a Project > Add API > "Firefly Services".
3.  Choose "OAuth Server-to-Server".
4.  Copy your **Client ID** and **Client Secret** into the node inputs.

## 📄 License
MIT License.