# CRT-HeartMuLa

A ComfyUI custom node for AI music generation using HeartMuLa models.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/7e8ba1ab-642b-4def-98be-4a6da30ae9ca" width="100%" /></td>
    <td><img src="https://github.com/user-attachments/assets/158d6860-b042-4794-bc20-7a855e69fbb4" width="100%" /></td>
  </tr>
</table>

https://www.youtube.com/watch?v=WZyfdSB2GV4


## Features

- Generate music from lyrics and style tags
- Custom UI with integrated audio player and waveform visualization
- Real-time audio metrics (Peak, RMS, LUFS)
- Multiple model versions and precision options
- Auto-download and model caching
- Persistent output saving

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/CRT-HeartMuLa.git
```

2. Install dependencies:
```bash
cd CRT-HeartMuLa
pip install -r requirements.txt
```

3. Restart ComfyUI

## Usage

1. Add the "HeartMuLa" node to your workflow
2. Configure your lyrics and tags in the Generation tab
3. Adjust generation parameters in the Settings tab
4. Click "Generate Music" to create audio
5. Use the built-in player to preview your generation

## Credits

This node is based on [HeartMuLa's HeartLib](https://github.com/HeartMuLa/heartlib) - the official library for HeartMuLa music generation models.

## License

Please refer to the original HeartMuLa project for licensing information.
