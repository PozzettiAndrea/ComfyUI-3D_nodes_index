# ComfyUI-QwenFrameSelector

Intelligent video frame selection node powered by Qwen3-VL-235B vision model. Automatically analyzes and selects the best quality frames from videos for further creative work.

## Overview

This node uses AI vision analysis to evaluate frames (from video or images) across multiple quality dimensions and intelligently selects the best frames based on your criteria. Perfect for extracting high-quality keyframes for image generation, video editing, or content creation workflows.

**New in v1.1**: Now supports both VIDEO and IMAGE inputs! Use it to analyze and filter existing image sets or extract frames from videos.

## Features

- **Dual Input Modes**: 
  - VIDEO input: Extract and analyze frames from videos
  - IMAGE input: Analyze and filter existing image batches
- **AI-Powered Frame Analysis**: Uses Qwen3-VL-235B to evaluate frame quality
- **Multi-Dimensional Scoring**: 
  - Sharpness (focus quality, motion blur)
  - Composition (rule of thirds, balance, framing)
  - Aesthetic (color harmony, lighting, artistic value)
  - Technical (exposure, contrast, color accuracy)
  - Content (information richness, key moments)
- **Multiple Selection Strategies**:
  - Quality Focused: Prioritize technical perfection
  - Aesthetic Focused: Emphasize beauty and composition
  - Balanced: Equal weight on all criteria
  - Content Diversity: Maximize scene variety
  - Keyframe Detection: Find significant moments
- **Flexible Filtering**: Control by percentage, minimum score, or max count
- **Compatible Inputs**: Works with Load Video, Load Image, image generators, and more
- **Detailed Scoring Reports**: JSON output with per-frame analysis

## Installation

### Method 1: ComfyUI Manager

1. Open ComfyUI Manager
2. Search for "QwenFrameSelector"
3. Click Install

### Method 2: Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/eddyhhlure1Eddy/ComfyUI-QwenFrameSelector.git
cd ComfyUI-QwenFrameSelector
pip install -r requirements.txt
```

### Requirements

- ComfyUI
- Python 3.8+
- FFmpeg (must be in PATH)
- OpenRouter API key

## API Key Setup

Get your OpenRouter API key:
1. Visit [OpenRouter](https://openrouter.ai/)
2. Create account and generate API key
3. Paste key into node's `api_key` field

## Usage

### Basic Workflows

**Video Mode:**
```
Load Video → Qwen Frame Selector → Preview Selected Frames
                                 → Save Images
                                 → Further Processing
```

**Image Mode:**
```
Load Image Batch → Qwen Frame Selector → Selected Best Images
                                       → Save/Process
```

### Node Parameters

**Required Inputs:**
- `api_key` (STRING): Your OpenRouter API key
- `sample_rate` (INT): Extract 1 frame every N frames (default: 30, for video mode)
- `selection_criteria` (COMBO): Analysis strategy
  - `quality_focused`: Best technical quality
  - `aesthetic_focused`: Most beautiful frames
  - `balanced`: Best overall frames
  - `content_diversity`: Maximum variety
  - `keyframe_detection`: Significant moments
- `top_percent` (FLOAT): Keep top X% of frames (default: 30%)
- `min_score` (FLOAT): Minimum quality score 0-10 (default: 6.0)

**Optional Inputs:**
- `video` (VIDEO): Input video for frame extraction (Video Mode)
- `images` (IMAGE): Input image batch for analysis (Image Mode)
- `max_frames` (INT): Maximum frames to select (0 = unlimited)

**Note**: You must provide either `video` OR `images` input, not both.

**Outputs:**
- `selected_frames` (IMAGE): Tensor of selected frames
- `scores_json` (STRING): Detailed JSON scoring data
- `summary` (STRING): Selection summary report

### Example Use Cases

#### 1. Extract Best Shots from Video (Video Mode)

```
Load Video (sample_rate: 60, balanced)
→ Qwen Frame Selector (top 10%, min_score: 7.5)
→ Preview or Save high-quality keyframes
→ Use as reference for image generation
```

#### 2. Filter AI-Generated Image Batch (Image Mode)

```
Batch Image Generator [100 images]
→ Qwen Frame Selector (images input, aesthetic_focused, top 20%)
→ Keep only the most beautiful 20 images
→ Save or further process
```

#### 3. Quality Control for Image Sets (Image Mode)

```
Load Image Folder [200 photos]
→ Qwen Frame Selector (images input, quality_focused, min_score: 8.0)
→ Filter out blurry/poorly exposed images
→ Output only high-quality images
```

#### 4. Create Aesthetic Photo Gallery from Video

```
Load Video (sample_rate: 30, aesthetic_focused)
→ Qwen Frame Selector (top 20%, min_score: 8.0)
→ Save selected frames as gallery
```

#### 5. Scene Change Detection (Video Mode)

```
Load Video (sample_rate: 10, keyframe_detection)
→ Qwen Frame Selector (top 40%, min_score: 6.0)
→ Extract scene transitions and key moments
```

#### 6. Curate Best Images from Multiple Sources (Image Mode)

```
Multiple Image Sources → Merge Images (e.g., 50 images)
→ Qwen Frame Selector (images input, balanced, top 30%)
→ Select best 15 images across all sources
```

## How It Works

### Input Processing

**Video Mode:**
1. Accepts VIDEO input from Load Video or similar nodes
2. Uses FFmpeg to extract frames at specified sample rate
3. Stores extracted frames temporarily for analysis

**Image Mode:**
1. Accepts IMAGE tensor from any image source
2. Converts tensor to temporary JPEG files
3. All input images are analyzed (sample_rate is ignored)

### AI Evaluation
For each frame, Qwen VL analyzes:
- **Sharpness**: Focus quality, clarity, motion blur detection
- **Composition**: Visual balance, rule of thirds, framing
- **Aesthetic**: Color harmony, lighting quality, artistic merit
- **Technical**: Exposure accuracy, contrast, color grading, noise
- **Content**: Information density, expression quality, action capture

Each dimension scored 0-10, with weighted overall score based on selected criteria.

### Selection Process
1. Filters frames below minimum score threshold
2. Ranks by overall score (weighted by criteria)
3. Selects top N% or max count
4. Returns frames in chronological order

### Output Format

**Selected Frames**: ComfyUI IMAGE tensor ready for:
- Preview Image node
- Save Image node
- Image-to-Image generation
- Video reconstruction
- Any image processing node

**Scores JSON**: Detailed per-frame data:
```json
[
  {
    "frame_index": 15,
    "sharpness": 8.5,
    "composition": 9.0,
    "aesthetic": 8.0,
    "technical": 8.5,
    "content": 7.5,
    "overall": 8.3,
    "reason": "Sharp focus, excellent rule-of-thirds composition..."
  },
  ...
]
```

## Performance Tips

- **Sample Rate**: Higher values (60-120) for long videos, lower (10-30) for short clips
- **Batch Processing**: Process multiple short segments rather than one long video
- **Score Threshold**: Start with 6.0, adjust based on results
- **Top Percent**: 20-40% for general use, 5-10% for best-of-best
- **API Limits**: ~2-4 seconds per frame analysis

## Troubleshooting

### FFmpeg Errors
**Problem**: Frame extraction fails

**Solution**: Ensure FFmpeg is installed and in PATH
```bash
ffmpeg -version
```

### API Errors
**Problem**: Frame evaluation fails or returns default scores

**Solution**: 
- Verify OpenRouter API key is valid
- Check API credit balance
- Ensure stable internet connection

### Out of Memory
**Problem**: Too many frames being processed

**Solution**:
- Increase sample_rate (extract fewer frames)
- Reduce top_percent
- Set max_frames limit

### Low Quality Results
**Problem**: Selected frames don't meet expectations

**Solution**:
- Increase min_score threshold
- Try different selection_criteria
- Reduce top_percent to be more selective

## Technical Details

### API Integration
- Model: `qwen/qwen3-vl-235b-a22b-thinking`
- Provider: OpenRouter API
- Timeout: 60 seconds per frame
- Image format: Base64-encoded JPEG

### Frame Processing
- Extraction: FFmpeg with quality level 2
- Format: JPEG
- Processing: Sequential frame-by-frame analysis
- Temporary storage: `ComfyUI/temp/qwen_frame_selector/`

### Score Weighting by Criteria
- **quality_focused**: 40% technical + 40% sharpness + 20% others
- **aesthetic_focused**: 40% aesthetic + 30% composition + 30% others
- **balanced**: Equal weights (20% each)
- **content_diversity**: Penalizes similar content, rewards uniqueness
- **keyframe_detection**: Prioritizes high-content frames with scene changes

## Limitations

- Requires internet connection for API access
- Processing time scales linearly with frame count
- API usage costs apply (check OpenRouter pricing)
- Maximum practical limit: ~500 frames per run
- Temporary files require disk space

## Project Structure

```
ComfyUI-QwenFrameSelector/
├── __init__.py          # Node registration
├── nodes.py             # Main implementation
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Workflow Examples

Example workflows available at:
[Hugging Face Gift Repository](https://huggingface.co/eddy1111111/gift)

## Credits

- Author: eddy
- AI Model: Qwen3-VL-235B (Alibaba Cloud)
- API Provider: OpenRouter

## License

MIT License

## Contributing

Issues and pull requests welcome on GitHub!

## Links

- [GitHub Repository](https://github.com/eddyhhlure1Eddy/ComfyUI-QwenFrameSelector)
- [Example Workflows](https://huggingface.co/eddy1111111/gift)
- [OpenRouter Platform](https://openrouter.ai/)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## Changelog

### Version 1.1.0
- Added IMAGE input support for analyzing existing image batches
- Dual input mode: VIDEO or IMAGE (mutually exclusive)
- Image mode bypasses frame extraction, analyzes all input images directly
- Enhanced flexibility for image quality control workflows
- Updated documentation with image mode examples

### Version 1.0.0
- Initial release
- Multi-dimensional frame quality analysis
- Five selection strategies
- Flexible filtering options
- JSON scoring output
- VIDEO input support
