# ComfyUI Gemini Nodes

[中文版](README_CN.md)

A comprehensive collection of custom nodes for integrating Google Gemini API with ComfyUI, providing powerful AI capabilities for text generation, structured output, image generation, and video analysis.

## 🚀 Available Nodes

### Core Nodes
- **Gemini Text API** - Advanced text generation with flexible model selection
- **Gemini Structured Output** - Generate JSON responses with schema validation
- **Gemini JSON Extractor** - Extract specific information from text into JSON format
- **Gemini Field Extractor** - Extract fields from JSON using path notation
- **Gemini JSON Parser** - Parse, validate, and manipulate JSON data

### Image Generation
- **Gemini Image Editor** - Generate images with optional reference images
- **Gemini Image Gen Advanced** - Multi-slot batch image generation system

### Video Processing
- **Gemini Video Generator (Veo)** - Generate videos using Google's Veo models
- **Gemini Video Captioner** - Generate intelligent captions for videos

### Unofficial API Support
- **Unofficial API Call** - Call unofficial APIs supporting Claude, GPT, Gemini and other models
- **Unofficial Stream API Call** - Stream responses from unofficial APIs with real-time output
  - **NEW**: Support for both OpenAI Compatible and Gemini Native API formats
  - **NEW**: Automatic image extraction from Gemini Native API responses

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Node Documentation](#node-documentation)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Credits](#credits)

## Features

### Core Capabilities
- **Text Generation**: Advanced text generation with all Gemini models
- **Structured Output**: JSON schema-based responses and data extraction
- **Image Generation**: Multi-reference image generation with batch processing
- **Video Analysis**: Intelligent video captioning and analysis
- **JSON Processing**: Extract, parse, and manipulate JSON data
- **API Debugging**: All processing nodes now output complete API request/response for debugging

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jqy-yo/comfyui-gemini-nodes.git
```

2. Install required dependencies:
```bash
cd comfyui-gemini-nodes
pip install -r requirements.txt
```

3. Restart ComfyUI

## Configuration

### API Key Setup

Set up your Google Gemini API key in one of these ways:

1. **Environment Variable (Recommended)**:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

2. **Node Input**: Enter directly in the node's API key field

### Model Selection

All nodes support flexible model input. Enter any valid Gemini model name:
- Text/Structured: `gemini-2.0-flash`, `gemini-1.5-pro`
- Image Generation: `imagen-3.0-generate-001`, `gemini-2.0-flash-exp`
- Video Analysis: `gemini-2.0-flash`, `gemini-1.5-pro`

## Node Documentation

### 🤖 Gemini Text API
Generate text responses using any Gemini model with flexible model selection and advanced generation parameters.

**Input Parameters:**
- `prompt` (STRING): The input text prompt
- `api_key` (STRING): Your Google API key (can use environment variable GOOGLE_API_KEY)
- `model` (STRING): Model name (default: "gemini-2.0-flash")
  - Examples: gemini-2.5-flash-lite, gemini-2.0-flash, gemini-1.5-pro
- `temperature` (FLOAT, 0.0-1.0, default: 0.7): Controls randomness in generation
  - 0.0: Most deterministic/focused
  - 1.0: Most creative/varied
- `max_output_tokens` (INT, 64-8192, default: 1024): Maximum response length
- `seed` (INT, 0-2147483647, default: 0): Random seed for reproducibility
- `system_instructions` (STRING, optional): System-level instructions to guide the model's behavior
- `top_p` (FLOAT, 0.0-1.0, default: 0.95): Nucleus sampling threshold
- `top_k` (INT, 1-100, default: 64): Top-k sampling parameter
- `api_version` (ENUM, optional): API version selection (auto/v1/v1beta/v1alpha)

**Output:**
- `response` (STRING): Generated text response
- `api_request` (STRING): Complete API request sent to Gemini (JSON format)
- `api_response` (STRING): Complete API response from Gemini (JSON format)

**Usage Examples:**

1. **Basic Text Generation:**
```
Prompt: "Write a haiku about artificial intelligence"
Model: gemini-2.0-flash
Temperature: 0.8
Output: A creative haiku poem about AI
```

2. **Technical Documentation:**
```
Prompt: "Explain the implementation of a binary search tree"
Model: gemini-1.5-pro
Temperature: 0.3
System Instructions: "Provide detailed technical explanations with code examples in Python"
Output: Comprehensive BST explanation with Python code
```

3. **Creative Writing:**
```
Prompt: "Continue this story: The door creaked open revealing..."
Model: gemini-2.5-flash-lite
Temperature: 0.9
Max Output Tokens: 2048
Output: Creative story continuation
```

**Best Practices:**
- Use lower temperature (0.1-0.3) for factual/technical content
- Use higher temperature (0.7-0.9) for creative content
- Set system instructions for consistent behavior across prompts
- Use seeds for reproducible outputs in production

### 📊 Gemini Structured Output
Generate responses in a specific JSON structure using JSON Schema validation.

**Input Parameters:**
- `prompt` (STRING): Input prompt describing what to generate
- `api_key` (STRING): Your Google API key
- `model` (STRING, default: "gemini-2.0-flash"): Model name
- `output_mode` (ENUM): 
  - `json_schema`: Use custom JSON schema
  - `enum`: Generate from predefined options
- `schema_json` (STRING): JSON Schema definition (for json_schema mode)
- `temperature` (FLOAT, 0.0-1.0, default: 0.7): Generation temperature
- `max_output_tokens` (INT, 64-8192, default: 1024): Maximum tokens
- `seed` (INT): Random seed for reproducibility
- `system_instructions` (STRING, optional): System-level instructions
- `enum_options` (STRING, optional): JSON array of enum options (for enum mode)
- `property_ordering` (STRING, optional): Comma-separated property order
- `top_p` (FLOAT, optional): Nucleus sampling parameter
- `top_k` (INT, optional): Top-k sampling parameter

**Output:**
- `structured_output` (STRING): Formatted JSON output
- `raw_json` (STRING): Raw JSON response
- `debug_request_sent` (STRING): Complete API request sent to Gemini (JSON format)
- `debug_response_received` (STRING): Complete API response from Gemini (JSON format)

**Usage Examples:**

1. **Product Information Schema:**
```json
{
  "type": "object",
  "properties": {
    "product_name": {"type": "string"},
    "price": {"type": "number"},
    "in_stock": {"type": "boolean"},
    "categories": {
      "type": "array",
      "items": {"type": "string"}
    },
    "specifications": {
      "type": "object",
      "properties": {
        "weight": {"type": "string"},
        "dimensions": {"type": "string"}
      }
    }
  },
  "required": ["product_name", "price", "in_stock"]
}
```

2. **Enum Mode Example:**
```
Output Mode: enum
Enum Options: ["positive", "negative", "neutral"]
Prompt: "Analyze the sentiment of this review: 'Great product!'"
Output: {"selection": "positive"}
```

3. **Complex Nested Structure:**
```json
{
  "type": "object",
  "properties": {
    "article": {
      "type": "object",
      "properties": {
        "title": {"type": "string"},
        "authors": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "email": {"type": "string"}
            }
          }
        },
        "sections": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "heading": {"type": "string"},
              "content": {"type": "string"}
            }
          }
        }
      }
    }
  }
}
```

**Best Practices:**
- Keep schemas focused and not overly complex
- Use clear property names and descriptions
- Test schemas with sample data first
- Use lower temperature (0.1-0.3) for consistent structured output
- Property ordering helps maintain consistent output format

### 🔍 Gemini JSON Extractor
Extract specific information from text into JSON format using field definitions.

**Input Parameters:**
- `prompt` (STRING): Extraction instructions describing what to extract
- `api_key` (STRING): Your Google API key
- `model` (STRING, default: "gemini-2.0-flash"): Model name
- `extract_fields` (STRING): Field definitions in simple format
- `temperature` (FLOAT, 0.0-1.0, default: 0.3): Lower values for accurate extraction
- `seed` (INT): Random seed for reproducibility
- `input_text` (STRING, optional): Text to extract from (can be combined with prompt)
- `system_instructions` (STRING, optional): Default: "Extract the requested information from the provided text. Be accurate and concise."

**Field Definition Format:**
```
field_name: type
field_name2: type[]
field_name3: type?
```

**Supported Types:**
- `string`: Text values
- `number`/`float`: Numeric values
- `integer`/`int`: Whole numbers
- `boolean`/`bool`: True/false values
- `string[]`: Array of strings
- `?` suffix: Optional field (not required)

**Output:**
- `extracted_json` (STRING): Raw JSON output
- `formatted_output` (STRING): Human-readable format with field labels

**Usage Examples:**

1. **Article Metadata Extraction:**
```
Extract Fields:
title: string
author: string
publish_date: string
categories: string[]
word_count: integer
is_featured: boolean

Input Text: "Breaking News: AI Advances in Healthcare by Dr. Smith..."
Output: {
  "title": "Breaking News: AI Advances in Healthcare",
  "author": "Dr. Smith",
  "publish_date": "2024-01-15",
  "categories": ["AI", "Healthcare", "Technology"],
  "word_count": 1250,
  "is_featured": true
}
```

2. **Product Review Analysis:**
```
Extract Fields:
product_name: string
rating: number
pros: string[]
cons: string[]
recommended: boolean
price_mentioned: string?

Prompt: "Extract review information"
Input Text: "[Product review text...]"
```

3. **Contact Information Parsing:**
```
Extract Fields:
full_name: string
email: string
phone: string?
company: string?
job_title: string?
address: string?

Prompt: "Extract contact details from the business card text"
```

**Best Practices:**
- Use low temperature (0.1-0.3) for accurate extraction
- Provide clear field names that describe the data
- Mark optional fields with '?' suffix
- Use arrays (type[]) for multiple values
- Combine with downstream nodes to process extracted data

### 📌 Gemini Field Extractor
Extract specific fields from JSON data using path notation. This node does NOT use the Gemini API - it's a pure JSON processing tool.

**Input Parameters:**
- `json_input` (STRING): JSON data to extract from (supports raw JSON or markdown-wrapped)
- `field_path` (STRING): Path to the field using dot notation
- `default_value` (STRING): Value returned if field not found
- `output_format` (ENUM):
  - `auto`: Automatically determine format
  - `string`: Convert to string
  - `json`: Format as JSON
  - `number`: Extract as number
  - `boolean`: Convert to boolean
  - `list`: Format as list/array
- `array_handling` (ENUM, optional):
  - `all`: Return entire array
  - `first`: Return first element
  - `last`: Return last element
  - `join`: Join array elements
- `join_separator` (STRING, default: ", "): Separator when joining arrays

**Path Notation Examples:**
- Simple field: `name`, `email`, `id`
- Nested object: `user.profile.age`, `settings.theme.color`
- Array by index: `items[0]`, `users[2].name`
- Negative index: `items[-1]` (last item)
- All array items: `users[*].email`, `products[*].price`
- Complex paths: `data.users[0].orders[*].items[0].price`

**Output:**
- `extracted_value` (STRING): The extracted value in specified format
- `formatted_output` (STRING): Detailed extraction information with type and structure
- `extraction_success` (BOOLEAN): True if extraction succeeded, False otherwise

**Usage Examples:**

1. **Extract User Email:**
```
JSON Input: {"user": {"name": "John", "email": "john@example.com"}}
Field Path: user.email
Output: john@example.com
```

2. **Extract All Product Prices:**
```
JSON Input: {
  "products": [
    {"name": "Item1", "price": 10.99},
    {"name": "Item2", "price": 25.50}
  ]
}
Field Path: products[*].price
Array Handling: join
Join Separator: ", "
Output: "10.99, 25.50"
```

3. **Extract Nested Configuration:**
```
JSON Input: {
  "config": {
    "database": {
      "host": "localhost",
      "port": 5432,
      "credentials": {
        "username": "admin"
      }
    }
  }
}
Field Path: config.database.credentials.username
Output: "admin"
```

4. **Extract with Default Value:**
```
JSON Input: {"name": "Product"}
Field Path: price
Default Value: "0.00"
Output: "0.00" (field not found, using default)
```

**Best Practices:**
- Test path syntax with sample JSON first
- Use meaningful default values
- Choose appropriate array handling for your use case
- Chain with other nodes for complex data processing
- Validate JSON input format before extraction

### 🛠️ Gemini JSON Parser
Parse and manipulate JSON data. This node does NOT use the Gemini API - it's a pure JSON processing utility.

**Input Parameters:**
- `json_input` (STRING): JSON data to process (supports raw JSON or markdown-wrapped)
- `operation` (ENUM): Operation to perform
  - `validate`: Check if JSON is valid and show structure info
  - `format`: Pretty-print with indentation
  - `minify`: Remove unnecessary whitespace for compact storage
  - `extract_keys`: Get all key paths in the JSON
  - `get_type`: Analyze type structure of the JSON
  - `count_items`: Count elements by type (objects, arrays, strings, etc.)
- `indent` (INT, 0-8, default: 2): Indentation spaces for formatting
- `sort_keys` (BOOLEAN, default: False): Sort object keys alphabetically

**Output:**
- `result` (STRING): Operation result
- `info` (STRING): Detailed operation information
- `success` (BOOLEAN): True if operation succeeded

**Usage Examples:**

1. **Validate JSON:**
```
Operation: validate
Input: {"name": "test", "values": [1, 2, 3]}
Result: ✅ Valid JSON
Info: 
  Type: Object
  Properties: 2
  Keys: name, values
```

2. **Format JSON:**
```
Operation: format
Indent: 4
Sort Keys: true
Input: {"b":1,"a":{"nested":true}}
Output:
{
    "a": {
        "nested": true
    },
    "b": 1
}
```

3. **Minify JSON:**
```
Operation: minify
Input: {
    "name": "test",
    "value": 123
}
Output: {"name":"test","value":123}
Info: Minified: 45 → 28 bytes (62.2%)
```

4. **Extract All Keys:**
```
Operation: extract_keys
Input: {
    "user": {
        "name": "John",
        "settings": {
            "theme": "dark"
        }
    }
}
Output: [
    "user",
    "user.name",
    "user.settings",
    "user.settings.theme"
]
```

5. **Get Type Structure:**
```
Operation: get_type
Input: {
    "users": [{"name": "John", "age": 30}],
    "count": 1
}
Output: {
    "users": [{"name": "string", "age": "number"}],
    "count": "number"
}
```

6. **Count Items:**
```
Operation: count_items
Output: {
    "total_keys": 5,
    "total_values": 3,
    "objects": 2,
    "arrays": 1,
    "strings": 2,
    "numbers": 1,
    "booleans": 0,
    "nulls": 0
}
```

**Best Practices:**
- Use validate to check JSON before processing
- Use minify before storing or transmitting JSON
- Use extract_keys to understand complex JSON structure
- Use format with sort_keys for consistent JSON output
- Chain with Field Extractor for targeted data extraction

### 🎨 Gemini Image Editor
Generate images with optional reference images using Gemini's image generation models.

**Input Parameters:**
- `prompt` (STRING): Detailed image generation prompt
- `api_key` (STRING): Your Google API key
- `model` (STRING): Model name
  - Default: "models/gemini-2.0-flash-preview-image-generation"
  - Alternatives: "imagen-3.0-generate-001", "gemini-2.5-flash", "models/gemini-2.0-flash-exp"
- `temperature` (FLOAT, 0.0-2.0, default: 1.0): Generation creativity
- `max_retries` (INT, 1-5, default: 3): API retry attempts
- `batch_size` (INT, 1-8, default: 1): Number of images to generate
- `seed` (INT, optional): Random seed for reproducibility
- `image1` to `image4` (IMAGE, optional): Reference images for style/content guidance
- `api_version` (ENUM, optional): API version (auto/v1/v1beta/v1alpha)

**Output:**
- `image` (IMAGE): Generated images batch
- `API Respond` (STRING): API response information
- `api_request` (STRING): Complete API request sent to Gemini (JSON format)
- `api_response` (STRING): Complete API response from Gemini (JSON format)

**Features:**
- Automatic image padding to minimum 1024x1024 with white borders
- Async parallel processing for batch generation
- Built-in retry logic with exponential backoff
- Error image generation on failure (black image with error text)
- Support for up to 4 reference images

**Usage Examples:**

1. **Simple Image Generation:**
```
Prompt: "A serene Japanese garden with cherry blossoms"
Model: imagen-3.0-generate-001
Batch Size: 4
Output: 4 variations of Japanese garden images
```

2. **Style Transfer with Reference:**
```
Prompt: "Transform this into a watercolor painting style"
Image1: [Original photo]
Temperature: 0.8
Output: Watercolor style version of the input image
```

3. **Product Visualization:**
```
Prompt: "Modern minimalist product photography on white background"
Image1: [Product sketch]
Model: gemini-2.0-flash-preview-image-generation
Batch Size: 3
Output: 3 professional product photos based on sketch
```

4. **Character Design Variations:**
```
Prompt: "Create variations of this character in different poses"
Image1: [Character reference]
Image2: [Style reference]
Temperature: 1.2
Batch Size: 6
Output: 6 character variations
```

**Best Practices:**
- Provide detailed, specific prompts for better results
- Use reference images to guide style and composition
- Lower temperature (0.5-0.8) for consistency
- Higher temperature (1.2-1.5) for more variation
- Images smaller than 1024x1024 are automatically padded
- Use batch generation for multiple variations
- Set seed for reproducible results in production

### 🚀 Gemini Image Gen Advanced
Advanced multi-slot image generation system for batch processing multiple image/prompt combinations.

**Input Parameters:**
- `inputcount` (INT, 1-100, default: 1): Number of input slots to use
- `api_key` (STRING): Your Google API key (supports env var GEMINI_API_KEY)
- `model` (STRING): Model name
  - Default: "models/gemini-2.0-flash-preview-image-generation"
  - Alternatives: "imagen-3.0-generate-001", "gemini-2.5-flash"
- `temperature` (FLOAT, 0.0-2.0, default: 1.0): Generation creativity
- `max_retries` (INT, 1-5, default: 3): API retry attempts per slot
- `prompt_1` (STRING, required): First generation prompt
- `image_1` (IMAGE, optional): First reference image
- `seed` (INT, optional): Random seed for reproducibility
- `retry_indefinitely` (BOOLEAN, optional): Keep retrying on failure
- `api_version` (ENUM, optional): API version selection

**Dynamic Inputs (based on inputcount):**
- `input_image_X` (IMAGE): Reference image for slot X
- `input_prompt_X` (STRING): Generation prompt for slot X
- Where X ranges from 1 to inputcount

**Features:**
- Asynchronous parallel processing of all slots
- Progress bar with real-time updates
- Automatic image padding to 1024x1024 minimum
- Batch result aggregation
- Error handling with fallback images
- Memory-efficient processing

**Output:**
- `images` (IMAGE): All generated images in a single batch
- `API_responses` (STRING): Detailed API response information
- `api_request` (STRING): Complete API requests sent to Gemini (JSON format)
- `api_response` (STRING): Complete API responses from Gemini (JSON format)

**Usage Examples:**

1. **Batch Product Variations:**
```
Input Count: 5
Slot 1: "Red leather handbag" + [reference image]
Slot 2: "Blue leather handbag" + [reference image]
Slot 3: "Black leather handbag" + [reference image]
Slot 4: "Brown leather handbag" + [reference image]
Slot 5: "White leather handbag" + [reference image]
Output: 5 handbag variations in different colors
```

2. **Scene Variations:**
```
Input Count: 10
Model: imagen-3.0-generate-001
Slot 1-10: Different time-of-day prompts for same scene
- "Sunrise over the mountains"
- "Morning light on the mountains"
- "Noon sunshine on the mountains"
- "Golden hour mountain view"
- "Sunset behind the mountains"
- etc.
Output: 10 images showing time progression
```

3. **Style Exploration:**
```
Input Count: 8
Base Image: [Portrait photo]
Slot 1: "Oil painting style"
Slot 2: "Watercolor style"
Slot 3: "Pencil sketch style"
Slot 4: "Digital art style"
Slot 5: "Anime style"
Slot 6: "Pop art style"
Slot 7: "Impressionist style"
Slot 8: "Photorealistic style"
Output: 8 different artistic interpretations
```

4. **Marketing Asset Generation:**
```
Input Count: 20
Batch processing for social media content:
- Different angles of products
- Various backgrounds
- Multiple lighting conditions
- Different compositions
Output: 20 marketing-ready images
```

**Best Practices:**
- Plan slot allocation for systematic variations
- Use consistent seed across slots for controlled variation
- Monitor progress bar for large batches
- Group similar prompts for better GPU utilization
- Use retry_indefinitely cautiously (may increase costs)
- Consider memory limits when setting high inputcount
- Batch related images together for workflow efficiency

### 🎥 Gemini Video Generator (Veo)
Generate high-quality videos using Google's Veo models with text-to-video and image-to-video capabilities.

**Input Parameters:**
- `prompt` (STRING): Detailed description of the video to generate
  - Default: "A cinematic drone shot of a red convertible driving along a coastal road at sunset"
- `api_key` (STRING): Your Google API key (requires Veo access)
- `model` (ENUM): Video generation model
  - `veo-3.0-generate-preview`: Highest quality Veo 3 model
  - `veo-3.0-fast-generate-preview`: Faster Veo 3 variant
  - `veo-2.0-generate-001`: Veo 2 model
- `aspect_ratio` (ENUM): Video dimensions
  - Options: "16:9", "9:16", "1:1", "4:3", "3:4"
  - Default: "16:9"
- `person_generation` (ENUM): Control human representation
  - `default`: Standard behavior
  - `allow`: Explicitly allow person generation
  - `dont_allow`: Prevent person generation
- `max_wait_minutes` (FLOAT, 1.0-30.0, default: 5.0): Maximum time to wait for generation
- `poll_interval_seconds` (INT, 2-30, default: 5): How often to check generation status
- `negative_prompt` (STRING, optional): Elements to exclude from the video
- `initial_image` (IMAGE, optional): Starting image for video generation
- `save_path` (STRING, optional): Path to save the generated video

**Output:**
- `video_path` (STRING): Path to the generated video file
- `preview_frame` (IMAGE): A preview frame extracted from the video
- `generation_info` (STRING): Details about the generated video
- `api_request` (STRING): Complete API request sent to Gemini (JSON format)
- `api_response` (STRING): Complete API response from Gemini (JSON format)

**Features:**
- Text-to-video generation with detailed prompts
- Image-to-video generation from initial frames
- Multiple aspect ratios for different platforms
- Negative prompting to exclude unwanted elements
- Asynchronous generation with progress tracking
- Automatic video download and storage
- Preview frame extraction for ComfyUI display
- SynthID watermarking (automatic)

**Video Specifications:**
- Duration: 8 seconds
- Resolution: 720p (1280x720 or equivalent based on aspect ratio)
- Format: MP4 with native audio
- Storage: Videos stored for 2 days on Google servers
- Watermark: Includes SynthID for AI-generated content identification

**Usage Examples:**

1. **Cinematic Scene Generation:**
```
Prompt: "A sweeping aerial view of a misty mountain range at dawn, clouds rolling through valleys, golden sunlight breaking through"
Model: veo-3.0-generate-preview
Aspect Ratio: 16:9
Output: 8-second cinematic landscape video
```

2. **Product Showcase:**
```
Prompt: "360-degree rotation of a luxury watch on a black velvet turntable, dramatic lighting highlighting the metallic finish"
Negative Prompt: "blurry, low quality, distorted"
Model: veo-3.0-generate-preview
Aspect Ratio: 1:1
Output: Professional product video
```

3. **Image-to-Video Animation:**
```
Prompt: "Bring this portrait to life with subtle movements, blinking, and breathing"
Initial Image: [Portrait photo]
Model: veo-3.0-fast-generate-preview
Person Generation: allow
Output: Animated portrait video
```

4. **Social Media Content:**
```
Prompt: "Time-lapse of a busy coffee shop, people coming and going, steam rising from cups, warm cozy atmosphere"
Model: veo-2.0-generate-001
Aspect Ratio: 9:16
Output: Vertical video for social media
```

**Best Practices:**
- Use detailed, specific prompts for better results
- Include style keywords (cinematic, documentary, anime, etc.)
- Use negative prompts to avoid unwanted elements
- Consider aspect ratio based on target platform
- Allow sufficient generation time (typically 2-5 minutes)
- Save videos locally as they're only stored for 2 days

**Important Notes:**
- Requires API access to Veo models (may need special permissions)
- Generation is asynchronous and may take several minutes
- Videos include SynthID watermark for transparency
- Person generation may be restricted in certain regions
- Maximum prompt length: 1,024 tokens

### 🎬 Gemini Video Captioner
Generate intelligent captions and descriptions for videos using Gemini's multimodal capabilities.

**Input Parameters:**
- `api_key` (STRING): Your Google API key
- `model` (STRING): Model name
  - Default: "gemini-2.0-flash"
  - Alternatives: "gemini-2.5-flash-lite", "gemini-1.5-pro"
- `frames_per_second` (FLOAT, 0.1-10.0, default: 1.0): Frame sampling rate
- `max_duration_minutes` (FLOAT, 0.1-45.0, default: 2.0): Maximum video duration to process
- `prompt` (STRING): Analysis instructions
  - Default: "Describe this video scene in detail. Include any important actions, subjects, settings, and atmosphere."
- `process_audio` (ENUM ["false", "true"], default: "false"): Include audio analysis
- `temperature` (FLOAT, 0.0-1.0, default: 0.7): Generation temperature
- `max_output_tokens` (INT, 50-8192, default: 1024): Maximum caption length
- `top_p` (FLOAT, 0.0-1.0, default: 0.95): Nucleus sampling
- `top_k` (INT, 1-100, default: 64): Top-k sampling
- `seed` (INT): Random seed for reproducibility
- `video_path` (STRING, optional): Path to video file
- `image` (IMAGE, optional): Image sequence/batch as video frames
- `api_version` (ENUM, optional): API version selection

**Features:**
- Automatic video format conversion to WebM
- Intelligent frame sampling based on FPS setting
- File size optimization (under 30MB limit)
- Support for both video files and image sequences
- Audio processing capability (model-dependent)
- Frame extraction with timestamps
- Progress tracking for long videos

**Output:**
- `caption` (STRING): Generated video description/caption
- `sampled_frame` (IMAGE): Representative frame from the video
- `raw_json` (STRING): Raw JSON response (for structured output mode)
- `api_request` (STRING): Complete API request sent to Gemini (JSON format)
- `api_response` (STRING): Complete API response from Gemini (JSON format)

**Video Processing Details:**
- Maximum file size: 30MB (automatically compressed if needed)
- Supported formats: MP4, AVI, MOV, WebM, WMV, FLV, MPG, MPEG
- Frame sampling: Based on frames_per_second parameter
- Duration limits: 2 minutes (Gemini 1.0), 45 minutes (Gemini 1.5+)

**Usage Examples:**

1. **Basic Video Description:**
```
Video Path: /path/to/video.mp4
Model: gemini-2.0-flash
Prompt: "Describe what happens in this video"
FPS: 1.0
Output: Detailed scene-by-scene description
```

2. **Technical Analysis:**
```
Prompt: "Analyze the cinematography techniques, camera movements, and visual composition"
FPS: 2.0
Max Duration: 5.0
Temperature: 0.3
Output: Technical cinematography analysis
```

3. **Action Detection:**
```
Prompt: "List all actions performed by people in this video with timestamps"
FPS: 5.0
Process Audio: true
Output: Timestamped action list with audio cues
```

4. **Content Moderation:**
```
Prompt: "Identify any potentially inappropriate content, violence, or safety concerns"
Model: gemini-1.5-pro
FPS: 3.0
Temperature: 0.1
Output: Safety analysis report
```

5. **Tutorial Summarization:**
```
Prompt: "Create a step-by-step summary of this tutorial video"
Max Duration: 10.0
Max Output Tokens: 2048
Output: Structured tutorial steps
```

6. **Sports Analysis:**
```
Prompt: "Analyze the gameplay, tactics, and key moments in this sports clip"
FPS: 10.0
Process Audio: true
Output: Detailed sports commentary
```

**Best Practices:**
- Use lower FPS (0.5-1.0) for slow-paced content
- Use higher FPS (5.0-10.0) for action sequences
- Enable audio processing for videos with important sound
- Set appropriate max_duration based on video length
- Use lower temperature for factual descriptions
- Use higher temperature for creative interpretations
- For long videos, consider splitting into segments
- Test with different prompts for specific analysis needs

### 🌐 Unofficial API Call
Call unofficial/third-party APIs supporting Claude, GPT, Gemini and other models with automatic image generation support.

**Input Parameters:**
- `prompt` (STRING): The input text prompt
- `api_key` (STRING): Your API key for the service
- `api_format` (ENUM): API format selection
  - **"OpenAI Compatible"**: For Claude, GPT, and OpenAI-compatible APIs
  - **"Gemini Native"**: For Gemini native API format (supports image generation)
- `model` (STRING): Model name
  - Examples: claude-3-5-sonnet, gpt-4o, gemini-2.5-flash-image-preview
- `temperature` (FLOAT, 0.0-1.0, default: 0.7): Generation temperature
- `max_tokens` (INT, 64-8192, default: 1024): Maximum response length
- `base_url` (STRING): API base URL
  - OpenAI format example: https://api.example.com/v1
  - Gemini format example: https://ai.example.com
- `seed` (INT): Random seed for reproducibility
- `system_prompt` (STRING, optional): System instructions
- `image1-5` (IMAGE, optional): Up to 5 input images for multimodal requests
- `top_p` (FLOAT, 0.0-1.0, default: 0.95): Nucleus sampling
- `frequency_penalty` (FLOAT, -2.0-2.0, default: 0.0): Frequency penalty
- `presence_penalty` (FLOAT, -2.0-2.0, default: 0.0): Presence penalty

**Features:**
- **Dual API Format Support**: Switch between OpenAI and Gemini native formats
- **Automatic Image Extraction**: Extracts images from Gemini native API responses
- **Multi-Image Input**: Support for up to 5 reference images
- **Flexible Model Support**: Works with various third-party API providers
- **Complete API Debugging**: Full request/response logging

**Output:**
- `response` (STRING): Generated text response
- `image` (IMAGE): Generated/extracted image (if available)
- `api_request` (STRING): Complete API request (JSON)
- `api_response` (STRING): Complete API response (JSON)

**Usage Examples:**

1. **Claude API (OpenAI Compatible):**
```
API Format: OpenAI Compatible
Model: claude-3-5-sonnet-20241022
Base URL: https://api.anthropic.com/v1
Prompt: "Explain quantum computing"
```

2. **Gemini Image Generation (Native):**
```
API Format: Gemini Native
Model: gemini-2.5-flash-image-preview
Base URL: https://ai.juguang.chat
Prompt: "Generate a cyberpunk city at night"
Output: Text description + Generated image
```

3. **GPT with Images (OpenAI Compatible):**
```
API Format: OpenAI Compatible
Model: gpt-4-vision-preview
Base URL: https://api.openai.com/v1
Prompt: "What's in this image?"
Image1: [Upload image]
```

### 🌊 Unofficial Stream API Call
Stream responses from unofficial APIs with real-time output and support for both OpenAI and Gemini formats.

**Input Parameters:**
- Same as Unofficial API Call, plus:
- `stream` (BOOLEAN, default: true): Enable streaming mode

**Additional Features:**
- **Real-time Streaming**: See responses as they're generated
- **Stream Log Output**: Track streaming progress
- **Chunk Processing**: Handle partial responses efficiently
- **Image Streaming Support**: Extract images from streaming Gemini responses

**Output:**
- `response` (STRING): Complete streamed response
- `image` (IMAGE): Generated/extracted image (if available)
- `stream_log` (STRING): Streaming progress log
- `api_request` (STRING): Complete API request (JSON)
- `api_response` (STRING): Complete streaming metadata

**Best Practices:**
- Use Gemini Native format for image generation tasks
- Use OpenAI Compatible format for Claude, GPT, and similar APIs
- Enable streaming for long responses to see progress
- Set appropriate max_tokens based on expected response length
- Use system prompts to guide model behavior
- Test with different temperature values for optimal results

## Usage Examples

### Example 1: Extract Product Information
```
1. GeminiStructuredOutput → Define product schema
2. Input: Product description text
3. Output: Structured JSON with name, price, features
4. GeminiFieldExtractor → Extract just the price
5. Use price in downstream nodes
```

### Example 2: Batch Image Generation with Data
```
1. GeminiJSONExtractor → Extract image descriptions from text
2. GeminiFieldExtractor → Get descriptions array
3. GeminiImageGenAdvanced → Generate images for each description
4. Output: Batch of generated images
```

### Example 3: Video Analysis Pipeline
```
1. Load Video → GeminiVideoCaptioner
2. Caption → GeminiJSONExtractor (extract key moments)
3. Key moments → GeminiStructuredOutput (timeline format)
4. Output: Structured video timeline
```

### Example 4: Complex Data Processing
```
1. API Response → GeminiJSONParser (validate)
2. If valid → GeminiFieldExtractor (extract nested data)
3. Extracted data → GeminiStructuredOutput (reformat)
4. Output: Cleaned, restructured data
```

## Best Practices

### For Structured Output
- Keep schemas simple and focused
- Use required fields sparingly
- Test schemas with sample data first
- Provide clear property descriptions

### For Field Extraction
- Use specific paths to avoid ambiguity
- Set meaningful default values
- Test path syntax with sample JSON
- Use array handling options appropriately

### For Image Generation
- Provide detailed, specific prompts
- Use reference images when possible
- Keep batch sizes reasonable for memory
- Use negative prompts to improve quality

### For Video Analysis
- Keep videos under 30MB
- Use clear, specific analysis prompts
- Consider frame sampling for long videos
- Combine with structured output for data extraction

## Troubleshooting

### API Debugging
All processing nodes now include `api_request` and `api_response` outputs for debugging:
- **api_request**: Complete request sent to Gemini API (JSON format)
- **api_response**: Complete response from Gemini API (JSON format)

Use these outputs to:
- Debug API communication issues
- Understand exact request format
- Analyze response structure
- Track token usage and costs
- Identify rate limiting issues

### Common Issues

**API Key Errors:**
- Verify key is valid and active
- Check key has required permissions
- Ensure no extra spaces in key

**Model Access Issues:**
- Some models require specific access levels
- Check regional availability
- Verify model name spelling

**JSON/Schema Errors:**
- Validate JSON syntax before input
- Check schema follows JSON Schema spec
- Use simpler schemas if errors persist

**Memory Issues:**
- Reduce batch sizes
- Lower image resolutions
- Process videos in segments

**Field Extraction Issues:**
- Verify JSON is valid
- Check field path syntax
- Test with simpler paths first

## Requirements

- ComfyUI
- Python 3.8+
- google-genai
- Pillow (PIL)
- numpy
- torch
- opencv-python
- moviepy
- aiohttp

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

This project is based on code from [ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes) by filliptm. Special thanks for the original implementation.

### Enhancements include:
- Structured output support
- JSON processing capabilities
- Field extraction system
- Flexible model selection
- Improved error handling

## Acknowledgments

- Original code by [filliptm](https://github.com/filliptm)
- Based on [ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes)
- Maintained by [jqy-yo](https://github.com/jqy-yo)

## Support

For issues, questions, or contributions, please open an issue on GitHub.