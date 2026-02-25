# ComfyUI Safety Checker

This project provides custom safety checkers for image classification using Falcons AI and CompVis models. The safety checkers are designed to detect and filter out NSFW content from images.

## Features

- Falcons AI Safety Checker
- CompVis Safety Checker

## Requirements

- Python 3.8+
- PyTorch
- Transformers
- ComfyUI

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/shabri-arrahim/ComfyUI-Safety-Checker.git
   cd ComfyUI-Safety-Checker
   ```

2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Download the models and place them into the `diffusers` folder in the `models` directory:

   - Falcon AI model:

     ```sh
     huggingface-cli download Falconsai/nsfw_image_detection --local-dir models/diffusers/Falconsai_nsfw_image_detection
     ```

   - CompVis model:
     ```sh
     huggingface-cli download CompVis/stable-diffusion-safety-checker --local-dir models/diffusers/CompVis_stable_diffusion_safety_checker
     ```

## Usage

### Running with ComfyUI

1. Ensure you have ComfyUI installed and set up. If not, follow the instructions on the [ComfyUI GitHub page](https://github.com/comfyanonymous/ComfyUI).

2. Place this cloned repository into the ComfyUI custom nodes directory:

   ```sh
   cp -r /path/to/ComfyUI-Safety-Checker /path/to/comfyui/custom_nodes/
   ```

3. Start ComfyUI:

   ```sh
   cd /path/to/comfyui
   python main.py
   ```

4. In the ComfyUI interface, you should now see the custom nodes `FalconsAISafetyChecker` and `CompVisSafetyChecker` available under the "SafetyChecker" category.

5. Use these nodes in your ComfyUI workflows to filter images for NSFW content.

## License

This project is licensed under the MIT License.
