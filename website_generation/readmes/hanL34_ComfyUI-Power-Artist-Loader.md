# Power Artist Loader

一个为 ComfyUI 设计的自定义节点，可同时加载多个画师名称并智能组合到提示词中，支持独立权重控制和实时预览。

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)

### 节点介绍

https://github.com/user-attachments/assets/585ec4e1-3a5d-47f7-b8c0-93a65052291b

### 管理器介绍

https://github.com/user-attachments/assets/d3fee3e2-7e16-4b09-b125-67ece43403a1

## 版本更新2025-11-4
1. 修正了Artist manager的新增词条，无法同步到本地，以及输出画师名字而不是keywords的问题
2. 修正了节点的预览keywords的无法同步的问题
3. 修正了Artist manager右上方保存功能会重置修改的BUG
4. 修复拖拽功能影响划词全选的问题，现在只会在最左的序号处显示抓手后触发拖拽功能
5. 新增Artist manager界面可以移动功能，方便观察对比工作流的内容
6. 修正了keywords编辑框的【保存】按钮改成【确定】，目前只会暂存到界面，点击界面的【保存】才会同步到本地和实时输出

## 版本更新2025-10-17
1. 新增右键Artist manager功能，可在界面添加删除和拖拽词条，点击保存后即时同步到本地CSV文件
2. 新增Artist manager撤销功能，最大可撤销20步操作
3. 优化预览图片实时同步功能，本地image文件夹添加对应Artist名称的图片后，节点能即时预览
4. 修复节点的网页缓存逻辑，现更新CSV或本地图片后，不会再显示旧的内容

## 版本更新2025-10-09
1. 修复刷新后节点重置，现在会保留上一次的设置状态
2. 新增权重左右拖动改变数值的功能
3. 修复字数过多，导致预览显示超出框外的bug，现在可在预览框内滚动显示
4. 右键菜单去掉strength0.5等3个低频使用功能项
5. 修改权重范围为-1.00-3.00，可使用负权重

## 特性

### 核心功能
- **多画师管理** - 动态添加/删除画师槽位，支持无限扩展
- **独立权重控制** - 每个画师 -1.00-3.00 精确权重调节
- **悬停预览** - 鼠标悬停在下拉菜单即可预览画师风格图片和关键词
- **批量开关** - 一键启用/禁用所有画师
- **智能合并** - 自动格式化为 SD 权重语法：`(artist:1.2)`

### 界面特点
- 可视化开关和权重滑块
- 右键快捷菜单
- 支持画师名称区域内悬停预览

<img width="900" height="620" alt="image" src="https://github.com/user-attachments/assets/6f471c4d-7468-433c-9831-44341988e3a4" />
<img width="2853" height="1511" alt="Power Artist loader" src="https://github.com/user-attachments/assets/5becbe46-c803-4271-8c4e-4f4cd86b41cf" />

## 安装

### 方法 : Git Clone
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/hanL34/ComfyUI-Power-Artist-Loader.git
cd ComfyUI-Power-Artist-Loader

## 使用说明

### 添加画师
1. 点击节点底部的 **➕ Add Artist** 按钮
2. 点击画师名称区域打开下拉菜单
3. 鼠标悬停可预览画师风格（需配置预览图）
4. 点击选择画师

### 调整权重
**方法 1**: 点击左右箭头按钮，每次 ±0.05  
**方法 2**: 点击数值区域，直接输入精确值  
**方法 3**: 在数值区域按住左键拖动调节

### 快捷操作
- **Toggle All** - 批量启用/禁用所有画师
- **右键菜单** - 快速设置常用权重值（0.5/1.0/1.5）
- **圆形开关** - 单个画师启用/禁用

## 自定义画师库

### CSV 格式
编辑 `artists.csv` 文件添加自定义画师：

```csv
画师名称,关键词,预览图文件名
Akira Toriyama,akira toriyama style anime dragon ball,toriyama.jpg
Your Artist,custom keywords here,custom.jpg
```

### 添加预览图
1. 将图片放入 `images/` 目录
2. 图片命名与 CSV 中的文件名一致
3. 推荐尺寸：200-400px 宽度，JPG/PNG 格式

## 技术栈

- **后端**: Python 3.8+, aiohttp
- **前端**: JavaScript (ES6+), LiteGraph
- **UI**: 自定义 Canvas 渲染

## 许可证

MIT License - 详见 [LICENSE](./LICENSE)

## 致谢

- [rgthree-comfy](https://github.com/rgthree/rgthree-comfy) - 设计灵感来源
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 强大的 SD 工作流平台
- 所有贡献者和使用者的反馈

## 支持

- **文档**: [Wiki](https://github.com/yourusername/ComfyUI-Power-Artist-Loader/wiki)
- **讨论**: [Discussions](https://github.com/yourusername/ComfyUI-Power-Artist-Loader/discussions)
- **问题**: [Issues](https://github.com/yourusername/ComfyUI-Power-Artist-Loader/issues)

---

如果这个项目对你有帮助，请给个 ⭐ Star！
