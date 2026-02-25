# ComfyUI-Cyber-Steganography 🕵️‍♂️💻

> "The best place to hide a secret is in plain sight."

A **Cyberpunk/Spy-craft** custom node pack for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to hide secret text messages inside AI-generated images using Steganography (LSB).

This tool acts as a "Digital Watermarking" or "Secret Comm Channel" for agents operating in the latent space.

## Features

-   **Stego Encode (The Hider)**: Embeds a secret text string into an image.
-   **Stego Decode (The Revealer)**: Extracts the hidden text from an image.
-   **Encryption**: Optional key-based XOR encryption for an extra layer of security.
-   **No External Dependencies**: Uses pure Python and Pillow (which ComfyUI already uses).

## Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository (or just copy the folder):
    ```bash
    git clone https://github.com/yourusername/ComfyUI-Cyber-Steganography.git
    ```
3.  Restart ComfyUI.

## Usage

### Hiding a Secret (StegoEncode)
1.  Load an image or generate one.
2.  Connect the image to the **Stego Encode** node.
3.  Enter your secret message in the `text` widget.
4.  (Optional) Enter a `key` to encrypt the message.
5.  Connect the output image to a `Save Image` node or continue your workflow.

### Revealing a Secret (StegoDecode)
1.  Load an image that contains a secret message.
    *   *Note: Steganography is fragile. Resizing, compressing (JPEG), or altering the image will destroy the message. Use PNG format.*
2.  Connect the image to the **Stego Decode** node.
3.  (Optional) Enter the `key` if one was used during encoding.
4.  Connect the output `text` to a `ShowText` node or inspect the output.

## Technical Details

This node uses **Least Significant Bit (LSB)** steganography.
-   It modifies the last bit of the Red, Green, and Blue channels of the pixels to store data.
-   Data format: `[32-bit Length Header] + [Message Bits]`.
-   Encryption: Simple XOR cipher if a key is provided.

## Disclaimer

This tool is for educational and artistic purposes. It is not military-grade encryption. Do not use for critical security.
