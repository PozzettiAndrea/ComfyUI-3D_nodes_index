# Example of Dynamic Combobox changes for ComfyUI

![image](https://github.com/user-attachments/assets/55e34d34-0e68-4dd1-8319-8f7ca2e8c4fa)

An example for how to do the specific mechanism of adding a combobox that dynamically changes values of other widgets in the same node.

## Why is this a thing?

Because a lot of people ask the same questions over and over and the examples are always in some type of compound setup which requires unwinding a lot of extra code or logic that is not required to answer the main question.

## How is this different than having to pull apart all those other repositories?

The example is kept to (at most) two files:
* The python entry point
* The supporting js
This keeps the focus on the actual problem being solved.

The file names for the nodes will match in name to the node example they represent.

## Installation:

Clone this repository to 'ComfyUI/custom_nodes` folder.

There are no extra requirements.

# Node List

## Combo Node (cozy)

Change the combobox value and get a dynamic update in the text box.
