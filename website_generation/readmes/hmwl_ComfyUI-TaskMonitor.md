# ComfyUI-TaskMonitor

A powerful task monitoring extension for ComfyUI that provides real-time progress tracking, workflow statistics, and execution monitoring.

ComfyUI-TaskMonitor 是一个功能强大的任务监控扩展，为 ComfyUI 提供实时进度跟踪、工作流统计和执行监控功能。

[English](#english) | [中文](#chinese)

<a id="english"></a>
## Features

- **Real-time Progress Tracking**
  - Monitor overall workflow progress
  - Track individual node execution
  - Display detailed progress information

- **Workflow Statistics**
  - Total nodes count
  - Executed nodes count
  - Current node type and status
  - Execution time tracking

- **Queue Management**
  - View running tasks
  - Monitor pending tasks
  - Track task IDs and client information

- **Error Handling**
  - Real-time error detection
  - Detailed error messages
  - Error status reporting

## Installation

1. Navigate to your ComfyUI's `custom_nodes` directory
2. Clone this repository:
```bash
git clone https://github.com/hmwl/ComfyUI-TaskMonitor.git
```
3. Restart ComfyUI

## Usage

1. Add the "Task Monitor API Node" to your workflow (no required)
2. Connect it to your workflow (the node doesn't require any inputs)
3. Access the monitoring interface at: `http://localhost:8188/task_monitor/index.html`

### Web Interface

The web interface provides:
- Overall workflow progress
- Current node execution status
- Queue information
- Error messages (if any)
- Execution time statistics

### API Endpoints

- `GET /task_monitor/status`: Get current task status and progress information
  - Returns JSON with task status, progress, queue information, and error details

## Response Format

The status endpoint returns a JSON object with the following structure:

```json
{
    "task_id": "string",
    "status": "idle|running|completed|error|queued",
    "queue": {
        "running_count": number,
        "pending_count": number,
        "running": [
            {
                "prompt_id": "string",
                "nodes_in_prompt": number,
                "client_id": "string"
            }
        ],
        "pending": [...]
    },
    "current_task_progress": {
        "node_id": number,
        "node_type": "string",
        "step": number,
        "total_steps": number,
        "text_message": "string"
    },
    "workflow_progress": {
        "total_nodes": number,
        "executed_nodes": number,
        "last_executed_node_id": number
    },
    "execution_time": number,
    "error_info": ["string"]
}
```

## Development

### Project Structure

```
ComfyUI-TaskMonitor/
├── __init__.py          # Main extension code
├── web/                 # Web interface files
│   └── index.html      # Monitoring interface
└── README.md           # This file
```

### Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- ComfyUI team for the amazing framework
- All contributors who have helped improve this extension

---

<a id="chinese"></a>
# ComfyUI-TaskMonitor 中文说明

ComfyUI-TaskMonitor 是一个功能强大的任务监控扩展，为 ComfyUI 提供实时进度跟踪、工作流统计和执行监控功能。

## 功能特点

- **实时进度跟踪**
  - 监控整体工作流进度
  - 跟踪单个节点执行情况
  - 显示详细的进度信息

- **工作流统计**
  - 总节点数量统计
  - 已执行节点计数
  - 当前节点类型和状态
  - 执行时间跟踪

- **队列管理**
  - 查看运行中的任务
  - 监控待处理任务
  - 跟踪任务 ID 和客户端信息

- **错误处理**
  - 实时错误检测
  - 详细的错误信息
  - 错误状态报告

## 安装说明

1. 进入 ComfyUI 的 `custom_nodes` 目录
2. 克隆此仓库：
```bash
git clone https://github.com/hmwl/ComfyUI-TaskMonitor.git
```
3. 重启 ComfyUI

## 使用方法

1. 在工作流中添加 "Task Monitor API Node" 节点（非必要）
2. 将节点连接到工作流（该节点不需要任何输入）
3. 访问监控界面：`http://localhost:8188/task_monitor/index.html`

### Web 界面

Web 界面提供以下功能：
- 整体工作流进度
- 当前节点执行状态
- 队列信息
- 错误信息（如果有）
- 执行时间统计

### API 接口

- `GET /task_monitor/status`：获取当前任务状态和进度信息
  - 返回包含任务状态、进度、队列信息和错误详情的 JSON 数据

## 响应格式

状态接口返回的 JSON 对象结构如下：

```json
{
    "task_id": "字符串",
    "status": "idle|running|completed|error|queued",
    "queue": {
        "running_count": 数字,
        "pending_count": 数字,
        "running": [
            {
                "prompt_id": "字符串",
                "nodes_in_prompt": 数字,
                "client_id": "字符串"
            }
        ],
        "pending": [...]
    },
    "current_task_progress": {
        "node_id": 数字,
        "node_type": "字符串",
        "step": 数字,
        "total_steps": 数字,
        "text_message": "字符串"
    },
    "workflow_progress": {
        "total_nodes": 数字,
        "executed_nodes": 数字,
        "last_executed_node_id": 数字
    },
    "execution_time": 数字,
    "error_info": ["字符串"]
}
```

## 开发信息

### 项目结构

```
ComfyUI-TaskMonitor/
├── __init__.py          # 主要扩展代码
├── web/                 # Web 界面文件
│   └── index.html      # 监控界面
└── README.md           # 说明文档
```

### 参与贡献

1. Fork 本仓库
2. 创建您的特性分支
3. 提交您的更改
4. 推送到分支
5. 创建新的 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

## 致谢

- ComfyUI 团队提供的优秀框架
- 所有帮助改进此扩展的贡献者 