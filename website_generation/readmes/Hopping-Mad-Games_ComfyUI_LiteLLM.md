# ComfyUI_LiteLLM

ComfyUI_LiteLLM is an addon for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that provides nodes for interacting with various language models using the [LiteLLM](https://github.com/BerriAI/litellm) library directly within the ComfyUI interface. This addon serves as a bridge between ComfyUI and LiteLLM, allowing you to leverage any model supported by LiteLLM in your ComfyUI workflows.

## Features

This addon provides ComfyUI nodes that interface with LiteLLM's functionality, including:

- `LiteLLMModelProvider`: Selects LiteLLM-supported models for use in other nodes
- `LiteLLMCompletion`: Generates completions using any LiteLLM-supported model
- `LiteLLMCompletionPrePend`: Similar to LiteLLMCompletion but with a pre-pended prompt
- `LiteLLMCompletionListOfPrompts`: Generates completions for a list of prompts
- `CreateReflectionFilter` and `FirstCodeBlockReflectionFilter`: Creates reflection filters for use with `LiteLLMCompletionWithReflectionFilter`
- `LiteLLMCompletionWithReflectionFilter`: Generates completions with a reflection filter
- `LiteLLMCompletionProvider`: Provides a completion function for use in other nodes
- `LiteLLMMessage`: Creates LiteLLM messages
- `ShowLastMessage` and `ShowMessages`: Display message content in the UI
- `ListToMessages` and `MessagesToList`: Convert between list and message formats
- `AppendMessages`: Combine multiple message sets
- `MessagesToText` and `TextToMessages`: Convert between text and message formats
- `LLLMInterpretUrl`: Fetch and process content from URLs

### **🚀 LightRAG Integration** 
Complete graph-based Retrieval-Augmented Generation with any LiteLLM model:
- **DocumentProcessor**: Process documents using LightRAG with any LiteLLM-supported model
- **QueryNode**: Query LightRAG knowledge graphs with multiple retrieval modes (naive, local, global, hybrid)
- **AgentMemoryProvider**: Create memory functions for LiteLLM agents
- **LinuxMemoryDirectory**: High-performance memory directory for faster processing
- **Local Embeddings**: Uses high-quality Stella 1.5B model locally (no OpenAI dependency)
- **Automatic Compatibility**: LiteLLM completion providers work seamlessly with LightRAG's async interface

## Supported Models

This addon supports all models that LiteLLM can interface with. This includes, but is not limited to:

- OpenAI models
- Anthropic models (Claude)
- Google models (PaLM, Gemini)
- Azure OpenAI
- AWS Bedrock models
- Cohere models
- AI21 models
- And many more

For the most up-to-date list of supported models, please refer to the [LiteLLM documentation](https://docs.litellm.ai/docs/).

## 🧠 LightRAG Integration - Graph-Based RAG with Any LLM

This addon features a **production-ready integration** between [LightRAG](https://github.com/HKUDS/LightRAG) (Graph-based Retrieval-Augmented Generation) and LiteLLM completion providers. Use any LiteLLM-supported model with LightRAG's powerful graph-based knowledge indexing and retrieval.

### 🎯 Key Features

- **🔄 Universal Model Support**: Use any LiteLLM model (OpenAI, Anthropic, Google, Kluster, etc.) with LightRAG
- **🏠 Local Embeddings**: High-quality Stella 1.5B model runs locally (no OpenAI API calls)
- **📊 Graph-Based Knowledge**: Build intelligent knowledge graphs from documents with entity and relationship extraction
- **🚀 Incremental Processing**: Add documents progressively while maintaining graph relationships
- **🔍 Multiple Query Modes**: naive, local, global, and hybrid retrieval strategies
- **💾 Persistent Storage**: Working directories maintain state across sessions
- **🧠 Agent Memory**: Seamless integration with LiteLLM agents for contextual memory
- **⚡ High Performance**: Linux memory directory support for faster processing

### 🔧 How It Works

The integration includes an **automatic compatibility wrapper** that bridges the gap between:
- **LiteLLM**: Synchronous `completion_function(prompt)` 
- **LightRAG**: Async `llm_func(prompt, system_prompt, history_messages, **kwargs)`

The wrapper intelligently combines system prompts, conversation history, and user prompts into the format expected by your chosen LLM.

### 📋 Available Nodes

| Node | Purpose | Key Features |
|------|---------|--------------|
| **DocumentProcessor** | Process documents into knowledge graphs | Chunking, entity extraction, relationship mapping |
| **QueryNode** | Query the knowledge graph | 4 retrieval modes, contextual responses |
| **AgentMemoryProvider** | Memory for LiteLLM agents | Query refinement, context retrieval |
| **LinuxMemoryDirectory** | High-speed storage | `/dev/shm` for faster processing |

### 🛠️ Example Workflows

**Basic Document Processing:**
```
LiteLLMModelProvider → LiteLLMCompletionProvider → DocumentProcessor
```

**Complete RAG Pipeline:**
```
LiteLLMModelProvider → LiteLLMCompletionProvider → DocumentProcessor → QueryNode
```

**Agent with Memory:**
```
DocumentProcessor → AgentMemoryProvider → [Your Agent Workflow]
```

### 🧪 Thoroughly Tested

- ✅ **Real API Integration**: Tested with actual Kluster API calls
- ✅ **Multi-Document Processing**: Handles incremental document addition
- ✅ **Cross-Document Queries**: Finds relationships across multiple documents  
- ✅ **State Persistence**: Working directories maintain state across sessions
- ✅ **Error Handling**: Robust error recovery and informative messages
- ✅ **No OpenAI Dependencies**: Local embeddings eliminate authentication errors

### 🔧 Local Embeddings Setup

**Requirements:**
```bash
pip install sentence-transformers
```

**DocumentProcessor Configuration:**
- `embedding_provider`: "local" (default - uses Stella 1.5B model)
- `embedding_model`: "NovaSearch/stella_en_1.5B_v5" (default)
- `embedding_dimension`: 1024 (recommended, options: 256-8192)
- `override_callable`: **REQUIRED** - Connect your LiteLLM completion provider

**Benefits:**
- ✅ High-quality embeddings (state-of-the-art MTEB scores)
- ✅ Complete privacy - no data sent to external APIs
- ✅ Fast local inference after initial model download (~3GB)
- ✅ No API costs for embeddings
- ✅ Works offline after setup

## Installation

### Manual Installation

1. Clone this repository into your `custom_nodes` directory in your ComfyUI installation.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Restart ComfyUI.

### Installation with ComfyUI-Manager

1. Add this addon's repository URL to your ComfyUI-Manager configuration.
2. Install the addon through ComfyUI-Manager.
3. Restart ComfyUI.

## Configuration

### Environment Variables (Recommended for Production)

For production use in ComfyUI, set your API keys as system environment variables:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
export KLUSTER_API_KEY="your-kluster-api-key"
# ... other API keys as needed
```

### Configuration Files

The addon uses a clean architecture that separates configuration from secrets:

- **`config.yaml`**: Contains non-sensitive settings like base URLs and paths. Never put API keys here.
- **`.env`**: Used only for testing and development. Not used in production ComfyUI.

### Environment Safety

This addon follows best practices for environment management:
- ✅ **Never pollutes global environment variables** - won't interfere with other ComfyUI custom nodes
- ✅ **Reads environment variables safely** - uses system environment first, falls back to `.env` for testing
- ✅ **No API keys in config files** - keeps secrets separate from configuration
- ✅ **Compatible with other node packs** - won't override API keys that other packages expect

### For Developers and Testing

If you're developing or testing, you can create a `.env` file in the addon directory:

```bash
# ComfyUI_LiteLLM/.env
OPENAI_API_KEY=your-test-key
KLUSTER_API_KEY=your-test-key
# etc.
```

This `.env` file is only used when system environment variables aren't available, making it perfect for development without affecting production deployments.

## Usage

After installation, the LiteLLM nodes will be available in the ComfyUI node editor under the "ETK/LLM/LiteLLM" category. You can use these nodes to integrate any LiteLLM-supported language model into your ComfyUI workflows.

### Basic LLM Usage:
1. Set up your API keys as system environment variables (see Configuration section above)
2. Select the desired model in the `LiteLLMModelProvider` node
3. Connect the nodes in your workflow

### LightRAG Document Processing:
1. **Install sentence-transformers**: `pip install sentence-transformers`
2. **Create workflow**: `LiteLLMModelProvider` → `LiteLLMCompletionProvider` → `DocumentProcessor`
3. **Connect completion provider** to DocumentProcessor's `override_callable` input (REQUIRED)
4. **Set embedding provider** to "local" for high-quality local embeddings
5. **First run** downloads Stella model (~3GB), then cached for future use

The addon will automatically use your environment variables for authentication without interfering with other ComfyUI custom nodes that may also use the same API services.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

### Running Tests

The addon includes comprehensive tests that can be run with:

```bash
cd ComfyUI_LiteLLM
python3 -m pytest tests/ -v
```

Tests use the `.env` file for API keys when available, or skip tests requiring real API calls if keys aren't configured.

## License

This addon is released under the [MIT License](LICENSE).

## Dependencies

- pyyaml
- addict
- litellm
- boto3
- lightrag-hku (for LightRAG graph-based RAG integration)
- sentence-transformers (for local embeddings with Stella 1.5B model)

For the full list of dependencies, please refer to the `requirements.txt` file.
