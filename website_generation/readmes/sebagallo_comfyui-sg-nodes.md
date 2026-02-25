# ComfyUI SG Nodes

A collection of custom nodes for ComfyUI.

## Nodes

### Load GGUF Path
Loads the full path to a general GGUF model file.

- **Category**: SGNodes/GGUF Loaders
- **Input**: Model name from dropdown
- **Output**: Full file path as string

### Load GGUF MPROJ Path
Loads the full path to a GGUF multi-modal projector model file.

- **Category**: SGNodes/GGUF Loaders
- **Input**: Model name from dropdown
- **Output**: Full file path as string

### Load GGUF DRAFT Path
Loads the full path to a GGUF draft model file.

- **Category**: SGNodes/GGUF Loaders
- **Input**: Model name from dropdown
- **Output**: Full file path as string

### Wait For Passthrough
A utility node that waits for one input to be ready before passing through another input.

- **Category**: SGNodes/Utilities
- **Inputs**:
  - `passthrough`: Any type, lazy input that will be returned
  - `wait_for`: Any type, required input that triggers execution
- **Output**: The `passthrough` input value
- **Behavior**: Executes when `wait_for` is ready, then requests the `passthrough` value if not already available

### Wait For Milliseconds
Pauses execution for a specified number of milliseconds.

- **Category**: SGNodes/Utilities
- **Inputs**:
  - `passthrough`: Any type, lazy input that will be returned
  - `milliseconds`: Integer, number of milliseconds to wait (default: 1000)
- **Output**: The `passthrough` input value

### Select File From Directory
Allows selecting a file from a specified folder and its subdirectories with dynamic filtering.

- **Category**: SGNodes/Utilities
- **Features**:
  - **Recursive Scanning**: Automatically lists files from the folder and all its subdirectories.
  - **Extension Filtering**: Filter files by one or more comma-separated extensions (e.g., `.png, .jpg`).
  - **Additional Filtering**: Use "Contains" or "Regex" matches on top of the extension filter to narrow down the list.
  - **Dynamic Updates**: The file list updates automatically whenever the folder path, extensions, or filters are changed in the UI.
- **Inputs**:
  - `folder_path`: The absolute path to the directory to scan.
  - `extensions`: Comma-separated list of allowed extensions (default: `*` searches all).
  - `filter_type`: Type of additional filtering (`none`, `contains`, `regex`).
  - `filter_text`: The text or regex pattern for the selected filter type.
  - `file_name**: The selected file from the dynamic dropdown list.
- **Outputs**:
  - `full_path**: The absolute path to the selected file.
  - `relative_path**: The path relative to the `folder_path` (includes subfolders).
  - `file_name`: Just the name of the file (no path).

### Any Adapter
A universal adapter node that bypasses ComfyUI's strict type validation. It accepts any input type and provides an output of type "any" (`*`), allowing you to connect nodes with incompatible types (e.g., connecting a path string to a model loader's combo input).

- **Category**: SGNodes/Utilities
- **Inputs**:
  - `any_input` (Optional): `*` (IO.ANY). Connect any node output here.
- **Outputs**:
  - `any_output`: `*` (IO.ANY). Connect this to any node input.
- **Usage**:
  1. Add `Any Adapter`.
  2. Connect your source node to the `any_input`.
  3. Right-click the destination node and select **"Convert [parameter] to input"**.
  4. Connect `any_output` to the newly created input.

### Any Lazy Adapter
A variant of the Any Adapter that uses **lazy evaluation**. It only requests and processes the input data when it is actually needed by a downstream node. This is useful for optimizing complex workflows or handling conditional logic.

- **Category**: SGNodes/Utilities
- **Inputs**:
  - `any_input` (Optional): `*` (IO.ANY, Lazy). Connect any node output here.
- **Outputs**:
  - `any_output`: `*` (IO.ANY). Connect this to any node input.

### Is None
A utility node that checks if an input is `None` or not connected.

- **Category**: SGNodes/Utilities
- **Inputs**:
  - `any_value` (Optional): `*` (IO.ANY). Connect any node output here.
- **Output**:
  - `is_none`: `BOOLEAN`. Returns `True` if the input is not connected or if it's connected and its value is `None`. Returns `False` otherwise.

### None Primitive
A utility node that outputs an explicit `None` value.

- **Category**: SGNodes/Utilities
- **Outputs**:
  - `none_value`: `*` (IO.ANY). An explicit `None` value.

### Select From List
Allows providing a list of items and selecting one using a dynamic dropdown.

- **Category**: SGNodes/Utilities
- **Features**:
  - **Dynamic Dropdown**: The selection dropdown updates in real-time as you modify the source list.
  - **Custom Delimiters**: Support for any delimiter (newline, comma, tab, etc.) to split your list.
  - **JSON Mode**: Explicitly parse the input as a JSON array.
  - **Auto Mode**: Intelligently tries to parse as JSON first, then falls back to newline-separated items.
- **Inputs**:
  - `list_data`: A multiline string containing the items.
  - `input_mode`: Choose how to parse the data (`auto`, `delimiter`, `json`).
  - `delimiter`: The separator to use in `delimiter` mode (supports `\n`, `\t`, `,`, etc.).
  - `selected_value`: The item selected from the dynamic dropdown.
- **Output**:
  - `selected_item`: The selected value. If the source was a JSON array, it returns the actual object/value from that array.

### Call Remote URL
Performs a server-side HTTP request to a remote URL. Useful for integrating with external APIs.

- **Category**: SGNodes/Network
- **Inputs**:
  - `url`: Target URL string
  - `method`: HTTP method (GET, POST, etc.)
  - `passthrough`: Any type (IO.ANY), passed through to output. Useful for execution ordering.
  - `body` (Optional): Request body string
  - `headers` (Optional): JSON string of request headers
- **Outputs**:
  - `passthrough`: The input `passthrough` value
  - `status_code`: HTTP status code (INT)
  - `response_body`: Response content (STRING)

### Poll Remote URL
Polls a remote URL until a matching condition is met or maximum attempts are reached.

- **Category**: SGNodes/Network
- **Inputs**:
  - `passthrough`: Any type (IO.ANY), passed through to output.
  - `url`: Target URL string.
  - `method`: HTTP method (GET, POST, etc.).
  - `match_type`: Type of matching to perform (`string`, `regex`, `json`).
    - `string`: Checks if `match_value` is a substring of the response.
    - `regex`: Checks if `match_value` regex pattern matches the response.
    - `json`: Checks if `match_value` (as JSON) is a subset of the response JSON. *Note: The match is partial but structural. To match `{"status": "ok"}` inside `{"data": {"status": "ok"}}`, your match value must include the full path: `{"data": {"status": "ok"}}`.*
  - `match_value`: The value to match against.
  - `invert_match`: (Boolean) If True, waits until the match condition is **FALSE** (e.g. wait for something to disappear).
  - `body` (Optional): Request body string.
  - `headers` (Optional): JSON string of request headers.
  - `max_attempts` (Optional): Maximum number of polling attempts (default: 30).
  - `delay_ms` (Optional): Delay between attempts in milliseconds (default: 500).
- **Outputs**:
  - `passthrough`: The input `passthrough` value.
  - `status_code`: Last HTTP status code (INT).
  - `response_body`: Last response content (STRING).

### Map JSON To Property
Extracts a property from a JSON object string.

- **Category**: SGNodes/JSON
- **Inputs**:
  - `json_string`: JSON object string (e.g., `{"a": 1}`).
  - `property_name`: Name of the property to extract. Supports dot notation for nested keys (e.g., `data.user.id`).
- **Output**: The value of the property as a string. If the value is an object or array, it returns a JSON string.

### Map JSON Array
Maps a property from each object in a JSON array.

- **Category**: SGNodes/JSON
- **Inputs**:
  - `json_array`: JSON array string (e.g., `[{"id": 1}, {"id": 2}]`).
  - `property_name`: Name of the property to extract from each item. Supports dot notation (e.g., `user.name`).
- **Output**: A JSON array string of the extracted values (e.g., `["User1", "User2"]`).

### Find JSON Element
Finds the first element in a JSON array that matches a key-value pair.

- **Category**: SGNodes/JSON
- **Inputs**:
  - `json_array`: JSON array string.
  - `match_key`: The key to check in each element. Supports dot notation (e.g., `status.code`).
  - `match_value`: The value to match against (compared as string).
- **Output**: The matching element as a JSON string. Returns empty string if not found.

### Make JSON List
Creates a JSON array from multiple inputs.

- **Category**: SGNodes/JSON
- **Features**:
  - **Dynamic Inputs**: Automatically adds a new input slot when the current ones are connected.
  - **Auto-Cleanup**: Automatically removes unused trailing input slots.
- **Inputs**:
  - `input_1`, `input_2`, ...: Any type (IO.ANY). Connect any number of values to build the array.
- **Output**:
  - `json_string`: A JSON array string containing all connected input values (e.g., `["val1", 42, "val3"]`).

### Sound Player
Plays audio provided via the `audio` input when the node is executed. Acts as a passthrough for its main input.

- **Category**: SGNodes/Utilities
- **Features**:
  - **Passthrough**: Connect any type to `any_input` and it will be passed to `passthrough` output.
  - **Volume Control**: Adjust playback volume from 0 to 100.
  - **Waveform Playback**: Plays audio directly from the `AUDIO` stream (compatible with "Load Audio" nodes).
  - **Client-Side Playback**: The audio is synthesized and played in the browser when the ComfyUI server executes the node.
- **Inputs**:
  - `any_input`: Any type (IO.ANY). The value to be passed through.
  - `audio`: The audio stream to play.
  - `volume`: Integer slider for volume control (0-100).
- **Output**:
  - `passthrough`: The original `any_input` value.

### Sigmas Slice (Start/End)
Allows slicing a `SIGMAS` object using step indices, mimicking the behavior of the native `KSampler (Advanced)`'s `start_at_step` and `end_at_step` options.

- **Category**: SGNodes/Sigmas
- **Inputs**:
  - `sigmas`: The SIGMAS tensor to slice.
  - `start_at_step`: 0-indexed start position (Default: 0).
  - `end_at_step`: 0-indexed end position (Default: 10000).
  - `return_with_leftover_noise`: Boolean (Default: True). If False, the last sigma in the sliced range is set to `0.0`, forcing a full denoise.
- **Output**:
  - `sigmas`: The sliced SIGMAS tensor.

## Configuration

Create a `config.json` file in the same directory as this package to specify additional model folders to scan:

```json
{
  "model_folders": [
    "C:\\Users\\YourUsername\\models",
    "D:\\AI\\LLM\\models",
    "/home/user/models"
  ]
}
```

The nodes will automatically scan:
- ComfyUI's `text_encoders` folder
- Any folders specified in `config.json`

## Installation

1. Place this folder in your ComfyUI `custom_nodes` directory
2. Restart ComfyUI
3. The nodes will appear in the "SGNodes" category

## Requirements

- ComfyUI
