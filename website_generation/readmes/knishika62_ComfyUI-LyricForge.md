# ComfyUI-LyricForge

AI音楽生成モデル用のスタイルタグと歌詞を、キーワードから自動生成するComfyUI Custom Nodeです。

## 対応モデル

- **[HeartMuLa](https://github.com/benjiyaya/HeartMuLa_ComfyUI)** - カンマ区切りスタイルタグ形式
- **[ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5)** - 自然言語キャプション形式 **NEW!**

**v2.2.0**: ACE-Step 1.5に対応しました。BPM・Key/Scaleの自動推測機能付き。

## 機能

- **キーワード入力**: 自然言語のキーワードを入力
- **自動タグ/キャプション生成**: 対象モデルに応じた形式で出力
- **歌詞生成**: 構造タグを含む完全な歌詞を生成
- **BPM/Key自動推測**: ACE-Step用にBPMとKey/Scaleを自動推測
- **LLM API対応**: OpenAI API互換のエンドポイント対応（OpenAI, LM Studio, Ollama等）
- **多言語対応**: 日本語、英語、中国語の歌詞生成

## インストール

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/ComfyUI-LyricForge.git
cd ComfyUI-LyricForge
pip install -r requirements.txt
```

ComfyUIを再起動してください。

## ノード一覧

| ノード名 | 対象モデル | 出力 |
|---------|-----------|------|
| LyricForge Song Generator | HeartMuLa | style_tags, lyrics |
| LyricForge ACE-Step Generator | ACE-Step 1.5 | caption, lyrics, bpm, key_scale |

---

## HeartMuLa用: LyricForge Song Generator

### 入力パラメータ

- **keywords**: 楽曲のキーワード（例: "j-pop 冬の歌 女性ボーカル 雪 カフェ"）
- **api_endpoint**: LLM APIのエンドポイントURL
- **api_key**: APIキー
- **model**: 使用するモデル名
- **language**: 歌詞の言語（Japanese / English / Chinese）
- **song_structure**: 楽曲構成（Standard / Short / Extended）
- **temperature**: 生成の創造性（0.0-2.0）

### 出力

| 出力名 | 説明 | 例 |
|--------|------|-----|
| style_tags | カンマ区切りスタイルタグ | `Pop,Female,Soft,Warm,Piano,Cafe` |
| lyrics | 構造タグ付き歌詞 | `[Verse]\n歌詞...` |

### ワークフロー例

```
LyricForge Song Generator
    ↓ style_tags, lyrics
HeartMuLa Node
    ↓
Save Audio
```

---

## ACE-Step 1.5用: LyricForge ACE-Step Generator

### 入力パラメータ

- **keywords**: 楽曲のキーワード（例: "j-pop 冬の歌 女性ボーカル 雪 カフェ"）
- **api_endpoint**: LLM APIのエンドポイントURL
- **api_key**: APIキー
- **model**: 使用するモデル名
- **language**: 歌詞の言語（Japanese / English / Chinese）
- **song_structure**: 楽曲構成（Standard / Short / Extended）
- **temperature**: 生成の創造性（0.0-2.0）

### 出力

| 出力名 | 型 | 説明 | 例 |
|--------|-----|------|-----|
| caption | STRING | 自然言語スタイル説明 | `soft piano ballad with female breathy vocal` |
| lyrics | STRING | 構造タグ付き歌詞 | `[Verse 1]\n歌詞...` |
| bpm | INT | 推測されたBPM | `80` |
| key_scale | STRING | 推測されたKey/Scale | `A minor` |

### ワークフロー例

```
LyricForge ACE-Step Generator
    ↓ caption → TextEncodeAceStepAudio1.5 (caption入力)
    ↓ lyrics  → TextEncodeAceStepAudio1.5 (lyrics入力)
    ↓ bpm     → TextEncodeAceStepAudio1.5 (bpm入力)
    ↓ key_scale → ※手動でコピペ（COMBO入力のため直接接続不可）
        ↓
    KSampler → VAEDecodeAudio → Save Audio
```

**注意**: key_scaleはCOMBO型入力のため直接接続できません。出力値（例: `E minor`）をACE-Stepノードで手動選択してください。

---

## 対応タグ体系

### HeartMuLa（公式論文 arXiv:2601.10547 準拠）

8カテゴリ、選択確率順：

1. **Genre (0.95)** - Pop, Rock, K-pop, Jazz, Electronic等
2. **Timbre (0.50)** - Bright, Dark, Warm, Soft等
3. **Gender (0.375)** - Male, Female
4. **Mood (0.325)** - Happy, Sad, Romantic, Energetic等
5. **Instrument (0.25)** - Piano, Guitar, Synthesizer等
6. **Scene (0.20)** - Cafe, Dance, Party等
7. **Region (0.125)** - Asian, Western等
8. **Topic (0.10)** - Love, Dream, Hope等

### ACE-Step 1.5

自然言語キャプション形式。以下の要素を組み合わせ：

- **ジャンル**: pop, rock, jazz, electronic, K-pop, J-pop等
- **雰囲気**: melancholic, uplifting, energetic, dreamy等
- **楽器**: acoustic guitar, piano, synth pads, 808 drums等
- **音質**: warm, bright, crisp, airy, punchy等
- **ボーカル**: female vocal, male vocal, breathy, powerful等

---

## API設定例

### LM Studio（推奨）

```
api_endpoint: http://localhost:1234
api_key: lm-studio
model: local-model
```

### OpenAI

```
api_endpoint: https://api.openai.com/v1/chat/completions
api_key: sk-...
model: gpt-4
```

### Ollama

```
api_endpoint: http://localhost:11434
api_key: dummy
model: llama3.1
```

**注意**: エンドポイントは `/v1/chat/completions` を自動補完します。

---

## 使用例

### 例1: 冬のカフェソング（HeartMuLa）

**入力キーワード:**
```
j-pop 冬の歌 女性ボーカル 雪 カフェ
```

**生成されるタグ:**
```
Pop,Female,Soft,Warm,Piano,Acoustic Guitar,Cafe,Romantic
```

### 例2: 同じキーワード（ACE-Step）

**生成されるキャプション:**
```
soft J-pop ballad with female breathy vocal, warm piano and acoustic guitar, cozy cafe atmosphere
```

**生成されるBPM:** `75`
**生成されるKey/Scale:** `F major`

---

## トラブルシューティング

### API接続エラー

- APIキーが正しいか確認
- エンドポイントURLが正確か確認
- ネットワーク接続を確認

### 生成結果が期待と異なる

- キーワードをより具体的に記述
- temperatureパラメータを調整
- 使用するLLMモデルを変更（GPT-4推奨）

### ノードが表示されない

- ComfyUIを完全に再起動
- `requirements.txt`の依存関係を再インストール

---

## ライセンス

MIT License

## 関連リンク

- [HeartMuLa_ComfyUI](https://github.com/benjiyaya/HeartMuLa_ComfyUI)
- [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

---

## 更新履歴

### v2.2.0 (2025-02-04)
- **ACE-Step 1.5対応** - 新ノード `LyricForge ACE-Step Generator` を追加
- 自然言語キャプション形式での出力に対応
- BPM・Key/Scaleの自動推測機能
- ACE-Step仕様解析ドキュメント（ACESTEP_ANALYSIS.md）を追加

### v2.1.0 (2025-01-24)
- 歌詞出力から細粒度スタイルタグを削除（構造タグのみに簡略化）

### v2.0.0 (2025-01-22)
- HeartMuLa公式論文（arXiv:2601.10547）の仕様に完全準拠
- 選択確率による優先度を明示化
- 公式論文との対照分析ドキュメント（HEARTMULA_ANALYSIS.md）を追加

### v1.0.0 (2025-01-22)
- 初回リリース
