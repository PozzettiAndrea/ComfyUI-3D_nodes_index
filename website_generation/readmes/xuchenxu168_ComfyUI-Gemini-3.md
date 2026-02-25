# ComfyUI-Gemini-3-2

Full-featured, high-performance Google Gemini 3 integration for ComfyUI. This plugin implements **all** Gemini 3 capabilities with optimized performance.

> **🔧 Latest Update (2025-11-19):** Fixed Gemini API error 400 "Invalid thinkingLevel field". The `thinkingLevel` parameter is now correctly placed in the API request. See [QUICK_FIX_GUIDE.md](QUICK_FIX_GUIDE.md) for details.

## 🌟 Features

### Core Gemini 3 Capabilities
- ✅ **Dynamic Thinking Levels** (Low/High) - Control reasoning depth vs latency
- ✅ **Media Resolution Control** - Fine-grained control over image/video/PDF processing
- ✅ **Thought Signatures** - Maintain reasoning context across API calls
- ✅ **Function Calling** - Strict validation with parallel and sequential support
- ✅ **Structured Outputs** - JSON schema validation with tools integration
- ✅ **Context Caching** - Reduce costs for repeated context (2048+ tokens)
- ✅ **Batch API Support** - Process multiple requests efficiently

### Multimodal Support
- 📝 Text generation with advanced reasoning
- 🖼️ Image understanding and generation (up to 1120 tokens per image)
- 🎥 Video analysis (70-280 tokens per frame)
- 🎵 Audio understanding (speech, music)
- 📄 PDF document processing (optimized at medium resolution)
- 🔗 URL context and web search integration

### Advanced Features
- 🧠 **Multi-step reasoning** with thought signature preservation
- 🔄 **Streaming support** with real-time updates
- 🛡️ **Safety settings** with configurable thresholds
- 📊 **Token counting** and usage tracking
- 🌡️ **Temperature control** (optimized for Gemini 3)
- 🔧 **System instructions** for behavior customization
- 🔍 **Google Search** integration for real-time information
- 💻 **Code Execution** for mathematical and data analysis tasks

## 📦 Installation

1. Clone into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-Gemini-3-2.git
```

2. Install dependencies:
```bash
cd ComfyUI-Gemini-3-2
pip install -r requirements.txt
```

3. Set your API key:
   - Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)
   - Set environment variable: `GEMINI_API_KEY=your_key_here`
   - Or configure in the node settings

## 🎮 Nodes

### 基础节点 (Basic Nodes)

#### 1. Gemini 3 文本生成 (Text Generation)
Generate text with advanced reasoning capabilities.
- **Inputs**: prompt, images, audio, video, PDFs, thinking level, media resolution, system instruction
- **Outputs**: text, thought signature, usage metadata
- **Features**: Multimodal input, customizable thinking levels, media resolution control

### 高级节点 (Advanced Nodes)

#### 2. Gemini 3 函数调用 (Function Calling)
Execute function calls with strict validation and thought signature preservation.
- **Inputs**: prompt, function declarations, thought signatures, function responses
- **Outputs**: function calls (JSON), updated thought signature, text response
- **Features**: Parallel and sequential function calling, multi-step reasoning

#### 3. Gemini 3 结构化输出 (Structured Output)
Generate JSON with schema validation and tool integration.
- **Inputs**: prompt, JSON schema, enable Google Search/Code Execution/URL Context
- **Outputs**: validated JSON output, usage metadata
- **Features**: Strict JSON schema validation, integrated with built-in tools

#### 4. Gemini 3 聊天 (Chat)
Multi-turn conversation with automatic context management.
- **Inputs**: message, chat history, system instruction, max output tokens
- **Outputs**: response, updated chat history (with thought signatures), usage metadata
- **Features**: Automatic history management, thought signature preservation

### 流式节点 (Streaming Nodes)

#### 5. Gemini 3 流式生成 (Streaming Generation)
Real-time streaming generation with progressive output.
- **Inputs**: prompt, thinking level, system instruction, max output tokens
- **Outputs**: full text, thought signature, stream chunks info
- **Features**: Real-time response streaming, chunk-by-chunk processing

### 优化节点 (Optimization Nodes)

#### 6. Gemini 3 创建缓存 (Create Context Cache)
Create cached contexts for cost optimization (10x cheaper for cached content).
- **Inputs**: content to cache (min 2048 tokens), TTL minutes, cache name
- **Outputs**: cache name/reference, cache info (with expiry), status
- **Features**: Automatic TTL management, usage metadata tracking

#### 7. Gemini 3 使用缓存 (Use Cached Content)
Generate content using previously cached context.
- **Inputs**: prompt, cache name, thinking level
- **Outputs**: response, usage metadata (showing cached token savings)
- **Features**: Significant cost reduction, maintains full functionality

#### 8. Gemini 3 批处理 (Batch Processing)
Process multiple requests efficiently with 50% discount.
- **Inputs**: prompts JSON array, thinking level
- **Outputs**: batch name/ID, status info
- **Features**: 50% cost reduction, 24-hour processing window

### 工具节点 (Tool Nodes)

#### 9. Gemini 3 + Google搜索 (With Google Search)
Generate content with real-time web search integration.
- **Inputs**: prompt, thinking level, max output tokens
- **Outputs**: response, grounding metadata (search sources), usage metadata
- **Features**: Real-time information, automatic grounding, source attribution

#### 10. Gemini 3 + 代码执行 (With Code Execution)
Generate content with automatic Python code execution.
- **Inputs**: prompt, thinking level
- **Outputs**: response, execution results (code + output), usage metadata
- **Features**: Automatic code generation and execution, mathematical computations

### 安全节点 (Safety Nodes)

#### 11. Gemini 3 安全设置 (Safety Settings)
Generate content with customizable safety thresholds.
- **Inputs**: prompt, thinking level, harassment/hate speech/sexually explicit/dangerous content thresholds
- **Outputs**: response, safety ratings
- **Features**: Fine-grained safety control, detailed safety ratings, block reason reporting

## 🚀 Usage Examples

### Basic Text Generation with High Thinking
```
Prompt: "Find the race condition in this multi-threaded C++ code..."
Thinking Level: High
→ Detailed analysis with deep reasoning
```

### Image Analysis with High Resolution
```
Prompt: "Read all the text in this image"
Image: [your image]
Media Resolution: High (1120 tokens)
→ Accurate OCR and detailed analysis
```

### Video Understanding
```
Prompt: "Describe what happens in this video"
Video: [your video]
Media Resolution: Low (70 tokens/frame) - for general description
Media Resolution: High (280 tokens/frame) - for text reading
```

### Function Calling with Thought Signatures
```
1. Model calls check_flight → Returns signature A
2. Send flight result + signature A
3. Model calls book_taxi → Returns signature B
4. Send taxi result + signatures A & B
→ Model maintains reasoning chain
```

## ⚙️ Configuration

### Thinking Levels
- **Low**: Fast, minimal reasoning - for simple tasks
- **High** (default): Maximum reasoning depth - for complex tasks

### Media Resolution
- **Images**: High (1120 tokens) recommended for most tasks
- **PDFs**: Medium (560 tokens) optimal for documents
- **Video**: Low/Medium (70 tokens) for general, High (280) for text

### Temperature
- **Default: 1.0** - Optimized for Gemini 3
- ⚠️ Changing temperature may cause looping or degraded performance

## 📊 Performance Tips

1. **Use Low Thinking** for simple tasks to reduce latency
2. **Use Medium Resolution** for PDFs (rarely benefits from High)
3. **Cache contexts** 2048+ tokens for repeated use
4. **Batch requests** when processing multiple items
5. **Keep temperature at 1.0** unless you have specific needs

## 🔗 Resources

- [Gemini 3 Developer Guide](https://ai.google.dev/gemini-api/docs/gemini-3)
- [API Reference](https://ai.google.dev/api)
- [Google AI Studio](https://aistudio.google.com/)
- [Pricing](https://ai.google.dev/pricing)

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions welcome! Please read CONTRIBUTING.md first.

## 💬 Support

- Issues: [GitHub Issues](https://github.com/yourusername/ComfyUI-Gemini-3-2/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/ComfyUI-Gemini-3-2/discussions)

