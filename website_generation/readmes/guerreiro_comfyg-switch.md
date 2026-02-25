# Comfyg Switch

Comfyg Switch is a custom node that dynamically selects model configuration parameters based on the chosen checkpoint.

It reads model-specific settings from a JSON file (model_configs.json). You can change the values, but updating the node will lose all changes.

Alternatively, you can create your own custom file, named "my_model_configs.json," place it in the node's root directory, and then insert your settings into the new file, using the same pattern as the default file. You can even overwrite some settings from the default file by creating an item with the same name as the model and changing any attributes.

Now, updating the node won't lose your custom settings because this file isn't in Git.

#### 2025-08-24:
- Preview/Load model config when change checkpoint and input to node fields;
- No need "use_custom_input" field anymore, when load the config, change all fields and then output to queue;
- Preview Selected Config in the "config_source" field;
- Wildcard for config name, ex: a "anything*" config name, loads the same config for models "anythingv3", "anything_beta_v4", etc...;
- Load a global default config, if model config not found in JSON file;
- Change the JSON file, not need restart ComfyUI anymore, because changing the checkpoint trigger a reload for JSON file;

## Inputs

- checkpoint_model: This value is used to determine which configuration to load.
- config_source (STRING): The name of loaded model config from JSON file.
- steps (INT): Number of inference steps (default: 30).
- refiner_steps (INT): Number of inference steps for enhancement (default: 30).
- cfg (FLOAT): Classifier-free guidance scale (default: 7.0).
- sampler (SAMPLER)
- scheduler (SCHEDULER)

## Outputs

- MODEL_NAME (STRING)
- CONFIG_SOURCE (STRING)
- STEPS (INT)
- REFINE_STEPS (INT)
- CFG (FLOAT)
- SAMPLER (SAMPLER)
- SCHEDULER (SCHEDULER)

## Example

See the file: ComfygSwitch-example.json

# Roadmap (or ideas)

- Maybe load configs from an external database or something like that, to avoid update the config file everytime;
- Import each model config dinamically from CivitAI API and use the config file as optional (maybe use LLM to read the model content and create the config object);
- When switch the model, load the config data into the node inputs (steps, cfg, etc...) and let us see the values before start queue, or change them too;
- Load more details about the selected model to help us with the workflow (result examples, tips, prompts...);

# Contributing

Contributions and suggestions are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.

# License

This project is licensed under the MIT License.
