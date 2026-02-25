# Hunyuan LoRA Loader Nodes

This collection provides four additional nodes for loading and managing Hunyuan Video LoRAs in ComfyUI:

## HunyuanLoadAndEditLoraBlocks

Interactive node for editing and applying individual LoRA block settings.  At the moment, it allows you to specifically enable/disable different double blocks when loading the lora.

**Inputs:**
- model: The base model to apply the LoRA to
- lora_name: Select from available LoRAs
- strength: LoRA strength (default: 1.0, range: -10.0 to 10.0)
- save_settings: Whether to save block settings to cache (default: true)
- use_single_blocks: Enable/disable single block layers (default: false)
- double_blocks.0-19: Individual toggles for each double block

## HunyuanLoadFromBlockCache

Loads a LoRA using previously cached block settings.

**Inputs:**
- model: The base model to apply the LoRA to
- lora_name: Select from available LoRAs
- strength: LoRA strength (default: 1.0, range: -10.0 to 10.0)
- use_single_blocks: Enable/disable single block layers (default: false)

## HunyuanLoraFromJson

Applies multiple LoRAs from a JSON configuration.

**Inputs:**
- model: The base model to apply the LoRA to
- json_data: JSON configuration string

**Example:**
```json
[
    {
        "filename": "kerbal30.safetensors",
        "strength": 0.75,
        "use_block_cache": true,
        "use_single_blocks": false
    },
    {
        "filename": "other_lora.safetensors",
        "strength": 0.5,
        "use_block_cache": false,
        "use_single_blocks": true
    }
]
```

## HunyuanLoraFromPrompt

Automatically applies LoRAs based on trigger words in the prompt.

**Inputs:**
- model: The base model to apply the LoRA to
- prompt: The input prompt text
- config_file: YAML config file name (default: "lora_triggers.yaml")

**Example Prompt:**

**Example Config File (lora_triggers.yaml):**
```yaml
loras:
  - filename: kerbal30.safetensors
    strength: 0.75
    use_block_cache: true
    use_single_blocks: false
    keywords:
      - kerbal
      - astronaut
      - spacesuit
```

## Cache Directory

Block settings are stored in the cache directory at:
```
ComfyUI_PixelFun/cache/
```

Each LoRA's block settings are saved as `[lora_name]_blocks.yaml` in this directory.
