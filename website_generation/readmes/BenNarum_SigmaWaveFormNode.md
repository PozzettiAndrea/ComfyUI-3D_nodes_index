# SigmaWaveFormNodes
A set of tools for generating and altering sigmas in ComfyUI.


![Example](https://github.com/BenNarum/SigmaWaveFormNodes/blob/main/Screenshot_2024-06-10_024654.png?raw=true)
Nodes Description

SigmaWaveFormNode
The SigmaWaveFormNode generates a variety of waveforms with adjustable parameters such as 
amplitude, 
frequency, 
damping factor, 
and waveform type. 

It supports multiple waveform types, 
including sine, 
sawtooth, 
stepped, 
square, 
random, 
triangle, 
and rectangular waves. 

The node also allows for optional Fourier transformation and uni-directional output.

Parameters:

steps: Number of steps in the waveform.
amplitude: Amplitude of the waveform.
frequency: Frequency of the waveform.
damping_factor: Damping factor applied to the waveform.
waveform_type: Type of waveform (sine, sawtooth, stepped, square, random, triangle, rectangular).
enable_damping: Boolean to toggle damping.
min_sigma: Minimum sigma value for the waveform.
apply_fourier: Boolean to toggle Fourier transformation.
horizontal_length: Proportion of each horizontal segment length in the stepped waveform.
enable_unidirectional: Boolean to toggle uni-directional transformation.


SigmaWaveFormNodeAdvanced
The SigmaWaveFormNodeAdvanced extends the functionality of the standard waveform generator by supporting the blending of two different waveforms. 
It provides additional parameters for the second waveform and a blend factor to control the mixture of the two waveforms.

Parameters:

steps: Number of steps in the waveform.
amplitude1: Amplitude of the first waveform.
frequency1: Frequency of the first waveform.
waveform_type1: Type of the first waveform.
amplitude2: Amplitude of the second waveform.
frequency2: Frequency of the second waveform.
waveform_type2: Type of the second waveform.
blend_factor: Factor to blend the two waveforms.
damping_factor: Damping factor applied to the waveform.
enable_damping: Boolean to toggle damping.
min_sigma: Minimum sigma value for the waveform.
apply_fourier: Boolean to toggle Fourier transformation.
horizontal_length: Proportion of each horizontal segment length in the stepped waveform.
enable_unidirectional: Boolean to toggle uni-directional transformation.


FourierFilterNode
The FourierFilterNode processes an input sigma sequence using a Fourier transform, applies a frequency filter, 
and optionally performs an inverse Fourier transform. 
It supports various filter types, including lowpass, highpass, bandpass, and bandstop.

Parameters:

sigmas: Input sigma sequence.
filter_type: Type of frequency filter to apply 
(lowpass, highpass, bandpass, bandstop).
cutoff_frequency: Cutoff frequency for the filter.
apply_inverse_fourier: Boolean to toggle inverse Fourier transform.


AttenuatorNode
The AttenuatorNode adjusts the amplitude of a sigma sequence by applying an attenuation factor. 
This node is useful for fine-tuning the output of waveform generators or after applying a Fourier filter.

Parameters:
sigmas: Input sigma sequence.
attenuation_factor: Factor by which to attenuate the sigma sequence.

PhaseLockedLoopNode
The PhaseLockedLoopNode locks the phase of an input sigma sequence to a reference sigma sequence. 
This node is useful for synchronization tasks where the phase of an output signal needs to match a reference signal.

Parameters:

input_sigmas: Input sigma sequence.
reference_sigmas: Reference sigma sequence to lock the phase to.
lock_factor: Factor by which to lock the phase.
frequency_range: Frequency range for the phase-locked loop.
