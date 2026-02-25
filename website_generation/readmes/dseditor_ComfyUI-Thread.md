# ComfyUI-Thread

A ComfyUI custom node package for seamless integration with Threads (Meta's social platform). This package allows you to publish posts, manage images/videos, and retrieve post history directly from your ComfyUI workflows.

ComfyUI 的 Threads 整合自定義節點包，讓您能夠直接在 ComfyUI 工作流程中發布貼文、管理圖片/影片和獲取發文歷史。

> **完整功能參考**: 本節點為實現發布的簡要功能，包括文字，圖片、影片與多圖片容器，需要自訂ComfyUIHTTPS網址，如使用ngrok，若需要設定更完整的發布節點包括使用圖床金鑰、臨時伺服器與權杖管理測試，請參考 [ComfyUI Threads Uploader](https://github.com/clinno0616/comfyui-threads-uploader)

## Features | 功能特色

### 🚀 **Post Publishing | 發文功能**
- ✅ Text-only posts | 純文字發文
- ✅ Single image posts | 單圖發文
- ✅ Multi-image carousel posts | 多圖輪播發文
- ✅ Video posts with smart path detection | 支援影片發文及智能路徑檢測
- ✅ Image tensor support (from ComfyUI generators) | 支援圖片張量（來自 ComfyUI 生成器）
- ✅ External image/video URL support | 支援外部圖片/影片網址
- ✅ Local video file processing | 支援本地影片檔案處理

### 📊 **Analytics | 數據分析**
- ✅ Retrieve post history | 獲取發文歷史
- ✅ Customizable date range (1-365 days) | 可自訂日期範圍（1-365天）
- ✅ Formatted post content output | 格式化的貼文內容輸出

### ⚙️ **Configuration | 配置管理**
- ✅ Long-lived access token management | 長期訪問令牌管理
- ✅ Custom ComfyUI URL support | 支援自訂 ComfyUI 網址
- ✅ Automatic configuration persistence | 自動配置持久化
- ✅ Intelligent media processing | 智能媒體處理

## Installation | 安裝方式

### Using ComfyUI Manager | 使用 ComfyUI Manager 安裝

1. Open ComfyUI Manager | 開啟 ComfyUI Manager
2. Search for **ComfyUI-Thread** | 搜尋 **ComfyUI-Thread**
3. Install the package | 安裝套件
4. Restart ComfyUI | 重啟 ComfyUI

### Manual Installation | 手動安裝

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-repo/ComfyUI-Thread.git
pip install -r ComfyUI-Thread/requirements.txt
```

## Setup | 設置

### 1. Get Threads API Credentials | 獲取 Threads API 憑證

You need to obtain the following from Meta Developers:
您需要從 Meta 開發者平台獲取以下資訊：

- `USER_ID` - Your Threads user ID | 您的 Threads 用戶 ID
- `ACCESS_TOKEN` - Short-lived access token | 短期訪問令牌
- `APP_SECRET` - Your app secret | 您的應用密鑰

**參考資源**: 有關憑證的取得方式，可以參考 SDK 的開發者網址，同時你也必須安裝 **requirements.txt** 中的 SDK：
https://nijialin.com/2024/08/17/python-threads-sdk-introduction/

### 2. Configure API Access | 配置 API 訪問

Use the **Start With Long Live Token** node with your credentials to generate a long-lived access token.

使用 **Start With Long Live Token** 節點輸入您的憑證來生成長期訪問令牌。

## Nodes | 節點說明

### 📝 **Start With Long Live Token**
Initialize the Threads API connection and generate a long-lived access token.

初始化 Threads API 連接並生成長期訪問令牌。

**Inputs | 輸入:**
- `USER_ID` - Your Threads user ID | 您的 Threads 用戶 ID
- `ACCESS_TOKEN` - Short-lived access token | 短期訪問令牌  
- `APP_SECRET` - Your app secret | 您的應用密鑰

**Outputs | 輸出:**
- `result` - Configuration status message | 配置狀態訊息

**Note | 注意**: 成功後會在 `token` 資料夾下產生一個 `thread_config.json` 檔案。

---

### 📤 **Publish Thread**
Publish posts to Threads with text and images, supporting single images and multi-image carousels.

發布包含文字和圖片的 Threads 貼文，支援單圖和多圖輪播。

**Inputs | 輸入:**
- `text` (required) - Post content | 貼文內容（必填）
- `ComfyUIHttpsURL` (optional) - Custom ComfyUI base URL | 自訂 ComfyUI 基礎網址（選填）
- `image` (optional) - Image tensor input | 圖片張量輸入（選填）
- `image_url` (optional) - External image URLs, one per line | 外部圖片網址，每行一個（選填）

**Outputs | 輸出:**
- `result` - Post status and URL | 發文狀態和網址

**Features | 特色功能:**
- Supports single and multiple images | 支援單圖和多圖
- Automatic carousel creation for multiple images | 多圖時自動創建輪播
- Image tensor processing with batch support | 支援批次圖片張量處理

---

### 🎬 **Thread Publish Video**
Publish video posts to Threads with intelligent path detection and media container status monitoring.

發布影片貼文到 Threads，具備智能路徑檢測和媒體容器狀態監控。

**Inputs | 輸入:**
- `text` (required) - Post content | 貼文內容（必填）
- `video_path` (required) - Video path or URL | 影片路徑或網址（必填）
- `ComfyUIHttpsURL` (optional) - Custom ComfyUI base URL | 自訂 ComfyUI 基礎網址（選填）

**Outputs | 輸出:**
- `result` - Post status and URL | 發文狀態和網址

**Smart Path Detection | 智能路徑檢測:**
- **Network URL**: Automatically detected if starts with `http://` or `https://` | 網路網址：以 `http://` 或 `https://` 開頭時自動檢測
- **Local Path**: All other inputs treated as local file paths | 本地路徑：其他輸入均視為本地檔案路徑

**Media Processing | 媒體處理:**
- Automatic file copying to ComfyUI output directory | 自動複製檔案到 ComfyUI 輸出目錄
- Status monitoring every 20 seconds | 每 20 秒檢查狀態
- Support for common video formats (MP4, MOV, AVI, etc.) | 支援常見影片格式
- File size validation (max 1GB) | 檔案大小驗證（最大 1GB）

---

### 📈 **Threads History**
Retrieve your post history from Threads with customizable date ranges.

從 Threads 獲取您的發文歷史，可自訂日期範圍。

**Inputs | 輸入:**
- `backfill_days` - Number of days to look back (1-365) | 回溯天數（1-365）

**Outputs | 輸出:**
- `history_content` - Formatted post history | 格式化的發文歷史

## Usage Examples | 使用範例

### Example Workflow | 範例工作流

範例工作流使用了 ollama-gemini 節點來產生圖文提示內容，此節點需自行配置 API 金鑰才能使用 Gemini：
https://github.com/al-swaiti/ComfyUI-OllamaGemini

有關圖像生成模型的部分，可以修改為你自己常用的模型與節點。

### Simple Text Post | 簡單文字發文
1. Configure **Start With Long Live Token** with your API credentials | 使用 API 憑證配置令牌節點
2. Connect **Publish Thread** and enter your text content | 連接發文節點並輸入文字內容
3. Execute to post | 執行發文

### Image Post with Generated Content | 使用生成內容的圖片發文
1. Create images using ComfyUI generators | 使用 ComfyUI 生成器創建圖片
2. Connect image output to **Publish Thread** `image` input | 將圖片輸出連接到發文節點的圖片輸入
3. Add your text content | 添加文字內容
4. Execute to post with generated images | 執行以發布包含生成圖片的貼文

**Note | 注意**: 支援 ImageBatch/BatchSize，不支援 ImageList 做為容器。可將多張圖片使用 MakeImageBatch 後上傳。

### Video Post | 影片發文
1. Configure **Thread Publish Video** with your content | 配置影片發文節點
2. Enter video path (local file or URL) | 輸入影片路徑（本地檔案或網址）
3. Add your text content | 添加文字內容
4. Execute and wait for processing | 執行並等待處理完成

### Multi-Image Carousel | 多圖輪播
1. In **Publish Thread**, enter multiple image URLs in `image_url` field (one per line) | 在發文節點的圖片網址欄位輸入多行 HTTPS 網址
2. Add your text content | 添加文字內容
3. Execute to create a carousel post | 執行創建輪播貼文

### Analyze Post History | 分析歷史貼文
1. Use **Threads History** to retrieve recent posts | 使用歷史節點獲取近期貼文
2. Set `backfill_days` to desired time range | 設定回溯天數
3. Review formatted output for content analysis | 查看格式化輸出進行內容分析

## File Structure | 檔案結構

```
ComfyUI-Thread/
├── __init__.py              # Module initialization | 模組初始化
├── nodes.py                 # Main node implementations | 主要節點實作
├── requirements.txt         # Python dependencies | Python 相依性
└── token/                   # Auto-generated config directory | 自動生成的配置目錄
    ├── thread_config.json   # API credentials | API 憑證
    └── url.json            # ComfyUI URL configuration | ComfyUI 網址配置
```

## Requirements | 系統需求

- ComfyUI
- Python 3.8+
- PIL (Pillow)
- numpy
- torch
- requests
- threads_sdk

## API Limitations | API 限制

- **Scope**: Only works with your own Threads account | 僅適用於您自己的 Threads 帳號
- **Rate Limits**: Subject to Meta's API rate limits (250 posts per 24 hours) | 受 Meta API 速率限制約束（24小時內250則貼文）
- **Video Requirements**: Follows Threads' strict video format requirements | 遵循 Threads 嚴格的影片格式要求
- **Image Requirements**: Must be publicly accessible URLs or properly configured HTTPS | 圖片必須是可公開存取的網址或正確配置的 HTTPS

## Configuration Notes | 配置說明

### ComfyUI HTTPS URL | ComfyUI HTTPS 網址
- 此網址必須使用 ngrok 等建立 HTTPS 對外的網址
- 填入一次之後會記憶在 `url.json` 檔案中
- 網址變更時才需要重新填寫
- 沒有填過則預設為 127.0.0.1，image 節點會無法傳圖只能使用網址

## Troubleshooting | 疑難排解

### Common Issues | 常見問題

**"Please execute StartWithLongLiveToken node first"**
- Make sure you've run the token configuration node before posting
- 確保在發文前已執行令牌配置節點

**"Param image_url is not a valid URL"**
- Check that your image URLs are complete and accessible
- Ensure URLs start with `https://`
- 檢查圖片網址是否完整且可存取

**Image not displaying in posts | 發送成功圖片無法顯示，只有文字**
- Verify your ComfyUI URL is accessible from the internet
- Check the `ComfyUIHttpsURL` configuration
- 確認您的 ComfyUI 網址可從網際網路存取

**Video processing timeout | 影片處理超時**
- Check video file size (max 1GB)
- Verify video format compatibility
- Ensure stable internet connection
- 檢查影片檔案大小（最大 1GB）
- 確認影片格式相容性

**Local video file not found | 本地影片檔案未找到**
- Verify the file path is correct
- Check file permissions
- Ensure the file exists and is accessible
- 確認檔案路徑正確
- 檢查檔案權限

## License | 授權

MIT License

## Support | 支援

If you encounter any issues or have questions, please open an issue on GitHub.

如果您遇到任何問題或有疑問，請在 GitHub 上開啟 issue。

---

**Note**: This project is not officially affiliated with Meta or Threads. Use responsibly and in accordance with Threads' Terms of Service.

**注意**：此專案與 Meta 或 Threads 無官方關聯。請負責任地使用並遵守 Threads 的服務條款。