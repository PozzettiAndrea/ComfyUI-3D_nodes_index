# Civitai Prompt Stats Node

## Description

When using generative models, it's often difficult to know which prompts and trigger words work best. The **Civitai Prompt Stats Node** is an all-in-one information hub that helps you master any model from Civitai.

This node helps you:

  * Fetch **positive / negative prompts** used in community-uploaded images to understand how others are using a model.
  * For **LoRA/LyCORIS models**, extract crucial **trigger words** from two authoritative sources:
    1.  The local `.safetensors` file's metadata (`ss_tag_frequency`).
    2.  The official Civitai API (`trainedWords`).
  * Quickly get a 360-degree view of a model's usage: official triggers, community trends, and raw training data tags.

**Multi-Layer Caching**: To ensure maximum speed and minimal API calls, the node uses several layers of caching. File hashes, official trigger words from the Civitai API, and community prompt statistics are all cached separately in the `data` folder.

## Outputs

The nodes provide different outputs based on the model type, giving you exactly the information you need.

### Civitai Prompt Stats (CKPT)

Designed for base models, focusing on community usage patterns.

| Output | Description |
| :--- | :--- |
| `positive_prompt` | A ranked list of the most frequently used positive prompts from community images. |
| `negative_prompt` | A ranked list of the most frequently used negative prompts from community images. |

### Civitai Prompt Stats (LORA)

A comprehensive analysis tool for LoRA/LyCORIS models, providing both community prompts and essential trigger words.

| Output | Description |
| :--- | :--- |
| `positive_prompt` | A ranked list of the most frequently used positive prompts from community images. |
| `negative_prompt` | A ranked list of the most frequently used negative prompts from community images. |
| `metadata_triggers` | Trigger words extracted from the **local file's metadata** (`ss_tag_frequency`). This reflects the raw tags used during training. |
| `civitai_triggers` | Official trigger words fetched from the **Civitai API** (`trainedWords`). This reflects the model author's explicit recommendations. |

*If no trigger words are found for a specific source, the output will clearly indicate that.*

## Parameters

| Parameter | Description |
| :--- | :--- |
| `file_name` | Select your local model file (CKPT or LORA). |
| `top_n` | Top N most frequent community prompts to output (default 20). |
| `max_pages` | Maximum pages of images to fetch per model (default 3). |
| `sort` | Sorting method for images: "Most Reactions" / "Most Comments" / "Newest". |
| `timeout` | Request timeout in seconds (default 10). |
| `retries` | Number of retries for failed requests (default 2). |
| `force_refresh` | Force refresh all caches for the selected model, default "no". |

## How to Use

1.  Place this project under ComfyUI’s `custom_nodes` directory, for example:
    ```
    ComfyUI/custom_nodes/comfyui_civitai_prompt_stats
    ```
2.  Restart ComfyUI. You will see two new nodes under the `Civitai` category:
      * **Civitai Prompt Stats (CKPT)** → for Checkpoint models
      * **Civitai Prompt Stats (LORA)** → for Lora models
3.  Select your local model file in the node, configure parameters, and run to get the results.
4.  The outputs vary by node. The LORA node provides four distinct string outputs. You can connect each to a `Show Text` node to view all the information at once.
![Civitai Prompt Stats (CKPT).png](image/Civitai%20Prompt%20Stats%20%28CKPT%29.png)
![Civitai Prompt Stats (LORA).png](image/Civitai%20Prompt%20Stats%20%28LORA%29.png)
5.  Results are cached to ensure subsequent runs are nearly instant. Set `force_refresh` to `yes` to fetch new data from Civitai.

## Acknowledgement

This project was inspired by [Extraltodeus/LoadLoraWithTags](https://github.com/Extraltodeus/LoadLoraWithTags).

The code logic for fetching trigger words in the LoRA node (`metadata_triggers` and `civitai_triggers`) is based on and uses parts of the [idrirap/ComfyUI-Lora-Auto-Trigger-Words](https://github.com/idrirap/ComfyUI-Lora-Auto-Trigger-Words) project. Special thanks to the original author.

-----

-----

## 功能说明

在使用生成模型时，我们常常不清楚哪些提示词和触发词效果最好。**Civitai Prompt Stats 节点**是一个一站式的信息中心，旨在帮你掌握任何来自 Civitai 的模型。

本节点可以帮助你：

  * 获取社区用户在 Civitai 上分享图片时使用的**正向 / 负向提示词**，了解大众用法。
  * 针对 **LoRA/LyCORIS 模型**，从两个权威来源提取关键的**触发词**：
    1.  本地 `.safetensors` 文件元数据 (`ss_tag_frequency`)。
    2.  Civitai 官方 API (`trainedWords`)。
  * 快速获得模型的 360 度全景视图：官方触发词、社区流行用法、以及原始训练标签。

**多层缓存机制**：为确保最快速度和最少的 API 请求，本节点采用了多层缓存策略。文件哈希、来自 Civitai API 的官方触发词、以及社区提示词统计数据都会被分别缓存在项目目录下的 `data` 文件夹中。

## 输出端口说明

本工具根据模型类型提供了不同的节点，每个节点的输出都经过精心设计，为你提供最需要的信息。

### Civitai Prompt Stats (CKPT)

专为基础模型设计，侧重于分析社区的通用玩法。

| 输出端口 | 说明 |
| :--- | :--- |
| `positive_prompt` | 从社区图片中统计出的、最常见正向提示词的排序列表。 |
| `negative_prompt` | 从社区图片中统计出的、最常见负向提示词的排序列表。 |

### Civitai Prompt Stats (LORA)

为 LoRA/LyCORIS 模型设计的综合分析工具，同时提供社区用法和核心触发词。

| 输出端口 | 说明 |
| :--- | :--- |
| `positive_prompt` | 从社区图片中统计出的、最常见正向提示词的排序列表。 |
| `negative_prompt` | 从社区图片中统计出的、最常见负向提示词的排序列表。 |
| `metadata_triggers` | 从**本地文件元数据** (`ss_tag_frequency`) 中提取的触发词。这反映了模型训练时使用的原始标签。 |
| `civitai_triggers` | 从 **Civitai API** (`trainedWords`) 获取的官方触发词。这反映了模型作者明确推荐的用法。 |

*如果某个来源未能找到触发词，对应的输出端口会明确提示。*

## 参数说明

| 参数 | 说明 |
| :--- | :--- |
| `file_name` | 选择你本地的模型文件（CKPT 或 LORA）。 |
| `top_n` | 输出社区最常见提示词的前 N 个（默认 20）。 |
| `max_pages` | 每个模型最多爬取的图片页数（默认 3）。 |
| `sort` | 图片排序方式，可选 "Most Reactions" / "Most Comments" / "Newest"。 |
| `timeout` | 请求超时时间（秒，默认 10）。 |
| `retries` | 请求失败重试次数（默认 2）。 |
| `force_refresh` | 是否强制刷新该模型的所有缓存，默认 "no"。 |

## 使用方法

1. 将项目放入 ComfyUI 的 `custom_nodes` 目录，例如：
   ```
   ComfyUI/custom_nodes/comfyui_civitai_prompt_stats
   ```
2. 重启 ComfyUI，你会在 `Civitai` 分类下看到两个新节点：
     * **Civitai Prompt Stats (CKPT)** → 用于 Checkpoint 模型
     * **Civitai Prompt Stats (LORA)** → 用于 Lora 模型
3. 在节点中选择本地模型文件，设置参数后运行，即可得到分析结果。
4. 输出因节点而异。Checkpoint 节点提供两个输出，而 LORA 节点提供四个。你可以将每个端口都连接到一个 `Show Text` 节点，以便同时查看所有信息。
![Civitai Prompt Stats (CKPT).png](image/Civitai%20Prompt%20Stats%20%28CKPT%29.png)
![Civitai Prompt Stats (LORA).png](image/Civitai%20Prompt%20Stats%20%28LORA%29.png)
5. 结果会被缓存，后续再次运行几乎瞬时完成。如需从 Civitai 获取最新数据，请将 `force_refresh` 设为 `yes`。

## 鸣谢

本项目在开发过程中参考了 [Extraltodeus/LoadLoraWithTags](https://github.com/Extraltodeus/LoadLoraWithTags) 的思路，特此感谢。

LoRA 节点中用于获取触发词（`metadata_triggers` 和 `civitai_triggers`）的相关代码逻辑，借鉴并使用了 [idrirap/ComfyUI-Lora-Auto-Trigger-Words](https://github.com/idrirap/ComfyUI-Lora-Auto-Trigger-Words) 项目的部分代码，在此特别感谢原作者。
