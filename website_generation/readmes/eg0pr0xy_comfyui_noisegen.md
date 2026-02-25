# ComfyUI-NoiseGen

<img src="./docs/images/noisegen_logo_hq.png" alt="NoiseGen Logo" width="256" height="256" align="right" style="image-rendering: crisp-edges;"/>

Noise synthesis and audio processing for ComfyUI. 18 nodes across generation, processing, and analysis.

## Overview

ComfyUI-NoiseGen provides tools for experimental audio, harsh noise, and sound design within the ComfyUI environment. All nodes use standard ComfyUI audio format and integrate with existing extensions.

**Node Categories:**
- Generate (4 nodes): Noise sources and chaos systems
- Process (10 nodes): Filters, distortion, granular, effects
- Utility (5 nodes): Mixing, analysis, output

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/eg0pr0xy/comfyui_noisegen.git
pip install -r comfyui_noisegen/requirements.txt
```

## Node Reference

### Generate

**NoiseGenerator** - Seven noise types with configurable spectral characteristics. White, pink, brown, blue, violet, perlin, and band-limited generation.

**PerlinNoise** - Organic noise textures using Perlin noise algorithms. Multi-octave generation with persistence control.

**BandLimitedNoise** - Frequency-constrained noise generation with precise high/low cutoffs.

**TrueChaos** - Mathematical chaos systems: Lorenz, Chua, Rössler, Henon, Duffing attractors with 4th-order Runge-Kutta integration.

### Process

**FeedbackProcessor** - Delay-based feedback with filtering and modulation. Six modes: simple, filtered, saturated, modulated, complex, runaway.

**HarshFilter** - Extreme filtering with self-oscillation capabilities. Eight filter types including comb, morph, and chaos modes.

**MultiDistortion** - Twelve distortion algorithms with multi-stage processing. Tube, transistor, digital, bitcrush, waveshaper, foldback, ring mod, chaos.

**SpectralProcessor** - FFT-based frequency domain manipulation. Ten modes: enhance, suppress, shift, morph, gate, compress, chaos, phase, vocoder, freeze.

**GranularProcessor** - Granular synthesis engine with professional controls. Five grain envelopes, positioning modes, pitch manipulation, stereo spread.

**GranularSequencer** - Pattern-based granular control with step sequencing. Euclidean rhythms, probability gates, swing timing.

**MicrosoundSculptor** - Extreme granular manipulation for harsh noise and microsound art. Destruction modes with spectral processing.

**ModulationMatrix** - 8x8 parameter routing system. LFOs, envelope, audio follower, chaos, random, step sequencer sources.

**ConvolutionReverb** - Impulse response processing with eight reverb types. Hall, room, cathedral, plate, spring, chamber, ambient spaces.

### Utility

**AudioMixer** - Four-channel mixer with gain and pan controls. Professional mixing with master gain.

**ChaosNoiseMix** - Experimental mixing algorithms. Nine mix modes including XOR, modulo, ring mod, chaos operations.

**AudioSave** - Enhanced audio output with waveform visualization and metadata. WAV and FLAC export.

**AudioAnalyzer** - Comprehensive audio analysis with RMS, peak, spectral centroid, frequency band analysis.

**SpectrumAnalyzer** - Real-time FFT spectrum analysis with magnitude, power, log, mel, bark display modes.

## Usage

Basic harsh noise wall:
```
NoiseGenerator (white) → FeedbackProcessor (complex) → HarshFilter (comb) → MultiDistortion (destruction) → AudioSave
```

Granular processing:
```
[Audio Input] → GranularProcessor → MicrosoundSculptor → ConvolutionReverb → AudioSave
```

External audio processing:
```
VHS_LoadAudio → SpectralProcessor (chaos) → MultiDistortion → AudioAnalyzer → AudioSave
```

## Technical Notes

- All nodes process audio at sample-by-sample level for real-time feedback
- Compatible with ComfyUI audio format: `{'waveform': torch.tensor, 'sample_rate': int}`
- Safety limiting prevents system damage from extreme parameter settings
- FFT processing uses configurable window sizes (512-8192) and overlap factors
- Chaos systems use numerical integration with adaptive step sizing

## External Dependencies

Works with VideoHelperSuite (VHS_LoadAudio), ACE-Step sequencers, and other ComfyUI audio extensions. No format conversion required.

## License

MIT 

## Enter the Void

NoiseGen is a gateway to uncharted sonic territories. We invite you to:
- Explore the mathematics of chaos
- Fork the project and synthesize new realities
- Share your sonic experiments
- Dissolve the boundaries between signal and noise

Whether you're exploring granular clouds, generative drones, or pure frequency manipulation - your research can help expand our understanding of digital sound art.

> "Noise is the voice of technological consciousness." - Zbigniew Karkowski 