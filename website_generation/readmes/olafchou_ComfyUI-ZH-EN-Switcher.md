# ComfyUI Language Switcher / ComfyUI 语言切换插件

<div align="center">

![ComfyUI Language Switcher](https://img.shields.io/badge/ComfyUI-Language%20Switcher-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)

[English](#english) | [中文](#中文)

一个简单易用的 ComfyUI 语言快速切换插件，无需进入设置界面即可一键切换中英文。

A simple and easy-to-use ComfyUI language switcher that allows you to switch between Chinese and English with one click without entering the settings.

</div>

---

## 中文

### ✨ 功能特性

- 🚀 **一键切换** - 无需进入设置界面，点击按钮即可快速切换语言
- 🎯 **热更新** - 使用ComfyUI官方API，无需刷新页面即可切换语言
- 🎨 **界面融合** - 按钮自动融入ComfyUI工具栏，风格统一
- 💾 **自动保存** - 语言设置自动保存，下次启动时保持
- 🔒 **完全安全** - 不修改ComfyUI任何源代码，使用官方扩展机制
- 📱 **自适应** - 按钮自动适配ComfyUI界面，支持窗口缩放

### 📸 效果展示
![动图](https://github.com/user-attachments/assets/a53af565-4a07-490d-9e7a-a9466b65076f)

### 📦 安装方法

#### 方法一：Git 克隆（推荐）

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/olafchou/ComfyUI-ZH-EN-Switcher.git
```

#### 方法二：手动下载

1. 下载本仓库的 ZIP 文件
2. 解压到 `ComfyUI/custom_nodes/ComfyUI-ZH-EN-Switcher` 目录
3. 重启 ComfyUI

### 🎮 使用方法

1. **启动 ComfyUI**
   
   正常启动你的 ComfyUI 应用程序

2. **找到语言切换按钮**
   
   启动后，在 ComfyUI 界面右上角工具栏会看到语言切换按钮
   - 中文状态显示："中文"
   - 英文状态显示："EN"

3. **切换语言**
   
   点击按钮即可切换语言，界面会立即更新

### 🔧 技术说明

#### 工作原理

- 使用 ComfyUI 官方的 JavaScript 扩展机制 (`app.registerExtension`)
- 调用 ComfyUI 的设置 API (`app.ui.settings.setSettingValue`)
- 实现热更新，无需刷新页面
- 完全不修改 ComfyUI 源代码

#### 文件结构

```
ComfyUI-ZH-EN-Switcher/
├── __init__.py              # Python 入口文件
├── js/
│   ├── ComfyUI-ZH-EN-Switcher.js   # 核心功能实现
│   └── styles.css           # CSS 样式（可选）
├── README.md                # 本文件
├── INSTALL.md               # 详细安装指南
└── CHANGELOG.md             # 版本更新日志
```

#### 兼容性

- ✅ ComfyUI 所有版本
- ✅ 支持中文 ⇄ 英文切换
- ✅ Chrome/Edge/Firefox/Safari

### ❓ 常见问题

<details>
<summary><b>Q: 按钮没有出现怎么办？</b></summary>

A: 
1. 确认 ComfyUI 已完全加载
2. 按 F12 打开开发者工具，查看控制台是否有错误
3. 确认插件安装在正确的位置：`ComfyUI/custom_nodes/ComfyUI-ZH-EN-Switcher`
4. 重启 ComfyUI
</details>

<details>
<summary><b>Q: 点击按钮没有反应？</b></summary>

A: 
1. 打开浏览器开发者工具（F12）查看控制台输出
2. 确认浏览器允许 localStorage
3. 尝试手动刷新页面（Ctrl+R）
</details>

<details>
<summary><b>Q: 会影响 ComfyUI 的其他功能吗？</b></summary>

A: 不会。插件使用官方扩展机制，完全独立运行，不修改任何 ComfyUI 源代码。如需卸载，直接删除插件文件夹即可。
</details>

<details>
<summary><b>Q: 支持其他语言吗？</b></summary>

A: 目前仅支持中英文切换。ComfyUI 官方目前也只支持这两种语言。
</details>

### 🗑️ 卸载方法

如不再需要，直接删除插件文件夹：

```bash
# Windows
rmdir /s ComfyUI\custom_nodes\ComfyUI-ZH-EN-Switcher

# Linux/Mac
rm -rf ComfyUI/custom_nodes/ComfyUI-ZH-EN-Switcher
```

然后重启 ComfyUI 即可。

### 📝 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新历史。

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

### 💖 支持

如果这个插件对你有帮助，请给个 ⭐ Star！

---

## English

### ✨ Features

- 🚀 **One-Click Switch** - Quickly switch languages without entering settings
- 🎯 **Hot Update** - Uses ComfyUI official API, no page refresh needed
- 🎨 **UI Integration** - Button automatically integrates into ComfyUI toolbar
- 💾 **Auto Save** - Language settings are automatically saved
- 🔒 **Completely Safe** - Does not modify any ComfyUI source code
- 📱 **Responsive** - Automatically adapts to ComfyUI interface

### 📸 Screenshots

<!-- Please add screenshots to the images folder and uncomment below -->
<!--
![Button Position](images/button-position.png)
*Button in ComfyUI toolbar*

![Chinese UI](images/chinese-ui.png)
*Chinese Interface*

![English UI](images/english-ui.png)
*English Interface*
-->

### 📦 Installation

#### Method 1: Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/olafchou/ComfyUI-ZH-EN-Switcher.git
```

#### Method 2: Manual Download

1. Download the ZIP file from this repository
2. Extract to `ComfyUI/custom_nodes/ComfyUI-ZH-EN-Switcher`
3. Restart ComfyUI

### 🎮 Usage

1. **Start ComfyUI**
   
   Launch your ComfyUI application normally

2. **Find the Language Switch Button**
   
   After startup, you'll see the language switch button in the top right toolbar
   - Chinese mode shows: "中文"
   - English mode shows: "EN"

3. **Switch Language**
   
   Click the button to switch languages, the interface will update immediately

### 🔧 Technical Details

#### How It Works

- Uses ComfyUI's official JavaScript extension mechanism (`app.registerExtension`)
- Calls ComfyUI's settings API (`app.ui.settings.setSettingValue`)
- Implements hot reload without page refresh
- Does not modify any ComfyUI source code

#### File Structure

```
ComfyUI-ZH-EN-Switcher/
├── __init__.py              # Python entry file
├── js/
│   ├── ComfyUI-ZH-EN-Switcher.js   # Core functionality
│   └── styles.css           # CSS styles (optional)
├── README.md                # This file
├── INSTALL.md               # Detailed installation guide
└── CHANGELOG.md             # Version changelog
```

#### Compatibility

- ✅ All ComfyUI versions
- ✅ Chinese ⇄ English switching
- ✅ Chrome/Edge/Firefox/Safari

### ❓ FAQ

<details>
<summary><b>Q: Button doesn't appear?</b></summary>

A: 
1. Confirm ComfyUI is fully loaded
2. Press F12 to open developer tools and check console for errors
3. Confirm plugin is installed in the correct location: `ComfyUI/custom_nodes/ComfyUI-ZH-EN-Switcher`
4. Restart ComfyUI
</details>

<details>
<summary><b>Q: Clicking button has no effect?</b></summary>

A: 
1. Open browser developer tools (F12) to check console output
2. Confirm browser allows localStorage
3. Try manually refreshing the page (Ctrl+R)
</details>

<details>
<summary><b>Q: Will it affect other ComfyUI functions?</b></summary>

A: No. The plugin uses the official extension mechanism, runs independently, and doesn't modify any ComfyUI source code. To uninstall, simply delete the plugin folder.
</details>

<details>
<summary><b>Q: Support for other languages?</b></summary>

A: Currently only supports Chinese and English. ComfyUI officially only supports these two languages.
</details>

### 🗑️ Uninstall

To remove the plugin, simply delete the folder:

```bash
# Windows
rmdir /s ComfyUI\custom_nodes\ComfyUI-ZH-EN-Switcher

# Linux/Mac
rm -rf ComfyUI/custom_nodes/ComfyUI-ZH-EN-Switcher
```

Then restart ComfyUI.

### 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

### 🤝 Contributing

Issues and Pull Requests are welcome!

### 📄 License

This project is licensed under the [MIT License](LICENSE).

### 💖 Support

If this plugin helps you, please give it a ⭐ Star!

---

<div align="center">

Made with ❤️ for ComfyUI Community

</div>






