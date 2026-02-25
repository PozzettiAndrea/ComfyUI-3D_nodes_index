# ComfyUI-API-Manager
A LLM API key management solution for ComfyUI with automatic load balancing support.

## Features

- **Centralized API Key Management**: Store and manage API keys for multiple AI services
- **Load Balancing**: Automatically rotate between multiple API keys for the same service
- **Pre-configured Providers**: Built-in support for 22+ AI services (OpenAI, Anthropic, DeepSeek, etc.)
- **Custom Hosts**: Override default API endpoints when needed
- **Easy Integration**: Simple string outputs for seamless integration with other nodes

## Installation

1. Clone or download this repository into your `ComfyUI/custom_nodes/` directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/1038lab/comfyui-api-manager
```

2. Restart ComfyUI

## Usage

### 1. Add API Keys (API Manager Node)

1. Add the **API Manager** node to your workflow
2. Configure:
   - **Action**: Choose `add_or_update` or `delete`
   - **Service**: Select from pre-configured providers
   - **Profile Name**: Give your configuration a name (e.g., "my_openai")
   - **API Keys**: Enter one or more keys separated by commas (keys will be masked)
   - **Custom Host** (optional): Override the default API endpoint
3. Run the workflow (Queue Prompt)
4. **Keys are automatically cleared** after execution for security
5. The API Manager node can be safely kept in your workflow or deleted

### 2. Use API Keys (API Service Node)

1. Add the **API Service** node to your workflow
2. Click the **Refresh Profiles** button to load available profiles
3. Select your profile from the dropdown
4. Connect the `api_key` and `host` outputs to your LLM/API nodes
5. (Optional) Use **override_host** to temporarily use a different endpoint

## Load Balancing

When multiple API keys are configured for a profile, the node automatically rotates through them using round-robin:

- First execution: Uses key 1
- Second execution: Uses key 2
- Third execution: Uses key 3
- Fourth execution: Back to key 1

The rotation state resets when ComfyUI restarts.

## Supported Providers

### International
- OpenAI, Anthropic, Google, Groq, Mistral, Together AI
- Replicate, Stability AI, Cohere, Fireworks AI
- OpenRouter, HuggingFace

### China Mainland
- DeepSeek, ZhipuAI (BigModel), Baidu (文心)
- DashScope (阿里云), Hunyuan (腾讯), XFYun (讯飞)
- Baichuan, MiniMax, Moonshot (月之暗面), Doubao (豆包/字节)

## Security Features

- **Auto-Clear**: API keys are automatically cleared from the node after execution
- **No Serialization**: API keys are never saved to workflow.json files
- **Password Display**: Keys are displayed as masked input for visual security
- **Safe Sharing**: Workflows can be safely shared without exposing API keys
- API keys are stored locally in `profiles.json` (consider file system permissions)
- Rotation index is stored in memory and resets on restart

- Created by: [AILab](https://github.com/1038lab)

If this custom node helps you or you like my work, please give me ⭐ on this repo! It's a great encouragement for my efforts!

## License
GPL-3.0 License

