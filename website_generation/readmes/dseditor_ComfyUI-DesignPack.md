# ComfyUI-DesignPack

A ComfyUI custom node package for generating professional interior design presentations using AI. This package integrates with Google's Gemini API to analyze floor plans and automatically generate PowerPoint presentations with AI-generated content and images.

## 功能簡介 (Features)

- **室內設計簡報自動生成**: 基於平面圖自動生成專業的室內設計簡報
- **AI 內容分析**: 使用 Google Gemini API 分析平面圖並生成結構化的簡報內容
- **多種簡報模板**: 提供五種不同風格的簡報模板
- **圖文整合**: 自動將 AI 生成的圖片整合到簡報中
- **PDF 雜誌生成**: 支援生成 PDF 格式的設計雜誌
- **LLM 管理**: 統一的 LLM API 管理界面

## 節點說明 (Nodes)

### 1. PresentationGenerator (簡報生成器)
分析平面圖並生成簡報數據和圖片提示詞

### 2. PresentationMaker (簡報製作器)
根據生成的數據和圖片創建 PowerPoint 簡報

### 3. PDFMagazineGenerator (PDF雜誌生成器)
生成 PDF 格式的設計雜誌

### 4. LLMManager (LLM管理器)
管理和配置各種 LLM API

## 安裝方法 (Installation)

1. 將此資料夾放入 ComfyUI 的 `custom_nodes` 目錄中
2. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```
3. 重啟 ComfyUI

## 使用方法 (Usage)

### 基本工作流程

1. **配置 LLM API**
   - 在 LLMManager 節點中輸入你的 Google Gemini API Key
   - API Key 會自動保存到 `config.json` 中

2. **準備平面圖**
   - 將平面圖圖片載入到 ComfyUI 中
   - 連接到 PresentationGenerator 節點的 `image` 輸入

3. **生成簡報數據**
   - PresentationGenerator 會分析平面圖並輸出：
     - `image_prompts`: 圖片生成提示詞
     - `json_data`: 結構化的簡報數據

4. **連接提示詞節點**
   - 將 `image_prompts` 輸出連接到 CLIPTextEncode 節點
   - 用於生成相應的室內設計圖片

5. **創建簡報**
   - 將生成的圖片和 `json_data` 連接到 PresentationMaker 節點
   - 配置輸出路徑和簡報模板
   - 執行節點生成 PowerPoint 簡報

### 連接說明

- **image_prompts → CLIPTextEncode**: 將提示詞連接到文字編碼器
- **json_data → PresentationMaker**: 將結構化數據連接到簡報製作器
- **AI生成圖片 → PresentationMaker**: 將生成的圖片連接到簡報製作器

### 配置項目

- **輸出路徑**: 設定簡報檔案的保存位置
- **簡報模板**: 選擇適合的視覺風格
  - 經典簡約 (Classic Minimalist)
  - 現代商務 (Modern Business)
  - 溫馨居家 (Warm Home)
  - 時尚雅緻 (Fashionable Elegant)
  - 清新自然 (Fresh Natural)

## 範例工作流程 (Example Workflow)

```
Floor Plan Image → PresentationGenerator → image_prompts → CLIPTextEncode → Image Generation
                                      ↓
                                  json_data → PresentationMaker ← Generated Images
                                                     ↓
                                              PowerPoint Output
```

## 檔案結構 (File Structure)

```
ComfyUI-DesignPack/
├── __init__.py                    # 節點註冊
├── presentation_generator.py     # 簡報生成器
├── presentation_maker.py        # 簡報製作器
├── pdf_magazine_generator.py    # PDF雜誌生成器
├── llm_manager.py               # LLM管理器
├── requirements.txt             # 依賴套件
├── config.json                  # API設定（自動生成）
└── fonts/                       # 字型檔案
    └── cht.ttf
```

## 注意事項 (Notes)

- 需要有效的 Google Gemini API Key
- 確保圖片格式為 PNG、JPG 或其他常見格式
- 建議使用高解析度的平面圖以獲得更好的分析結果
- 生成的簡報會包含中文內容，需要支援中文字型的 PowerPoint

## 故障排除 (Troubleshooting)

- **記憶體錯誤**: 嘗試降低輸入圖片的解析度
- **API 錯誤**: 檢查 API Key 是否有效及網路連線
- **簡報生成失敗**: 確認輸出路徑可寫入且有足夠空間
- **字型問題**: 確認 fonts 目錄中有必要的字型檔案