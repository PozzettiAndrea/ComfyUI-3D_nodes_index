# ComfyUI-Easy-DotsOCR

ComfyUI-Easy-DotsOCR is a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that provides text extraction via the DotsOCR engine. This node enables users to extract text from images directly within ComfyUI workflows.

## Installation
1. Clone this repository into your ComfyUI `custom_nodes` directory:
   ```bash
   git clone https://github.com/yolain/ComfyUI-Easy-DotsOCR
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Restart ComfyUI. The DotsOCR node will be available in the node list.

## Usage
- Add the DotsOCR node to your ComfyUI workflow.
- Connect an image input to the node.
- Run the workflow to extract text from the image.

## Download Models (Manual)

Download [All models](https://huggingface.co/rednote-hilab/dots.ocr/tree/main) to `ComfyUI/models/LLM/dots-ocr`

## Development
This project is developed based on [dots.ocr](https://github.com/rednote-hilab/dots.ocr). Many core OCR functionalities are adapted from this upstream project. Please refer to their repository for more details and credits.

## File Structure
- `dots.py`: Core OCR logic
- `nodes.py`: ComfyUI node definitions
- `utility/`: Helper functions for image and download operations
- `prompt_templates.yaml`: Prompt templates for OCR tasks
- `requirements.txt`: Python dependencies

## License
This project inherits the license from [dots.ocr](https://github.com/rednote-hilab/dots.ocr). Please review their license terms before use.

## Acknowledgements
- [dots.ocr](https://github.com/rednote-hilab/dots.ocr) for the original OCR implementation
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the node workflow framework

## Contact
For issues or feature requests, please open an issue on this repository.
