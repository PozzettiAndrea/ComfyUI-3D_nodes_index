# ComfyUI-Qwen-CUDA

基于 llama-cpp-python 的 Qwen3 + Qwen2.5VL 的推理。

## Installation
下载到自定义节点后，执行下面的命令

```bash
pip install -r requirements.txt
```

llama-cpp-python 的安装较为麻烦，推荐去 https://github.com/abetlen/llama-cpp-python/releases 下载对应的 whl，比如当前环境是 python3.12、cuda12.4，则下载 https://github.com/abetlen/llama-cpp-python/releases/download/v0.3.12-cu124/llama_cpp_python-0.3.12-cp312-cp312-linux_x86_64.whl

## About models.json

```json
{
    "cuda": [
        {
            "repo_id": "Qwen/Qwen3-8B-GGUF",
            "local_path": "models/LLM",
            "files": [
                "Qwen3-8B-Q5_K_M.gguf"
            ]
        },
        {
            "repo_id": "Qwen/Qwen3-8B",
            "local_path": "models/LLM",
            "files": [
                "tokenizer_config.json",
                "vocab.json",
                "merges.txt",
                "tokenizer.json",
                "config.json",
                "generation_config.json"
            ]
        },
        {
            "repo_id": "unsloth/Qwen2.5-VL-7B-Instruct-GGUF",
            "local_path": "models/LLM",
            "files": [
                "Qwen2.5-VL-7B-Instruct-Q8_0.gguf",
                "mmproj-F16.gguf"
            ]
        }
    ]
}
```

cuda[0] 代表 Qwen3 模型。如果你想使用其他参数或量化级别的模型，可以修改这部分内容。以 Qwen3-8B-Q5_K_M.gguf 为例，该文件将被下载到 ComfyUI/models/LLM/Qwen3-8B-GGUF/Qwen3-8B-Q5_K_M.gguf 路径下。
cuda[1] 部分包含了 Qwen3 的分词器配置信息，无需修改。
cuda[2] 为 Qwen2.5-VL 的模型信息，可以酌情修改不同参数规模/量化级别的模型。
