# ComfyUI Segmentation Agent

![](https://raw.githubusercontent.com/adambarbato/ComfyUI-Segmentation-Agent/refs/heads/main/assets/example.png)

A ComfyUI custom node that uses a Vision LLM agent to segment specific characters in images using [SAM 3](https://github.com/facebookresearch/sam3).

## Features

- Uses an Agent loop to iteratively build up an image specific segmentation mask from natural-language prompts by segmenting multiple smaller concepts
- Allows either local GGUF LLM (via llama-cpp-python) or OpenRouter for LLM access
- Leverages SAM3 for high-quality segmentation
- Handles complex concepts that aren't in SAM 3's built-in vocabulary (woman *with* a bag, mythical creatures like centaurs, etc.) by decomposing them into component parts

## Background

[SAM 3](https://github.com/facebookresearch/sam3) is an amazing new segmentation model that is trained on "open-vocabulary" segmentation, meaning you can segment a wide variety of concepts with prompt-like inputs like "woman", "elephant", or even slightly more advanced concepts like "blonde man". This is very useful for the use-cases SAM was made for, but it's vocabulary is much smaller than LLMs and is less useful in more granular work (like Agentic AI art) where being able to segment image-specific concepts like "the fourth woman from the left holding a suitcase" is needed.

Previous work like [Grounded SAM](https://github.com/IDEA-Research/Grounded-SAM-2) and [ByteDance's Sa2VA](https://github.com/bytedance/Sa2VA) ([and my ComfyUI node based on that project](https://github.com/adambarbato/ComfyUI-Sa2VA)) tried to address these usecases by adding a language layer on top of SAM that would give it better concept understanding. Along with the release of SAM 3, the SAM team released an example notebook of a [SAM 3 Agent](https://github.com/facebookresearch/sam3/blob/main/examples/sam3_agent.ipynb) that demonstrated how SAM 3 could be used in a Vision LLM agentic loop to segment more advanced concepts. This repo is an adaptation of that agent into the ComfyUI environment.

## How It Works

1. The agent analyzes the base image and character description prompt
2. It chooses one or more appropriate simple noun phrases for segmentation (e.g., "woman", "brown hair", "red dress") that will likely be known by the SAM 3 model
3. SAM 3 generates masks for those phrases
4. The masks are numbered and visualized on the original image and shown to the agent
5. The agent evaluates if the masks correctly segment the character
6. If correct, it accepts all or a subset of the masks that best cover the intended character; if not, it tries additional phrases
7. This iterates until satisfactory masks are found or max_iterations is reached and the agent fails

### Limitations

This agentic process works, but the results are often worse (and much slower) than purpose-trained solutions like [Grounded SAM](https://github.com/IDEA-Research/Grounded-SAM-2) and [Sa2VA](https://github.com/bytedance/Sa2VA). The agentic method CAN get even more correct results than those solutions if used with frontier vision models (mostly the Gemini series from Google) but I've found that the rate of hallucinations from the VLM often cancels out the benefits of checking the segmentation results rather than going with the 1-shot approach of Grounded SAM/Sa2VA.

This may still be the best approach if your usecase needs to be 100% agentic and can tolerate long latencies and needs the absolute highest accuracy. I suspect using frontier VLMs paired with many more iterations and a more aggresive system prompt may increase accuracy at the cost of price and speed.

### Future Improvements

1. Refine the system prompt to include known-good SAM 3 prompts
    - A lot of the system's current slowness involves the first few steps where the agent may try phrases that are too complicated for SAM and result in 0 masks being generated (often this is just a rephrasing of the user's initial prompt). Including a larger list of known-useful SAM 3 prompts may help speed up the agentic loop at the cost of more system prompt tokens.

2. Use the same agentic loop but with Grounded SAM or Sa2VA
    - What may produce the best results is to pair this agentic loop with one of the segmentation solutions that has a more open vocabulary. Although not as powerful as the new SAM 3, Grounded SAM or Sa2VA may play better with the verbose tendencies of most VLMs and their smaller number of masks produced per prompt may help cut down on hallucinations.

3. Try with bounding box/pointing VLMs like Moondream
    - The original SAM 3 Agent (which is reproduced here) uses text prompts from the VLM to SAM to indicate what should be segmented, but, as mentioned, SAM's native language is not text, it's visuals. Some VLMs (like the Moondream series) are trained to produce bounding boxes/points. Putting one of those into a similar agentic loop may reduce the issues described above, but may introduce its own issue in deciding what each system considers segmentable within a bounding box.

## Installation

1. Clone or copy this node pack into your ComfyUI `custom_nodes` directory or install via the ComfyUI Manager Registry
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Note:** For `llama-cpp-python`, you may need to install a pre-compiled wheel for your hardware.
   - I recommend [JamePeng's llama-cpp-python fork](https://github.com/JamePeng/llama-cpp-python/releases) which supports newer vision models (required for this to work)
   - CUDA/Python 3.12 example: `pip install llama-cpp-python --extra-index-url https://github.com/JamePeng/llama-cpp-python/releases/download/v0.3.18-cu130-AVX2-linux-20251220/llama_cpp_python-0.3.18-cp312-cp312-linux_x86_64.whl`
   - See [llama-cpp-python](https://github.com/JamePeng/llama-cpp-python/releases) for your specific backend/Python combo

3. Download models:
   - Place your GGUF LLM model and mmproj files in `ComfyUI/models/llm_gguf/` (same local as [Searge_LMM](https://github.com/SeargeDP/ComfyUI_Searge_LLM))
   - Place [`sam3.pt`](https://huggingface.co/facebook/sam3) in `ComfyUI/models/sam3/` (this may already be present if you use other SAM 3 nodes)

## Recommended Models

A vision-capable model is required for this node to work since the LLM needs to judge the masks that come out of SAM 3.
- Local: Gemma 3 27b and Qwen 3 VL 30b work best, but I haven't tested too many others
- Cloud: Gemini 2.5 and 3 Flash produce the best results for this node of all the models I've tried

## Usage

### Option 1: Local LLM (SAM3 Character Agent)
1. Add the **SAM3 Character Agent (Local)** node to your workflow
2. Connect an image input
3. Enter a character description (e.g., "The woman with long brown hair wearing a red dress")
4. Select your LLM and mmproj models from the dropdowns
5. Run the workflow - the node will iteratively refine masks until satisfied or max iterations reached

### Option 2: Cloud LLM via OpenRouter (SAM3 Character Agent (OpenRouter))
1. Add the **SAM3 Character Agent (OpenRouter)** node to your workflow
2. Connect an image input
3. Enter a character description
4. Provide your OpenRouter API key (get free credits at https://openrouter.ai)
5. Select a model (recommended: `google/gemini-3-flash-preview` for best quality)
6. Run the workflow


## Node Inputs

### SAM3 Character Agent (Local)

| Input | Type | Description |
|-------|------|-------------|
| image | IMAGE | The input image to segment |
| character_description | STRING | Description of the character to segment |
| llm_model | COMBO | GGUF model file from `models/llm_gguf/` |
| mmproj_model | COMBO | Vision mmproj file from `models/llm_gguf/` |
| max_iterations | INT | Maximum agentic refinement loops (default: 5, max: 20) |
| confidence_threshold | FLOAT | SAM3 mask confidence threshold (default: 0.5, range: 0.1-1.0) |

### SAM3 Character Agent (OpenRouter)

| Input | Type | Description |
|-------|------|-------------|
| image | IMAGE | The input image to segment |
| character_description | STRING | Description of the character to segment |
| openrouter_api_key | STRING | OpenRouter API key (get at https://openrouter.ai) |
| model_name | STRING | OpenRouter model ID (e.g., `google/gemini-3-flash-preview`) |
| max_iterations | INT | Maximum agentic refinement loops (default: 5, max: 20) |
| confidence_threshold | FLOAT | SAM3 mask confidence threshold (default: 0.5, range: 0.1-1.0) |

## Node Outputs

Both nodes return the same outputs:

| Output | Type | Description |
|--------|------|-------------|
| mask | MASK | Combined segmentation mask covering the target character |
| debug_images | IMAGE | Batch of intermediate mask visualizations (one per segmentation attempt) |

## Credits

- **SAM 3**: Meta AI Research (https://github.com/facebookresearch/sam3)
- **llama-cpp-python**:
    - Original: https://github.com/abetlen/llama-cpp-python
    - Fork: https://github.com/JamePeng/llama-cpp-python

## License

MIT
