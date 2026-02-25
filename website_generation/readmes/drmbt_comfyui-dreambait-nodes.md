## comfyui-dreambait-nodes

A collection of forks, QoL nodes, and utilities for ComfyUI.

### Nodes Overview

#### Aspect Pad Image For Outpainting

A node to calculate arguments for the default ComfyUI node 'Pad Image For Outpainting' based on justifying and expanding to common SDXL and SD1.5 aspect ratios.

![](/examples/aspect_pad_for_outpainting.png)

#### Load Media

Loads media from various sources with advanced options for sequence handling.

- Supports images, directories, videos, archives (zip/tar/7z), and URLs.
- Smart sorting options including visual similarity-based ordering.
- Seamless loop creation with `loop_first_frame`.


#### Multi Min/Max

A node that finds the minimum or maximum value among multiple inputs. Forked from Impact Pack's MinMax node, extended to support up to 8 inputs. Accepts any comparable type and returns the min/max value of the same type.

#### String Item Menu

A context selector that extracts an item's index from a list of delimiter-separated strings.

#### TextPlusPlus

Combines text with optional prepend, append, and override operations.

#### NumberPlusPlus


A node to perform arithmetic operations on a number, including pre-addition, multiplication, and post-addition. It also provides formatted string outputs for the number, its integer representation, and a boolean indicating if the number is greater than 0.

#### NumberRemap

A node to remap a number from one range to another.

#### BoolPlusPlus

A node to handle boolean operations with additional features.

#### SwitchDuo

A node that switches between two outputs based on a boolean value. Supports overriding the boolean value with an optional input.

#### ListItemSelector

A node to select an item from a list based on a given index.

#### ImageFrameBlend

A node to blend frames of an image sequence.

#### Image Resize Face Aware

A fork of ComfyUI_essentials' Image Resize node with added face detection capabilities:
- All original resize methods (stretch, keep proportion, fill/crop, pad)
- New 'crop to face' method that detects faces, crops to them, and resizes
- New 'crop to face (keep_size)' method that produces a square crop centered on the largest detected face without resizing

Uses OpenCV's DNN face detector for reliable face detection, falling back to center crop if no face is found.

![](/examples/ImageResizeFaceAware.jpg)

#### Text Line Select

A node to select specific lines from a text input based on line numbers, with an optional random toggle.

#### Text Lines To List

Converts multi-line text input into a list, with each line as a separate item.

#### List Item Extract

Extracts a specific item from a list at the given index, with options for handling out-of-range indices.

#### MiniCPM-V

A node that provides access to OpenBMB's MiniCPM-V multimodal model for image and video analysis. Supports both the full model and a memory-efficient int4 version.

- Text analysis of images and videos
- Support for both full and int4 quantized models

Models:
- MiniCPM-V (Full): Best quality, higher VRAM usage
- MiniCPM-V-2_6-int4: 7GB VRAM usage, good quality/performance balance

Requires Hugging Face authentication (free) for model download.

#### MusicGen

A node that generates music using Meta's MusicGen model based on text prompts. This is a fork of 
comfyui-sound-lab's musicNode, modified to conform to ComfyUI's standard AUDIO format for better 
integration with the core audio workflow.

Features:
- Text-to-music generation using any MusicGen model:
  - Basic models:
    - small (300M parameters): Fastest, good for testing
    - medium (1.5B parameters): Balanced performance
    - large (3.3B parameters): Highest quality
  - Melody models:
    - melody: Base melody-conditioned generation
    - melody-large: High quality melody-conditioned generation
    - stereo-melody: Stereo melody-conditioned generation
  - Stereo models:
    - stereo-small: Basic stereo generation
    - stereo-medium: Better stereo quality
    - stereo-large: Best stereo quality

Inputs:
- Required:
  - model: Choose from available MusicGen models
  - prompt: Text description of the desired music
  - seconds: Duration of generated audio (1-1000 seconds)
  - guidance_scale: How closely to follow the text prompt (0-20)
  - seed: Random seed for reproducible results
  - device: CPU or auto (uses GPU if available)
- Optional:
  - audio: Input audio for melody-conditioned models (ignored by non-melody models)
  - melody_guidance_scale: Controls how closely melody models follow the input audio

The node outputs audio in the standard ComfyUI AUDIO format, compatible with audio preview and save nodes.

Models are stored in ComfyUI's models directory under 'musicgen/[model_name]' and are downloaded
automatically when first selected. You can also manually place model files in these directories
if you've downloaded them separately.

#### Draw Text

A comprehensive text rendering node that combines and enhances features from multiple ComfyUI text nodes.

Features:
- Proper text justification with word spacing and hyphenation
- Percentage-based positioning with pixel offsets
- Drop shadows with angle, distance, and blur
- Full RGBA color support with hex codes (#RRGGBBAA format)
- Text rotation with selectable pivot point
- Transparent backgrounds and alpha compositing
- Smart hyphenation in multiple languages
- Outputs both rendered image and text mask

Inputs:
- Required:
  - `image_width/height`: Output dimensions (ignored if img_composite provided)
  - `text`: Text to render (supports multiple lines)
  - `font_name`: TTF font file from fonts directory
  - `font_size`: Size in pixels
  - `font_color`: Predefined color or custom hex
  - `background_color`: Background color with transparency support
  - `x_percent/y_percent`: Position as percentage of dimensions
  - `x_offset/y_offset`: Additional pixel offsets
  - `vertical_align`: top/center/bottom
  - `horizontal_align`: left/center/right/justify
  - `shadow_distance/angle/blur`: Shadow parameters
  - `rotation_angle`: Text rotation in degrees
  - `language`: Language for hyphenation rules
- Optional:
  - `img_composite`: Background image to composite over
  - `*_color_hex`: Custom colors in #RRGGBBAA format

Outputs:
- `image`: Rendered text with background/shadow
- `mask`: Alpha mask of text and shadow

Originally forked from ComfyUI_Comfyroll_CustomNodes Draw Text node, with significant enhancements inspired by comfyui_essentials and ComfyUI-LayerStyle text rendering features.

#### Dynamic String Concatenate

A utility node that concatenates multiple string inputs using a configurable delimiter with dynamic input handling.

Features:
- Accepts an arbitrary number of string inputs through dynamic connection OR manual typing
- Smart delimiter parsing that handles escaped characters
- Configurable options for handling empty strings and whitespace
- Automatic conversion of non-string inputs to strings
- Dual output: both concatenated string and list of individual strings

Inputs:
- Optional:
  - `delimiter`: Character(s) to separate strings (default: `, `)
    - Use `\n` for newlines
    - Leave empty for newlines 
    - Supports any custom delimiter
  - `skip_empty`: Skip empty or whitespace-only strings (default: True)
  - `trim_whitespace`: Remove leading/trailing whitespace from inputs (default: True)
  - Dynamic string inputs: 
    - Connect any number of strings to concatenate (named STRING1, STRING2, etc.)
    - OR type directly into "string" input fields - new empty fields appear automatically

Outputs:
- `concatenated_string`: The combined result of all input strings with delimiter
- `list_string`: Array/list of individual string values (useful for further processing)

The node intelligently handles various input types by converting them to strings, and provides flexible formatting options for different use cases like creating lists, paragraphs, or custom-separated data. The dual output allows you to use the data as either a single concatenated string or as separate list items.

## Available Nodes

### Audio Processing

#### Normalize Audio
comfy Professional-grade audio normalization using broadcast standards (BS.1770-4) with true-peak limiting.

Inputs:
- `audio`: AUDIO format input
- `target_lufs`: Target integrated loudness (default: -14 LUFS for streaming)
- `true_peak_limit`: Maximum true-peak level (default: -1 dBTP)
- `normalize_type`: Choose between LUFS or peak normalization

Output:
- Normalized AUDIO

Example usage:
1. Connect your audio source to the NormalizeAudio node
2. Choose normalization type:
   - LUFS: For streaming/broadcast (measures perceived loudness)
   - Peak: For sample libraries or technical applications
3. Set target levels:
   - Streaming: -14 LUFS, -1 dBTP
   - Broadcast: -23 LUFS, -2 dBTP
   - Sample Library: Peak mode, -0.3 dBTP
4. Connect to output nodes

Technical Details:
- Uses BS.1770-4 standard for loudness measurement
- True-peak limiting prevents inter-sample peaks
- LUFS measurement considers perceived loudness
- Handles silence and very quiet audio gracefully

## Compare Image Similarity Node

The Compare Image Similarity node allows you to find the most similar image to an input image from a folder of images. It uses feature extraction and similarity metrics to match images.

Key features:
- Supports cosine similarity and euclidean distance metrics
- Can return multiple similar images ranked by similarity
- Implements efficient caching for faster performance
- Returns images at their original resolution by default

### Parameters

- **input_image**: The image to compare against
- **folder_path**: Path to folder containing images to search through
- **similarity_method**: Method to calculate similarity (cosine or euclidean)
- **resize_images**: Controls output image dimensions:
  - `False` (default): Return images at their original resolution
  - `True`: Resize images to match input image dimensions
- **return_best_n**: Number of most similar images to return
- **use_cache**: Use cached embeddings for faster processing
- **force_refresh_cache**: Force recalculation of embeddings
- **debug_mode**: Enable detailed debug logging

### Returns

- **image**: The most similar image(s) found
- **mask**: Corresponding mask(s)
- **FILE_PATH**: Path to the similar image file
- **FILE_NAME**: Filename of the similar image
- **SIMILARITY_SCORE**: Similarity score (higher is more similar)

### How It Works

The node extracts standardized features from all images (including the input image) to perform accurate similarity comparison, but it preserves the original resolution of found images when returning results. This allows you to find visually similar images while maintaining their original quality.
