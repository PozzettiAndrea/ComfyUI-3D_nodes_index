# ComfyUI DCI Extension - DCI Icons & Debian Package (DEB) Creator

**Language / 语言**: [English](#english) | [中文](#中文)

**Keywords**: ComfyUI, DCI, DSG Combined Icons, Debian package, deb creator, icon packaging, Linux distribution, package manager, dpkg, apt

---

## English

# ComfyUI DCI Image Export Extension - DCI Icons & Debian Package Creator

A comprehensive ComfyUI extension for creating, previewing, and analyzing DCI (DSG Combined Icons) format files. This extension implements the complete DCI specification, supporting multi-state icons, multi-tone variants, scaling factors, and advanced metadata analysis. **Features Debian package (deb) creation and extraction capabilities for icon distribution and system integration.**

## DCI Specification Documentation

This project is designed and implemented strictly based on the **DCI (DSG Combined Icons) standard format documentation**.

### Official Specification Documents
- **Official Specification**: [Desktop Spec Group - Icon File Specification](https://desktopspec.org/unstable/%E5%9B%BE%E6%A0%87%E6%96%87%E4%BB%B6%E8%A7%84%E8%8C%83.html)
- **Local Documentation**: **[dci-specification.md](./dci-specification.md)**

### Documentation Features

The `dci-specification.md` document in this project is based on the official specification and optimized for practical use:

- 📋 **Complete DCI file format description**: Binary structure, file headers, metadata formats
- 📝 **Detailed layer file naming conventions**: Optimized naming formats and parameter descriptions
- 🎨 **Color adjustment algorithm explanations**: Precise color calculation formulas and examples
- 💡 **Practical application examples**: Complete directory structures and filename examples
- 🔍 **Lookup rules and fallback mechanisms**: Icon resource matching and selection logic
- ⚡ **Alpha8 format in-depth analysis**: Technical details based on [dtkgui implementation](https://github.com/linuxdeepin/dtkgui)

### Standard Compatibility

This tool fully complies with DCI standard specifications:
- ✅ **File format compatibility**: Generated DCI files fully conform to official binary format specifications
- ✅ **Directory structure standards**: Strictly follows `<icon_size>/<icon_state>.<tone_type>/<scale_factor>/<layer_file>` structure
- ✅ **File naming conventions**: Complete support for `priority.paddingp.palette.hue_saturation_brightness_red_green_blue_alpha.format[.alpha8]` format
- ✅ **Filename omission rules**: Supports DCI specification filename optimization strategies, default values can be omitted (e.g., `1.webp`)
- ✅ **Layer system support**: Complete implementation of priority, padding, palette, and color adjustment features
- ✅ **Alpha8 optimization**: Supports alpha channel storage optimization based on grayscale format
- ✅ **Backward compatibility**: Supports both simplified and complete filename formats

## Project Status

- ✅ **Complete DCI format implementation**: Full support for DCI file creation and reading
- ✅ **Multi-state icon support**: Normal, hover, pressed, disabled states
- ✅ **Multi-tone support**: Universal, light and dark tone variants with automatic symlink creation
- ✅ **Advanced preview system**: Grid-based visualization with metadata overlay
- ✅ **Modular node architecture**: Refactored into more flexible composable nodes
- ✅ **Binary data flow**: Support for inter-node binary data transfer
- ✅ **Binary file processing**: Dedicated binary file loading and saving nodes
- ✅ **Debian package support**: Full deb package creation and extraction with symlink support
- ✅ **Complete Chinese localization**: All interface elements fully support Chinese display
- ✅ **Enhanced error handling**: Detailed error reporting and debugging information
- ✅ **Checkerboard background support**: Checkerboard backgrounds for transparent image preview
- ✅ **Comprehensive testing framework**: Complete unit tests with GitHub Actions CI/CD
- ✅ **Organized project structure**: Clean directory structure with centralized test management
- ✅ **Production ready**: Thoroughly tested with example workflows

## Directory Structure

```
comfyui-dci/
├── py/                          # Core Python modules
│   ├── __init__.py             # Module initialization
│   ├── dci_format.py           # DCI format implementation
│   ├── dci_reader.py           # DCI file reader
│   └── nodes/                  # ComfyUI node definitions
├── locales/                     # Internationalization files
├── resources/                   # Static resources
├── tools/                       # Development tools
├── tests/                       # Test files (centralized)
├── examples/                    # Example workflows
├── web_version/                 # Web components (reserved)
├── __init__.py                  # Extension entry point
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── install.sh                   # Linux/Mac installation script
├── install.bat                  # Windows installation script
├── preliminary-design.md        # Preliminary design
└── detailed-design.md           # Detailed design
```

## Features

### Export Functions
- **DCI Image Creation**: Convert single images to DCI image data with custom parameters
- **DCI File Composition**: Combine multiple DCI images into complete DCI files
- **Multiple Scale Factors**: Support decimal scaling like 1x, 1.25x, 1.5x, 2x, etc.
- **Format Support**: WebP, PNG, and JPEG formats
- **Tone Support**: Universal, light and dark tone variants
- **Customizable Icon Sizes**: From 16x16 to 1024x1024 pixels

### Preview Functions
- **Visual Preview**: Generate grid previews of all images in DCI files
- **Metadata Display**: Show comprehensive metadata for each image including size, state, tone, scale, format
- **In-node Display**: Display preview content directly in the node interface

### Binary File Processing Functions
- **Universal File Loading**: Load arbitrary binary files from the file system (DCI, images, archives, etc.)
- **Flexible File Saving**: Save binary data to specified locations with custom output directory support
- **Base64 Encoding/Decoding**: Convert binary data to/from base64 text format for data transfer and storage
- **Data Structuring**: Provide unified binary data structures including content, metadata, and path information
- **Cross-Format Support**: Works with any file type, not limited to DCI format
- **Workflow Integration**: Seamlessly integrate file operations into ComfyUI workflows

### Debian Package (DEB) Support
- **DEB Package Creation**: Create standard Debian packages (.deb) from DCI icon files for system distribution
- **DEB Package Extraction**: Extract and load files from existing Debian packages with filtering capabilities
- **Symlink Support**: Automatic creation of symbolic links in deb packages for icon compatibility
- **Version Management**: Intelligent version incrementing and package metadata handling
- **Cross-Platform**: Pure Python implementation works on Windows, Linux, and macOS
- **Standard Compliance**: Generated packages are fully compatible with dpkg and apt package managers

> **⚠️ Important Notice (January 2025)**: DEB packages generated before the January 2025 symlink position fix need to be regenerated. The fix ensures symlinks are correctly placed alongside their target files instead of at the root level.

### Universal Tone Type Support
- **Universal Tone Type**: New "Universal" tone type that works for both light and dark themes
- **Automatic Symlink Creation**: When using universal tone, images are stored in light directory with automatic symlinks created in dark directory
- **Default Setting**: Universal tone is now the default option for new icons
- **DCI Specification Compliance**: Symlinks follow DCI specification using relative paths (../../target/path)
- **Backward Compatibility**: Existing light and dark tone types continue to work as before

### Internationalization Support
- **Complete Chinese Interface**: All node names, parameter names, and output names support Chinese display
- **Bilingual Support**: Support switching between Chinese and English interfaces
- **Localized Translation**: All user interface elements are professionally translated
- **Color Name Translation**: 20 color names fully localized (Light Gray, Blue, Red, etc.)
- **Option Value Translation**: All dropdown options and default values support Chinese display

### Error Handling & Debugging
- **Detailed Error Reporting**: Display detailed error messages and solution suggestions directly in the interface
- **Visual Error Preview**: DCI preview node generates red preview images with error information when errors occur
- **Analysis Node Debugging**: DCI analysis node outputs detailed error logs and data status
- **Parameter Compatibility**: Support both translated and original parameter names for backward compatibility

## Installation

### From ComfyUI Registry (Recommended)

This extension is available on the official ComfyUI Registry. You can install it directly through ComfyUI Manager:

1. Open ComfyUI Manager in your ComfyUI interface
2. Search for "DCI Image Export Extension", "comfyui-dci", "debian package creator", or "deb packager"
3. Click Install and restart ComfyUI

### Automatic Installation (Alternative)

1. Clone this repository to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-username/comfyui-dci.git
```

2. Run the installation script:

**Linux/Mac:**
```bash
cd comfyui-dci
chmod +x install.sh
./install.sh
```

**Windows:**
```cmd
cd comfyui-dci
install.bat
```

### Manual Installation

1. Clone the repository (same as above)

2. Manually install dependencies:
```bash
cd comfyui-dci
pip install -r requirements.txt
```

3. Restart ComfyUI

4. After installation, all DCI nodes will appear in the ComfyUI node menu under the **"DCI"** category

## Available Nodes

This extension provides 14 ComfyUI nodes, all unified under the **"DCI"** category:

### DCI/Export
- **DCI_Image** - Full-featured DCI image creation node
- **DCI_SampleImage** - Simplified DCI image creation node
- **DCI_FileNode** - Combine multiple DCI images into complete DCI files

### DCI/Preview
- **DCI_PreviewNode** - Generate grid previews of DCI files
- **DCI_ImagePreview** - Preview individual DCI images

### DCI/Analysis
- **DCI_Analysis** - Analyze DCI file structure and metadata

### DCI/Files
- **DCI_BinaryFileLoader** - Load binary files from filesystem
- **DCI_BinaryFileSaver** - Save binary data to files
- **DCI_FileSaver** - Save DCI files with custom paths
- **DCI_Base64Encoder** - Encode binary data to Base64
- **DCI_Base64Decoder** - Decode Base64 to binary data
- **DCI_DirectoryLoader** - Load multiple files from directories
- **DCI_DebPackager** - Create Debian packages from icon files
- **DCI_DebLoader** - Extract files from Debian packages

## Example Workflows

The `examples/` directory contains sample ComfyUI workflows demonstrating:

- Basic DCI icon creation
- Multi-state icon workflows
- Debian package creation
- File processing pipelines
- Advanced preview configurations

## Technical Implementation

### DCI Format Support
- Complete binary format implementation
- Layer system with priority, padding, and color adjustments
- Multi-state and multi-tone icon support (including universal tone with symlinks)
- Alpha8 format optimization

### Node Architecture
- Modular design with composable nodes
- Binary data flow between nodes
- Comprehensive error handling
- Internationalization support

### Testing Framework
- Unit tests for all core functionality
- Integration tests for complete workflows
- GitHub Actions CI/CD pipeline
- Cross-platform compatibility testing

## Contributing

We welcome contributions! Please see our contributing guidelines for details on:
- Code style and standards
- Testing requirements
- Pull request process
- Issue reporting

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- ComfyUI team for the excellent framework
- Desktop Spec Group for the DCI specification
- dtkgui project for Alpha8 format insights

---

## 中文

# ComfyUI DCI 图像导出扩展 - DCI 图标与 Debian 软件包创建器

一个全面的 ComfyUI 扩展，用于创建、预览和分析 DCI（DSG Combined Icons）格式文件。此扩展实现了完整的 DCI 规范，支持多状态图标、多色调、缩放因子和高级元数据分析。**具备 Debian 软件包（deb）创建和提取功能，用于图标分发和系统集成。**

## DCI 规范文档

本项目严格基于 **DCI（DSG Combined Icons）标准格式文档** 设计和实现。

### 官方规范文档
- **官方规范**：[Desktop Spec Group - 图标文件规范](https://desktopspec.org/unstable/%E5%9B%BE%E6%A0%87%E6%96%87%E4%BB%B6%E8%A7%84%E8%8C%83.html)
- **本地文档**：**[dci-specification.md](./dci-specification.md)**

### 文档特色

本项目的 `dci-specification.md` 文档基于官方规范并进行了实用性优化：

- 📋 **完整的 DCI 文件格式说明**：二进制结构、文件头、元数据格式
- 📝 **详细的图层文件命名规范**：优化后的命名格式和参数说明
- 🎨 **颜色调整算法说明**：精确的颜色计算公式和示例
- 💡 **实际应用示例**：完整的目录结构和文件名示例
- 🔍 **查找规则和回退机制**：图标资源的匹配和选择逻辑
- ⚡ **Alpha8格式深度解析**：基于 [dtkgui实现](https://github.com/linuxdeepin/dtkgui) 的技术细节

### 标准兼容性

本工具完全遵循 DCI 标准规范：
- ✅ **文件格式兼容**：生成的DCI文件完全符合官方二进制格式规范
- ✅ **目录结构标准**：严格按照 `<图标大小>/<图标状态>.<色调类型>/<缩放倍数>/<图层文件>` 结构
- ✅ **文件命名规范**：完整支持 `优先级.外边框p.调色板.色调_饱和度_亮度_红_绿_蓝_透明度.格式[.alpha8]` 格式
- ✅ **文件名省略规则**：支持DCI规范的文件名优化策略，默认值可省略（如`1.webp`）
- ✅ **图层系统支持**：完整实现优先级、外边框、调色板和颜色调整功能
- ✅ **Alpha8优化**：支持基于灰度格式的alpha通道存储优化
- ✅ **向后兼容**：同时支持简化文件名和完整文件名格式

## 项目状态

- ✅ **完整的 DCI 格式实现**：完全支持 DCI 文件创建和读取
- ✅ **多状态图标支持**：正常、悬停、按下、禁用状态
- ✅ **多色调支持**：通用、浅色和深色调变体，支持自动符号链接创建
- ✅ **高级预览系统**：基于网格的可视化与元数据覆盖
- ✅ **模块化节点架构**：重构为更灵活的组合式节点
- ✅ **二进制数据流**：支持节点间二进制数据传递
- ✅ **二进制文件处理**：专用的二进制文件加载和保存节点
- ✅ **Debian 软件包支持**：完整的 deb 包创建和提取功能，支持软链接
- ✅ **完整中文本地化**：所有界面元素完全支持中文显示
- ✅ **增强错误处理**：详细的错误报告和调试信息
- ✅ **棋盘格背景支持**：透明图像预览的棋盘格背景
- ✅ **完整测试框架**：完整的单元测试和GitHub Actions CI/CD，已修复所有导入问题
- ✅ **规范项目结构**：清洁的目录结构和集中化测试管理
- ✅ **生产就绪**：通过示例工作流程全面测试

## 目录结构

```
comfyui-dci/
├── py/                          # 核心Python模块
│   ├── __init__.py             # 模块初始化
│   ├── dci_format.py           # DCI格式实现
│   ├── dci_reader.py           # DCI文件读取器
│   └── nodes/                  # ComfyUI节点定义
├── locales/                     # 国际化文件
├── resources/                   # 静态资源
├── tools/                       # 开发工具
├── tests/                       # 测试文件（集中管理）
├── examples/                    # 示例工作流
├── web_version/                 # Web组件（预留）
├── __init__.py                  # 扩展入口点
├── README.md                    # 项目文档
├── requirements.txt             # Python依赖
├── install.sh                   # Linux/Mac安装脚本
├── install.bat                  # Windows安装脚本
├── preliminary-design.md        # 概要设计
└── detailed-design.md           # 详细设计
```

## 功能特性

### 导出功能
- **DCI 图像创建**：将单个图像转换为 DCI 图像数据，支持自定义参数
- **DCI 文件组合**：将多个 DCI 图像组合成完整的 DCI 文件
- **多种缩放因子**：支持小数缩放如 1x、1.25x、1.5x、2x 等
- **格式支持**：WebP、PNG 和 JPEG 格式
- **色调支持**：通用、浅色和深色调变体
- **可自定义图标尺寸**：从 16x16 到 1024x1024 像素

### 预览功能
- **可视化预览**：生成 DCI 文件中所有图像的网格预览
- **元数据显示**：显示每个图像的全面元数据，包括尺寸、状态、色调、缩放、格式
- **节点内显示**：直接在节点界面中显示预览内容

### 二进制文件处理功能
- **通用文件加载**：从文件系统加载任意二进制文件
- **灵活文件保存**：将二进制数据保存到指定位置，支持自定义输出目录
- **Base64编码/解码**：二进制数据与base64文本格式的相互转换
- **数据结构化**：提供统一的二进制数据结构，包含内容、元数据和路径信息
- **跨格式支持**：适用于任何文件类型，不限于DCI格式
- **工作流集成**：无缝集成文件操作到ComfyUI工作流中

### Debian 软件包（DEB）支持
- **DEB 包创建**：从 DCI 图标文件创建标准 Debian 软件包（.deb）用于系统分发
- **DEB 包提取**：从现有 Debian 软件包中提取和加载文件，支持过滤功能
- **软链接支持**：在 deb 包中自动创建符号链接，确保图标兼容性
- **版本管理**：智能版本递增和软件包元数据处理
- **跨平台支持**：纯 Python 实现，在 Windows、Linux 和 macOS 上均可运行
- **标准兼容**：生成的软件包完全兼容 dpkg 和 apt 包管理器

### 通用色调类型支持
- **通用色调类型**：新增"通用"色调类型，同时适用于浅色和深色主题
- **自动符号链接创建**：使用通用色调时，图像存储在浅色目录中，并在深色目录中自动创建符号链接
- **默认设置**：通用色调现在是新图标的默认选项
- **DCI规范兼容**：符号链接遵循DCI规范，使用相对路径（../../目标/路径）
- **向后兼容**：现有的浅色和深色调类型继续正常工作

### 国际化支持
- **完整中文界面**：所有节点名称、参数名、输出名均支持中文显示
- **双语支持**：支持中文和英文界面切换
- **本地化翻译**：所有用户界面元素都经过专业翻译
- **颜色名称翻译**：20种颜色名称完全本地化（浅灰色、蓝色、红色等）
- **选项值翻译**：所有下拉选项和默认值都支持中文显示

### 错误处理与调试
- **详细错误报告**：在界面上直接显示详细的错误信息和解决建议
- **可视化错误预览**：DCI预览节点在出错时生成包含错误信息的红色预览图
- **分析节点调试**：DCI分析节点输出详细的错误日志和数据状态
- **参数兼容性**：同时支持翻译后和原始参数名，确保向后兼容

## 安装

### 从ComfyUI注册表安装（推荐）

此扩展已在官方ComfyUI注册表中提供。您可以通过ComfyUI Manager直接安装：

1. 在ComfyUI界面中打开ComfyUI Manager
2. 搜索"DCI Image Export Extension"、"comfyui-dci"、"debian package creator"或"deb packager"
3. 点击安装并重启ComfyUI

### 自动安装（备选）

1. 将此仓库克隆到您的 ComfyUI 自定义节点目录：
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-username/comfyui-dci.git
```

2. 运行安装脚本：

**Linux/Mac:**
```bash
cd comfyui-dci
chmod +x install.sh
./install.sh
```

**Windows:**
```cmd
cd comfyui-dci
install.bat
```

### 手动安装

1. 克隆仓库（同上）

2. 手动安装依赖项：
```bash
cd comfyui-dci
pip install -r requirements.txt
```

3. 重启 ComfyUI

4. 安装完成后，所有 DCI 节点将出现在 ComfyUI 节点菜单的 **"DCI"** 分类下

## 可用节点

本扩展提供了14个ComfyUI节点，全部统一归类在**"DCI"**分类下：

### DCI/Export（导出）
- **DCI_Image** - 完整功能的DCI图像创建节点
- **DCI_SampleImage** - 简化的DCI图像创建节点
- **DCI_FileNode** - 将多个DCI图像组合成完整DCI文件

### DCI/Preview（预览）
- **DCI_PreviewNode** - 生成DCI文件的网格预览
- **DCI_ImagePreview** - 预览单个DCI图像

### DCI/Analysis（分析）
- **DCI_Analysis** - 分析DCI文件结构和元数据

### DCI/Files（文件处理）
- **DCI_BinaryFileLoader** - 从文件系统加载二进制文件
- **DCI_BinaryFileSaver** - 将二进制数据保存为文件
- **DCI_FileSaver** - 保存DCI文件到自定义路径
- **DCI_Base64Encoder** - 将二进制数据编码为Base64
- **DCI_Base64Decoder** - 将Base64解码为二进制数据
- **DCI_DirectoryLoader** - 从目录加载多个文件
- **DCI_DebPackager** - 从图标文件创建Debian软件包
- **DCI_DebLoader** - 从Debian软件包中提取文件

## 使用示例

`examples/` 目录包含示例ComfyUI工作流，演示：

- 基本DCI图标创建
- 多状态图标工作流
- Debian软件包创建
- 文件处理管道
- 高级预览配置

## 技术实现

### DCI格式支持
- 完整的二进制格式实现
- 支持优先级、外边框和颜色调整的图层系统
- 多状态和多色调图标支持（包括通用色调和符号链接）
- Alpha8格式优化

### 节点架构
- 模块化设计，支持节点组合
- 节点间二进制数据流
- 全面的错误处理
- 国际化支持

### 测试框架
- 所有核心功能的单元测试（43个测试用例）
- 完整工作流的集成测试
- GitHub Actions CI/CD管道（已修复系统依赖问题）
- 跨平台兼容性测试
- 模块导入兼容性处理（支持独立测试环境）

## 贡献

我们欢迎贡献！请查看我们的贡献指南了解详情：
- 代码风格和标准
- 测试要求
- 拉取请求流程
- 问题报告

## 许可证

本项目采用MIT许可证 - 详情请参阅LICENSE文件。

## 致谢

- ComfyUI团队提供的优秀框架
- Desktop Spec Group提供的DCI规范
- dtkgui项目提供的Alpha8格式见解
