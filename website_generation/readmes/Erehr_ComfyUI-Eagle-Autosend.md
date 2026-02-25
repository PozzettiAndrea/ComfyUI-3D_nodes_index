# 🦅 ComfyUI-Eagle-Autosend

> A seamless, node-independent way to automatically send your ComfyUI generations to [Eagle](https://eagle.cool/), complete with full metadata and tags.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-brightgreen)](https://github.com/comfyanonymous/ComfyUI)

Tired of manually saving and organizing your generated images? This custom node for ComfyUI automates the entire process. Any image saved during your workflow is instantly sent to your Eagle library, intelligently tagged and annotated for effortless organization. 

## 📚 Table of Contents

- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## ✨ Key Features

-   **Automatic Sending**: No extra nodes needed. Any "Save Image" in your workflow will automatically send the final image to Eagle.
-   **Full Metadata Annotation**: Captures the entire metadata (prompts, seed, sampler, CFG, etc.) and adds it to the image's "Annotation" field in Eagle.
-   **Intelligent Tagging**: Automatically parses your positive prompt and adds each keyword as a tag to the image in Eagle, making your library instantly searchable.
-   **Custom Folders**: Use the settings to specify a target folder in your Eagle library. If the folder doesn't exist, it will be created for you.

## 📦 Installation

### Manual Installation

```bash
# Navigate to your ComfyUI custom_nodes directory
cd /path/to/ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/Erehr/ComfyUI-Eagle-Autosend.git

# Restart ComfyUI
```

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, please feel free to submit a Pull Request or open an issue.

## 📄 License

This project is licensed under the **MIT License**.

## 🙏 Acknowledgments

- **ComfyUI Community** - For their continuous support and valuable feedback.
- **[DraconicDragon](https://github.com/DraconicDragon)** - Comprehensive tag lists csv files

---

<div align="center">

**⭐ If you find this project helpful, please consider giving it a star! ⭐**

[Report Bug](https://github.com/Erehr/ComfyUI-Eagle-Autosend/issues) • [Request Feature](https://github.com/Erehr/ComfyUI-Eagle-Autosend/issues) • [Discussions](https://github.com/Erehr/ComfyUI-Eagle-Autosend/discussions)

</div>
