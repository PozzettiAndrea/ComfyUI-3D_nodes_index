# ComfyUI-Foxpack
A collection of nodes to automate workflows. I created the node to save nodes within the workflows. I therefore developed it primarily for my own purposes.

# Get Started

## Install

1. Install the great [ComfyUi](https://github.com/comfyanonymous/ComfyUI).
2. Clone this repo into `custom_modules`:
    ```
    cd ComfyUI/custom_nodes
    git clone https://github.com/gisu/comfyui-foxpack.git
    ```
3. Start up ComfyUI.

## Smart Sampler Setup (SSS)

![SmartSamplerSetup](https://raw.githubusercontent.com/gisu/comfyui-foxpack/main/assets/smartsampler.png)

Consisting of three nodes, the override node is optional.

You still need two nodes, one to pass the name of the model into the selector. WAS nodes have a checkpoint loader that optionally outputs the name of the checkpoint.
There is also a node for multiline string literals in which you can create the setups.

### Setup
Each setup is noted as follows:

```cfg/steps/scheduler/sampler```

CFG and steps can consist of a value, but also of a range (`3-10`). Schedulers and samplers can be created as a list or as individual strings.

**Example**

```
!NAMEOFTHECHECKPOINT1="4/10-40/karras/dpmpp_2m"
!NAMEOFTHECHECKPOINT2="2-6/20-60/karras,exponential/dpmpp,dpmpp_3m_sde"
```

### Setup Selector

**Input**
- checkpoint_name: The name of the checkpoint for which the setup is being selected.
- checkpoint_setups: A list or dictionary containing the setups available for each checkpoint.
- prefix: Checkpoint name prefix
- delmiter: Seperator for the setup properties
- default_setup: Used if no suitable setup is found

**Output**
- set_[X]: Setup settings as strings
- setup_text: Prepared String with all settings
- setup: Settings as list

### Base Sampler Setup
Sets the settings according to the setup specifications. CFG and Steps are limited to the values, so they cannot be increased or decreased. Scheduler and sampler can only be selected as specified in the setup, if the selection does not match, the first value of the setup is used. For example, if the setup says `dpmpp_2m,dpmpp_3m_sde` for samplers, `dpmpp_2m` will be used if the user selects `euler`.

_Unfortunately it is not yet possible for me to limit the values within the dropdowns and input fields, as I do not yet know how to build this in ComfyUI. Therefore the filtering takes place after the selection_

**Input**
- setup: The settingslist from the selector
- cfg, steps, scheduler, sampler: base setup, will be limited

**Output**
- setup_text: Prepared String with all settings
- selected_setup: Limited settings

### Override Sampler Setup
Optional node with which you can overwrite the settings, e.g. to test settings

**Input**
- setup: The settingslist from the selector
- override: activate the override
- cfg, steps, scheduler, sampler: override values, only used if the override is activated