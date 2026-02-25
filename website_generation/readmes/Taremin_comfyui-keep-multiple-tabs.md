# comfyui-keep-multiple-tabs [Deprecated]

> [!WARNING]
> **この拡張機能は非推奨（Deprecated）です。**
>
> ComfyUI 公式フロントエンドにワークフロータブの永続化機能が組み込まれたため、この拡張機能は不要になりました。
> 競合を避けるため、アンインストールをお勧めします。

## 非推奨の経緯

この拡張機能は、ComfyUI でブラウザをリロードや再起動した際に複数のワークフロータブが失われる問題を解決するために作成されました。

その後、ComfyUI 公式フロントエンド ([ComfyUI_frontend](https://github.com/Comfy-Org/ComfyUI_frontend)) に同等の機能が組み込まれました:

- [PR #6050](https://github.com/Comfy-Org/ComfyUI_frontend/pull/6050): ワークフロータブの永続化機能の追加
- [PR #8854](https://github.com/Comfy-Org/ComfyUI_frontend/pull/8854): 自動保存に関するバグ修正 ([Issue #8778](https://github.com/Comfy-Org/ComfyUI_frontend/issues/8778))

バグ修正を含む安定版は **v1.38.14** 以降、nightly 版は **v1.40.4** 以降でリリースされています。

この拡張機能はバージョン検出を行い、修正済みのフロントエンドバージョンが検出された場合にトースト通知でアンインストールを推奨します。

---

これは [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 用の拡張です。
複数のワークフロータブをリロードや再起動をしたときに失われないように保持します。


## インストール

### ComfyUI

下記の二通りからお好きな方法でインストールしてください。

1. `custom_nodes` にこのリポジトリを clone する
2. `ComfyUI Manager Menu` の `Install via Git URL` にこのリポジトリのURLを入力してインストールする


## 注意

ブラウザの `localStorage` を使用して保持しています。
`keep-multiple-tabs-workflows` にこの拡張で使用するデータが入っているので、不要になってこの拡張の痕跡を消したい場合はこのキーを削除してください。

## ライセンス

[MIT](./LICENSE)
