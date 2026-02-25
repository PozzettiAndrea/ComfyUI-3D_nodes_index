# DJZ_ENH - Enhanced Prompt Management System for ComfyUI

A powerful ComfyUI custom node package for managing and utilizing advanced system prompts with multi-shot enhancement capabilities, designed specifically for Vision Language Models (VLMs) and dynamic prompt workflows.

## Features

- **Dynamic System Prompt Loading**: Browse and load system prompts from organized markdown files
- **Multi-Prompt JSON Extraction**: Parse and extract multiple enhanced prompts from structured JSON responses
- **Vision Language Model Integration**: Optimized templates for VLMs like Qwen2.5VL
- **LoRA-Aware Prompting**: Enhanced accuracy through trained caption knowledge integration
- **Template-Based Enhancement**: Consistent multi-angle prompt generation with cinematic perspectives

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```

2. Clone or download this repository:
   ```
   git clone https://github.com/MushroomFleet/DJZ-ENH-system
   ```

3. Restart ComfyUI

## Core Components

### 1. ZenkaiENH Node (`ZenkaiENH.py`)

**Purpose**: Dynamically loads system prompts from the `ENH-store/` directory

**Features**:
- Automatic detection of `.md` files in ENH-store folder
- Dropdown selection interface for easy prompt switching
- Real-time file change detection
- UTF-8 encoding support
- Automatic folder creation

**Inputs**:
- `enh_file`: Dropdown list of available `.md` prompt files

**Outputs**:
- `STRING`: Complete content of the selected prompt file

**Usage**:
1. Place your system prompt `.md` files in the `ENH-store/` folder
2. Connect the ZenkaiENH node to your Ollama/API nodes
3. Select desired prompt from dropdown
4. System prompt is automatically loaded and sent to output

### 2. ENH_JSON Node (`ENH_JSON.py`)

**Purpose**: Extracts multiple prompts from JSON-formatted LLM responses

**Features**:
- Robust JSON parsing with markdown code block handling
- Multiple format support (direct keys, array format, object format)
- Automatic fallback to safe default prompts
- Enhanced error handling and logging
- Trailing comma and quote cleanup

**Inputs**:
- `json_text`: Multi-line string containing JSON response from LLM

**Outputs**:
- `output1`: First extracted prompt (Standard Shot)
- `output2`: Second extracted prompt (Closeup Shot)
- `output3`: Third extracted prompt (Wide Shot)  
- `output4`: Fourth extracted prompt (Action Shot)

**Supported JSON Formats**:

```json
// Format 1: Direct keys
{
  "prompt1": "description here",
  "prompt2": "description here",
  "prompt3": "description here",
  "prompt4": "description here"
}

// Format 2: Array format
{
  "prompts": ["desc1", "desc2", "desc3", "desc4"]
}

// Format 3: Object array format
{
  "prompts": [
    {"prompt": "desc1"},
    {"prompt": "desc2"},
    {"prompt": "desc3"},
    {"prompt": "desc4"}
  ]
}
```

### 3. ENH-store Templates

The `ENH-store/` directory contains system prompt templates designed for specific enhancement workflows.

#### Example: `t2i_ENH-vision-4shot.md`

**Purpose**: Multi-angle image prompt enhancement for VLMs

**Key Features**:
- Vision analysis protocol for image inputs
- Four distinct camera perspectives (Standard, Closeup, Wide, Action)
- Consistency rules across all generated prompts
- Professional photography and cinematography terminology
- 80-100 word target length per prompt

**Shot Types Generated**:
1. **Standard Shot**: Medium shot, balanced composition
2. **Closeup Shot**: Portrait perspective, detailed features
3. **Wide Shot**: Environmental context, establishing shot
4. **Action Shot**: Dynamic movement, dramatic angles

## Workflow Integration

### Basic Workflow Setup

1. **Load System Prompt**:
   - Add `ZenkaiENH` node
   - Select desired enhancement template
   - Connect output to your LLM node (Ollama/API)

2. **Process User Input**:
   - Send user prompt + optional image to LLM
   - LLM processes using loaded system prompt
   - LLM returns JSON with 4 enhanced prompts

3. **Extract Multiple Prompts**:
   - Add `ENH_JSON` node
   - Connect LLM JSON output to `json_text` input
   - Use the 4 outputs for different image generations

### Advanced Multi-Shot Workflow

```
[User Input] → [ZenkaiENH] → [LLM Node] → [ENH_JSON] → [4x Image Generation]
                    ↓              ↓           ↓
              [System Prompt] [JSON Response] [4 Enhanced Prompts]
```

**Benefits**:
- Consistent subject details across all variations
- Professional cinematic perspectives
- Enhanced composition and framing
- Reduced prompt engineering time

## Creating Custom Templates

### Template Structure

1. **Header Section**: Clear description of template purpose
2. **Input/Output Specification**: Expected inputs and JSON format
3. **Processing Rules**: Enhancement guidelines and consistency requirements
4. **Technical Specifications**: Quality descriptors, style guidelines
5. **Example Output**: Sample JSON structure

### Template Guidelines

- Use markdown format (`.md` files)
- Place files in `ENH-store/` directory
- Include clear JSON output format specifications
- Define consistency rules for multi-prompt generation
- Specify target word counts and quality standards

### LoRA Integration

For LoRA-aware prompting:
1. Include LoRA caption knowledge in system prompt
2. Reference trained descriptions for alignment
3. Leverage vision analysis for consistency
4. Maintain coherency across prompt variations

## Best Practices

### System Prompt Design
- Keep JSON output rules clearly defined
- Maintain flexibility for different input types
- Include fallback behaviors for edge cases
- Test with various VLM models

### Workflow Optimization
- Use consistent naming conventions for prompt files
- Organize templates by use case (t2i, style, character, etc.)
- Test multi-prompt outputs for consistency
- Monitor LLM token usage

### Quality Control
- Verify JSON output format compliance
- Check prompt consistency across all outputs
- Validate enhancement quality improvements
- Test with different image inputs

## Troubleshooting

### Common Issues

**No .md files found**:
- Ensure files are placed in `ENH-store/` directory
- Check file extensions are `.md`
- Restart ComfyUI after adding files

**JSON parsing errors**:
- Check LLM output format matches expected JSON
- Verify no markdown code blocks in JSON
- Ensure proper JSON syntax (no trailing commas)

**Inconsistent prompts**:
- Review system prompt consistency rules
- Check if VLM is following template guidelines
- Adjust temperature/generation parameters

**Empty outputs**:
- Verify JSON contains required keys
- Check fallback prompt functionality
- Review LLM response completeness

## Technical Requirements

- **ComfyUI**: Latest version recommended
- **Python**: 3.8+ with UTF-8 support
- **VLM Support**: Qwen2.5VL, GPT-4V, or similar vision models
- **Memory**: Sufficient for multi-prompt processing

## Contributing

1. Create new templates in `ENH-store/` directory
2. Follow existing template structure and naming conventions
3. Test with multiple VLM models
4. Document specific use cases and requirements

## License

[Add your license information here]

## Changelog

### v1.0.0 - Initial Release
- ZenkaiENH system prompt loader
- ENH_JSON multi-prompt extractor  
- t2i_ENH-vision-4shot template
- Basic workflow integration
- LoRA-aware prompting foundation

---

*This system transforms single prompts into professional, multi-perspective image generation workflows while maintaining consistency and quality across all outputs.*
