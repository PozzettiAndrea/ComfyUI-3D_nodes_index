# ComfyUI GroqNodes
A comprehensive ComfyUI extension for the Groq API with support for chat, vision, audio transcription, tool use, and batch processing.

## Features
- Chat Node: Text generation with conversation history support
- Vision Node: Image analysis with multi-image batch support
- Audio Node: Audio transcription with timing metadata
- Tool Use Node: Structured function calling with JSON schema validation
- Batch Node: Concurrent request processing with progress tracking

## Installation
1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-GroqNodes.git
```

2. Install dependencies:
```bash
cd ComfyUI-GroqNodes
pip install -r requirements.txt
```

3. Set your Groq API key (choose one method):
Option A: Using .env file (recommended)
```bash
cp .env.example .env
# Edit .env and add your API key
```

Option B: Using environment variable
```bash
export GROQ_API_KEY="your_api_key_here"
```

**Option C: Direct input**
Provide the API key directly in each node's interface.

## Usage
### Basic Chat Example
1. Add a "Groq Chat" node to your workflow
2. Configure the model and parameters
3. Connect a text input for your prompt
4. Execute to get the response

### Vision Example
1. Load an image using ComfyUI's image loader
2. Add a "Groq Vision" node
3. Connect the image and provide a prompt
4. Execute to analyze the image

### Audio Transcription Example
1. Add a "Groq Audio" node
2. Provide the path to an audio file
3. Execute to get the transcription

## Configuration
Model configurations are stored in `configs/models.json`. You can modify this file to add or update available models.

## Requirements
- Python 3.8+
- ComfyUI
- Groq API key (get one at https://console.groq.com)
