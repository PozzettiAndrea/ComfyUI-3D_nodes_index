# 📦 ComfyForEach: Custom ComfyUI Nodes for Batch Image Processing and Used in AWS

![version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![license](https://img.shields.io/badge/license-MIT-green.svg)

A collection of ComfyUI custom nodes designed for image batch processing, per-index image operations, and AWS integration using EventBridge.

[👉 Comfy Registry Link](https://registry.comfy.org/nodes/foreach)

## 📁 Directory Structure

```
custom_nodes/
└── Comfy_ForEach/
    ├── __init__.py
    ├── context.py
    ├── task_manager.py
    ├── loader_nodes.py
    ├── index_selector_nodes.py
    ├── logic_nodes.py
    ├── save_nodes.py
    ├── aws_event_node.py
    └── requirements.txt
```

## ✅ What needs to be modified in the ComfyUI

**`execution.py`**

```python
######### Error Logging #########
try:
    results.append(getattr(obj, func)(**inputs))

except Exception as e:
    import logging
    from datetime import datetime
    import traceback
    import boto3
    import custom_nodes.Comfy_ForEach.context as context
    import json

    logger = logging.getLogger("comfy_node_error")
    node_name = obj.__class__.__name__
    error_msg = f"[ERROR {datetime.now().isoformat()} | TaskID:{context.get_task_id()} | Node: {node_name} | Index: {index} | {type(e).__name__}: {e}"

    logger.error(error_msg)
    logger.error(traceback.format_exc())

    event = boto3.client("events",region_name="us-east-1")

    # Changed Your Message
    resp = event.put_events(
        Entries=[
            {
                "Source":"comfyui.ec2",
                "DetailType":"ComfyUI Task State",
                "Detail":json.dumps({
                    "task_id":task_id,
                    "status":"FAILED",
                    "timestamp":datetime.utcnow().isoformat(),
                    "error_msg":error_msg
                }),
                "EventBusName":"default"
            }
        ]
    )
    if resp.get("FailedEntryCount", 0) > 0:
        raise RuntimeError("❌ EventBridge Send Failed")
    else:
        print("✅ EventBridge Send Success")

    raise
#################################
```

**`main.py`**

```python
setup_logger(log_level=args.verbose, use_stdout=args.log_stdout,log_path="./logs")
```

**`app/logger`**

```python
...
from logging.handlers import TimedRotatingFileHandler
import os
...

def setup_logger(log_level: str = 'INFO', capacity: int = 300, use_stdout: bool = False,log_path:str | None=None):
    global logs
    if logs:
        return

    # Override output streams and log to buffer
    logs = deque(maxlen=capacity)

    global stdout_interceptor
    global stderr_interceptor
    stdout_interceptor = sys.stdout = LogInterceptor(sys.stdout)
    stderr_interceptor = sys.stderr = LogInterceptor(sys.stderr)

    # Setup default global logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(logging.Formatter("%(message)s"))
    stream_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))

    if use_stdout:
        # Only errors and critical to stderr
        stream_handler.addFilter(lambda record: not record.levelno < logging.ERROR)

        # Lesser to stdout
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(logging.Formatter("%(message)s"))
        stdout_handler.addFilter(lambda record: record.levelno < logging.ERROR)
        logger.addHandler(stdout_handler)

    logger.addHandler(stream_handler)

    # Error Log
    if log_path:
        os.makedirs(log_path, exist_ok=True)
        error_log_file = os.path.join(log_path, "errors.log")

        error_file_handler = TimedRotatingFileHandler(
            error_log_file,
            when="midnight",
            interval=1,
            backupCount=7,
            encoding="utf-8"
        )
        error_file_handler.suffix = "%Y-%m-%d"
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
        logger.addHandler(error_file_handler)

```

## 🧩 Node Overview

### 🔹 TaskIDStorageNode

- Stores a task ID in global memory (context.py) for use across the workflow.

- **Category** : Workflow Utils

- **Output** : task_id (STRING)

### 🔹 FolderImageLoaderNode

- Loads all .png images from a specified folder.

- Outputs a list of image tensors and their filenames.

- **Category** : ComfyForEach/Load

- **Outputs** : image_list (IMAGE), image_name_list (STRING)

### 🔹 IndexedImageSelectorNode

- Selects a specific image from a list using an index.

- **Category** : ComfyForEach/Select

- **Output** : image (IMAGE)

### 🔹 IndexedNameSelectorNode

- Selects a specific image from a list using an index.

- **Category** : ComfyForEach/Select

- **Outputs** : file_name (STRING)

### 🔹 IsLastIndexNode

- Checks whether the current index is the last in a sequence.

- Useful for triggering events only once at the end of a loop.

- **Category** : ComfyForEach/Logic

- **Output** : is_last (BOOLEAN)

### 🔹 SaveExactNameImageNode

- Saves an image tensor with an exact filename and folder path.

- **Category** : ComfyForEach/Save

- **Output** : None (Terminal node)

### 🔹 EventBridgeTriggerNode

- Simulates AWS EventBridge notification.

- Writes a SUCCESS or FAILED event as a .json log based on is_last. (🔥 Please change it to the region of your **Event Bridge** that you will definitely request. And please also grant it from **IAM**.)

- **Category** : ComfyForEach/AWS

- **Output** : None (Terminal node)

### 🔹 StringViewer

- Displays two input string directly in the terminal

- Can be used as a terminal output node for debugging or displaying intermediate results.

- **Category** : ComfyForEach/PreLoad

- **Output** : None (Terminal node)

### 🔹 LoadPreCheckpointModel

- Loads and validates a pre-loaded checkpoint model.

- Primarily used to check the successful loading of a checkpoint model before proceeding with further processing.

- **Category** : ComfyForEach/PreLoad

- **Output** : STRING

### 🔹 LoadPreControlNetModel

- Loads and validates a pre-loaded ControlNet model.

- Verifies that the ControlNet model object is not empty.

- **Category** : ComfyForEach/PreLoad

- **Output** : STRING

## 🧪 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`

```txt
pillow
boto3
opencv-python-headless
numpy
# torch (usually installed with ComfyUI)
```

## 🔧 How to Use

1. Clone or copy this into your ComfyUI/custom_nodes/Comfy_ForEach/ directory.

2. Launch ComfyUI. The nodes will appear under categories like:

   - ComfyForEach/Load

   - ComfyForEach/Select

   - ComfyForEach/Save

   - ComfyForEach/AWS

   - ComfyForEach/TaskID

   - ComfyForEach/PreLoad

```bash
python3 main.py --use-split-cross-attention --fast --input-directory ./test --output-directory ./test --verbose ERROR
```

3. Build workflows that iterate over image folders and process each image index-by-index.

## 📌 Example Use Case

A loop-style batch processor that:

- Loads all images from a task-specific folder.

- Selects images by index.

- Saves outputs with structured filenames.

- Triggers an event only when the last image is processed.

Used in distributed processing systems where each image may be handled independently but result aggregation is done based on a `task_id` .

## 🛠 Maintainer Notes

- Uses `context.py` to globally store and retrieve task_id across node executions.

- EventBridge simulation can be replaced with real AWS API (boto3.client("events")) as needed.
