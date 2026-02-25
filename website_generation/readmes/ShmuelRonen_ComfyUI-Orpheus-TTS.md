# ComfyUI-Orpheus-TTS
This project adds high-quality Text-to-Speech capabilities to ComfyUI using the Orpheus TTS model. Create natural-sounding voices with emotional expressions, multilingual support, and audio effects.

![image](https://github.com/user-attachments/assets/3e167915-2ac3-4dbe-8b34-e65e6df2a94c)

## Features

- 🎙️ High-quality, natural-sounding speech synthesis
- 🎭 Support for emotional expressions and paralinguistic elements
- 👥 Multiple voice options (tara, leah, jess, leo, dan, mia, zac, zoe, etc.)
- 📝 Long text handling with automatic chunking for consistent output
- 🎛️ Professional audio effects:
  - Pitch shifting (-12 to +12 semitones)
  - Speed adjustment (0.5x to 2.0x speed)
  - Volume control with anti-clipping protection
  - Audio normalization option
  - Reverb with adjustable room size and amount
  - Echo with configurable delay and decay
- 🌐 Optional support for private Hugging Face models
- 💻 Cross-platform: Works on Windows, Linux/WSL, and macOS

## Installation

### 1. Install the Extension

Clone this repository into your ComfyUI's `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ShmuelRonen/ComfyUI-Orpheus-TTS.git
```

### 2. Install Required Python Dependencies

```bash
pip install torch numpy soundfile transformers huggingface_hub nltk snac
```

For WSL 2, you may need to install directly from the GitHub repository:
```bash
pip install git+https://github.com/hubertsiuzdak/snac.git
```

### 3. Install SoX (Required for Audio Effects)

#### Windows

1. Download SoX for Windows from the [official SourceForge page](https://sourceforge.net/projects/sox/files/sox/14.4.2/)
   - Download the `.exe` installer (e.g., `sox-14.4.2-win32.exe`)

2. Run the installer:
   - Follow the installation prompts
   - **Important**: Note the installation directory (default is usually `C:\Program Files (x86)\sox-14-4-2\`)
   
3. No need to add to PATH - the extension uses the direct path to SoX

#### WSL 2 (Ubuntu)

```bash
sudo apt-get update
sudo apt-get install sox
```

#### macOS

```bash
brew install sox
```

### 4. Restart ComfyUI

After installing all required components, restart ComfyUI to load the extension.

## Configuration

### Hugging Face Authentication (Optional)

To access private models on Hugging Face, create a file named `hf_config.json` in the extension directory and insert your HF Token KEY:

   ```json
   {
     "token": "YOUR_HUGGING_FACE_TOKEN_HERE"
   }
   ```

3. Save the file and restart ComfyUI

Your token will be used to authenticate with Hugging Face when downloading models. This is only required if you're using private models or if you need higher rate limits.

## Nodes

### Orpheus TTS Model Loader

Loads the required models for Orpheus TTS.

**Inputs:**
- `snac_model_path` (optional): Path to SNAC model (default: "hubertsiuzdak/snac_24khz")
- `orpheus_model_path` (optional): Path to Orpheus model (default: "canopylabs/orpheus-3b-0.1-ft")

**Outputs:**
- `model`: Model reference to be passed to the generate node

### Orpheus TTS Generate

Generates speech from text input.

**Inputs:**
- `model`: Model reference from the loader node
- `text`: The text to convert to speech
- `voice`: Voice style to use (tara, leah, jess, leo, dan, mia, zac, zoe, etc.)
- `language` (optional): Language for multilingual output (en, fr, es, etc.)
- `max_chunk_size` (optional): Maximum chunk size for long text processing

**Outputs:**
- `audio`: Audio data to be passed to preview or effects nodes

### Orpheus Audio Effects

Applies high-quality audio processing to the generated speech.

**Inputs:**
- `audio`: Audio data from the generate node
- `pitch_shift`: Semitone adjustment (-12 to +12)
- `speed_factor`: Playback speed modifier (0.5x to 2.0x)
- `sox_path` (optional): Custom path to SoX executable
- `gain_db` (optional): Volume adjustment in decibels
- `use_limiter` (optional): Enable/disable limiter for positive gain
- `normalize_audio` (optional): Enable/disable audio normalization
- `add_reverb` (optional): Enable/disable reverb effect
- `reverb_amount` (optional): Reverb intensity
- `reverb_room_scale` (optional): Size of virtual space
- `add_echo` (optional): Enable/disable echo effect
- `echo_delay` (optional): Time between echo repetitions
- `echo_decay` (optional): How quickly echo fades

**Outputs:**
- `audio`: Processed audio data

Looking at the README section you provided, I'll expand it to include information about the different element position options, including the new pipe feature:

## Paralinguistic Elements
You can add expressive elements to the speech by inserting these tags:
- **`<laugh>`** - Natural laughter
- **`<chuckle>`** - Light, subtle laughter
- **`<sigh>`** - Exhaling with emotion
- **`<cough>`** - Clearing throat
- **`<sniffle>`** - Subtle nasal sound
- **`<groan>`** - Low, grumbling sound
- **`<yawn>`** - Tired exhale
- **`<gasp>`** - Sudden intake of breath

### Element Position Options
The Element Position dropdown provides different ways to add these paralinguistic elements to your text:

1. **None** - No automatic element insertion. You can manually type the element tags in your text where desired.
   ```
   I can't believe it! <laugh> That's amazing!
   ```

2. **Append** - Automatically adds the selected element at the end of your text.
   ```
   Input: "That's amazing!"
   Output: "That's amazing! <laugh>"
   ```

3. **Prepend** - Automatically adds the selected element at the beginning of your text.
   ```
   Input: "I need to get back to work."
   Output: "<sigh> I need to get back to work."
   ```

4. **Pipe** - Replace pipe characters (|) in your text with the selected element. This gives you precise control over element placement.
   ```
   Input: "I can't believe it! | That's the funniest thing | I've heard all day."
   Element: laugh
   Output: "I can't believe it! <laugh> That's the funniest thing <laugh> I've heard all day."
   ```

### Examples:

#### Manual placement (Element Position: None):
```
I can't believe it! <laugh> That's the funniest thing I've heard all day.
<sigh> But now I need to get back to work.
```

#### Using pipe placeholders (Element Position: Pipe):
```
Input: "Did you hear that? | It's hilarious! | I can't stop laughing!"
Element: laugh
Result: "Did you hear that? <laugh> It's hilarious! <laugh> I can't stop laughing!"
```

#### Multiple elements in one text:
```
<gasp> What was that? <pause> Did you hear something? <sigh> Maybe I'm just tired.
```

## Audio Effect Tips

### Volume Control

- **Gain Control**: Use `gain_db` to increase or decrease volume without distortion
  - Positive values (0 to +20 dB): Increase volume with automatic clipping prevention
  - Negative values (-20 to 0 dB): Decrease volume
  - For best results with multiple effects, set gain last in your workflow

- **Normalization**: Enable `normalize_audio` to automatically balance levels
  - Great for ensuring consistent volume across different voice samples
  - Applied before other effects for best results

### Reverb

Reverb adds a sense of space to your audio. Here are some suggested settings:

- **Small Room**: reverb_amount = 20, reverb_room_scale = 25
- **Medium Room**: reverb_amount = 40, reverb_room_scale = 50
- **Large Hall**: reverb_amount = 70, reverb_room_scale = 80
- **Cathedral**: reverb_amount = 90, reverb_room_scale = 95

### Echo

Echo creates repeating sound reflections. Good settings to try:

- **Subtle Echo**: echo_delay = 0.3, echo_decay = 0.3
- **Moderate Echo**: echo_delay = 0.5, echo_decay = 0.5
- **Canyon Echo**: echo_delay = 1.0, echo_decay = 0.7

### Effect Combinations

- **Phone Call**: pitch_shift = 0, speed_factor = 1.0, add_reverb = True, reverb_amount = 10, reverb_room_scale = 10
- **Radio Announcer**: pitch_shift = -2, speed_factor = 0.9, add_reverb = True, reverb_amount = 20, gain_db = 3
- **Stadium Announcement**: pitch_shift = 0, speed_factor = 1.0, add_reverb = True, reverb_amount = 60, add_echo = True, echo_delay = 0.8
- **Child Voice**: pitch_shift = 4, speed_factor = 1.1, gain_db = 2
- **Deep Voice**: pitch_shift = -4, speed_factor = 0.9, gain_db = -2

## Usage Examples

### Basic Text-to-Speech

1. Add "Orpheus TTS Model Loader"
2. Add "Orpheus TTS Generate"
3. Connect the model loader's output to the generate node's input
4. Enter your text and select voice options
5. Connect to "Preview Audio" node to hear the result

### Advanced: TTS with Audio Effects

1. Add "Orpheus TTS Model Loader"
2. Add "Orpheus TTS Generate"
3. Add "Orpheus Audio Effects"
4. Connect in sequence: Model Loader → Generate → Audio Effects → Preview Audio
5. Adjust pitch shift and speed factor sliders

## Cross-Platform Compatibility

This extension has been tested and works on:

- Windows 10/11
- Linux (including WSL 2 on Windows)
- macOS

Different environments may require specific setup steps:

### Windows Notes
- SoX is automatically located in standard installation directories
- If installed elsewhere, provide the full path in the effects node

### WSL 2 Notes
- Use `pip install git+https://github.com/hubertsiuzdak/snac.git` to ensure compatibility
- SoX is automatically located through the system PATH

### macOS Notes
- Install SoX via Homebrew for best compatibility

## SoX Troubleshooting

### Windows

If you encounter issues with SoX:

1. Verify the SoX path in the "Orpheus Audio Effects" node:
   - Default: `C:\Program Files (x86)\sox-14-4-2\sox.exe`
   - If your installation is in a different location, provide the full path to sox.exe

2. Check if SoX is installed correctly:
   - Open Command Prompt
   - Run `"C:\Program Files (x86)\sox-14-4-2\sox.exe" --version`
   - If you get an error, reinstall SoX

### WSL 2 (Ubuntu)

1. Verify SoX installation:
   ```bash
   sox --version
   ```

2. If SoX is not found, install it:
   ```bash
   sudo apt-get update
   sudo apt-get install sox
   ```

## Model Details

This extension uses the following models:

- **Orpheus TTS**: A powerful text-to-speech model developed by Canopy AI
- **SNAC Codec**: A high-quality neural audio codec for voice synthesis

## License

This project uses models with their own licenses:
- Orpheus Model: [Canopy AI's Orpheus-TTS](https://github.com/canopyai/Orpheus-TTS)
- SNAC Model: [Hubert Siuzdak's model](https://huggingface.co/hubertsiuzdak/snac_24khz)

Please consult these licenses for usage terms and restrictions.

## Credits

- Original Orpheus TTS implementation by [Canopy AI](https://github.com/canopyai/Orpheus-TTS)
- SoX audio processing library: [SoX - Sound eXchange](http://sox.sourceforge.net/)
- ComfyUI: [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
