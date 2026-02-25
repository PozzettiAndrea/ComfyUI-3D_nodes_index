# ComfyUI Llama.cpp Client Node

A comprehensive ComfyUI custom node that provides complete client functionality for **llama-server** from [llama.cpp](https://github.com/ggml-org/llama.cpp). This node acts as a bridge between ComfyUI workflows and llama-server instances, supporting **every single parameter and endpoint** that llama-server offers.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![ComfyUI](https://img.shields.io/badge/ComfyUI-compatible-orange.svg)
![llama.cpp](https://img.shields.io/badge/llama.cpp-compatible-red.svg)

## 🎯 What This Repository Does

This repository provides a **single, powerful ComfyUI node** that can communicate with any llama-server instance and utilize all of its capabilities within ComfyUI workflows. Instead of being limited to basic text generation, you get access to:

- **8 Complete API Endpoints**: Every llama-server endpoint with full parameter support
- **100+ Parameters**: Every single parameter that llama-server accepts
- **Advanced AI Features**: Function calling, multimodal processing, structured output, and more
- **Production Ready**: Error handling, authentication, caching, and performance optimization
- **Plug & Play**: Easy integration into existing ComfyUI workflows

## 🚀 Key Capabilities

### **Complete API Coverage**
| Endpoint | Purpose | What You Can Do |
|----------|---------|-----------------|
| `/completion` | Text generation | Stories, articles, creative writing, Q&A |
| `/v1/chat/completions` | Chat conversations | Multi-turn conversations, roleplay, assistants |
| `/v1/embeddings` | Text embeddings | Semantic search, clustering, similarity analysis |
| `/tokenize` | Text analysis | Token counting, text preprocessing |
| `/detokenize` | Token conversion | Debug tokenization, convert tokens back |
| `/apply-template` | Chat formatting | Test chat templates, format conversations |
| `/infill` | Code completion | Fill-in-the-middle coding, code assistance |
| `/v1/rerank` | Document ranking | Search relevance, document sorting |

### **Advanced Sampling Methods**
- **DRY Sampling**: Eliminates repetition with smart sequence detection
- **XTC Sampling**: Cross-token coherence for better consistency  
- **Mirostat**: Perplexity-based sampling for controlled creativity
- **Dynamic Temperature**: Adaptive temperature that changes during generation
- **Custom Sampler Chains**: Define your own sampling pipeline

### **Structured Output & Constraints**
- **JSON Schema**: Force valid JSON output with custom schemas
- **BNF Grammar**: Use formal grammars to constrain generation
- **Logit Bias**: Fine-tune token probabilities for specific words/concepts
- **Stop Sequences**: Precise control over when generation stops

### **Multimodal & Function Calling**
- **Vision Models**: Process images with base64 encoding
- **Function Calling**: Let models call tools and functions
- **Tool Integration**: OpenAI-compatible function definitions
- **Image References**: Embed images directly in prompts

### **Performance & Production Features**
- **KV Cache Management**: Reuse computations between requests
- **Slot Management**: Handle concurrent requests efficiently  
- **LoRA Adapters**: Dynamic model adaptation per request
- **Streaming**: Real-time token generation
- **Authentication**: API key support for secure deployments

## 📦 Installation

### Prerequisites
- ComfyUI installed and running
- llama-server (from llama.cpp) running somewhere accessible
- Python 3.7+ with pip

### Install the Node

1. **Clone into ComfyUI custom nodes**:
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/fidecastro/comfyui-llamacpp-client.git
   ```

2. **Install dependencies**:
   ```bash
   cd comfyui-llamacpp-client
   pip install -r requirements.txt
   ```

3. **Restart ComfyUI** - The node will appear in `AI/LlamaCpp` category

### Start Your llama-server

For basic functionality:
```bash
./llama-server -m your-model.gguf -c 4096 --host 0.0.0.0 --port 8080
```

For all features:
```bash
./llama-server -m your-model.gguf -c 4096 \
  --host 0.0.0.0 --port 8080 \
  --slots --metrics --props \
  --embedding --reranking
```

## 🛠️ Quick Start Examples

### Basic Text Generation
```
Endpoint: completion
Server URL: http://127.0.0.1:8080
Prompt: "Write a short story about a robot learning to paint"
Temperature: 0.8
N Predict: 200
```

### Creative Writing with Advanced Sampling
```
Endpoint: completion
Prompt: "Chapter 1: The Last Library"
Temperature: 1.0
Dynamic Temperature Range: 0.4
DRY Multiplier: 0.8
XTC Probability: 0.1
Repeat Penalty: 1.05
```

### Structured JSON Output
```
Endpoint: completion  
Prompt: "Generate a product review for a laptop"
JSON Schema: {
  "type": "object",
  "properties": {
    "rating": {"type": "integer", "minimum": 1, "maximum": 5},
    "title": {"type": "string"},
    "pros": {"type": "array", "items": {"type": "string"}},
    "cons": {"type": "array", "items": {"type": "string"}},
    "summary": {"type": "string"}
  }
}
```

### Chat Conversation
```
Endpoint: chat_completions
System Message: "You are a helpful coding tutor"
User Message: "Explain recursion with a simple Python example"
Temperature: 0.3
Max Tokens: 300
```

### Code Completion
```
Endpoint: infill
Input Prefix: "def fibonacci(n):\n    if n <= 1:\n        return n\n    "
Input Suffix: "\n    return fibonacci(n-1) + fibonacci(n-2)"
Temperature: 0.1
```

### Function Calling
```
Endpoint: chat_completions
User Message: "What's the weather like in Tokyo?"
Tools: [
  {
    "type": "function",
    "function": {
      "name": "get_weather", 
      "description": "Get weather for a location",
      "parameters": {
        "type": "object",
        "properties": {"location": {"type": "string"}}
      }
    }
  }
]
```

## 📊 What Makes This Special

### **Completeness**
Unlike other ComfyUI nodes that support only basic parameters, this node exposes **every single option** that llama-server provides. No feature is left behind.

### **Real-World Ready**
Built for production use with proper error handling, authentication, timeouts, and comprehensive logging. Works reliably in complex workflows.

### **Thoroughly Documented**
- **[PARAMETERS.md](PARAMETERS.md)**: Complete reference for all 100+ parameters
- **[examples.md](examples.md)**: Real-world configuration examples
- **[CHANGELOG.md](CHANGELOG.md)**: Version history and updates
- **[test_node.py](test_node.py)**: Automated testing script

### **Extensible Design**
Easy to extend and modify. Clean, well-commented code that follows ComfyUI conventions.

## 🧪 Testing Your Setup

Run the included test script to verify everything works:

```bash
python test_node.py
```

This tests all endpoints and validates your server connection.

## 🔧 Advanced Use Cases

### **Content Creation Workflows**
- Generate story outlines with structured JSON
- Create character dialogues with chat completions  
- Fill in story gaps with infill completion
- Rank story ideas with reranking

### **Code Development Workflows**
- Generate code with completion endpoint
- Debug with tokenize/detokenize
- Code completion with infill
- Documentation generation with structured output

### **Data Processing Workflows**
- Generate embeddings for semantic search
- Rank documents by relevance
- Extract structured data with JSON schemas
- Process images with multimodal models

### **Interactive AI Workflows**
- Multi-turn conversations with chat completions
- Function calling for external integrations
- Dynamic model behavior with LoRA adapters
- Real-time streaming for responsive UIs

## 🎯 Node Outputs

The node provides four outputs for maximum flexibility:

1. **Response**: Clean, formatted response text
2. **Raw Response**: Complete JSON response from server
3. **Error**: Detailed error messages (empty if successful)
4. **Status Code**: HTTP status code for debugging

## 🔍 Parameter Categories

### **Generation Control** (20+ parameters)
Temperature, top-k, top-p, min-p, seed, n_predict, streaming, etc.

### **Advanced Sampling** (25+ parameters)  
DRY, XTC, Mirostat, dynamic temperature, custom sampler chains, etc.

### **Repetition Management** (10+ parameters)
Repeat penalty, presence penalty, frequency penalty, DRY settings, etc.

### **Constraints & Grammar** (8+ parameters)
JSON schema, BNF grammar, logit bias, stop sequences, etc.

### **Multimodal & Tools** (12+ parameters)
Image data, function definitions, tool choice, response format, etc.

### **Performance & Caching** (15+ parameters)
Cache settings, slot management, timeouts, LoRA adapters, etc.

### **Chat & Conversation** (10+ parameters)
Messages, system prompts, chat templates, prefilling, etc.

### **Specialized Endpoints** (20+ parameters)
Tokenization, embeddings, infill, reranking specific options, etc.

## 🚨 Troubleshooting

### Common Issues
- **Connection refused**: Check if llama-server is running and accessible
- **Timeout errors**: Increase timeout parameter for long generations
- **Invalid JSON**: Verify JSON parameter formatting in multiline fields
- **Feature not working**: Ensure llama-server started with required flags

### Performance Tips
1. Use `cache_prompt=true` for similar prompts
2. Set appropriate `id_slot` for concurrent requests  
3. Configure `n_keep` to retain important context
4. Use streaming for long generations
5. Optimize server batch sizes for your hardware

## 🤝 Contributing

We welcome contributions! This project aims to maintain complete compatibility with llama-server as it evolves.

1. Fork the repository
2. Create a feature branch
3. Test with `python test_node.py`
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[llama.cpp team](https://github.com/ggml-org/llama.cpp)** for the excellent server implementation
- **[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** for the amazing workflow platform  
- **Open source community** for feedback and contributions

## 📈 Project Stats

- **8 API Endpoints**: Complete coverage
- **100+ Parameters**: Every llama-server option
- **800+ Lines of Code**: Robust implementation
- **Full Documentation**: Comprehensive guides and examples
- **Production Ready**: Error handling, testing, validation

---

**Transform your ComfyUI workflows with the full power of llama.cpp** 🚀

*This node bridges the gap between ComfyUI's visual workflow system and llama.cpp's powerful inference server, giving you access to cutting-edge AI capabilities in an intuitive, visual interface.*