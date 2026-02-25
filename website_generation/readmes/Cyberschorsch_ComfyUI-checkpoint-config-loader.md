# ComfyUI Checkpoint Loader Config

Provides a custom node to load config for sampler nodes from a yaml file.

## Installation

Add this project to your custom_nodes directory.

## Usage

### Setup

Create a new directory called "checkpoints" in the _models/configs_ directory.

Create one or more yaml files which you can use later in your workflow. 

See _example_config.yaml_ as a starting point.

### Use the custom node

Add node from utils->Checkpoint Loader Config and choose the yaml file you want to use.

You can connect all available connections to the nodes you want, e.g. KSampler. 
To convert a manual input in the KSampler Node make a right-click on the KSampler Node and select _Convert Widet to Input_
and the property you want to connect, e.g. steps.



