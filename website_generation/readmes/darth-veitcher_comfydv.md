# comfydv

A collection of workflow efficiency and quality of life nodes that I've created for personal use out of necessity.

* **String Formatting**: Use either plain python f-strings or more advanced Jinja2 templating to format outputs.
* **Random Choice**: Add an abitrary number of inputs and then, with seed control, randomly select one for an output.

## Documentation

Full documentation can be found: [darth-veitcher.github.io/comfydv](https://darth-veitcher.github.io/comfydv/stable/)

## String Formatting

The FormatString node provides flexible string formatting with dynamic input/output configuration.

### Python F-String

A simple python f-string dynamically creates the necessary inputs/outputs for the detected keys.

![f-string](docs/assets/fstring.png)

### Jinja 2

Switching to Jinja2 allows you to use more advanced control blocks and other filters/features of that templating language. See [Jinja documentation](https://jinja.palletsprojects.com/en/latest/) for further details.

![jinja2](docs/assets/jinja2.png)

### Output Structure

The node's outputs are organized for maximum reliability and flexibility:

1. **`formatted_string`** (Output 0): The formatted result string - always in position 0
2. **`saved_file_path`** (Output 1): Path to saved state file (if save_path provided) - always in position 1
3. **Variable outputs** (Output 2+): Pass-through values for any variables detected in the template, enabling easy chaining

For example, with template `"Hello {name}, you are {age}"`:

* Output 0: The formatted string (e.g., "Hello Alice, you are 30")
* Output 1: The save file path (or empty string)
* Output 2: The value of `name` (e.g., "Alice")
* Output 3: The value of `age` (e.g., "30")

This structure ensures the primary outputs (`formatted_string` and `saved_file_path`) are always in predictable, fixed positions for reliable workflow connections.

## Random Choice

Ability to take arbitrary length and type of inputs to then output a **choice** with a controllable seed.

![random](docs/assets/random.png)
