# ComfyUI Finetuners

A collection of utility nodes for ComfyUI to enhance your workflow.

## Nodes

### 🔄 Variables Injector
Dynamically replace placeholders (like !variable_name) in a text prompt with actual values, making it easy to reuse and modify prompts without changing their structure.

### 📐 Auto Image Resize
Automatically resizes images based on a desired width while maintaining aspect ratio, using high-quality Lanczos scaling.

### 🔗 Group Link
A utility node that allows you to link and toggle multiple groups of nodes simultaneously, helping you organize and control complex workflows.

### 🔵 Variables Logic
A toggle boolean node that changes colors (purple/green) based on its state and displays custom text from a string input. Perfect for visual workflow control and status indication.

### Model List
A utility node that reads LoRA models from a CSV file, providing an easy-to-use dropdown menu for model selection with automatic path and prompt formatting for ComfyUI's LoRA loader.

## Variables Injector Node

The Variables Injector node allows you to dynamically replace placeholders in your prompts with variable values. This makes it easy to reuse prompts with different values.

### How to Use

1. Load the Variables Injector node into your workflow
2. Connect a string node to Var1's input
3. Use the following syntax in the string node: `variable_name | variable_value`
   - For example: `item | bag`
4. In your prompt, reference the variable using `!variable_name`
   - For example: `"A woman holding a !item"`
5. The node will replace `!item` with `bag` in the final prompt
6. You can add as many variables as you like using Var1 through Var8

### Example
Input string: `item | bag`
Prompt: `"A woman holding a !item"`
Result: `"A woman holding a bag"`

## Variables Logic Node

The Variables Logic node provides a visual toggle with customizable text labels. It's useful for controlling workflow logic and providing visual feedback.

### How to Use

1. Add the Variables Logic node to your workflow
2. Connect a String Literal node to the labels input using the format: `text_when_off | text_when_on`
   - For example: `"book | shoos"`
3. The toggle will:
   - Display purple color and first text when OFF
   - Display green color and second text when ON
4. The node outputs a boolean value that can be used to control other parts of your workflow

### Example
Input string: `"book | shoos"`
Result: Shows "book" in purple when OFF, "shoos" in green when ON

### Model List Node

A utility node that provides a convenient way to manage and select LoRA models from a CSV list. The node reads model paths and metadata from a CSV file and provides them in a format compatible with ComfyUI's LoRA loader.

#### Features:
- Reads model paths and metadata from a CSV file
- Provides a dropdown menu for easy model selection
- Outputs model path (M), prefix (P), and suffix (S) for each model
- Compatible with ComfyUI's LoRA loader node
- Configurable model list location via modellocation.txt

#### Setup:
1. The default path in modellocation.txt is set to Rundiffusion's storage location, but can be easily changed by editing the file
2. A sample CSV file format is provided in the workflows folder
3. The CSV should contain columns: "Name on list", "model path", "prefix", "sufix"

#### Usage:
1. Connect the 'M' output to a CR String To Combo node
2. Connect the CR String To Combo output to the LoRA loader's 'lora_name' input
3. Optionally use the 'P' (prefix) and 'S' (suffix) outputs for prompt engineering


## Credits

- Custom nodes were developed by Finetuners
- Variables Injector's UI was created with the help of Shmuel Ronen (https://github.com/ShmuelRonen)
- The group link custom node is heavily based on RGThree mute groups node

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes` directory:
```bash
cd custom_nodes
git clone https://github.com/FinetunersAI/finetunersTest.git
```

2. Restart ComfyUI

## Usage

After installation, you'll find the nodes in the node menu under the "finetuners" category.
