# ComfyUI Dataset Helper & Batch Node

This custom node set for ComfyUI provides a `DatasetBatchNode` for automated, sequential processing of datasets, particularly useful for iterative training or batched image/video generation workflows.

## Usage

**Key Features:**

* Loads datasets from local files (JSONL, CSV) or Hugging Face `datasets`.
* Processes individual rows sequentially, triggering a new job for each.
* `magic_number` input automatically tracks the row index across multiple jobs, ensuring seamless dataset iteration even across workflow restarts.
* Offers flexible prompt construction using `mixed_fields_config_json` to combine dataset fields and apply filters.
* *data utilities*: currently only includes `process_miradata.py` script to preprocess the MiraData dataset for this node, but really can use any dataset. These can be found in `./data_utils/` with a separate `README.md` on how to use that.

**Node Configuration (`DatasetBatchNode`)**

* **`dataset_path`:** (Required) Path to your dataset file (JSONL, CSV) or a Hugging Face dataset identifier (e.g., `TencentARC/MiraData`).
* **`prompt_field`:** (Required)  Name of the dataset field containing the base text prompt (e.g., `combined_caption`).
* **`num_rows`:** (Required) Total rows to process. Use `-1` to process the entire dataset.
* **`start_row`:** (Required) Row index to begin processing from (0-indexed).
* **`random_seed`:** (Required) Seed for dataset shuffling, if enabled.
* **`shuffle`:** (Required) Enable dataset shuffling before processing.
* **`magic_number`:** (Optional, but **connect a Constant node with value 0**).  This input is automatically managed; connect a Constant Number node set to `0` and leave it connected (although you can probably just leave it disconnected too - need to test more).
* **`delimiter`:** (Optional) Separator used to join combined caption fields (default: newline `\n`).
* **`text_input`:** (Optional)  Prepended text added to every generated prompt.
* **`mixed_fields_config_json`:** (Optional) JSON configuration for advanced prompt construction. See "Advanced Prompt Construction" below.

**Important:**  Connect an `INT Constant` node set to `0` to the `magic_number` input. This node is managed automatically by the extension and is crucial for sequential processing.

**Advanced Prompt Construction (`mixed_fields_config_json`)**

Use this optional JSON input for sophisticated prompt creation by combining and filtering different fields from your dataset.

**JSON Configuration Format:**

```json
[
    {
        "field": "field_name_1",
        "filter": "filter_expression_1"  // Optional filter
    },
    {
        "field": "field_name_2",
        "filter": "filter_expression_2"  // Optional filter
    },
    // etc etc
]
```

* **`field` (Required):**  The name of a field in your dataset (e.g., `"dense_caption"`, `"short_caption"`).
* **`filter` (Optional):** A Python expression string used to conditionally include data from this field. The expression is evaluated for each row, with `example` representing the current dataset row (dictionary). If the expression evaluates to `True`, the field's value is included in the combined prompt.

## JSON Examples:**

Assuming you are using the "TencentARC/MiraData" dataset, here are some practical examples:

### Example 1: Combine `dense_caption` and `style_caption`**

```json
[
    {
        "field": "dense_caption",
        "filter": ""
    },
    {
        "field": "style_caption",
        "filter": ""
    }
]
```

This configuration will create prompts by concatenating the `dense_caption` and `style_caption` fields from each row, separated by the `delimiter` you specify in the node (default is newline).

### Example 2: Use `short_caption` for clip IDs >= 7.0, otherwise use `camera_caption`**

```json
[
    {
        "field": "short_caption",
        "filter": "example['clip_id'] >= 7.0"
    },
    {
        "field": "camera_caption",
        "filter": "example['clip_id'] < 7.0"
    }
]
```

This example demonstrates conditional prompt creation. For dataset rows where `clip_id` is 7.0 or greater, the `short_caption` will be used. For rows with `clip_id` less than 7.0, the `camera_caption` will be used instead.

### Example 3: Combine all caption fields**

```json
[
    { "field": "dense_caption" },
    { "field": "main_object_caption" },
    { "field": "background_caption" },
    { "field": "camera_caption" },
    { "field": "style_caption" }
]
```

```markdown
This configuration combines all five available caption fields from the MiraData dataset into a single, detailed prompt.

**Important Notes:**

* The `DatasetBatchNode` is designed to work in conjunction with the provided `dataset_batch_automation.js` JavaScript extension. Ensure both the Python node and the JavaScript extension are installed correctly in your `ComfyUI/custom_nodes` directory.
* The `magic_number` input of the `DatasetBatchNode` should be connected to a Constant Number node, but should **not** be manually modified. The automation script manages this value.
```
