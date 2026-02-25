# ComfyUI-AudioBridge

Bridges ComfyUI's native **AUDIO** type to raw audio tensors (**VCAUDIOTENSOR**) used by nodes like [MuseTalk-KJ](https://github.com/kijai/ComfyUI-MuseTalk-KJ) and VoiceCraft.

## Nodes

| Node               | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| **Audio → Tensor** | Converts `AUDIO` → `VCAUDIOTENSOR` (mono, resampled to target rate)       |
| **Tensor → Audio** | Converts `VCAUDIOTENSOR` → `AUDIO` (wraps tensor back for standard nodes) |

## Why?

ComfyUI's native `AUDIO` type is a dict (`{waveform, sample_rate}`), but some custom nodes expect `VHS_AUDIO` (a callable) or `VCAUDIOTENSOR` (a raw torch tensor). This node bridges the gap without requiring VideoHelperSuite or duplicate audio loading.

## Install

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/RyanHolanda/ComfyUI-AudioBridge.git
```

No additional dependencies required — uses PyTorch and torchaudio (already included with ComfyUI).

## Usage Example

```
LoadAudio → [Audio → Tensor] → whisper_to_features → MuseTalk Sampler
```
