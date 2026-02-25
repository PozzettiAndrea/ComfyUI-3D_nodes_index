# ComfyUI Ranbooru 节点

一个将 WebUI Forge 插件“Ranbooru”核心能力迁移到 ComfyUI 的自定义节点，支持从各类 Booru 站点搜索帖子并生成可用的提示词（正/负），提供标签清理、评分排序、随机与混合、背景/配色调整、可选缓存与凭据管理等能力。

## 安装
- 将本目录放置到 ComfyUI 的 `custom_nodes/comfyui-ranbooru` 下。
- 依赖：
  - 必需：`requests`
  - 可选：`requests_cache`（启用缓存时更高效）
- 若需凭据保存，请确保有写入权限：`user/credentials/credentials.json`。

## 提供的节点
- Ranbooru Prompt
  - 输出：`positive(STRING)`、`negative(STRING)`
  - 用途：生成正向与负向提示词，可直接连接到 `CLIPTextEncode` 节点，再进入 `KSampler` 等推理节点。

## 快速使用
- 最简单的工作流：
  - `Ranbooru Prompt -> CLIPTextEncode -> KSampler`
- 设置示例：
  - `booru`: `safebooru`
  - `tags`: `1girl,long_hair`
  - `shuffle_tags`: 开启（True）
  - `sorting_order`: `Random`
  - `limit_tags`: `1.0`（不限制）
  - `max_tags`: `50`（上限）
  - 运行后，`positive/negative` 即可作为文本编码输入。

## 参数说明
- `booru`: 选择站点（`safebooru/rule34/danbooru/gelbooru/aibooru/xbooru/e621/konachan/yande.re`）
- `tags(STRING)`: 搜索标签，逗号分隔
- `remove_bad_tags(BOOLEAN)`: 是否移除内置无效/不期望标签
- `remove_tags(STRING)`: 自定义需要移除的标签（支持通配形如 `*text*`）
- `change_background`: 背景策略（不变/添加/移除/全部移除）
- `change_color`: 颜色策略（不变/彩色/有限色/黑白）
- `shuffle_tags(BOOLEAN)`: 是否对标签随机洗牌
- `change_dash(BOOLEAN)`: 将 `_` 替换为空格
- `mix_prompt(BOOLEAN)`: 从多帖混合标签
- `mix_amount(INT)`: 混合的帖子数量（2–10）
- `mature_rating`: 根据不同站点映射的评级过滤（`All/Safe/Questionable/Explicit/g/s/q/e`）
- `sorting_order`: 帖子选择方式（`Random/High Score/Low Score`）
- `limit_tags(FLOAT)`: 0.05–1.0 按比例保留标签数量
- `max_tags(INT)`: 上限裁剪标签数量（1–100）
- `use_search_txt(BOOLEAN)`: 是否从文件追加搜索标签
- `search_file(STRING)`: 默认 `user/search/tags_search.txt`
- `use_remove_txt(BOOLEAN)`: 是否从文件追加移除标签
- `remove_file(STRING)`: 默认 `user/remove/tags_remove.txt`
- `use_cache(BOOLEAN)`: 是否启用缓存（需要安装 `requests_cache`）
- `api_key/user_id(STRING)`: `gelbooru/rule34` 可选凭据
- `post_id(STRING)`: 指定帖 ID（指定后将固定到该帖）
- `max_pages(INT)`: 分页上限（默认 100）
- `chaos_mode`: `None/Chaos/Less Chaos`（启用时会生成负提示词）
- `chaos_amount(FLOAT)`: 混沌比例（0.1–1.0）

## 文件与路径
- 用户数据目录：`user/`
  - `search/tags_search.txt`：每行一个标签集合，可在运行时随机追加
  - `remove/tags_remove.txt`：逗号分隔标签，将被移除
  - `credentials/credentials.json`：按 Booru 名称保存 `api_key/user_id`（若提供）

## 与 WebUI Forge 的差异
- 移除了 A1111 专属逻辑与 Gradio UI，包括：`modules.processing`、`StableDiffusionProcessingImg2Img`、`deepbooru`、`controlnet` 等。
- LoRA 注入（`<lora:...>`）未在节点内直接拼接，推荐使用 ComfyUI 的 LoRA 节点组合实现。

## 常见问题
- 每次运行结果相同：
  - 确保未设置 `post_id`（设置会固定到同一帖）。
  - 使用 `sorting_order = Random` 且 `shuffle_tags = True`。
  - 已内置系统随机源，避免全局随机种子影响。
- Rule34 无结果：
  - 默认会尝试排除 `animated`，若无结果会自动回退至不排除 animated 的查询。
- 网络错误/证书问题：
  - 某些网络环境可能出现 `WinError 10054` 连接被重置；可重试或切换网络。

## 贡献与扩展
- 可继续扩展：
  - 图片拉取节点 `RanbooruFetchImage`（输出 `IMAGE` 与元数据）
  - LoRA 选择节点 `RanbooruLoraSelect`（输出名称与权重列表）

---

若需要示例工作流或额外节点支持，请在 Issues 中提出需求。
