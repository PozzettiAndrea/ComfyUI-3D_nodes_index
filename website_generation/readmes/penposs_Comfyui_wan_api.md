
# ComfyUI WanAPI 节点

[English Version](README_EN.md)

白嫖通义万相 wan2.1模型，这是一个批量调用wan2.1 api的实现，给你的短剧生产提供批量解决方案。

## 功能特点
- 🎬 支持图片转视频
- 📤 自动上传图片到 GitHub
- 🔄 支持批量处理
- 🧹 自动清理临时文件
- 💾 定期清理 GitHub 仓库

## 安装步骤
1. 克隆仓库到 ComfyUI 的 custom_nodes 目录：
```bash
cd custom_nodes
git clone https://github.com/penposs/Comfyui_wan_api.git
```

2. 安装依赖：
   Install dependencies:
```bash
pip install -r Comfyui_wan_api/requirements.txt
```

## 初始配置
### 1. 创建 GitHub 图床
方法一：自动配置（新手自动）
1. 运行自动配置脚本setup_github.bat：
2. 配置步骤：
   - 输入 GitHub 邮箱
   - 创建 Token：
     - Token 名称： WanAPI
     - 有效期：永不过期
     - 权限：勾选 repo
   - 复制并粘贴 Token 方法二：手动配置
1. 访问： https://github.com/settings/tokens/new
2. 创建 Token
3. 创建公开仓库
4. 编辑配置文件
### 2. 配置百炼 API
1. 访问并登录百炼平台： https://www.aliyun.com/minisite/goods?userCode=4onztxky
2. 白嫖通义万相 200秒
   注意查看模型调用页面的收费
3. 配置 API Key：
## 使用方法
### 1. 基本用法
1. 添加 WanAPIImageUploader 节点
2. 连接图片输入
3. 添加 WanAPIImageToVideo 节点
4. 设置参数
5. 运行工作流
### 2. 示例工作流
- 提供多个示例工作流
- 包括基础和高级用法
- 可直接加载使用
## 模型说明
### wanx2.1-i2v-plus
- 高质量模型
- 固定 5 秒时长
- 处理时间：7-10 分钟
- 计费：0.70元/秒
### wanx2.1-i2v-turbo
- 快速模型
- 支持 3-5 秒时长
- 处理时间：3-5 分钟
- 计费：0.24元/秒
## 常见问题
1. Token 无效
   
   - 检查权限
   - 确认未过期
2. 上传失败
   
   - 检查网络
   - 验证权限
   - 确认配置
3. 视频生成失败
   
   - 检查 API Key
   - 确认图片上传
   - 查看错误信息
## 更新日志
### v1.0.0
- 初始版本发布
- 支持图片转视频
- 自动上传到 GitHub
- 添加仓库清理功能
## 联系方式
- GitHub Issues
- Email: 2363939182@qq.com
  please buy me a coffee 3Q！
- ![f4dbacc3915c1240ada06333d04f0ce](https://github.com/user-attachments/assets/f815a86f-64aa-46bc-92e8-8488e203c112)

- 
## 许可证
MIT License
