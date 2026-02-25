Passthrough node that instantly unloads any running ollama model mid workflow. No API calls, just accepts plain string as a model name and executes 'ollama stop <model>' command in your system. 

Note that for the command to work the model name should be exactly as it appears in ollama lists:
- ❌️'qwen3-vl-abliterated'
- ❌️'qwen3-vl-abliterated:4b-instruct'
- ✅️'huihui_ai/qwen3-vl-abliterated:4b-instruct'
