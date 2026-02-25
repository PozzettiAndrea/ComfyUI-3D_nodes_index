# TJ_PolkaDot

[English](./README_EN.md) | 日本語

ComfyUI用の水玉コラージュ生成カスタムノード集です。様々な形状のマスクを自動配置し、美しいコラージュ画像を簡単に作成できます。

> **注意**: このプロジェクトは生成AIのサポートを受けて開発されています。一部、不完全な箇所や改善の余地がある可能性があります。問題を見つけた場合は、Issueでお知らせください。

![Example Output](sample/ScreenShot.png)

## 特徴

- 🎨 **10種類の形状**: 円、ハート、星、ダイヤ、四角、六角形、三角、十字、月、花
- 🎯 **高度な配置制御**: 重なり率、カバレッジ、回転、スケールを細かく調整可能
- 🚫 **除外マスク対応**: 特定領域への配置を禁止
- 🔗 **チェーン配置**: 複数ノードを直列接続して段階的に配置
- 🎨 **カラー合成**: 最大3レイヤーのマスクを個別の色で合成
- 📏 **画面外配置**: はみ出し許容率を設定して、エッジまで自然に配置
- ⚡ **最適化された配置アルゴリズム**: 占有領域を動的に除外し、効率的に配置

## インストール

### ComfyUI Manager経由（推奨）

1. ComfyUI Managerを開く
2. "Custom Nodes Manager"を選択
3. "TJ_PolkaDot"を検索してインストール
4. ComfyUIを再起動

## ノード一覧

### 1. Shape Mask Generator（形状マスク生成）

単一の形状マスクを生成します。

**パラメータ:**
- `shape_type`: 形状の種類（circle, heart, star, diamond, square, hexagon, triangle, cross, moon, flower)
- `size`: 形状のサイズ（ピクセル）
- `rotation`: 回転角度（度）
- `scale`: スケール倍率
- `blur_radius`: ぼかし半径

**利用可能な形状:**
- **circle** - 円形
- **heart** - ハート
- **star** - 星（5角星）
- **diamond** - ダイヤモンド
- **square** - 正方形
- **hexagon** - 六角形
- **triangle** - 三角形
- **cross** - 十字/プラス
- **moon** - 三日月
- **flower** - 花（5枚花弁）

### 2. Advanced Shape Placement（高度な形状配置）★メイン機能

形状マスクを領域内に複数配置します。

**入力:**
- `shape_mask`: 配置する形状マスク（必須）
- `region_mask`: 配置可能領域を定義するマスク（オプション、省略時は全画面）
- `base_mask`: 既存の配置（チェーン接続用、オプション）
- `exclusion_mask`: 配置禁止領域（オプション）

**パラメータ:**
- `count`: 配置する形状の数（デフォルト: 30）
- `scale_min` / `scale_max`: スケール範囲（デフォルト: 0.06 - 0.15）
- `rotation_min` / `rotation_max`: 回転角度範囲（度、デフォルト: -30 - 30）
- `overlap_ratio`: 重なり許容率（0-1、デフォルト: 0.5）
  - 0.0 = 重なり禁止
  - 1.0 = 完全に重なってもOK
- `coverage_min`: 領域内カバレッジ最小値（0-1、デフォルト: 0.0）
  - 0.0 = 少しでも領域内ならOK
  - 1.0 = 完全に領域内に収まる必要あり
- `exclusion_tolerance`: 除外領域への侵入許容率（0-1、デフォルト: 0.0）
- `out_of_bounds_tolerance`: 画面外へのはみ出し許容率（0-1、デフォルト: 0.0）
  - 0.0 = 完全に画面内に収まる必要あり
  - 0.5 = 50%まで画面外に出てもOK（推奨）
- `max_consecutive_fails`: 早期終了の連続失敗回数（デフォルト: 100）
- `seed`: ランダムシード

**出力:**
- `MASK (all)`: すべての配置を含む合成マスク（base_mask含む）
- `MASK (new)`: このノードで新規追加した形状のみ
- `JSON`: 各形状の位置・スケール・回転情報

### 3. Colored Mask Compositor（カラーマスク合成）

複数のマスクレイヤーを個別の色で合成します。

**入力:**
- `base_image`: ベース画像
- `mask_1` / `mask_2` / `mask_3`: マスクレイヤー（オプション）



**パラメータ（各レイヤー）:**
- `color_X_r/g/b`: RGB色（0-255）
- `opacity_X`: 不透明度（0.0-1.0）
- `blend_mode_X`: ブレンドモード（normal, multiply, screen, overlay, add）

## 使用例

### 基本的な使い方

1. **Shape Mask Generator**で形状を作成
2. **Advanced Shape Placement**で配置
3. **Colored Mask Compositor**で色を付ける

### チェーン配置

複数の形状を段階的に配置:

```
Shape(Heart) → Advanced Placement(count=50) → Advanced Placement(count=30, shape=Circle) → Compositor
                                    ↓
                              MASK (new) を次の base_mask に接続
```

### 除外マスク

人物などを避けて配置:

```
画像 → Mask生成 → Invert → exclusion_mask入力
```

## パラメータ推奨値

### 密度の高い配置
```
count: 100-150
overlap_ratio: 0.7-0.8
out_of_bounds_tolerance: 0.3-0.5
```

### 散らばった配置
```
count: 20-40
overlap_ratio: 0.2-0.4
out_of_bounds_tolerance: 0.5
```

### エッジまで配置
```
out_of_bounds_tolerance: 0.3以上
```

## トラブルシューティング

### 配置数が目標に達しない

- `overlap_ratio`を増やす（重なりを許容）
- `max_consecutive_fails`を増やす
- `out_of_bounds_tolerance`を増やす（エッジ配置を許容）
- `exclusion_tolerance`を増やす（除外領域を緩和）

### 配置が偏る

- `seed`を変更してランダム性を変える
- `region_mask`を調整して配置可能領域を広げる

### エッジに配置されない

- `out_of_bounds_tolerance`を0.3〜0.5に設定

## 技術詳細

### 配置アルゴリズム

1. **有効位置の取得**: `region_mask`から配置可能なピクセル座標を抽出
2. **シャッフル**: 空間的な偏りを防ぐため座標をランダム化
3. **動的除外**: 配置済み領域を定期的に除外し、効率を向上
4. **衝突判定**: 重なり率、カバレッジ、除外領域をチェック
5. **早期終了**: 連続失敗が閾値を超えたら終了

### パフォーマンス

- 150個の形状を159回の試行で配置（効率99.4%）
- 占有領域の動的除外により、密な配置でも高速

## ライセンス

MIT License

## 作者

TJ16th

## 貢献

Issue、Pull Requestを歓迎します！

## 更新履歴

### v0.1.0 (2025-11-03)
- 初回リリース
- 10種類の形状サポート
- 高度な配置制御
- チェーン配置対応
- カラー合成機能
- 画面外配置対応
- 配置効率の最適化
