# ComfyUI Google Image Search Node

A custom node for ComfyUI that enables Google Image Search functionality, allowing you to search and retrieve images directly within your workflows.

## Features

- Search Google Images with any query
- Returns the first image result as a ComfyUI-compatible tensor
- Automatic image format conversion and handling
- Error handling with visual feedback
- Simple integration with existing ComfyUI workflows

## Prerequisites

Before using this node, you need to set up Google Custom Search API:

1. **Enable Google Custom Search API**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the "Custom Search API"
   - Create credentials (API Key)

2. **Create a Custom Search Engine**:
   - Visit [Google Custom Search Engine](https://cse.google.com/cse/)
   - Create a new search engine
   - In settings, enable "Image search"
   - Enable "Search the entire web"
   - Note your Search Engine ID (cx parameter)

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-Google-Image-Search
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API credentials:
```bash
cd ComfyUI-Google-Image-Search
cp config.json.example config.json
# Edit config.json with your API key and Search Engine ID
```

4. Restart ComfyUI

## Configuration

Create a `config.json` file in the node directory with your credentials:

```json
{
    "api_key": "your_google_api_key_here",
    "search_engine_id": "your_search_engine_id_here"
}
```

## Usage

1. Add the "Google Image Search" node to your workflow
2. Type your search query
3. The node will output an image tensor that can be connected to any image input

### Input Parameters

- **search_query**: The search term (default: "cat")

### Output

- **IMAGE**: A tensor containing the first image result from Google

## Error Handling

The node includes comprehensive error handling:
- Missing config.json or credentials show a red error image
- Failed searches return a red indicator image
- All errors are logged to the console for debugging

## API Limits

Be aware of Google's API quotas:
- Free tier: 100 searches per day
- Each search counts against your daily quota
- Consider implementing caching for repeated searches

## Security Notes

- Never commit your config.json file to version control (it's in .gitignore)
- Keep your config.json file secure with appropriate file permissions
- The example file (config.json.example) can be safely committed

## Troubleshooting

- **Red output image**: Check that config.json exists and has valid credentials
- **Config not found**: Copy config.json.example to config.json and add your credentials
- **No results**: Verify your search engine has image search enabled
- **Quota exceeded**: You've hit the daily API limit

## Requirements

- ComfyUI
- Google Cloud account with Custom Search API enabled
- Python packages listed in requirements.txt

## License

MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.