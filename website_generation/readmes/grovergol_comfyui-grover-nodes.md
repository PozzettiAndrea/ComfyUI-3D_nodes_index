# ComfyUI Grover Nodes

## Open Path Node 📁

A custom ComfyUI node that provides an easy way to open file and folder paths in your system's default file explorer.

### Features

- **Cross-platform support**: Works on Windows, macOS, and Linux
- **Smart path handling**: Automatically detects whether the path is a file or folder
- **File selection**: On Windows, if you provide a file path, it will open the folder and select the file
- **Simple interface**: Just enter a path and click the "📁 Open Path" button

### Usage

1. Add the "📁 Open Path" node to your workflow
2. **For manual paths**: Enter a file or folder path in the text input field
3. **For dynamic paths**: Connect any node that outputs a string path to the "path" input
4. **For dynamic paths**: Execute the workflow first (click "Queue Prompt") to compute the path values
5. Click the "📁 Open Path" button to open the location in your system's file explorer

### Important Note for Dynamic Paths

When using **connected inputs** (like from Save Image, Load Image, or text processing nodes), you must **execute the workflow first** before the Open Path button will work. This is because dynamic paths are only computed during execution.

**Workflow for dynamic paths:**
1. Connect your path-generating node → Open Path node
2. Click "Queue Prompt" to execute the workflow
3. After execution completes, click "📁 Open Path" button
4. The computed path will be opened in your file explorer

### Supported Path Types

- **Absolute paths**: `C:\Users\YourName\Documents\file.txt` (Windows) or `/home/username/documents/file.txt` (Linux/macOS)
- **Relative paths**: `./outputs/image.png`
- **Folder paths**: Any valid directory path
- **File paths**: Any valid file path

### Platform-Specific Behavior

- **Windows**: Uses `explorer.exe` with `/select` for files to highlight them
- **macOS**: Uses the `open` command
- **Linux**: Uses `xdg-open` with fallbacks to common file managers (nautilus, dolphin, thunar, pcmanfm)

### Error Handling

The node will show error messages if:
- The path doesn't exist
- The path is empty
- The system cannot open the file explorer
- Network errors occur when communicating with the backend

### Installation

1. Clone or download this repository to your ComfyUI custom_nodes directory
2. Restart ComfyUI
3. The node will appear under the "Grover/System" category

### Technical Details

This node consists of:
- **Backend**: Python node that handles the file system operations
- **Frontend**: JavaScript component that provides the button interface
- **API**: HTTP endpoint for communication between frontend and backend
