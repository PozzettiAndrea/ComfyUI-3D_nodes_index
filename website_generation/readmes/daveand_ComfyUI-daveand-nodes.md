# ComfyUI-daveand-nodes

```
cd custom_nodes
git clone https://github.com/daveand/ComfyUI-daveand-nodes.git
```

## Nodes
### ModelConfigSelector
This node saves a configuration for each checkpoint located in `models/checkpoints/` \
You can enable manual override and also save the current manual values with `save_manual_values` enabled. \
\
<img height="500" alt="image" src="https://github.com/user-attachments/assets/a1ef78b4-6297-4a7f-9813-ae5bf945b6d7" />

| Input      | Type | Description |
|------------|-----------|-------------|
|`ckpt_name` | -         | Select the checkpoint you want to load the configuration for. |
|`manual_values` | BOOLEAN | Enable this if you want to use manual values. This bypasses all the values from the configuration file. |
|`save_manual_values` | BOOLEAN | Enable this if you want to save the manual values to the current checkpoint configuration. | 
|`steps, cfg, sampler, scheduler, clipskip, bypass_clipskip` | INT, FLOAT, SAMPLERS, SCHEDULERS, BOOLEAN, BOOLEAN | Manual values effective only if `manual_values` is enabled |

| Output | Type | Description |
|--------|------|-------------|
|`ckpt_name` | - |  To checkpoint loader. |
|`steps, cfg, sampler, scheduler` | INT, FLOAT, SAMPLERS, SCHEDULERS | To 'KSampler' or other sampler node. |
|`clipskip` | INT | To 'CLIP Set Last Layer' node. |
|`bypass_clipskip` | BOOLEAN | You can use this with an 'if/else' node if you want to be able to bypass the 'Clip Set Last Layer' node. |
|`current_config` | STRING | The current configuration loaded in JSON format. To use with for example 'Show Any' node. |
|`available_configs` | STRING | A list of all the checkpoints currently available in the configuration file. |

