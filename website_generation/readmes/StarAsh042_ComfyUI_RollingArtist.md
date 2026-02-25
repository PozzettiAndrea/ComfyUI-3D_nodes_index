# ComfyUI RollingArtist

**RollingArtist** 是一个 ComfyUI 节点，用于生成包含随机权重的艺术家提示文本。通过动态调整 Top 艺术家比例，实现可控的随机组合。

![ComfyUI_RollingArtist](https://github.com/user-attachments/assets/157de400-e4e9-479b-ac8e-8698d2661112)


## 核心功能

- **动态控制**：定义Top艺术家范围，控制实际输出数量
- **权重分配**：精确控制每个艺术家的权重范围和总和
- **种子控制**：统一随机种子确保结果可复现
- **线程安全**：支持多线程环境下的稳定运行
- **优化算法**：简化的权重分配算法，提高性能和可读性
- **类型注解**：完整的类型提示，提高代码可维护性
- **结构化输出**：新增 `artists_json`，包含艺术家、权重、是否Top 等信息
- **性能优化**：CSV 路径与修改时间缓存，仅在文件变更时重载
- **格式规则**：权重为 `1.0` 时不输出权重，直接输出名称

## 安装指南

1. 克隆仓库到 ComfyUI 的 `custom_nodes` 目录：
   ```bash
   git clone https://github.com/StarAsh042/ComfyUI_RollingArtist.git
   ```
2. 确保以下文件存在：
   - `RollingArtist.py`（主节点文件）
   - `danbooru_art_001.csv`（艺术家数据源）
   - `modify_danbooru_csv.py`（可选预处理工具）

## 参数说明

| 参数名称           | 类型    | 范围         | 说明                          |
|--------------------|---------|--------------|-------------------------------|
| artist_count       | INT     | 1-10         | 选择生成的艺术家人数（默认3） |
| artist_top_count   | INT     | 1-10         | 输出中包含的Top艺术家数量（默认1） |
| artist_top_ratio   | FLOAT   | 0.01-1.0     | 提取CSV中Top艺术家占前百分比（默认0.01） |
| artists_prefix     | BOOLEAN | -            | 添加"artist:"前缀             |
| weight_min         | FLOAT   | 0.1-2.0      | 单个艺术家最小权重值          |
| weight_max         | FLOAT   | 0.1-2.0      | 单个艺术家最大权重值          |
| weight_total       | FLOAT   | 0.0-20.0     | 所有权重总和（默认2.0）       |
| seed               | INT     | 0-4294967295 | 控制随机性的种子值            |

### 可选参数

- `custom_csv_path`：STRING，自定义 CSV 路径（留空使用默认）
- `exclude_artists`：STRING，逗号分隔的排除名单（精确匹配）
- `sort_by_weight`：BOOLEAN，是否按权重降序排序（默认开启）

## 技术特性

- **优化的权重生成算法**：单次循环分配权重，提高效率
- **精确的权重控制**：保证权重总和在有效范围内，每个权重值保留一位小数
- **完善的类型注解**：使用Python类型提示增强代码可读性和IDE支持
- **线程安全设计**：使用锁机制确保在多线程环境下安全运行

## 使用示例

典型工作流配置：
1. 添加 **RollingArtist** 节点
2. 连接至文本编码器
3. 调整参数以获得理想的艺术家组合
4. 输出示例：
   - Prompt：
     ```
     artist:Jane_Smith,(artist:John_Doe:0.8),(artist:FooBar:0.2)
     ```
     当权重为 `1.0` 时，直接输出 `artist:名称`，不包含括号与权重。
   - JSON：
     ```json
     {
       "artists": [
         {"name": "Jane_Smith", "weight": 1.0, "top": true},
         {"name": "John_Doe", "weight": 0.8, "top": false},
         {"name": "FooBar", "weight": 0.2, "top": false}
       ]
     }
     ```

## 最佳实践

- 使用较小的`artist_count`（3-5）获得更聚焦的风格（默认3）
- 调整`weight_min`和`weight_max`的差值来控制艺术家影响力的变化范围
- 使用固定的`seed`值以便在多次生成中保持一致的艺术家组合
- 大型CSV（>10MB）建议将 `artist_top_ratio` 设为较小值（如 0.01-0.1）
- 自定义CSV路径时，节点会检测文件是否变更，仅在变更时重载，避免重复解析

## 数据预处理
当 CSV 文件出现格式问题时，运行：
```bash
python modify_danbooru_csv.py
```

## 许可证
[GNU Affero General Public License v3](LICENSE)
