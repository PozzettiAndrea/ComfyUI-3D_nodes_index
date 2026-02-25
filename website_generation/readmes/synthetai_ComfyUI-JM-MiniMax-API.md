# ComfyUI-JM-MiniMax-API

A collection of ComfyUI custom nodes that integrate with MiniMax API services.

[中文文档](README_CN.md)

## Features

### Speech Nodes (JM-MiniMax-API/Speech)

- **Text to Speech**: Convert text to natural-sounding speech using MiniMax's advanced text-to-speech API
- **Voice Cloning**: Clone voices from audio samples
- **Voice Design**: Generate custom voices from text descriptions using AI-powered voice design
- **Load Audio**: Load and preview audio files for voice cloning

### Video Nodes (JM-MiniMax-API/Video)

- **Video Generation**: Generate videos using MiniMax's unified video generation API (supports text-to-video, image-to-video, and subject-referenced video)
- **Check Video Status**: Check the status of video generation tasks
- **Download Video**: Download generated videos to local storage

## Installation

1. Clone this repository to your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-JM-MiniMax-API.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Restart ComfyUI

## Usage

### Load Audio Node

This node allows you to load and preview audio files for voice cloning.

#### Input Parameters:
- **audio_path**: Select an existing audio file from the input directory
- **Upload Button**: Click to upload a new audio file (supports .mp3, .wav, .m4a)

#### Output:
- **audio_file**: Absolute path to the selected audio file

### Voice Cloning Node

This node uses MiniMax's voice cloning API to clone voices from audio samples.

#### Input Parameters:
- **api_key**: MiniMax API key
- **group_id**: MiniMax group ID
- **audio_file**: Path to the audio file to clone (connect from Load Audio node)
- **voice_id**: ID for the cloned voice (at least 8 characters, start with a letter, include numbers)
- **need_noise_reduction**: Whether to apply noise reduction (true/false)
- **need_volume_normalization**: Whether to normalize volume (true/false)
- **preview_text**: Optional text to preview the cloned voice (max 300 characters)
- **model**: TTS model to use for preview
- **accuracy**: Cloning accuracy threshold (0.0-1.0)

#### Output:
- **voice_id**: ID of the cloned voice (can be connected to TextToSpeech node)

### Voice Design Node

This node uses MiniMax's voice design API to generate custom voices from text descriptions. Simply describe the voice characteristics you want, and the AI will create a unique voice for you.

#### Input Parameters:
- **api_key**: MiniMax API key
- **prompt**: Detailed description of the desired voice characteristics
  - Example: "讲述悬疑故事的播音员，声音低沉富有磁性，语速时快时慢，营造紧张神秘的氛围。"
  - Include: gender, age, emotion, speaking style, tone, usage scenario, etc.
- **preview_text**: Optional text for voice preview (max 200 characters)
  - Example: "夜深了，古屋里只有他一人。窗外传来若有若无的脚步声..."
- **custom_voice_id** (optional): Custom voice ID for the generated voice
  - If empty, a unique voice ID will be automatically generated
  - Format: Can be any string identifier you prefer

#### Output:
- **voice_id**: Generated or custom voice ID (can be used in Text to Speech node)
- **trial_audio**: Path to preview audio file (if generated)

#### Voice ID Generation:
- **Custom ID**: If you provide a custom_voice_id, it will be used as-is
- **Auto-generated**: If left empty, format will be `voice_{timestamp}_{unique_id}`
- **Example auto-generated**: `voice_1704067200_a1b2c3d4`

#### Usage Tips:
1. **Be Specific**: Describe gender, age, emotion, speaking style in detail
2. **Include Context**: Mention the usage scenario (narrator, customer service, etc.)
3. **Voice Characteristics**: Specify tone (deep, bright), pace (fast, slow), style (formal, casual)
4. **Preview**: Use preview_text to test the generated voice
5. **Custom ID**: Use meaningful custom_voice_id for easier management

#### Example Prompts:
- "专业新闻主播，女性，30岁左右，声音清晰标准，语调平稳，适合播报新闻"
- "儿童故事讲述者，温和亲切的女声，语速适中，充满关爱和耐心"
- "商务客服代表，男性，声音稳重专业，语调友好，适合电话客服"

### Text to Speech Node

This node uses MiniMax's API to convert text to speech.

#### Input Parameters:
- **api_key**: MiniMax API key
- **group_id**: MiniMax group ID
- **text**: Text to convert (up to 5000 characters)
- **model**: TTS model selection (speech-02-hd, speech-02-turbo, etc.)
- **voice_id**: Voice selection (multiple options available)
- **custom_voice_id** (optional): Custom voice ID from voice cloning (overrides voice_id if provided)
- **speed**: Speech rate (0.5 to 2.0)
- **volume**: Volume (0.1 to 10.0)
- **pitch**: Pitch adjustment (-12 to 12)
- **emotion**: Emotion selection (happy, sad, etc.)
- **subtitle_enable**: Whether to generate subtitle file (true/false)
- **filename_prefix**: Prefix for output filenames
- **language_boost** (optional): Language enhancement

#### Output:
- **audio_path**: Absolute path to the generated audio file
- **subtitle_path**: Absolute path to the generated subtitle file (if subtitles enabled)

#### Output File Details:
1. Audio File (audio_path):
   - Format: MP3
   - Filename format: prefix_YYYYMMDD-HHMMSS.mp3
   
2. Subtitle File (subtitle_path):
   - Format: JSON
   - Filename format: prefix_subtitle_YYYYMMDD-HHMMSS.json
   - Contains sentence-level timestamps accurate to milliseconds

## Workflow Examples

### Basic Text-to-Speech Workflow:
1. Use **Text to Speech** node with a predefined voice
2. Enter your API key, text, and configure voice parameters
3. Run to generate speech audio

### Voice Cloning Workflow:
1. Use **Load Audio** node to upload or select an audio file
2. Connect the output to a **Voice Cloning** node to clone the voice
3. Connect the voice_id output to a **Text to Speech** node's custom_voice_id input
4. Enter text and configure other parameters in the Text to Speech node
5. Run the workflow to generate speech using the cloned voice

### Voice Design Workflow:
1. Use **Voice Design** node to create a custom voice from description
2. Write a detailed prompt describing the voice characteristics you want
3. Optionally add preview text to test the voice
4. Run to get a custom voice_id and preview audio
5. Connect the voice_id to a **Text to Speech** node to use the custom voice

### Video Generation Node

This node uses MiniMax's unified video generation API to create videos from text prompts, images, or subject references.

#### Input Parameters:
- **api_key**: MiniMax API key
- **model**: Video generation model selection:
  - **T2V-01-Director**, **T2V-01**: Text-to-video models (require text prompt)
  - **I2V-01-Director**, **I2V-01**, **I2V-01-live**: Image-to-video models (require image input)
  - **S2V-01**: Subject-referenced video model
- **prompt**: Video generation description (max 2000 characters, supports camera movement instructions)
- **prompt_optimizer**: Whether to auto-optimize prompt for better quality (true/false)
- **image** (optional): Image input for I2V models (required for I2V-01-Director, I2V-01, I2V-01-live)
- **callback_url** (optional): URL for status update callbacks

#### Model Usage Guidelines:
- **Text-to-Video (T2V models)**: Only requires a text prompt. Image input is optional.
- **Image-to-Video (I2V models)**: Requires both image input and optionally a text prompt. If prompt is empty, the model will auto-generate video content based on the image.
- **Subject-Referenced (S2V models)**: Currently S2V-01 model for subject-referenced video generation.

#### Camera Movement Instructions:
When using T2V-01-Director or I2V-01-Director models, you can use movement instructions in the prompt:
- Movement: [左移], [右移], [推进], [拉远], [上升], [下降]
- Rotation: [左摇], [右摇], [上摇], [下摇]
- Zoom: [变焦推近], [变焦拉远]
- Other: [晃动], [跟随], [固定]

#### Image Requirements (for I2V models):
- Format: JPG/JPEG/PNG
- Aspect ratio: between 2:5 and 5:2
- Short side: minimum 300px
- File size: maximum 20MB

#### Output:
- **task_id**: Task ID for the video generation job

## Video Workflow Examples

### Text-to-Video Workflow:
1. Use **Video Generation** node with T2V-01-Director or T2V-01 model
2. Enter your API key and write a detailed text prompt
3. Run to get a task_id
4. Use **Check Video Status** node to monitor progress
5. Once status is "success", use **Download Video** node to save the video

### Image-to-Video Workflow:
1. Load an image into ComfyUI (using Load Image node)
2. Connect it to the **Video Generation** node
3. Select an I2V model (I2V-01-Director recommended)
4. Enter API key and optionally write a prompt with movement instructions
5. Run to get a task_id
6. Use **Check Video Status** node to monitor progress (it will automatically wait until completion)
7. Once status is "success", use **Download Video** node with the file_id to save the video

## License

MIT License

### Check Video Status Node

This node checks the status of video generation tasks and waits until completion.

#### Input Parameters:
- **api_key**: MiniMax API key
- **task_id**: Task ID from Video Generation node
- **check_interval**: Check interval in seconds (default: 30, range: 10-300)
- **max_wait_time**: Maximum wait time in seconds (default: 1800/30 minutes, range: 5 minutes-2 hours)

#### Output:
- **status**: Task status (processing, success, failed)
- **file_id**: File ID of the generated video (required for downloading)
- **video_url**: Download URL for the generated video (may be empty)
- **cover_image_url**: URL for the video cover image

#### Features:
- **Automatic polling**: Continuously checks status until completion or failure
- **Progress tracking**: Shows elapsed time, remaining time, and attempt count
- **Timeout protection**: Prevents infinite waiting with configurable maximum wait time
- **Smart intervals**: Customizable check intervals to balance responsiveness and API usage

### Download Video Node

This node downloads generated videos using the file_id from the status check.

#### Input Parameters:
- **api_key**: MiniMax API key
- **file_id**: File ID from Check Video Status node
- **filename_prefix**: Prefix for the downloaded video file

#### Output:
- **video_path**: Absolute path to the downloaded video file

#### Process:
1. Uses file_id to retrieve download URL from MiniMax file API
2. Downloads the video file with progress tracking
3. Saves to ComfyUI output directory with timestamp
