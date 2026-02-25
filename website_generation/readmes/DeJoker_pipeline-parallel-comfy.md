# Pipeline Parallel for ComfyUI
This custom node provide extra api to run prompt request with parallel execution of independent nodes.

## Installation

To install, clone this repository into `ComfyUI/custom_nodes` folder with `git clone https://github.com/DeJoker/pipeline-parallel-comfy` and restart ComfyUI.

## usage
/parallel/prompt same request parameter with comfyui /prompt, but need fill workflow_name.
```shell
curl localhost:8080/parallel/prompt '{"prompt": {"2":..,"3":..}, "client_id": "prompt_id:"6ea5acdb-ab6f-4127-9dd0-cf34689098d9", "extra_data":{"workflow_name": "workflow-api.json"}}'

curl localhost:8080/parallel/history
```

## Implementation
lock independent node for threadExecutor.


## todo list
- [ ] support multi-workflow name
- [ ] show node execute time

