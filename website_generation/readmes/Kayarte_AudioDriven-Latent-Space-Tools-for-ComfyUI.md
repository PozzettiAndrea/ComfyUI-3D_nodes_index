# AudioDriven Latent Space Tools for ComfyUI

Generate dynamic latent noise patterns driven by audio analysis.

### Nodes

### Librosa Audio Analysis
Analyzes audio files using various methods:
- Onset detection (note starts)
- Spectral content
- Beat tracking
- Tempo analysis
- MEL spectrograms

### Audio To Noise Parameters
Converts audio analysis into noise parameters:
- Intensity based on audio energy
- Grain size from spectral features
- Persistence from temporal changes

### Audio Noise to Latent
Converts noise parameters to latent space noise using:
- Gaussian noise
- Salt & pepper noise
- Perlin noise

### Advanced Audio Noise Patterns
Creates musical visualization-style patterns:
- Simplex noise
- Cellular patterns
- Fractal Brownian Motion (FBM)
- Wave patterns
- Domain warping

## Usage

1. Input audio file through Librosa Analysis
2. Choose analysis type (onset/tempo/mel/etc.)
3. Convert to noise parameters
4. Generate latent noise
5. Connect to ksampler
6. Use with low denoising (<0.5) for audio-visual blending

WARNING: Advanced Audio Noise Patterns Node
    
    Typical image counts: Average measurements by analysis type (from 3s, 11.65s, and 89s samples)

    Default: huge (~122K for 89s)
    
    Mel/spectral/tempo: high (~7.6K for 89s)

    Onset: moderate (60-500 depending on complexity) 

    Beat: low (14-168 based on tempo) 

    Second: consistent (~length in seconds) 

    Half_second: consistent (~2x seconds) 

        
Installation

Download or clone this repository to your ComfyUI\custom_nodes folder


This node is part of a ongoing solo project to integrate music analysis. plz enjoy.

![m2ng-ezgif com-optimize](https://github.com/user-attachments/assets/4fd765ef-3d75-48b5-b9e7-ec37bd6052ad)

![image](https://github.com/user-attachments/assets/b5080a53-398b-48c2-bdac-4e8e6890e1f5)



