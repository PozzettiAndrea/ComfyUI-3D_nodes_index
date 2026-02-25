# Super Captioner for ComfyUI

一個強大的多模型圖像描述節點，支援本地 BLIP 模型和雲端的 Google Gemini API，專為 ComfyUI 設計。

![workflow_example](https://i.imgur.com/your-image-url.jpg) <!-- 強烈建議您截一張工作流圖片並上傳到圖床（如 imgur.com），然後替換此 URL -->

---

## ✨ 功能特色 (Features)

- **多模型支援**: 在同一個節點中透過下拉選單選擇 `blip-large` (本地) 或 `gemini-pro-vision` (雲端)。
- **本地優先**: BLIP 模型完全在本地運行，保護您的隱私，無需 API Key。
- **高品質雲端**: 整合 Google Gemini Pro Vision，提供頂級的中文和多語言描述能力。
- **智慧 VRAM 管理**: 本地模型在使用後會自動從 VRAM 中卸載，為後續的 Stable Diffusion 流程騰出空間。

## 🔧 如何安裝 (Installation)

### 方法一: 使用 ComfyUI Manager (推薦)
1. 安裝 [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)。
2. 在 Manager 菜單中，點擊 "Install Custom Nodes"。
3. 搜尋 "SuperCaptioner" 或您的 GitHub 用戶名，找到此節點並點擊安裝。
4. **重啟 ComfyUI**。節點所需的依賴項 (`requirements.txt`) 將會被自動安裝。

### 方法二: 手動安裝 (Git Clone)
1. 進入 `ComfyUI/custom_nodes/` 目錄。
2. 打開終端機，執行以下指令：
   ```bash
   git clone https://github.com/ARPlanet-Gary/SuperCaptioner.git
