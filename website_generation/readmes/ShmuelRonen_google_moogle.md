# Google Moogle

Google Moogle is a Google Translator node for ComfyUI that provides easy-to-use text translation capabilities directly within your ComfyUI workflows.

![image](https://github.com/user-attachments/assets/1371b294-c65f-4547-8fbc-4bca77115368)


## Features

- Translate text between multiple languages
- Auto-detect source language
- Simple interface that integrates with ComfyUI's node system
- Support for all languages available in Google Translate

## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/ShmuelRonen/google_moogle.git
cd google_moogle
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. After installation, restart ComfyUI
2. In the node browser, search for "Google Moogle" or look in the "text" category
3. Connect the node to any text source in your workflow
4. Configure the source and destination languages
5. Run your workflow to generate the translation

## Node Parameters

- **input_text**: The text you want to translate
- **source_language**: The language of the input text (set to "auto" for automatic detection)
- **destination_language**: The language to translate the text into

## Example Workflow

1. Create a "Text" node with your source text
2. Connect the "Text" node to the "Google Moogle" node
3. Set the destination language
4. Connect the "Google Moogle" output to any node that accepts text input

## Important Notes

- This node uses the unofficial `googletrans` Python package, which relies on Google Translate's web interface
- As this does not use an official API, translations may occasionally fail or be rate-limited
- For production use cases with high volume, consider using an official translation API

## Requirements

- ComfyUI
- Python 3.8+
- Dependencies listed in requirements.txt:
  - googletrans
  - idna
  - sniffio
  - typing-extensions

## License

[MIT License](LICENSE)

## Disclaimer

This tool is not affiliated with, authorized by, or endorsed by Google Inc. "Google Translate" is a trademark of Google Inc.
