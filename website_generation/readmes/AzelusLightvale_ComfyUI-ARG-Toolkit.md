# ComfyUI ARG Toolkit

A collection of ComfyUI nodes meant mostly for doing cryptography, steganography, encryption, decryption, and everything needed to both make and solve ARGs (Alternative Reality Games) and secret messages hidden within text or images (and hopefully audio) without ever leaving ComfyUI.

Might also double as a poor-man's cryptanalysis and steganography lab

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager).
1. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

# Features

- Classic ciphers and cryptography techniques (Caesar, Playfair, Vigénere, Foursquare,...) - powered by [`secretpy`](https://github.com/tigertv/secretpy).
- Image steganography and invisible watermarking tools - powered by [`stegano`](https://github.com/cedricbonhomme/Stegano) and [`invisible-watermark`](https://github.com/ShieldMnt/invisible-watermark/).
- Bitwise operators and string converters for use with other ciphers.
- Multi-language Morse code encoder and decoder.
- (WIP) Modern cryptographic encryption tools and functions - powered by [`cryptography`](https://github.com/pyca/cryptography).
- (Planned) Historical encoding and encrypting formats (Kansas City System, SNOW, SSTV,...) made user-friendly and available through a node interface.
- (Planned) Recreations of historical cipher machines (Enigma, Lorenz, M-209,...) within ComfyUI.
- (Planned) Audio spectrogram analysis tools.
- (Planned) Generative steganography models
- (Far Future plans) Post-quantum cryptography tools.

# Testing methodology

Since this project started as an amateur project, the test files only cover the functions and most common use cases, not the edge cases or any automated testing yet.

# Others

## Related projects

If you like the idea behind this node pack, want to explore cryptography, steganography, ARGs, and more, please visit these projects and sites:

- [Ciphereditor](https://github.com/wierkstudio/ciphereditor) - Basically what this is doing, but more formalized and not a custom node pack sitting on top of an AI image generation platform.
- [CyberChef](https://github.com/gchq/CyberChef) - The Cyber Swiss Army Knife, and for a good reason.
- [cryptii](https://github.com/Cryptii/Cryptii) [(Official link)](https://cryptii.com/) - One of the more modern cryptography encrypt/decrypt sites out there.
- [CrypTool](https://www.cryptool.org/en/) - A good place to learn more about everything cryptography. [CrypTool2](https://www.cryptool.org/en/ct2/) is probably one of the accidental inspiration for this project as well.
- [dCode.fr](https://www.dcode.fr/en) - The original and most well known site for all things related to solving math, cryptography, and ARGs as they basically contain the most amount of tools out there.
- [Game Detectives](https://gamedetectives.net/) - A quite useful site to learn about how ARGs work and get standalone tools for learning and solving ARGs. Unfortunately, many of the tools listed on the [ARG Toolbox](https://wiki.gamedetectives.net/index.php?title=ARG_Toolbox) are dead and either requires the Wayback Machine or finding a sketchy alternative.

## Companion node packs

- [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts) - Provides a lot of useful features and nodes in general for ComfyUI.
- [ComfyUI-Crystools](https://github.com/crystian/ComfyUI-Crystools) - System monitor extension for ComfyUI.
- [ComfyUI_Invisible_Watermark](https://github.com/web3nomad/ComfyUI_Invisible_Watermark) - The main reason I even started this project in the first place, for making an "invisible watermark" node that left such an impression on me I decided to make my own.
- [ComfyLiterals](https://github.com/M1kep/ComfyLiterals) - Optional custom nodes for use with these nodes to provide or bypass certain limitations of ComfyUI.

# License

    This project is licensed under the GNU General Public License 3.0 (GPLv3)
    See the LICENSE file for full license details.
    See the ATTRIBUTIONS file for notices regarding third-party software used.
    
Moreover, this project uses additional libraries and projects as both reference and implementations. Additional attributions and citations are listed in the ATTRIBUTIONS file.
