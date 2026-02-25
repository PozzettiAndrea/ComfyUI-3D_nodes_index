# ViewComfy Utils

A lightweight ComfyUI custom node pack to enable [ViewComfy app](https://github.com/ViewComfy/ViewComfy) functionalities like workflow branching, optional image inputs, input validations and custom errors. 

This node pack has no extra dependencies beyond the standard ComfyUI ones. It can be added to any ComfyUI environment with no risk of breaking anything.

## Nodes

1. [Compare](#compare)

2. [Conditional Select](#conditional-select)

3. [Show Anything](#show-anything)

4. [Load Image](#load-image)

5. [Anything Inversed Switch](#anything-inversed-switch)

6. [Show Error Message](#show-error-message)

7. [Save Text](#save-text)

8. [Download and Save Video](#download-and-save-video)

## Demo

[![Demo Video](https://github.com/user-attachments/assets/ac06c9e3-c2f0-4941-97f5-8f91ea6c781d)](https://youtu.be/kMSHMvVe-W8)


---

  

## Compare

Compares two inputs and returns a Boolean. 

### Inputs
Supports multiple data types, including primitives, tensors (images or videos), Booleans, etc. 

The default value for a and b is `None`

### Supported operators

-  `a == b`

-  `a != b`

-  `a < b`

-  `a > b` 

-  `a <= b` 

-  `a >= b`

-  `a and b`

-  `a or b` 

  
### Outputs

-  Boolean

### Special Behavior

- Only `==` and `!=` operators are supported for Tensor Comparison (e.g. Images and Videos)

-  The `and` and `or` operations require both inputs to be boolean values.

  

### Example Use Cases

- Comparing numeric values to control workflow branching

- Checking if tensors/images are identical

- Create custom input validations in ComfyUI workflows 

---

  

## Conditional Select

Outputs one of two input values based on a boolean condition. This is essentially a programmatic if-else statement that works with any data type.

  

### Inputs

- A boolean value that determines which input to output. Default: `True`

- Values A and B. They can be of any type. Default: `None`


### Outputs

-  Returns Value A if the condition is True, otherwise returns Value B.

### Example Use Cases

- Selecting between different models, images, or parameters based on conditions.

- Implementing conditional logic in ComfyUI workflows. 

  

---

  

## Show Anything

A visualization node that displays any type of data in the ComfyUI interface. It can handle strings, lists, objects, and complex data structures by converting them to readable text format.


### Inputs

-  Anything


### Outputs

-  The input as a JSON string
  

### Example Use Cases

- Can be used to display text in ViewComfy apps
- Debugging workflows by inspecting intermediate values
- Monitoring data flow through complex workflows

 
---

  

## Load Image

A variation of the Load Image node with optional image loading capability. This allows ComfyUI workflows to run even when the node is not pointing to any image.  

### Inputs

- An Image. Default: `"None"`

  

### Outputs

- An image and/or a mask
- Returns `None` if no image is selected or if the file doesn't exist

  

### Special Behavior

-  Unlike standard ComfyUI LoadImage, this node can work with `"None"` as input, returning `None` instead of raising an error.
  

### Example Use Cases

- Build ViewComfy apps or ComfyUI based APIs with optional image inputs.

  

---

  

## Anything Inversed Switch

Routes a single input to one of multiple outputs (up to 10) based on an index value. All non-selected outputs are blocked from execution, making this useful for conditional execution paths. 

### Inputs

- An index value to determine which output to route the input to. Default: `0`

- The value to route to the selected output. This can be of any data type.
  

### Outputs

- Only the output at the position matching `index` will receive the input value

- All other outputs are blocked. 

  

### Special Behavior

-  Nodes downstream of non-selected outputs will not execute
  

### Example Use Cases

- Creating ViewComfy apps with conditional execution paths based on a user selected index

- Routing data to different processing pipelines based on conditions

- Building switch/case-like logic in ComfyUI

  

---

  

## Show Error Message

Conditionally displays an error message and halts workflow execution. 

  

### Inputs

- A boolean to control whether to raise an error or not. Default: `True`

- The first and second parts of the error message. 


### Outputs

-  An error showing both parts of the messages combined. 
  

### Example Use Cases

- Validating workflow inputs

- Creating conditional error messages based on workflow state

- Implementing user-friendly error handling in complex workflows



---

## Save text

Save a string in the output folder as a text file. 

### Inputs

- Any string

### Example Use Cases

- Display text in a viewcomfy app

---

## Download and Save Video

Downloads a video from a URL and saves it to the output directory. Designed to be fast and reliable when called via API, skipping the usual tensor conversion processes.

### Inputs

- A URL pointing to the video file
- A filename prefix for the downloaded video

### Outputs

- Saves the video file to the output directory

### Special Behavior

- The node does not display a video preview in the ComfyUI interface after downloading. The video will still appear in the ComfyUI history tab (left sidebar). This limitation only affects the ComfyUI interface and has no impact when using the node via API or in a ViewComfy app.
- Defaults to `.mp4` if no extension can be determined from the URL or the MIME type

### Example Use Cases

- Fast video downloads with no extra processes
