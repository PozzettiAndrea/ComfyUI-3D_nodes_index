# ComfyUI Chinese Converter

為了解決部分 TTS 模型不支援繁體中文的問題，提供繁體與簡體中文的相互轉換。 <br/>
此節點透過 OpenCC 進行轉換，完全離線運行。


## 🔧 自訂節點
   - **"TraditionalToSimplifiedNode"** - 繁體轉簡體
   - **"SimplifiedToTraditionalNode"** - 簡體轉繁體

## 🚀 安裝

1. 導航到 ComfyUI 的 custom_nodes 資料夾
2. 開啟命令列介面 (cmd, powershell, mac terminal 等)
3. `git clone` (或下載此專案並拖拽到該位置)
4. `pip install -r requirements.txt`
5. 重啟 ComfyUI

## ⚠️ 備註

- 如果無法使用，請注意現存的依賴和 opencc 是否有版本衝突
- OpenCC 基於預定義的轉換字典，無法涵蓋所有漢字，因此部分生僻字可能無法轉換