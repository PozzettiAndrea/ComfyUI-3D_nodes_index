# ComfyUI-LLM-GGUF

model:https://huggingface.co/eddy1111111/qwen3_coder_8b_COT_un/blob/main/Qwen3-8B-Coder-Abliterated-Q4_K_M.gguf

ComfyUI custom nodes for LLM GGUF model inference.

## Features

- Load and cache GGUF LLM models
- Chat inference with conversation history (hot session)
- Session management (reset, list)
- Model cache management
- Output condition prefix (Chinese T5 format)
- Supports llama-cpp-python binding or subprocess fallback

## Nodes

### Load GGUF Model
Load a GGUF LLM model for inference.

**Inputs:**
- `model_name`: Select GGUF model file from `models/LLM` folder
- `gpu_layers`: Number of layers to offload to GPU (default: 99 = all)
- `context_size`: Context window size in tokens (default: 32768)
- `llama_cli_path`: (Optional) Path to llama-cli.exe for subprocess fallback

**Output:**
- `model`: LLM_MODEL object

### LLM Chat
Run LLM inference with chat support.

**Inputs:**
- `model`: LLM model from LoadGGUFModel
- `user_prompt`: User message to send to the model
- `system_prompt`: (Optional) System prompt to set model behavior
- `session_id`: Session ID for maintaining conversation history (default: "default")
- `max_tokens`: Maximum tokens to generate (default: 1024)
- `temperature`: Sampling temperature (default: 0.7)
- `top_p`: Top-p sampling threshold (default: 0.9)
- `top_k`: Top-k sampling (default: 40)
- `repeat_penalty`: Repetition penalty (default: 1.1)
- `keep_history`: Keep conversation history for hot session (default: True)
- `output_condition`: Output condition prefix (None / Chinese_T5)

**Output:**
- `response`: Model response text

### Reset Chat Session
Reset chat session history.

**Inputs:**
- `session_id`: Session ID to reset
- `trigger`: (Optional) Connect any input to trigger reset

**Outputs:**
- `success`: Boolean indicating success
- `message`: Status message

### Clear Model Cache
Clear all cached LLM models to free memory.

**Inputs:**
- `trigger`: (Optional) Connect any input to trigger cache clear

**Outputs:**
- `success`: Boolean indicating success
- `message`: Status message

### List Chat Sessions
List all active chat sessions.

**Output:**
- `sessions`: List of active sessions with message counts

## Installation

1. Place the `ComfyUI-LLM-GGUF` folder in `ComfyUI/custom_nodes/`
2. Place GGUF model files in `ComfyUI/models/LLM/`
3. (Optional) Install llama-cpp-python for native inference:
   ```
   pip install llama-cpp-python
   ```
4. Restart ComfyUI

## Model Folder

GGUF models should be placed in:
```
ComfyUI/models/LLM/
```

## Requirements

- ComfyUI
- llama-cpp-python (optional, for native binding)
- llama-cli.exe (for subprocess fallback if binding not available)

## Author

eddy

