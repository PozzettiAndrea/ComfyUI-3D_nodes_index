[English](./README.md) | [Русский](./README.ru.md)

# ComfyUI Nano Banana Node

![Nano banana Node](./images/screenshot.png)

This repository contains a custom node for ComfyUI, "Nano banana", designed for advanced image editing using the Google Gemini API.

This project is based on the original [Visionatrix/ComfyUI-Gemini](https://github.com/Visionatrix/ComfyUI-Gemini) repository.

## Features

The "Nano banana" node allows you to perform context-aware image editing by providing:
- A base image to be modified.
- One or more reference images (for style, patterns, etc.).
- A descriptive text prompt detailing the desired changes.

## How to Use

1.  **`image_to_edit`**: Connect the primary image you want to modify to this input. The output image will maintain the aspect ratio of this input.
2.  **`reference_image_1` / `reference_image_2` / `reference_image_3` / `reference_image_4` / `reference_image_5`**: Use these inputs for any reference images, such as textures, patterns, or style examples that you want to apply to the main image.
3.  **`prompt`**: Write a descriptive, narrative prompt explaining the edit. For example: "On the main image, change the color of the walls to a rich red, using the texture from the reference image."

## Outputs

- **`image`**: The resulting edited image. In case of an error, a black image will be outputted to prevent workflow crashes.
- **`status`**: A string indicating the status of the generation:
    - "Complete": The image generation was successful.
    - "Error: Prompt or image was blocked by safety filters.": The Gemini API refused to generate content due to safety settings.
    - "Error: Could not decode image from API response: [details]": The API returned data that could not be interpreted as an image.
    - "Error: [other details]": A general error occurred during processing or API communication.
