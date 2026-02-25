# ComfyUI Queue Manager

A comprehensive queue management system for ComfyUI workflows with persistent storage, advanced filtering, archiving capabilities, and import/export functionality.

## 🚀 Features

- **🔄 Persistent Queue**: Workflows survive ComfyUI restarts
- **🌐 Web Interface**: Modern, responsive web interface accessible from ComfyUI menu
- **🔍 Advanced Filtering**: Filter by status, date, workflow name, and more
- **🔎 Search Functionality**: Full-text search across workflow names and data
- **📦 Archive System**: Archive old workflows to keep queue clean
- **📤 Import/Export**: Share workflows and backup queue configuration
- **📊 Real-time Monitoring**: Track workflow execution status and performance
- **🔌 REST API**: Programmatic access to all queue management features
- **⚡ Performance Optimized**: Handles thousands of workflows efficiently
- **🛡️ Error Handling**: Comprehensive error handling and recovery

## 🚀 Quick Start

### Installation

```bash
# Navigate to ComfyUI custom nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/abdullahceylan/ac-comfyui-queue-manager.git comfyui-queue-manager

# Install dependencies
cd comfyui-queue-manager
pip install -r requirements.txt

# Restart ComfyUI
```

### First Use

1. **Open ComfyUI** and look for "Queue Manager" in the menu
2. **Click Queue Manager** to open the web interface
3. **Create a workflow** in ComfyUI as usual
4. **Execute the workflow** - it will automatically appear in the Queue Manager
5. **Explore features** like filtering, archiving, and exporting

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [📖 User Guide](docs/USER_GUIDE.md) | Complete usage instructions and features |
| [⚙️ Installation Guide](docs/INSTALLATION.md) | Detailed installation for all platforms |
| [🔌 API Documentation](docs/API_DOCUMENTATION.md) | REST API reference and examples |
| [💡 Examples & Use Cases](docs/EXAMPLES.md) | Practical examples and automation scripts |

## 🎯 Key Features

### 🔄 Queue Management
- **Automatic Tracking**: All workflows are automatically added to the queue
- **Persistent Storage**: Queue survives ComfyUI restarts using SQLite database
- **Real-time Updates**: Interface updates automatically as workflows execute
- **Queue Control**: Pause/resume queue processing as needed

### 🔍 Advanced Filtering & Search
- **Status Filtering**: Filter by pending, running, completed, failed, or archived
- **Date Range**: Filter workflows by creation or completion date
- **Name Filtering**: Filter by workflow name patterns
- **Full-text Search**: Search across workflow names and metadata
- **Combined Filters**: Use multiple filters simultaneously

### 📦 Archive System
- **Smart Archiving**: Keep your active queue clean by archiving old workflows
- **Bulk Operations**: Archive multiple workflows at once
- **Restore Capability**: Restore archived workflows when needed
- **Auto-Archive**: Automatically archive workflows after a specified time
- **Separate Storage**: Archived items don't clutter the main interface

### 📤 Import/Export
- **Complete Backup**: Export entire queue including configuration
- **Selective Export**: Export only specific workflows or statuses
- **Easy Sharing**: Share workflows between different ComfyUI installations
- **Version Control**: Track changes to your workflow library
- **Merge Import**: Import workflows without overwriting existing ones

### 🌐 Web Interface
- **Modern Design**: Clean, responsive interface that works on all devices
- **Real-time Updates**: See workflow progress without refreshing
- **Bulk Operations**: Select and operate on multiple workflows
- **Detailed Views**: Inspect workflow data, results, and error messages
- **Keyboard Shortcuts**: Efficient navigation and operations

### 🔌 REST API
- **Complete Access**: All features available programmatically
- **RESTful Design**: Standard HTTP methods and status codes
- **JSON Format**: Easy to integrate with any programming language
- **Error Handling**: Comprehensive error responses with details
- **Documentation**: Full API documentation with examples

## ⚙️ Configuration

### Basic Settings
```json
{
  "max_concurrent_workflows": 1,
  "auto_archive_completed": false,
  "auto_archive_days": 30,
  "queue_state": "running"
}
```

### Performance Tuning
- **Concurrent Workflows**: Adjust based on your system resources
- **Auto-Archive**: Enable to keep queue size manageable
- **Database Optimization**: Built-in tools for large queues
- **Memory Management**: Automatic cleanup of old data

## 🔧 System Requirements

### Minimum Requirements
- **OS**: Windows 10, macOS 10.14, or Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **RAM**: 2GB available
- **Storage**: 1GB free space
- **ComfyUI**: Latest version recommended

### Recommended for Large Queues (1000+ workflows)
- **RAM**: 4GB+ available
- **Storage**: 5GB+ free space
- **CPU**: Multi-core processor
- **SSD**: For better database performance

## 🚀 Advanced Usage

### API Integration Example
```python
import requests
import json

BASE_URL = "http://localhost:5000/api/queue"

# Add workflow to queue
workflow_data = {
    "workflow_name": "My Automated Workflow",
    "workflow_data": {
        "nodes": [...],
        "links": [...]
    }
}

response = requests.post(
    f"{BASE_URL}/items",
    headers={"Content-Type": "application/json"},
    data=json.dumps(workflow_data)
)

print(f"Workflow queued: {response.json()['item']['id']}")
```

### Automation Script
```python
# Daily cleanup script
def daily_cleanup():
    # Archive workflows older than 7 days
    old_workflows = get_old_workflows(days=7)
    archive_workflows(old_workflows)
    
    # Delete failed workflows older than 30 days
    old_failed = get_failed_workflows(days=30)
    delete_workflows(old_failed)
```

## 🛠️ Development

### Development Setup

```bash
# Clone the repository
git clone https://github.com/abdullahceylan/ac-comfyui-queue-manager.git
cd ac-comfyui-queue-manager

# Install development dependencies
pip install -r requirements.txt

# Set up development environment
python setup.py
# Or manually:
make install-dev
make setup-hooks

# Run tests
python -m pytest tests/
python run_integration_tests.py
```

### Development Commands

- **Format code**: `make format`
- **Lint code**: `make lint`
- **Run all checks**: `make check`
- **Clean cache files**: `make clean`
- **Show help**: `make help`

### Code Quality

This project uses modern Python tooling:

- **Ruff** - Fast Python linter and formatter
- **Pre-commit hooks** - Automatic code quality checks
- **MyPy** - Static type checking
- **Pytest** - Comprehensive testing framework

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🐛 Report Bugs**: Use GitHub Issues to report problems
2. **💡 Suggest Features**: Share your ideas for improvements
3. **📝 Improve Documentation**: Help make the docs better
4. **🔧 Submit Code**: Fork, develop, and submit pull requests

### Contributing Steps
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and checks: `make check`
5. Submit a pull request

## 📊 Performance

### Benchmarks
- **Queue Size**: Tested with 10,000+ workflows
- **Response Time**: < 100ms for most operations
- **Memory Usage**: ~1MB per 1000 workflows
- **Database Size**: ~10MB per 1000 workflows

### Optimization Tips
1. Enable auto-archiving for large queues
2. Use filtering to reduce displayed items
3. Regular database cleanup
4. Adjust concurrent workflow limits

## 🛠️ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Queue Manager not in menu | Restart ComfyUI, check installation |
| Workflows not appearing | Open Queue Manager interface first |
| Interface not loading | Check port 5000, try different browser |
| Performance issues | Enable auto-archive, reduce concurrent workflows |

### Getting Help
- **📖 Documentation**: Check the docs folder
- **🐛 GitHub Issues**: Report bugs and get support
- **💬 Discord**: Join the ComfyUI community

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **ComfyUI Team**: For creating an amazing tool
- **Community**: For feedback and contributions
- **Contributors**: Everyone who helped improve this project

## 📈 Roadmap

### Upcoming Features
- [ ] **WebSocket Support**: Real-time updates without polling
- [ ] **Workflow Templates**: Save and reuse workflow templates
- [ ] **User Management**: Multi-user support with permissions
- [ ] **Cloud Sync**: Sync queues across multiple instances
- [ ] **Advanced Analytics**: Detailed performance metrics
- [ ] **Plugin System**: Extensible architecture for custom features

### Version History
- **v1.0.0**: Initial release with core features
- **v1.1.0**: Added advanced filtering and search
- **v1.2.0**: Performance improvements and API enhancements
- **v1.3.0**: Archive system and bulk operations

---

**⭐ Star this repository if you find it useful!**

**🔗 Links**:
- [GitHub Repository](https://github.com/abdullahceylan/ac-comfyui-queue-manager)
- [Issue Tracker](https://github.com/abdullahceylan/ac-comfyui-queue-manager/issues)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)