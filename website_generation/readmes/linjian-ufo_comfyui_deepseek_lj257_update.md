# DeepSeek Chat Node for ComfyUI

这是一个ComfyUI的自定义节点，用于调用DeepSeek Chat API处理文本输入并返回文本输出。

## 功能特点

- 接收单一文本输入，调用DeepSeek Chat API进行处理
- 从配置文件中读取API密钥，保证安全性
- 支持自定义系统提示词、温度和最大token数等参数
- 返回纯文本输出，便于在ComfyUI工作流中使用
- **新增测试模式**：无需实际调用API即可测试节点功能，避免消耗API额度
- **增强错误处理**：提供详细的错误信息和解决方案，特别是针对API余额不足的情况

## 安装步骤

1. 确保您已经安装了ComfyUI（版本0.3.27或更高）
2. 将此仓库克隆或下载到ComfyUI的`custom_nodes`目录中：

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui_deepseek_node.git
# 或者解压下载的zip文件到此目录
```

3. 安装所需的依赖项：

```bash
cd comfyui_deepseek_node
pip install -r requirements.txt
```

4. 配置DeepSeek API密钥：
   - 编辑`comfyui_deepseek_node/config.json`文件
   - 将`your_deepseek_api_key_here`替换为您的实际DeepSeek API密钥

```json
{
    "api_key": "your_actual_deepseek_api_key"
}
```

5. 重启ComfyUI

## 使用方法

1. 启动ComfyUI
2. 在节点选择菜单中，找到`DeepSeek`分类下的`DeepSeek Chat`节点
3. 将节点添加到您的工作流中
4. 连接文本输入到节点的`text`输入端口
5. 可选：调整节点的参数设置
   - `temperature`：控制输出的随机性（0.0-2.0）
   - `max_tokens`：控制输出的最大token数（1-8192）
   - `system_prompt`：设置系统提示词，定义AI助手的行为
   - `test_mode`：启用测试模式，不实际调用API（适合测试节点连接和参数设置）
6. 运行工作流，节点将处理输入文本并返回响应

## 参数说明

- **text**（必需）：要发送到DeepSeek Chat API的输入文本
- **temperature**（可选）：控制输出的随机性，默认为0.7
  - 较低的值（如0.2）会使输出更加确定和集中
  - 较高的值（如1.0）会使输出更加随机和创造性
- **max_tokens**（可选）：控制输出的最大token数，默认为1024
- **system_prompt**（可选）：系统提示词，用于定义AI助手的行为，默认为"You are a helpful assistant."
- **test_mode**（可选）：启用测试模式，默认为关闭
  - 启用后，节点不会实际调用API，而是返回测试信息
  - 适合用于验证节点连接和参数设置，不消耗API额度

## 故障排除

- **API密钥错误**：确保您已在`config.json`文件中设置了正确的DeepSeek API密钥
- **API余额不足**：如果遇到"Insufficient Balance"错误，请检查以下可能的原因：
  1. 您的DeepSeek账户余额已用完
  2. 您的API密钥可能未绑定付款方式
  3. 您的账户可能有未结清的账单
  
  解决方法：
  1. 登录DeepSeek官网检查账户余额
  2. 充值您的DeepSeek账户
  3. 确认您的付款方式设置正确
  4. 暂时可以启用测试模式来验证节点功能
- **连接问题**：检查您的网络连接，确保可以访问DeepSeek API
- **响应为空**：尝试调整`temperature`和`max_tokens`参数

## 注意事项

- 此节点需要互联网连接才能访问DeepSeek API
- API调用可能会产生费用，请参考DeepSeek的定价政策
- 请确保您的API使用符合DeepSeek的服务条款
- 启用测试模式可以在不消耗API额度的情况下测试节点功能
