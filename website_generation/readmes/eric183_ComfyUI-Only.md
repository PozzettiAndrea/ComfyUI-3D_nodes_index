[Read this document in Chinese (简体中文)](./docs/zh-CN.md)

# ComfyUI-Only

A collection of custom nodes for ComfyUI, initially focused on workflow parsing, now expanded to provide advanced file loading features designed to enhance your workflow efficiency and experience.

## 🌟 Key Features

### 1. Load Latent (Advanced) ⭐ Core Feature
- 📤 **Upload from Anywhere**: Select `.latent` files from anywhere on your computer using the "Upload Latent" button, eliminating the need to place them in the `input` folder.
- ✨ **Drag and Drop**: Upload `.latent` files by simply dragging them from your file manager onto the node.
- 🤖 **Intelligent Structure Parsing**: Automatically parses various internal latent structures, whether it's the standard `samples` key, the non-standard `latent_tensor` key, or even a raw tensor.
- 🔢 **Smart Dimension Handling**: Automatically processes 3D (image), 4D (batched images), and 5D (video) latent tensors to ensure compatibility with downstream nodes like VAEDecode.

### 2. WorkflowImageFileLoader
- 📁 **Direct File Loading**: Load image files directly from your file system.
- 🔍 **Auto-Parse Metadata**: Automatically parses workflow metadata from the image.
- 🎯 **Smart Prompt Extraction**: Intelligently extracts positive and negative prompts.
- 🏷️ **Smart Model Extraction**: Extracts the model name from the CheckpointLoaderSimple node.
- ✅ **Solves a Core Problem**: Addresses the issue where the native `IMAGE` type does not contain metadata, making workflow reuse difficult.

---

*(Older node descriptions have been collapsed for brevity.)*

## 🚀 Installation & Setup

### Recommended Method: Install via ComfyUI Manager
1.  **Install ComfyUI Manager**: If you haven't already, install it by following the [official ComfyUI Manager instructions](https://github.com/ltdrdata/ComfyUI-Manager).
2.  **Search for the Node**:
    -   Launch ComfyUI.
    -   Click the "Manager" button in the sidebar.
    -   Click "Install Custom Nodes".
    -   Type `ComfyUI-Only` or `eric183` in the search bar.
3.  **Install Node**: Find this extension in the search results and click the "Install" button.
4.  **Restart ComfyUI**: After installation, restart ComfyUI.

### Alternative Method: Manual Installation (Git Clone)
1.  **Navigate to Directory**: Open a terminal and navigate to the `custom_nodes` directory within your ComfyUI installation.
    ```bash
    cd path/to/your/ComfyUI/custom_nodes
    ```
2.  **Clone the Repository**: Use the `git clone` command to clone this repository.
    ```bash
    git clone https://github.com/eric183/ComfyUI-Only.git
    ```
3.  **Restart ComfyUI**: Restart ComfyUI to load the new nodes.

## 📖 How to Use

#### ⭐ Loading Latent Files (Recommended)
1. Add the `Load Latent (Advanced)` node from the menu (under the `ComfyUI-Only/Latent` category).
2. Click the `Upload Latent` button to select a `.latent` file from your computer.
3. Alternatively, drag and drop the `.latent` file directly onto the node.
4. The node will automatically handle the upload, parsing, and formatting, then connect the `LATENT` output to the next node (e.g., `VAEDecode`).

#### Parsing Workflows from Images
1. Add the `WorkflowImageFileLoader` node (under the `ComfyUI-Only/Image` category).
2. Select the image file you want to parse from the `image_file` dropdown menu.
3. The `positive_prompt`, `negative_prompt`, and `checkpoint_name` will be automatically extracted.

## 📁 Project Structure
```
.
├── __init__.py           <-- Main entry point, registers nodes and JS extensions
├── js/
│   └── latent_loader.js  <-- Frontend UI logic for the advanced latent loader
├── nodes/
│   ├── image_processing_nodes.py
│   └── latent_nodes.py
├── LICENSE
└── README.md
```

## ⚙️ Requirements
- Python 3.8+
- ComfyUI
- PyTorch
## 📝 Changelog

### v2.1.0 - Integration & Simplification (Codename: Orion)
- 🎉 **Integration**: The project has been successfully added to the official **ComfyUI Manager** list for one-click installation.
- 🚀 **Simplification**: **Highly recommended** to install via ComfyUI Manager for a streamlined user experience.
- 🧹 **Refactor**: Removed `requirements.txt`. Dependencies are now managed by ComfyUI or the user as needed, making the project more lightweight.
- 📚 **Documentation**: Completely rewrote `README.md` with updated installation instructions, project structure, and dependency information for clarity and accuracy.

### v2.0.0 - Advanced Loader Edition (Codename: Phoenix)
- 🔥 **New**: Released the `Load Latent (Advanced)` node with support for uploading and dragging-and-dropping latent files from any location.
- ✨ **Added**: Developed a standalone frontend JS extension for the new node, providing a native-level UI experience.
- 🧹 **Refactor**: Restructured the project, adding a `js` directory and `requirements.txt`.
- 📚 **Documentation**: Overhauled `README.md` to focus on new features and simplify older descriptions.

### v1.2.0
- ✅ Added: Checkpoint model name extraction from CheckpointLoaderSimple nodes.
- ✅ All nodes now have a `checkpoint_name` output.

*(Older logs have been omitted.)*

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

MIT License - See the [LICENSE](LICENSE) file for details.
