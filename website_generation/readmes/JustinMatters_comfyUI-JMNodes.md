# JMNodes for ComfyUI

Nodes to allow for binary combinations of several additive prompts.
Useful for situations where you want to create every combination of a set of prompts.
Can be more controllable than random picks using comfyUIs built in {option1|option2} prompt syntax

# Installation
1. Clone this repo into `custom_nodes` folder.
2. These nodes have no dependencies so no need to pip install a requirements.txt
3. You will need a combination node to join multiple prompt options together like
4. An example workflow is provided in the repo (it uses some other nodes you can install from comfyUI Manager)

## Nodes:

### Create List of Numbers JM

Given an integer from 0 to 1023, returns a list of every integer up to that number
Useful as an input to `Integer to Boolean Values JM`

### Integer to Boolean Values JM

Converts the list of integers provided by `create List of Numbers JM` (or any other integer input) into binary outputs 
For use by `Switchable Prompt JM` or other Nodes

### Switchable Prompt JM
Takes a string input and passes on either that string or the empty string depending on a boolean input
Can be used with `create List of Numbers JM` and `Integer to Boolean Values JM` to create prompt combinations

### Binary Not JM
Takes a boolean input and inverts it convertinging True to False and vice versa, useful for creating negative prompts
Can be used with  `Integer to Boolean Values JM` and `Switchable Prompt JM` to create appropriate negative prompts
