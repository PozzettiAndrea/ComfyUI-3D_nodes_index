# ComfyUI Ollama Model Manager

Custom nodes for managing [Ollama](https://ollama.com/) models in ComfyUI workflows. Load and unload models on-demand to optimize memory usage in constrained environments.

## Features

- 🔄 **Auto-Fetch Models** - Models load automatically when you connect nodes (no workflow execution needed!)
- 💬 **Chat Completion** - Full text generation with conversation history
- 🔄 **Dynamic Dropdowns** - Model list updates instantly via ComfyUI API
- 🎯 **Type-Safe Connections** - Client config passed between nodes
- ⬇️ **Load/Unload Models** - Control memory usage efficiently
- 📋 **Beautiful Logging** - Colored console output with JSON file logs
- 💾 **Model Caching** - Per-endpoint caching for better performance
- ✨ **No CORS Issues** - Backend API proxy eliminates browser restrictions

## Installation

### Recommended: ComfyUI-Manager

1. Install via [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "Ollama Manager"
3. Click Install

### Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/darth-veitcher/comfyui-ollama-model-manager
cd comfyui-ollama-model-manager

# Install dependencies (auto-detects uv or uses pip)
python install.py

# OR manually with uv (recommended)
uv pip install httpx loguru rich

# OR manually with pip
pip install httpx loguru rich
```

For portable ComfyUI installations:

```bash
# Windows Portable
ComfyUI\python_embeded\python.exe install.py

# Or manually
ComfyUI\python_embeded\python.exe -m pip install httpx loguru rich
```

## 🎯 Quick Start Guide

### Step 1: Add Ollama Client

1. Add an **Ollama Client** node to your workflow
2. Set `endpoint` to your Ollama server URL
   - Default: `http://localhost:11434`
   - Or use your remote server URL

### Step 2: Add Model Selector

1. Add an **Ollama Model Selector** node
2. Connect the `client` output from **Ollama Client** to the `client` input
3. **✨ Models auto-fetch immediately!** - No need to execute the workflow
4. Select your desired model from the dropdown

### Step 3: Load the Model

1. Add an **Ollama Load Model** node
2. Connect `client` from **Model Selector**
3. The model dropdown auto-populates with available models
4. Set `keep_alive` (default `-1` keeps it loaded)
5. Execute the workflow to load the model

### Step 4: Generate Text with Chat

1. Add an **Ollama Chat Completion** node
2. Connect `client` from **Model Selector** (model auto-populates)
3. Enter your prompt in the `prompt` field
4. (Optional) Add a `system_prompt` to control behavior
5. Execute to generate a response!

**Example:**
- **prompt**: "Write a haiku about programming"
- **system_prompt**: "You are a helpful assistant"
- **response**: Returns the generated text
- **history**: Returns the conversation (for multi-turn chat)

### Step 5: Multi-Turn Conversations (Optional)

For conversations with memory:

1. Connect the `history` output from one **Chat Completion** node
2. To the `history` input of the next **Chat Completion** node
3. Each response remembers the previous messages

### Step 6: Unload When Done (Optional)

1. Add an **Ollama Unload Model** node
2. Connect it after your processing
3. This frees up memory

## Nodes Reference

### Core Nodes

| Node | Description |
|------|-------------|
| **Ollama Client** | Creates a reusable Ollama connection config |
| **Ollama Model Selector** | Select model with auto-fetch on connection |
| **Ollama Load Model** | Loads a model into Ollama's memory |
| **Ollama Chat Completion** | Generate text with conversation history |
| **Ollama Unload Model** | Unloads a model to free memory |

### Debug/Utility Nodes

| Node | Description |
|------|-------------|
| **Ollama Debug: History** | Formats conversation history as readable text for inspection |
| **Ollama Debug: History Length** | Returns the number of messages in conversation history |

### Option Nodes (Composable Parameters)

| Node | Parameter | Range/Type | Default | Description |
|------|-----------|------------|---------|-------------|
| **Temperature** | `temperature` | 0.0-2.0 | 0.8 | Controls randomness (0=deterministic, 2=very random) |
| **Seed** | `seed` | INT | 42 | Random seed for reproducible generation |
| **Max Tokens** | `max_tokens` | 1-4096 | 128 | Maximum tokens to generate |
| **Top P** | `top_p` | 0.0-1.0 | 0.9 | Nucleus sampling threshold |
| **Top K** | `top_k` | 1-100 | 40 | Top-k sampling (Ollama-specific) |
| **Repeat Penalty** | `repeat_penalty` | 0.0-2.0 | 1.1 | Penalty for repetition (Ollama-specific) |
| **Extra Body** | `extra_body` | JSON | {} | Advanced parameters (num_ctx, num_gpu, etc.) |

## Advanced Usage

The architecture provides a clean, composable workflow:

```text
[Ollama Client] → [Model Selector] → [Load Model] → [Chat Completion] → [Unload Model]
       ↓               ↓                   ↓                ↓
  (endpoint)     (pick model,        (load with)      (generate text,
                  auto-refresh)       keep_alive)      track history)
```

**Key Benefits:**

- **Reusable Client**: Create one client, connect to multiple nodes
- **Auto-refresh**: Model Selector can refresh the list automatically
- **Type Safety**: Client connection passed between nodes
- **Cleaner Workflows**: Less redundant endpoint configuration
- **Dynamic Dropdowns**: Model list automatically populates after refresh
- **Conversation Memory**: History passed between chat nodes for multi-turn conversations

**Example Workflow: Simple Chat**

```text
1. Ollama Client (endpoint: http://localhost:11434)
       ↓
2. Model Selector (model: "llama3.2", refresh: true)
       ↓
3. Load Model (keep_alive: "-1")
       ↓
4. Chat Completion (prompt: "Hello!")
       ↓
5. Unload Model
```

**Example Workflow: Multi-Turn Conversation**

```text
1. [Client] → [Selector] → [Load] → [Chat 1: "My name is Alice"]
                                          ↓ (history)
                                    [Chat 2: "What's my name?"]
                                          ↓ (history)
                                    [Chat 3: "Tell me a joke"]
       ↓
2. Unload Model
```

**Example Workflow: Chat with Options**

```text
[Client] → [Selector] → [Load Model]
                           ↓
       ┌───────────────────┴────────────────────┐
       ↓                   ↓                     ↓
[Temperature=0.7]    [Seed=42]          [MaxTokens=200]
       └───────────────────┬────────────────────┘
                           ↓ (merged options)
                   [Chat Completion]
                           ↓
                    "Deterministic response"
```

**Example Workflow: Advanced Parameters**

```text
[Temperature=0.8] → [TopK=50] → [RepeatPenalty=1.2] → [ExtraBody]
                                                           ↓
                                                    {"num_ctx": 4096}
                                                           ↓
                                                    [Chat Completion]
```

This pattern optimizes memory by unloading models when not needed, while maintaining full conversation context and precise control over generation parameters.

## Configuration

### Ollama Endpoint

Default: `http://localhost:11434`

Override by specifying a different endpoint in the "Refresh Model List" or "Load/Unload" nodes.

### Keep Alive

Control how long models stay in memory:

- `-1` (default): Keep loaded indefinitely
- `5m`: Keep for 5 minutes
- `1h`: Keep for 1 hour
- `0`: Unload immediately

### Chat Parameters

The **Ollama Chat Completion** node supports:

**Required:**
- `client` - Ollama client connection
- `model` - Model name (auto-populated from selector)
- `prompt` - User message/question

**Optional:**

- `system_prompt` - Instructions to guide model behavior
- `history` - Previous conversation (for multi-turn chat)
- `options` - Generation parameters (temperature, seed, etc.)
- `format` - Output format: "none" (default, text) or "json" (structured JSON)
- `image` - Image input for vision models

**Outputs:**

- `response` - Generated text
- `history` - Updated conversation (connect to next chat node)

**Caching & Performance:**

The chat node intelligently caches results to avoid unnecessary LLM calls:

- **With Seed**: When you provide a seed via the `OllamaOptionSeed` node, identical inputs will be cached (like standard ComfyUI nodes). This prevents wasteful re-execution when re-running the same workflow.
- **Without Seed**: When no seed is provided, the node will always re-execute to generate fresh, non-deterministic responses.

**Example: Deterministic workflow with caching**
```text
[Seed=42] → [Chat Completion] → Output
              ↓
        (Cached on re-run!)
```

This matches ComfyUI's standard behavior and significantly reduces API costs when iterating on workflows.

### JSON Mode (Phase 3)

The **format** parameter enables structured output for workflows that need parseable data:

**Example: Extract structured data**

```text
[Chat Completion]
├── format: "json"
├── prompt: "Extract person data: 'Alice is 30 years old'"
└── system_prompt: "Return JSON with keys: name, age"

Output: {"name": "Alice", "age": 30}
```

**When to use JSON mode:**
- Data extraction workflows
- Structured output for downstream processing
- API integrations requiring JSON
- ComfyUI workflows that parse the response

**Note:** Set `format` to "json" to enable. The model will ensure valid JSON output.

### Debug Utilities (Phase 3)

**Ollama Debug: History** - Inspect conversation memory

```text
[Chat History] → [Debug: History]
                      ↓
           Formatted Text Output:
           === Conversation History (3 messages) ===

           [1] SYSTEM:
               You are helpful

           [2] USER:
               Hello

           [3] ASSISTANT:
               Hi there!
```

**Ollama Debug: History Length** - Count messages

```text
[Chat History] → [History Length] → Output: 5 (messages)
```

**Use cases:**
- Debugging conversation flow
- Monitoring context length
- Workflow conditional logic based on message count
- Understanding what the model "remembers"

## Logging

Logs are written to:
- **Console**: Colored output with timestamps
- **File**: `logs/ollama_manager.json` (14-day retention, compressed)

Example log output:
```
08:36:30 | INFO     | refresh-abc123 | 🔄 Refreshing model list from http://localhost:11434
08:36:30 | INFO     | refresh-abc123 | ✅ Model list refreshed: 3 models available
08:36:31 | INFO     | load-def456    | ⬇️  Loading model 'llava:latest' (keep_alive=-1)
08:36:32 | INFO     | load-def456    | ✅ Model 'llava:latest' loaded successfully
```

## Requirements

- Python ≥3.12
- httpx ≥0.28.1
- loguru ≥0.7.3
- rich ≥14.2.0
- [Ollama](https://ollama.com/) running locally or remotely

## Development

### Project Structure

```text
comfyui-ollama-model-manager/
├── __init__.py              # ComfyUI entry point
├── install.py               # Dependency installer (uv/pip auto-detect)
├── pyproject.toml           # Package metadata & dependencies
├── src/
│   └── comfyui_ollama_model_manager/
│       ├── __init__.py      # Package init
│       ├── nodes.py         # Model management nodes
│       ├── chat.py          # Chat completion node
│       ├── types.py         # Custom type definitions
│       ├── ollama_client.py # API client (fetch, load, unload, chat)
│       ├── api.py           # ComfyUI API routes
│       ├── state.py         # Model cache
│       ├── log_config.py    # Logging setup
│       └── async_utils.py   # Async utilities
├── tests/                   # Pytest test suite (52 tests)
└── web/
    └── ollama_widgets.js    # Auto-fetch UI logic
```

### Running Tests

```bash
# With uv (recommended)
uv run pytest

# Or with pip
pip install pytest pytest-asyncio
pytest
```

## Troubleshooting

### Nodes don't appear in ComfyUI

1. Check that dependencies are installed: `pip list | grep -E "httpx|loguru|rich"`
2. Restart ComfyUI completely
3. Check ComfyUI console for error messages
4. Verify Ollama is running: `curl http://localhost:11434/api/tags`

### Import errors

If you see `ModuleNotFoundError`, install dependencies manually:
```bash
pip install httpx loguru rich
```

### Permission errors (Windows)

Close ComfyUI and run:
```bash
ComfyUI\python_embeded\python.exe -m pip install --upgrade httpx loguru rich
```

## License

[Add your license here]

## Credits

- Built for [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- Uses [Ollama](https://ollama.com/) API
