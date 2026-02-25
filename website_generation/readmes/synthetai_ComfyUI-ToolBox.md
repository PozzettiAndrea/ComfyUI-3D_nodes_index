# ComfyUI-ToolBox

A collection of utility nodes for ComfyUI, including audio/video processing, file uploads, and AI image generation.

[中文文档 (Chinese Documentation)](README_CN.md)

## Utility Nodes

### Create Image (OpenAI)

The Create Image node allows you to generate images using OpenAI's API, supporting DALL-E and GPT-Image models.

**Features:**
- Integration with OpenAI's DALL-E and GPT-Image image generation APIs
- Customizable image size, quality, style, and background
- Support for URL or base64 JSON response formats
- Automatic handling of API rate limits and error retries
- Support for various output formats and compression settings
- Transparent background support (with GPT-Image-1 model)

**Node Parameters:**
- Required Parameters:
  - `api_key`: OpenAI API key
  - `prompt`: Text description for image generation (max length varies by model: 32000 chars for GPT-Image-1, 4000 chars for DALL-E-3, 1000 chars for DALL-E-2)

- Optional Parameters:
  - `model`: Model to use, one of "dall-e-2", "dall-e-3", or "gpt-image-1" (default: "gpt-image-1")
  - `size`: Image dimensions, with various size options that are validated against the selected model (default: "1024x1024")
  - `quality`: Image quality, options vary by model (default: "auto")
    - GPT-Image-1: "auto", "high", "medium", "low"
    - DALL-E-3: "auto", "standard", "hd"
    - DALL-E-2: "auto", "standard"
  - `style`: Image style, only for DALL-E-3 model, one of "vivid" or "natural" (default: "vivid")
  - `background`: Background setting, only for GPT-Image-1 model, one of "auto", "transparent", or "opaque" (default: "auto")
  - `moderation`: Content moderation level, only for GPT-Image-1 model, one of "auto" or "low" (default: "auto")
  - `response_format`: Return format for DALL-E models, one of "url" or "b64_json" (default: "b64_json")
  - `output_format`: Output format for GPT-Image-1 model, one of "png", "jpeg", or "webp" (default: "png")
  - `output_compression`: Image compression level, only for GPT-Image-1 model with webp or jpeg formats, range 0-100 (default: 100)
  - `n`: Number of images to generate, range 1-10 (DALL-E-3 only supports n=1)
  - `user`: User identifier for tracking and monitoring

**Output:**
- `image`: The generated image, returned as an image object in ComfyUI
- `b64_json`: The base64-encoded image data that can be passed to the Save Image node

### Save Image (OpenAI)

The Save Image node specifically designed to handle and save OpenAI's image data.

**Features:**
- Decodes base64 image data and saves it to a file
- Automatically loads the saved image and outputs it for further processing
- Properly handles image format and EXIF orientation data
- Extracts alpha channel as mask (if available)
- Provides detailed debug logs
- Fully compatible with ComfyUI's Preview Image node

**Node Parameters:**
- `b64_json`: Base64-encoded image data from OpenAI
- `filename_prefix`: Prefix for the saved file name (default: "openai")
- `output_dir`: Custom output directory (optional, uses ComfyUI's default output directory if empty)

**Output:**
- `filename`: Path to the saved image file
- `image`: The image as a ComfyUI image object (ready for preview or further processing)
- `mask`: Alpha channel mask (if present in the image, otherwise returns an empty mask)

### Edit Image (OpenAI)

The Edit Image node allows you to edit or extend existing images using OpenAI's API, supporting both DALL-E-2 and GPT-Image-1 models.

**Features:**
- Takes existing images and modifies them based on a text prompt
- Dynamic input interface with adjustable number of image inputs
- Support for up to 4 separate input images when using GPT-Image-1 model
- Optional mask support to specify areas to be edited
- Supports both DALL-E-2 and GPT-Image-1 models
- Handles image format conversion and size requirements automatically
- Automatic retries for API rate limits and errors
- Returns multiple images when requested (n parameter)

**Node Parameters:**
- Required Parameters:
  - `api_key`: OpenAI API key
  - `inputcount`: Number of image inputs to display
  - `image_1`: Primary input image to be edited (as ComfyUI IMAGE type)
  - `prompt`: Text description of the desired modifications (max length: 32000 chars for GPT-Image-1, 1000 chars for DALL-E-2)

- Optional Parameters:
  - `mask`: Optional mask to specify which areas to edit (transparent areas in the mask indicate regions to modify)
  - `model`: Model to use, one of "gpt-image-1" or "dall-e-2" (default: "gpt-image-1")
  - `n`: Number of images to generate, range 1-10
  - `size`: Image dimensions with model-specific options:
    - GPT-Image-1: "auto", "1024x1024", "1536x1024" (landscape), "1024x1536" (portrait)
    - DALL-E-2: "256x256", "512x512", "1024x1024"
  - `quality`: Image quality, options vary by model (default: "auto")
  - `response_format`: Return format, one of "url" or "b64_json" (default: "b64_json")
  - `user`: User identifier for tracking and monitoring

**Usage:**
1. Set the desired number of image inputs using the `inputcount` parameter
2. Click "Update inputs" to update the node interface
3. Connect your images to the displayed image inputs
4. When using DALL-E-2 model, only the first image will be used regardless of inputcount value
5. For GPT-Image-1 model, up to 4 images can be used; if inputcount is set higher, only the first 4 will be used

**Output:**
- `image`: The edited image(s), returned as an image object in ComfyUI
- `b64_json`: The base64-encoded image data that can be passed to the Save Image node

### Video Combine

The Video Combine node merges an audio file with a video file, ideal for use as the final node in a workflow.

**Features:**
- Takes a video file and an audio file as input
- Combines the audio with the video
- Provides various methods for handling long audio (cut off audio, bounce video, loop video)
- Customizable output filename prefix
- Merged video is saved to ComfyUI's output directory

**Node Parameters:**
- `video_file`: Path to the input video file
- `audio_file`: Path to the input audio file
- `filename_prefix`: Prefix for the output filename, defaults to "output"
- `audio_handling`: Method for handling audio longer than the video:
  - `cut off audio`: Truncate audio to match video duration
  - `bounce video`: Alternate forward/reverse video playback to match audio length (default)
  - `loop video`: Repeat video playback to match audio length

**Output:**
- `video_path`: Absolute path to the merged video file

### AWS S3 Upload

The AWS S3 Upload node uploads local files to Amazon S3 storage service.

**Features:**
- Support for uploading any local file type to AWS S3 buckets
- Flexible storage path configuration with parent and subdirectory support
- Automatic directory hierarchy handling
- AWS region specification
- Returns the S3 file path after upload

**Node Parameters:**
- `bucket`: AWS S3 bucket name
- `access_key`: AWS access key ID
- `secret_key`: AWS secret access key
- `region`: AWS region name (defaults to "us-east-1")
- `parent_directory`: Parent directory path within the bucket (optional)
- `file_path`: Absolute path to the local file to upload
- `sub_dir_name` (optional): Subdirectory name under the parent directory, if set files will be stored in the subdirectory

**Directory Structure Rules:**
- If both `parent_directory` and `sub_dir_name` have values, files will be stored under `bucket/parent_directory/sub_dir_name/`
- If only `parent_directory` has a value, files will be stored under `bucket/parent_directory/`
- If only `sub_dir_name` has a value, files will be stored under `bucket/sub_dir_name/`
- If neither has a value, files will be stored directly in the bucket root

**Output:**
- `s3_file_path`: S3 path of the uploaded file (format: s3://bucket/path/to/file)

### Trim Audio To Length

The Trim Audio To Length node trims audio files to a specified duration.

**Features:**
- Takes an audio file path as input
- Trims the audio to a user-specified duration
- If target duration exceeds original audio length, returns the original audio
- Customizable output filename prefix
- Trimmed audio is saved to ComfyUI's output directory

**Node Parameters:**
- `audio_path`: Path to the input audio file
- `target_duration`: Duration in seconds to trim the audio to (range: 0.1 to 3600.0 seconds)
- `filename_prefix`: Prefix for the output filename, defaults to "trimmed_audio"

**Output:**
- `file_path`: Absolute path to the trimmed audio file

## Installation

1. Make sure you have ComfyUI installed
2. Ensure FFmpeg is installed on your system (for audio/video processing)
3. Clone this repository into the `custom_nodes` directory of ComfyUI:
```
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-ToolBox.git
```
4. Install the required Python dependencies:
```
cd ComfyUI-ToolBox
pip install -r requirements.txt
```
5. Restart ComfyUI
6. The nodes should now be available in the ComfyUI interface under the "ToolBox" category

## Dependencies

The main dependencies for this project are listed in `requirements.txt`, including:
- boto3 - for AWS S3 file uploads
- FFmpeg - for audio/video processing (system-level installation required)
- requests - for API requests and file downloads
- Other Python libraries - see requirements.txt for details

## Usage Examples

### Create Image (OpenAI) Node Usage
1. Add the "Create Image (OpenAI)" node to your ComfyUI workflow (under the ToolBox/OpenAI category)
2. Enter your OpenAI API key
3. Input your desired image description (prompt)
4. Select a model (such as dall-e-3 or gpt-image-1)
5. Configure the appropriate parameters based on your selected model (size, quality, style, background, etc.)
6. Run the workflow to generate the image
7. The generated image can be used directly in ComfyUI for further processing, such as editing or applying effects with other nodes

### Video Combine Node Usage
1. Add the "Video Combine" node to your ComfyUI workflow (under the ToolBox/Video Combine category)
2. Set the paths for input video file and audio file
3. Set the output filename prefix
4. Choose the method for handling audio longer than the video (cut off audio, bounce video, or loop video)
5. Run the workflow to get the merged video file path
6. The merged video will be saved in the ComfyUI output directory

### AWS S3 Upload Node Usage
1. Add the "AWS S3 Upload" node to your ComfyUI workflow (under the ToolBox/AWS S3 category)
2. Enter your AWS S3 bucket name, access key, and secret key
3. Select the correct AWS region (e.g., "us-east-1", "eu-west-1", etc.)
4. Set the parent directory path (optional) and subdirectory name (optional) to define the storage structure
5. Enter the path of the local file to upload
6. Run the workflow to get the S3 file path of the uploaded file

### Trim Audio To Length Node Usage
1. Add the "Trim Audio To Length" node to your ComfyUI workflow (under the ToolBox/Audio category)
2. Set the path for the input audio file
3. Specify the target duration in seconds for the trimmed audio
4. Set the output filename prefix (optional, defaults to "trimmed_audio")
5. Run the workflow to get the trimmed audio file path
6. The trimmed audio will be saved in the ComfyUI output directory with an incrementing file number

## License

This project is released under the MIT License.