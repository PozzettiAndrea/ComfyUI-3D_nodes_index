# ComfyUI-ProductPromptGenerator

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) designed to generate structured prompts for product display images based on analysis results from Vision Language Models (like Qwen2.5-VL).

This node is particularly useful for e-commerce workflows where you want to automatically generate image-to-image prompts based on product characteristics (wearable, handheld, etc.).

## Features

- **Automated Prompt Logic**: Automatically determines the best action verb ("wear", "hold", or "use") based on product attributes.
- **JSON Parsing**: Robustly parses JSON outputs from LLM/VLM nodes (handles markdown code blocks).
- **Context Aware**: Integrates product type, background, and interaction details into a cohesive natural language prompt.

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ComfyUI-ProductPromptGenerator.git
   ```
3. Restart ComfyUI.

## Usage

The node **ProductPromptGenerator(Simple)** accepts three string inputs, typically outputs from a VLM (Vision Language Model) that analyzes a product image.

### Inputs

1. **qwen_output_1** (String): Analysis of product type and background.
   - Expected JSON format:
     ```json
     {
         "商品类型": "Ring",
         "是否支持手持": "No",
         "推荐背景": "Jewelry Store"
     }
     ```

2. **qwen_output_2** (String): Analysis of interaction.
   - Expected JSON format:
     ```json
     {
         "交互方式": "wearing on a finger"
     }
     ```

3. **qwen_output_3** (String): Analysis of wearability.
   - Expected JSON format:
     ```json
     {
         "是否支持佩戴": "Yes"
     }
     ```

### Output

- **prompt** (String): A fully constructed prompt ready for CLIP Text Encode or other conditioning nodes.
  - Example Output:
    > "请让图中模特佩戴图中戒指，背景为珠宝店，要求保持图中戒指与模特相对比例、大小、位置不变，画面聚焦模特与商品，人脸细节必须完整，戒指正确佩戴在模特的一根手指上。"

## Example Logic

- If `是否支持佩戴` is "Yes" -> Verb: **"佩戴" (Wear)**
- If `是否支持手持` is "Yes" -> Verb: **"手持" (Hold)**
- Default -> Verb: **"使用" (Use)**

