# comfyui-sg-process-manager

A ComfyUI custom node package for managing subprocesses within ComfyUI workflows.

![Screenshot](assets/node_preview.png)

## Features

- **Start Process Node**: Launch subprocesses with custom commands, arguments, and working directories
- **Kill Process Node**: Terminate or force-kill running processes
- **Global Process Management**: Processes are managed globally by key, allowing coordination across the workflow
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Automatic Cleanup**: Running processes are automatically terminated when ComfyUI exits

## Installation

   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/sebagallo/comfyui-sg-process-manager.git
   ```

## Nodes

### Start Process

**Inputs:**
- `trigger` (*): Passthrough trigger - node executes when this input is provided
- `process_key` (STRING): Unique identifier for the process (default: "my_process")
- `command` (STRING, multiline): The command to execute
- `args` (STRING, multiline, optional): Arguments for the command (space-separated)
- `cwd` (STRING, multiline, optional): Working directory for the process
- `buffer_size` (INT, optional): Size of output buffer in bytes (default: 1024, min: 1, max: 1048576)
- `trigger_phrase` (STRING, optional): Phrase to wait for in process output before continuing (default: "")
- `print_output` (BOOLEAN, optional): Whether to print process output to console (default: False)
- `post_start_wait_ms` (INT, optional): Milliseconds to wait after process starts (default: 500, min: 0, max: 30000)
- `trigger_timeout` (FLOAT, optional): Seconds to wait for trigger phrase (default: 10.0, min: 0.1, max: 300.0)

**Outputs:**
- `trigger` (*): Passthrough of the input trigger
- `pid` (INT): Process ID of the started process (0 if failed)
- `status` (STRING): Status message ("Process started successfully" or error message)

### Kill Process

**Inputs:**
- `trigger` (*): Passthrough trigger - node executes when this input is provided
- `process_key` (STRING): Key of the process to terminate (default: "my_process")
- `force_kill` (BOOLEAN, optional): Whether to force kill (default: False)

**Outputs:**
- `trigger` (*): Passthrough of the input trigger
- `success` (BOOLEAN): Whether the termination was successful
- `status` (STRING): Status message describing the result

### List Processes

**Inputs:**
- `trigger` (*): Passthrough trigger - node executes when this input is provided

**Outputs:**
- `trigger` (*): Passthrough of the input trigger
- `process_keys` ([STRING]): List of all currently managed process keys

### Kill All Processes

**Inputs:**
- `trigger` (*): Passthrough trigger - node executes when this input is provided

**Outputs:**
- `trigger` (*): Passthrough of the input trigger
- `success` (BOOLEAN): Whether the operation was successful
- `status` (STRING): Status message describing the result

### Kill Process by PID

**Inputs:**
- `trigger` (*): Passthrough trigger - node executes when this input is provided
- `pid` (INT): Process ID to terminate (default: 0)
- `force_kill` (BOOLEAN, optional): Whether to force kill (default: False)

**Outputs:**
- `trigger` (*): Passthrough of the input trigger
- `success` (BOOLEAN): Whether the termination was successful
- `status` (STRING): Status message describing the result

### Kill Process by Name

**Inputs:**
- `trigger` (*): Passthrough trigger - node executes when this input is provided
- `name` (STRING): Process name to terminate (e.g., "notepad.exe")
- `force_kill` (BOOLEAN, optional): Whether to force kill (default: False)

**Outputs:**
- `trigger` (*): Passthrough of the input trigger
- `success` (BOOLEAN): Whether the termination was successful
- `status` (STRING): Status message describing the result

## Usage

1. Use **Start Process** to launch a subprocess with your desired command and arguments
2. The process is stored globally using the `process_key`
3. Use **Kill Process** with the same `process_key` to terminate the process
4. Both nodes are passthrough - they execute when triggered and pass the trigger value through

## Example

```
[Some Trigger] -> Start Process -> [pid, status] -> Some Other Node
                                    |
                                    v
                               Kill Process <- [Another Trigger]
```

## Notes

- Processes are managed globally across the entire ComfyUI session
- Only one process can run per `process_key` at a time
- Processes are automatically cleaned up when ComfyUI exits
