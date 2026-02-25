# ComfyUI Pinecone Prompt Upserter

A custom ComfyUI node for managing image generation prompts using Pinecone vector database with OpenAI embeddings. Features interactive approval with image preview for quality control.

## Features

- **Interactive Approval**: Visual preview with buttons before saving prompts
- **Automatic Trigger Word Sanitization**: Replaces character names (e.g., `Sarah01`) with `<trigger_word>` placeholder
- **Deduplication**: Prevents duplicate prompts using SHA256 hashing
- **Smart Memory**: Remembers decisions - only prompts first-time prompts
- **OpenAI Embeddings**: Uses `text-embedding-3-large` model (3072 dimensions)
- **Image Preview**: See generated image before deciding to save prompt
- **Beautiful UI**: Gradient buttons with hover animations in centered popup

## Prerequisites

- Python 3.8+
- ComfyUI installation
- OpenAI API key
- Pinecone account with an index created (3072 dimensions)

## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd /path/to/ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/Hearmeman24/ComfyUI-Pinecone.git
```

3. Install dependencies:
```bash
cd ComfyUI-Pinecone
pip install -r requirements.txt
```

4. Set environment variables:
```bash
export OPENAI_API_KEY=your_openai_api_key_here
export PINECONE_API_KEY=your_pinecone_api_key_here
```

5. Restart ComfyUI

## Usage

1. In ComfyUI, add the **Pinecone Prompt Upserter** node to your workflow (found under `prompt_management` category)

2. Connect inputs:
   - **image** (optional): Connect the generated image output to see it during approval
   - **prompt_text**: The prompt used (connect from prompt node)
   - **model_name**: Name of the model (e.g., "flux", "qwen", "wan", "sdxl")
   - **index_name**: Your Pinecone index name (default: "prompts")
   - **pinecone_api_key** (optional): Your Pinecone API key (uses env var if empty)
   - **openai_api_key** (optional): Your OpenAI API key (uses env var if empty)

3. How it works:

   **First Time Seeing a Prompt:**
   - Workflow pauses when it reaches the node
   - Popup appears automatically showing the generated image
   - Two buttons below image: **"Insert to Index"** (green) and **"Cancel"** (red)
   - Make your decision based on the image quality
   - Popup closes and workflow continues

   **Subsequent Runs with Same Prompt:**
   - Node recognizes the prompt instantly
   - Silently skips without interrupting
   - No popup, no pause - smooth workflow execution

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Required for generating embeddings
- `PINECONE_API_KEY`: Required for accessing Pinecone index
- `INDEX_NAME`: Optional, defaults to "prompts"

### Pinecone Index Setup

Make sure your Pinecone index is configured with:
- **Dimensions**: 3072 (for `text-embedding-3-large`)
- **Metric**: cosine (recommended for text embeddings)

Example index creation:
```python
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="your_api_key")
pc.create_index(
    name="prompts",
    dimension=3072,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)
```

## Metadata Structure

Each prompt stored in Pinecone includes:
- `text`: The full prompt text (with trigger words sanitized)
- `model`: The model name you specify (e.g., "flux", "qwen", "wan", "sdxl")
- `prompt_hash`: SHA256 hash for deduplication

## Trigger Word Sanitization

The node automatically replaces character-specific trigger words with a generic placeholder:
- **Pattern**: `Name01` (capital letter + letters + "01")
- **Examples**: `Sarah01`, `Onyx01`, `MaryJane01`
- **Result**: All replaced with `<trigger_word>`
- **Purpose**: Maintains consistency and allows flexible character substitution

## Deduplication

Prompts are deduplicated using SHA256 hashing of normalized text (lowercase, stripped whitespace):
- **First time**: Popup appears for approval
- **Already seen**: Silently skips (no interruption)
- **Already in Pinecone**: Won't duplicate even if approved again

## Preview Features

- **Auto-Appear**: Popup automatically displays when a new prompt is detected
- **Image Display**: Large centered preview (up to 90% of viewport)
- **Styled Buttons**: Gradient green (Insert) and red (Cancel) with hover animations
- **Manual Re-display**: Click "📷 Show Preview" on node if you close the popup
- **One-Click Decision**: See image and click choice in single popup window

## Troubleshooting

### "API key not found" error
- Ensure environment variables are set before starting ComfyUI
- Alternatively, provide API keys directly in the node inputs

### "Index not found" error
- Verify your Pinecone index name matches your configuration
- Ensure the index exists and has 3072 dimensions

### Node not appearing in ComfyUI
- Restart ComfyUI completely after installation
- Check console for errors
- Verify dependencies installed in correct Python environment

### Preview popup not appearing
- Check browser console for JavaScript errors
- Ensure you're connecting an image to the node's image input
- Try clicking "📷 Show Preview" button manually

### Dimension mismatch error
- Pinecone index must be created with **3072 dimensions**
- This matches OpenAI's `text-embedding-3-large` model

## License

MIT License
