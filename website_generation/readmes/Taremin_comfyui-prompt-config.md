# ComfyUI Prompt Config

これは [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 用のカスタムノードです。
`PromptGenerationConfig` ノードでは画像生成時の縦横のサイズやステップ数, CFGScaleなどの設定をプロンプトで設定することが出来ます。
`PromptEdit`ノードではプロンプトからネガティブプロンプトへ追加（またはその逆）や、正規表現を用いたプロンプトの置換も行うことが出来ます。

## 機能

### PromptGenerationConfig

```
<config[:swap][:key1=value1[:key2=value2...]]>
```

`key` として有効なものは以下の通りです。
- width
- height
- steps
- cfg
- sampler_name
- scheduler
- denoise

`swap` と記述した場合は `width` と `height` を入れ替えます。


### PromptEdit

#### add

```
<edit:add:prompt=string[:to={ positive | negative }][:position={ head | tail }]>
```

プロンプトを追加します。

- `prompt`: 追加するプロンプトを記載します。 `:`, `<`, `>`, `=` を使用する場合は `\:` のようにエスケープしてください。`\` 自体を使用する場合は `\\` です。
- `to`: `positive` の場合は `positive_prompt` に `negative` の場合は `negative_prompt` に追加します。 デフォルトは `negative` です。
- `position`: `head` の場合は先頭に `tail` の場合は末尾に追加します。 デフォルトは `tail` です。

#### replace

```
<edit:replace:pattern=string:replace=string>
```

プロンプトを置換します。置換対象はこの記法が書かれたプロンプトです。例えばネガティブプロンプトに書かれていたらネガティブプロンプトが置換対象になります。

- `pattern`: 置換範囲にマッチする正規表現です。上記と同様にエスケープしてください。
- `replace`: 置換対象を置き換える文字列です。後方参照 `\1` などが使用可能ですがエスケープが必要です。 （例えば `\\1` など）


## ライセンス

[MIT](./LICENSE)
