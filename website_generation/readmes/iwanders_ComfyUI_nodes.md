# ComfyUI Nodes

Some custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

- `StringSave`: Writes a string to a text or json file in the output directory. For json output, string is parsed and pretty printed.
- `StringPrint`: Prints the input string to stdout (would be nice if it went to the UI...).
- `StringReplace`: Replace the needle in the haystack by the value.
- `StringNode`: A node that just provides a string, like the primitive node, but then always a string.
- `StringConcat`: Concatenates the prefix with the suffix and returns the combined string.
- `JsonPickItem`: Pick an element from a json list using the provided pick (integer) value.
- `TokenizerVocab`: Converts the tokenizer vocabulary to a json string (limited to SDXL clips atm).
- `OllamaGenerateString`: A simple ollama-llm text generator, off-by-one to ensure the UI & png holds the actual text used for image generation.

### License
License is GPLv3, just like ComfyUI.
