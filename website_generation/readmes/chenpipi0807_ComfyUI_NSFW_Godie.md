# ComfyUI_NSFW_Godie 违禁词过滤节点

这是一个简单好用的 ComfyUI 自定义节点，专门用来过滤文本中的不良内容。它会自动检测输入文本中的违禁词，并将其替换成自定义字符(默认为星号*)，同时保留原始格式。

![微信截图_20250314193058](https://github.com/user-attachments/assets/b5e6da3b-a835-400b-818b-aec72873e0c9)

## 功能特点

 
* 根据自定义违禁词列表过滤文本
* 可自定义替换字符（默认为星号*）
* 保留原始大小写和标点符号
* 缓存违禁词列表提升性能
* 轻松更新词库

## 更新记录
0320 优化了部分含空格的短语无法生效的问题

## 安装方法

### 方法一：手动安装

 
1. 把这个仓库克隆到你的 ComfyUI 自定义节点文件夹：

 
```bash
cd /你的ComfyUI路径/custom_nodes/
git clone https://github.com/chenpipi0807/ComfyUI_NSFW_Godie.git
```

 
2. 重启 ComfyUI

### 方法二：通过 ComfyUI Manager 安装

 
1. 打开 ComfyUI
2. 切换到 Manager 标签页
3. 搜索 "NSFW Godie"
4. 点击安装

## 使用方法

 
1. 在工作流中添加 "ComfyUI_NSFW_Godie" 节点
2. 将文本源连接到节点输入
3. （可选）通过"replacement_char"参数自定义替换字符（默认为"*"）
4. 节点会自动过滤掉不良内容，保留原始格式
5. 使用过滤后的输出继续你的工作流

## 自定义违禁词列表

你可以通过编辑节点目录中的 `nsfw.txt` 文件来添加或删除违禁词。很简单，添加或删除就行了！

## 重点表扬
重点表扬攻坚队的@企鹅@狐狸 两位老师倾情贡献违禁词（手动狗头）

## 许可证

MIT

