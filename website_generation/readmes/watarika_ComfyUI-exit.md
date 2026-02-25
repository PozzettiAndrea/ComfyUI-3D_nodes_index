# ComfyUI-exit

[English][<a href="README_ja.md">日本語</a>]

Custom node to exit ComfyUI.

## Exit when Last Batch
This custom node automatically terminates ComfyUI once all its executions have finished.\
It does not immediately shut down when it appears that “the number of remaining batches is 0”. Instead, it **rechecks multiple times after a set delay** before terminating.

![image](https://github.com/user-attachments/assets/2e105f4c-08f3-462c-8e5e-290870677c48)

### Features
* Simply place it at the end of the graph to **automatically terminate after all batches complete**
* **With rechecks**: After `confirm_delay_sec` seconds, it rechecks `/queue` `confirm_attempts` times at `confirm_interval_sec`-second intervals. If it's 0 every time, it exits.
* **Force exit/Normal exit** selectable (`os._exit(0)` / `sys.exit(0)`)
* Utilizes ComfyUI's **HTTP `/queue` API** (operates without external extensions)

### Parameters
* `any`: Dummy input for the terminal node. Connect it to the output of the final node.
* `confirm_delay_sec` (int): **After the initial “0 remaining” determination**, the wait time (in seconds) before starting rechecks. Allows time for saving or post-processing.
* `confirm_attempts` (int): **Number of retry attempts**. The process ends when all attempts show consecutive 0s.
* `confirm_interval_sec` (int): **Interval between each retry attempt**.
* `base_url` (str): ComfyUI base URL. Change if running outside localhost. Example: `http://127.0.0.1:8188`
* `hard_exit` (bool): `True` for **guaranteed immediate shutdown** via `os._exit(0)`, `False` for `sys.exit(0)` (normal shutdown if possible).
* `http_timeout_sec` (int): Timeout in seconds for fetching `/queue`.

#### Recommended Settings
* Generally, default settings are fine
* For local operation or simple storage only:
  `confirm_delay_sec=3~5`, `confirm_attempts=2~3`, `confirm_interval_sec=2~3`, `hard_exit=True`
* If downstream processes require custom post-processing and you “prefer normal termination whenever possible”:
  Consider setting `hard_exit=False`


## Exit ComfyUI

Exit ComfyUI after a specified number of seconds.

![image](https://github.com/user-attachments/assets/efe0e7a6-2df0-4d68-9d5b-910b3ab5e300)

Use this node if you want Google Colab to automatically terminate after mass generation.
It is necessary to disconnect and delete the Google Colab runtime on the Notebook side.

## Fetch API

Sends a request to the specified URL.

![image](https://github.com/user-attachments/assets/f7e9a497-7579-4f91-ad11-d45e2e15630b)

## Change Log
- V1.2.0 (September 29, 2025)
  - Added `Exit when Last Batch` node
- V1.1.0 (December 31, 2024)
  - Added `Fetch API` node
- v1.0.0 (December 13, 2024)
  - Released `Exit ComfyUI` node
