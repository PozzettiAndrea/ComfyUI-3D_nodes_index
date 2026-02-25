# MultiString Prompt Nodes for ComfyUI

This is a simple but powerful set of custom nodes for ComfyUI, designed to help you manage and sequence multiple prompts from a single, clean interface.

This pack contains two nodes:

---
1.  **`MultiString Prompts`**: A utility node for managing and batching multiple *string* prompts. Ideal for feeding into loops or other nodes that process text.
<img width="324" height="431" alt="image" src="https://github.com/user-attachments/assets/e6ba4cc5-8652-48ab-8728-d73fd84dccaa" />

---

2.  **`MultiString Prompts Encode`**: An all-in-one encoder that takes your prompts and a CLIP model and directly outputs *conditioning* blocks, ready for a KSampler.
<img width="328" height="475" alt="image" src="https://github.com/user-attachments/assets/2b32935b-6a65-441f-a6c3-84145a9791a5" />

---

## How to Install

1.  Navigate to your ComfyUI installation directory.
2.  Go into the `ComfyUI/custom_nodes/` folder.
3.  Create a new folder inside `custom_nodes` (e.g., `MultiStringNodes`).
4.  Place all three files (`multi_prompt_node.py`, `multi_prompt_encode_node.py`, and `__init__.py`) inside that new folder.
5.  **Restart your ComfyUI server.**

The nodes will be available by right-clicking the canvas and selecting **Add Node > MultiString Prompts**.

---

## 1. MultiString Prompts

This is the original string-management node. It's perfect for workflows like sequential video generation where you need to feed a series of different text prompts into your model.

### What It Does

* **5 Prompt Slots:** Provides five large, multiline text boxes for your main prompts.
* **Prefix & Suffix:** Includes two compact, single-line text boxes to add a `prefix` (like style or quality keywords) and a `suffix` to all of your prompts.
* **Enable/Disable Toggles:** You can instantly turn the `prefix` or `suffix` on or off using "true/false" dropdowns, allowing you to test prompts without deleting your keywords.
* **Smart Empty Handling:** If you leave a prompt box empty, the node outputs a completely empty string (it won't just output `prefix,suffix`).
* **List Output:** In addition to 5 individual string outputs, it provides a single `prompt_list` output. This is perfect for feeding all 5 prompts into a "Loop" or "Batch" node for a more compact workflow.

### Inputs & Outputs

* **Inputs**
    * `enable_prefix` (toggle): Set to `true` to use the prefix, `false` to ignore it.
    * `enable_suffix` (toggle): Set to `true` to use the suffix, `false` to ignore it.
    * `prefix` (string): A single-line string added to the *beginning* of each prompt.
    * `suffix` (string): A single-line string added to the *end* of each prompt.
    * `multi_prompt_1` - `multi_prompt_5` (string): Five multiline text boxes for your individual prompts.
* **Outputs**
    * `prompt_1` - `prompt_5` (string): The final, processed string for each corresponding prompt (e.g., `prefix,multi_prompt_1,suffix`).
    * `prompt_list` (LIST): A single ComfyUI list that contains all 5 processed strings.

---

## 2. MultiString Prompts Encode

This is a powerful encoder node that handles both prompt processing and CLIP encoding in one step. It allows you to manage 5 separate positive prompts and one shared negative prompt.

### What It Does

* **Direct-to-Conditioning:** Takes your `CLIP` model as a direct input.
* **5 Positive, 1 Negative:** Provides five multiline text boxes for *positive* prompts and one multiline text box for a *negative* prompt.
* **Prefix & Suffix:** Uses the same powerful prefix/suffix system with toggles, which will be applied to all 6 prompt boxes.
* **Individual Outputs:** Outputs 6 separate `CONDITIONING` blocks (5 positive, 1 negative).
* **Workflow Power:** This is ideal for advanced workflows like regional prompting (where you need separate conditioning for different areas) or for creating prompt sequences where each positive prompt is encoded individually against a single, shared negative prompt.

### Inputs & Outputs

* **Inputs**
    * `clip` (CLIP): The CLIP model to use for encoding.
    * `enable_prefix` (toggle): Set to `true` to use the prefix.
    * `enable_suffix` (toggle): Set to `true` to use the suffix.
    * `prefix` (string): A string added to the *beginning* of all 6 prompts.
    * `suffix` (string): A string added to the *end* of all 6 prompts.
    * `positive_prompt_1` - `positive_prompt_5` (string): Five multiline text boxes for your positive prompts.
    * `negative_prompt` (string): A single multiline text box for your negative prompt.
* **Outputs**
    * `positive_1` - `positive_5` (CONDITIONING): Five separate positive conditioning blocks, one for each input prompt.
    * `negative` (CONDITIONING): A single negative conditioning block.
