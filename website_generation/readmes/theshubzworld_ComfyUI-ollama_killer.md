
# OllamaKiller Node for ComfyUI

**OllamaKiller** is a utility node for ComfyUI designed to manage VRAM usage more efficiently by automatically terminating the Ollama process (`ollama.exe` on Windows, `ollama` on macOS/Linux). This is particularly useful for users with limited VRAM, allowing them to clear up memory after running models and improve workflow performance.

## Features

- **Cross-Platform Support**: Works on Windows, Unconfirmed with macOS, and Linux so test yourself.
- **Automatic Process Detection**: Finds and terminates Ollama processes
- **Graceful Termination**: Attempts clean shutdown before force killing
- **Detailed Status**: Provides clear feedback about process termination
- **Seamless Integration**: Passes through text input while managing processes in the background

## Purpose

Running Ollama in ComfyUI workflows can consume significant VRAM. The OllamaKiller node automatically terminates the Ollama process after each use, freeing up valuable memory and enhancing performance in subsequent generations.

## How It Works

1. When triggered, the node searches for any running Ollama processes
2. It first attempts to gracefully terminate the process
3. If needed, it can force kill stubborn processes
4. The original text input is passed through to the output
5. Process status is returned separately for monitoring

## Installation

### Method 1: Git Clone
```bash
# In your ComfyUI custom_nodes directory
git clone https://github.com/theshubzworld/ComfyUI-ollama_killer.git
```

### Method 2: ComfyUI Manager
1. Open ComfyUI
2. Go to Manager tab
3. Search for "OllamaKiller"
4. Click Install

Restart ComfyUI after installation.

## Usage

1. **Add OllamaKiller to Your Workflow**:
   - Place the node after any Ollama model node
   - Connect the text output to the OllamaKiller input
   - The node will automatically handle process termination

2. **Inputs**:
   - `text`: Connect any text input (required)
   - `trigger`: Toggle to manually trigger process termination (optional)
   - `force_kill`: Enable to force kill stubborn processes (optional)

3. **Outputs**:
   - `status`: Information about process termination
   - `output_text`: The original input text (passed through)

## Node Information

- **Node Class**: `OllamaKiller`
- **Category**: `utils`
- **Input Types**:
  - Text (String): Any text input
  - Trigger (Boolean): Manual trigger (optional)
  - Force Kill (Boolean): Force process termination (optional)
- **Output Types**:
  - Status (String): Process termination status
  - Output Text (String): Original input text

## Example Workflow

1. Add an Ollama model node to your workflow
2. Connect its output to OllamaKiller's input
3. Connect OllamaKiller's output to the next node in your workflow
4. Run the workflow - Ollama processes will be automatically managed

## Troubleshooting

- If processes aren't being terminated, try enabling `force_kill`
- Ensure you have the necessary permissions to manage processes
- Check the status output for detailed error messages

## License

This project is open-source and available under the MIT License. Contributions are welcome!

## Credits

Maintained by [Shubz World](https://github.com/theshubzworld)
