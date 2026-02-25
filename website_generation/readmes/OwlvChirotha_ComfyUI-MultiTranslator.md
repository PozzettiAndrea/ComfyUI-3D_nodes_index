# ComfyUI Translator Nodes
ComfyUI plug-in collection of basic translator, LLM translator and a series of LLM Service Connectors.

## Node List

### 1. Basic Translator
Supports traditional machine translation services: Google/Baidu/Youdao/Tencent

### 2. LLM Translator
High-quality translation powered by Large Language Models, works with:
- **Load LLM Model** - Load local LLM models
- **General LLM Service Connector** - OpenAI-compatible API gateway connector (private gateway support)
- **Dedicated Service Connectors** - Provider-specific connectors:
  - SiliconFlow Service Connector
  - ZhiPu Service Connector
  - DeepSeek Service Connector
  - Kimi Service Connector
  - Gemini Service Connector
  - ChatGPT Service Connector
- **Ollama LLM Connector** - Call models via Ollama

## Features

### Basic Translator
- **Multiple Translation Services**: Google Translate, Baidu Translate, Youdao Translate, Tencent Translate
- **Text Input**: Supports multi-line text input, manual input or upstream node connection
- **Target Language Selection**: Dropdown menu with 10 common languages
- **API Key Configuration**: Optional API key input for domestic services
- **Error Handling**: Comprehensive exception handling

### LLM Translator
- **Multiple Providers**: 9 mainstream LLM providers including OpenAI, Claude, DeepSeek, Qwen, Grok
- **Local Model Support**: Load locally deployed large language models
- **Ollama Integration**: Call local or remote models via Ollama
- **Flexible Configuration**: Customizable system prompts and model parameters

## Supported Languages

- English
- Chinese (中文)
- Japanese (日本語)
- Korean (한국어)
- French (Français)
- German (Deutsch)
- Spanish (Español)
- Italian (Italiano)
- Russian (Русский)
- Portuguese (Português)

## Installation

### Method 1: Manual Installation

1. Copy the entire folder to ComfyUI's `custom_nodes` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Restart ComfyUI.

### Method 2: Git Clone

1. Navigate to ComfyUI's `custom_nodes` directory.
2. Clone the repository:
   ```bash
   git clone https://github.com/OwlvChirotha/ComfyUI-Translator.git
   ```
3. Install dependencies:
   ```bash
   pip install -r ComfyUI-Translator/requirements.txt
   ```
4. Restart ComfyUI.

### Method 3: ComfyUI Manager

1. Open ComfyUI Manager and search for `ComfyUI-Translator`.
2. Install the plugin through the Manager interface.
3. Restart ComfyUI to load the newly installed nodes.

## Usage

### Basic Translator Guide

1. Find "Text Processing" category in ComfyUI node menu
2. Add "Basic Translator" node to workflow
3. Input text to translate (manual or from upstream node)
4. Select target language
5. Choose translation service
6. Execute workflow to get translation result

#### Translation Service Configuration

##### Google Translate
- **Environment**: International network
- **Requirements**: No configuration needed
- **Note**: Requires proxy in mainland China

##### Baidu Translate (Recommended for China)
- **Environment**: Mainland China network
- **Free Quota**: 2 million characters/month
- **Apply**: https://fanyi-api.baidu.com/
- **Setup**:
  1. Register Baidu account and login
  2. Create application to get App ID and Secret Key
  3. Fill in `baidu_app_id` and `baidu_secret_key` in node

##### Youdao Translate (Recommended for China)
- **Environment**: Mainland China network
- **Free Quota**: Daily free API calls
- **Apply**: https://ai.youdao.com/
- **Setup**:
  1. Register Youdao AI Cloud account
  2. Create application to get App ID and Secret
  3. Fill in `youdao_app_id` and `youdao_secret_key` in node

### LLM Translator Guide

#### Method 1: Cloud LLM Services

**Option A: General LLM Service Connector** (for private gateways & OpenAI-compatible APIs)
1. Add "General LLM Service Connector" node
2. Enter API endpoint URL (default: https://api.openai.com/v1/chat/completions)
   - For private gateways: http://your-gateway-url/v1/chat/completions
   - For vLLM: http://localhost:8000/v1/chat/completions
   - For any OpenAI-compatible service
3. Fill in API key (password protected)
4. Select model from dropdown or enter custom model name
5. Connect to "LLM Translator" node

Use Cases:
- Private/internal LLM deployments (vLLM, FastChat, Text Generation WebUI)
- Enterprise API gateways
- OpenAI-compatible proxy services
- Custom LLM endpoints

**Option B: Dedicated Service Connectors** (provider-specific, recommended)
1. Add specific connector node:
   - **ChatGPT Service Connector** - OpenAI GPT models (gpt-4o, gpt-4o-mini, gpt-4-turbo, o1, etc.)
   - **DeepSeek Service Connector** - DeepSeek models (deepseek-chat, deepseek-v3, deepseek-r1, etc.)
   - **Kimi Service Connector** - Moonshot Kimi models (moonshot-v1-8k/32k/128k, kimi-v1)
   - **ZhiPu Service Connector** - Zhipu GLM models (glm-4, glm-4v, glm-3-turbo)
   - **Gemini Service Connector** - Google Gemini models (gemini-1.5-pro/flash, gemini-2.0-flash-exp)
   - **SiliconFlow Service Connector** - Multiple models via SiliconFlow API
2. Select model from provider-specific dropdown
3. (Optional) Enter custom model ID for unlisted models
4. Fill in API key (password protected)
5. Connect to "LLM Translator" node
6. Input text and target language
7. Execute translation

Benefits of Dedicated Connectors:
- Only shows models supported by selected provider
- Easier model selection without confusion
- Clearer workflow organization

#### Method 2: Local Models

1. Add "Load LLM Model" node
2. Select model source:
   - ComfyUI models/LLM directory
   - Custom directory (absolute path)
3. Connect to "LLM Translator" node
4. Execute translation

#### Method 3: Ollama

1. Add "Ollama LLM Connector" node
2. Configure Ollama host (default http://localhost:11434)
3. Specify model name (e.g., llama3:8b, qwen2:7b)
4. Connect to "LLM Translator" node
5. Execute translation

## Technical Implementation

### Basic Translator
- **Google Translate**: Uses googletrans library, free but requires international network
- **Baidu Translate**: Official API, MD5 signature authentication
- **Youdao Translate**: Official API, SHA256 signature authentication
- **Auto Language Detection**, comprehensive error handling

### LLM Translator
- **Unified Interface**: Supports 9 mainstream LLM providers
- **Real API Calls**: Integrated with official APIs
- **Local Model Support**: Reserved interface for local model loading
- **Ollama Integration**: Supports local/remote Ollama calls

## Notes

### Network Environment
- **Mainland China Users**: For Basic Translator, use Baidu/Youdao; for LLM, use DeepSeek/Qwen or other domestic services
- **International Users**: Can use Google Translate and OpenAI/Claude or other international services
- **Stable network connection required**

### API Configuration
- API keys are password-protected in UI (not displayed in plain text)
- Clear API keys before sharing workflows to avoid leakage
- Keep API keys secure

### Usage Limits
- Each translation service has rate limits and quotas
- May require payment after free quota is exhausted
- Use responsibly, avoid frequent calls

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

- You may use, modify, and redistribute this project under the terms of the GPL-3.0.
- Any derivative works must also be distributed under the GPL-3.0.
- A full copy of the license is provided in the `LICENSE` file or at <https://www.gnu.org/licenses/gpl-3.0.en.html>.



