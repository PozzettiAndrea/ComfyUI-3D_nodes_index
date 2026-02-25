# ComfyUI-FailSafe-Translate-Node

A fail-safe Google Translate node for ComfyUI, designed to handle network flakiness and provide robust translation capabilities for your workflows.

**Category**: `utils/text`

## Features

- **Fail-Safe**: Built-in retry logic and configurable failure modes.
- **Caching**: Caches results to avoid redundant API calls.
- **Two Modes**:
    - **Simple**: Zero-config, translates to English (default).
    - **Advanced**: Full control over destination language, retries, and failure behavior.

## Supported Languages

`auto, en, ja, zh-CN, zh-TW, ko, fr, de, es, it, ru, pt, nl, pl, tr, ar, hi, bn, pa, jw, ms, vi, th, id, [No Translation]`

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/ah-kun/ComfyUI-FailSafe-Translate-Node.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Nodes

#### 1. Prompt Translate (Google, Fail-safe)
*Simple mode for quick translation to English.*
- **text**: Input text (multiline).
- **src_lang**: Source language (or 'auto', or '[No Translation]').
- **Output**: English translation.

#### 2. Prompt Translate (Google, Fail-safe, Advanced)
*Advanced mode with full configuration.*
- **text**: Input text.
- **src_lang**: Source language (default: 'en', 'auto' removed).
- **dest_lang**: Target language.
- **fail_mode**: Behavior when translation fails after retries:
    - `return_input`: Returns the original text.
    - `return_cached`: Returns the last successful result (if any), otherwise input.
    - `return_error`: Returns an error message string (e.g., "[ERROR] ...").
    - `raise`: Stops the workflow with an error.
- **retries**: Number of retry attempts (default: 3).
- **retry_wait_sec**: Seconds to wait between retries (default: 1.0).

## Requirements

- `deep-translator`

---

# 日本語 (Japanese)

**カテゴリ**: `utils/text`

ComfyUI用のフェイルセーフなGoogle翻訳ノードです。ネットワークの不安定さに対応し、ワークフローに堅牢な翻訳機能を提供します。

## 特徴

- **フェイルセーフ**: リトライロジックと設定可能な失敗時の動作を内蔵。
- **キャッシュ**: 結果をキャッシュして冗長なAPI呼び出しを回避。
- **2つのモード**:
    - **Simple**: 設定不要、英語への翻訳（デフォルト）。
    - **Advanced**: 翻訳先言語、リトライ回数、失敗時の動作を完全に制御可能。

## 対応言語

`auto, en, ja, zh-CN, zh-TW, ko, fr, de, es, it, ru, pt, nl, pl, tr, ar, hi, bn, pa, jw, ms, vi, th, id, [No Translation]`

## インストール

1. `ComfyUI/custom_nodes/` ディレクトリにリポジトリをクローンします:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/ah-kun/ComfyUI-FailSafe-Translate-Node.git
   ```
2. 依存関係をインストールします:
   ```bash
   pip install -r requirements.txt
   ```

## 使い方

### ノード

#### 1. Prompt Translate (Google, Fail-safe)
*英語への素早い翻訳のためのシンプルモード。*
- **text**: 入力テキスト（複数行）。
- **src_lang**: 元の言語（または 'auto'、または '[No Translation]'）。
- **Output**: 英語の翻訳結果。

#### 2. Prompt Translate (Google, Fail-safe, Advanced)
*完全な設定が可能なアドバンスドモード。*
- **text**: 入力テキスト。
- **src_lang**: 元の言語（デフォルト: 'en'、'auto'は除外）。
- **dest_lang**: 翻訳先の言語。
- **fail_mode**: リトライ後の翻訳失敗時の動作:
    - `return_input`: 元のテキストを返します。
    - `return_cached`: 最後に成功した結果があればそれを返し、なければ入力を返します。
    - `return_error`: エラーメッセージ文字列（例: "[ERROR] ..."）を返します。
    - `raise`: エラーでワークフローを停止します。
- **retries**: リトライ試行回数（デフォルト: 3）。
- **retry_wait_sec**: リトライ間の待機秒数（デフォルト: 1.0）。
