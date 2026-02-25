# Example of connecting to remote combobox and dynamically mirror the selection.

![image](https://github.com/user-attachments/assets/55e34d34-0e68-4dd1-8319-8f7ca2e8c4fa)

How to connect to a remote combobox and iteract with it's value list while keeping the selection in sync.

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

## Combo Dynamic (cozy)

Connect the `OPTIONS` output to populate the local combobox and see the list displayed in the text area.

Change the combobox value and get a dynamic update in the remote combobox.

You could use something to iterate the list, or automatically select a default in the remote box.
