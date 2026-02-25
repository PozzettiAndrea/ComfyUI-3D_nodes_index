# ComfyUI-WebPrompter
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

一個為 ComfyUI 設計的自訂節點套件，旨在將網路內容自動化地轉換為由 AI 精煉的新聞稿。這個簡化版專注於核心的「獲取-處理」流程，提供了一個快速、直接的自動化體驗。

This is a custom node suite for ComfyUI that automates the conversion of web content into an AI-refined news script. This simplified version focuses on the core "fetch-and-process" workflow for a fast and direct automation experience.

---

### ✨ 功能亮點 (Features)

*   **網址直達新聞稿**: 直接輸入一個新聞網址，節點會自動抓取主要內容。
*   **LLM 智能轉化**: 利用強大的大語言模型（如 GPT-4o）將原始文本轉化為符合事實、適合播報的新聞字幕稿。
*   **支援手動輸入**: 除了網址，您也可以直接貼上自己的文本作為輸入源。
*   **高度可配置**: 您可以自訂指導 LLM 的 System Prompt，以及模型、溫度等參數。

### 🎨 節點工作流預覽 (Node Workflow)

簡化後的工作流非常直接。`LLM News Script Generator` 的輸出即為最終結果，可以直接連接到下游節點。

```
+-------------------+      +--------------------------+      +--------------------+
|                   |      |                          |      |                    |
| 1. Content Fetcher+----->| 2. News Script Generator +----->| Downstream Node    |
| (URL / Manual)    | text | (Converts to script)     | script| (e.g., Save Text,  |
|                   |      |                          |      |  CLIP Text Encode) |
+-------------------+      +--------------------------+      +--------------------+

```

### 📦 安裝 (Installation)

#### 方法 1: 使用 ComfyUI Manager (推薦)

1.  安裝 [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)。
2.  點擊 `Manager` 按鈕 -> `Install Custom Nodes`。
3.  搜尋 `WebPrompter` 並點擊 `Install`。
4.  重啟 ComfyUI。

#### 方法 2: 手動安裝 (Git Clone)

1.  打開終端 (Terminal)，進入 `ComfyUI/custom_nodes/` 資料夾。
2.  執行以下指令，複製本專案：
    ```bash
    git clone https://github.com/Gary-yeh/ComfyUI-WebPrompter.git
    ```

3.  安裝所需的依賴套件：
    ```bash
    cd ComfyUI-WebPrompter
    pip install -r requirements.txt
    ```

4.  重啟 ComfyUI。

### 🚀 使用指南 (Usage)

#### ⚠️ 第一步：設置 API 金鑰

`LLM News Script Generator` 節點需要使用 OpenAI 的 API。請務必在使用前將您的 API 金鑰設置為名為 `OPENAI_API_KEY` 的**環境變數**。

#### 核心工作流程

1.  **新增 `1. Content Fetcher` 節點**:
    *   `mode` 設為 `URL`，並填入新聞網址。
    *   或者，`mode` 設為 `Manual`，直接輸入您的內容。
    *   **（可選，但推薦）**: 為了在處理前預覽抓取的內容，您可以將此節點的 `original_text` 輸出額外連接到一個 `Show Text` 或 `Save Text File` 節點進行檢查。

2.  **新增 `2. News Script Generator` 節點**:
    *   將 `Content Fetcher` 的 `original_text` 輸出接口，連接到本節點的 `original_text` 輸入接口。
    *   根據您的需求調整 `system_prompt` 和模型參數。

3.  **連接到最終目標**:
    *   `News Script Generator` 的 `news_script` 輸出即為**最終結果**。
    *   **目標是生成文本文件**: 將 `news_script` 連接到 `Save Text File` (來自 WAS Node Suite) 節點的 `text` 輸入。
    *   **目標是生成圖像**: 將 `news_script` 連接到 `CLIP Text Encode` 節點的 `text` 輸入。

### 🤝 貢獻 (Contributing)

歡迎任何形式的貢獻！如果您發現了 Bug 或有任何功能建議，請隨時在 [GitHub Issues](https://github.com/Gary-yeh/ComfyUI-WebPrompter/issues) 中提出。

### 📄 授權 (License)

本專案採用 [MIT License](LICENSE) 授權。
