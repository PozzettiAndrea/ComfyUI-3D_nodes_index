# Network Bending for ComfyUI

A custom node pack for ComfyUI that enables the creative manipulation of generative models. Allows you to corrupt, modify, and blend neural networks.

## Features

- **Add Noise**: Inject Gaussian noise into model weights
- **Scale Weights**: Scale model weights up or down to amplify or dampen features
- **Prune Weights**: Remove small weights for sparsification
- **Randomize Weights**: Replace portions of weights with random values
- **Smooth Weights**: Apply spatial smoothing to weight matrices
- **Quantize Weights**: Reduce weight precision to discrete levels
- **Layer Swap**: Swap weights between similar layers
- **Activation Replace**: Replace activation functions
- **Weight Transpose**: Transpose weight matrices
- **Channel Shuffle**: Randomly shuffle channels in convolutional layers
- **Frequency Filter**: Apply frequency domain filtering
- **Weight Clustering**: Group similar weights together

Mix two models together with various blending modes:
- **Linear Interpolation**: Simple weighted average of weights
- **Weighted Sum**: Weighted sum with normalization
- **Layer-wise Mix**: Different mix ratios for different layers
- **Frequency Blend**: Mix models in frequency domain
- **Random Mix**: Randomly select weights from either model

### Audio Processing Nodes

The package also includes comprehensive audio processing capabilities for Stable Audio models:

#### Audio VAE Nodes
- **Audio VAE Encode**: Encode audio waveforms into latent space
- **Audio VAE Decode**: Decode latent representations back to audio

#### Audio Latent Manipulation
- **Audio Latent Interpolate**: Smoothly interpolate between audio latents
- **Audio Latent Blend**: Blend multiple audio latents with various modes
- **Audio Latent Manipulator**: Direct manipulation of audio latent features
- **Audio Feature Extractor**: Extract specific features from audio latents

#### Audio Style Transfer
- **Audio Style Transfer**: Transfer style from one audio to another
- **Audio Latent Guidance**: Guide generation with reference audio
- **Audio Reference Encoder**: Encode reference audio for style transfer

## Installation

### Basic Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DavidPiazza/network_bending.git
```

2. Restart ComfyUI

### Audio Network Bending

1. **Load an audio model** (e.g., Stable Audio VAE)
2. **Add audio processing nodes** from the network_bending/audio category
3. **Connect audio inputs** either from file loaders or generated audio
4. **Apply bending operations** to the audio latents
5. **Decode back to audio** using Audio VAE Decode

#### Cross-Modal Bending
Apply image model bending techniques to audio models or vice versa for experimental results.

## License

This project is licensed under the GNU General Public License v3 (GPL-3.0) - see the LICENSE file for details.

## 
