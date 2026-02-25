# ComfyUI-Env-Loader

一个 ComfyUI 的自定义节点集：在启动时读取项目根目录的 `.env` 文件，并提供两种能力：

1. 下拉选择单个 key 并输出对应的值；
2. 按 `.env` 的 key 动态生成多个输出端口，端口名即键名，输出为各自对应的值。启动时会在日志中打印已加载的 key，便于排查配置问题。

## 特性

- 自动读取 ComfyUI 根目录下的 `.env` 文件
- Env Key Selector：在节点输入处显示可选 key 的下拉菜单；输出选中 key 的值（`STRING`）
- Env Keys：按 `.env` 的所有 key 生成多个输出端口；端口名称为键名，输出为对应的值
- 启动日志打印：加载的 `.env` 路径与已解析出的 key 列表
- 变更检测：当 `.env` 文件修改后，节点选项和输出会刷新

## 安装

- 通过 ComfyUI-Manager：选择“Install via URL”，填入本仓库地址即可安装
- 手动安装：将仓库克隆到 `ComfyUI/custom_nodes/ComfyUI-Env-Loader`

```bash
# 示例（请替换为你的实际路径）
cd path/to/ComfyUI/custom_nodes
git clone https://github.com/hubo502/ComfyUI-Env-Loader.git
```

## 使用

- Env Key Selector（单值选择）：

  - 位置：`Utils / Env Key Selector`
  - 输入：`key`（下拉选择从 `.env` 中解析出的 key）
  - 输出：`value`（选中 key 的字符串值）

- Env Keys（多端口输出）：
  - 位置：`Utils / Env Keys`
  - 输入：无
  - 输出：多个端口，端口名为 `.env` 中的键名，值为对应字符串

### `.env` 示例

```
API_KEY=12345
MODEL_PATH="C:/Models"
DEBUG=true
a=b
c=d
```

- 支持 `#` 注释与空行
- 支持用单引号或双引号包裹的值

## 工作原理

- 节点在模块导入时根据 `custom_nodes` 目录定位 ComfyUI 根目录，并读取根目录下的 `.env`：
  - `ENV_PATH = <ComfyUI 根目录>/.env`
  - 启动时打印：`[Env Loader] Loading env from ...` 和已加载的 key 列表
- `INPUT_TYPES` 返回下拉菜单元数据，展示所有可用 key（用于 Env Key Selector）
- `Env Keys` 的 `RETURN_TYPES` 与 `RETURN_NAMES` 在模块导入时根据当前 `.env` 的 key 动态生成；运行过程中若键数量或名称变更，端口数量与名称不会自动变化，需要重启 ComfyUI 以刷新端口；端口中的值会根据最新的 `.env` 重新读取
- `IS_CHANGED` 返回 `.env` 的 `mtime`，确保在值变更时刷新计算

## 依赖

- 仅使用 Python 标准库，无额外依赖

## 许可

- 本仓库使用 MIT 许可，详情见 `LICENSE`

## 贡献

- 欢迎提交 Issue 和 PR

## 常见问题

- 没有看到 key：确认 `.env` 位于 ComfyUI 根目录（与 `custom_nodes` 同级），且包含合法的 `KEY=VALUE`
- 值未刷新：修改 `.env` 后重新触发图或重启 ComfyUI；节点会依据 `mtime` 变化刷新
- 增加或删除了 key，但 Env Keys 端口未变化：需要重启 ComfyUI 以重新加载节点并根据新的 `.env` 生成端口
