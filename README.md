# Dialogue Skills

人間の意図を対話から育て、文章・指示・レビュー・公開へつなぐ4つの独立したスキルです。

| スキル | 役割 |
|---|---|
| [dialogue-essay](skills/dialogue-essay/SKILL.md) | 人間の見解を残し、AIの検討と総括を分けた文章を作る |
| [dialogue-prompt](skills/dialogue-prompt/SKILL.md) | 対話の意図から、Why / IntentとHow / Schemaを分けたプロンプトを作る |
| [dialogue-checker](skills/dialogue-checker/SKILL.md) | 制作意図と完成条件に照らして評価し、修正不要なら完了する |
| [dialogue-publisher](skills/dialogue-publisher/SKILL.md) | 希望の掲載先・形態を確認し、掲載・更新・告知・記録を扱う |

各スキルは単独で使えます。すべてを順番に実行する必要はありません。現在の本文と事例は日本語です。

## 利用方法

必要なスキルのフォルダを、使用するエージェントのスキル保存先へ配置してください。Codexでは通常 `~/.codex/skills/` を使用します。同名のスキルがある場合は、既存版を保存して差分を確認してから置き換えます。付属のreferencesとagentsも一緒に配置してください。

呼び出し例：

```text
$dialogue-essay この対話を、人間の考えとAIの検討を分けた論考にしてください。
$dialogue-prompt この対話から、意図を保った実行用プロンプトを作ってください。
$dialogue-checker このMVPを、今回の目的と完成条件に照らして確認してください。
$dialogue-publisher この原稿を掲載したいです。掲載先と公開形態を確認してください。
```

Publisherの配布時設定は白紙です。アカウント、掲載先、言語、公開・下書き・予約、通知方法を利用者に確認し、設定と作業記録はスキル外の非公開領域へ保存します。このリポジトリには個人設定・認証情報・投稿ログを含めません。実際に操作できる媒体は利用環境のツールと権限に依存します。

## 制作と改訂の関係

Dialogue Essayの、意図とAIの検討を分ける方法からDialogue Promptが生まれました。Dialogue Promptは自身の改訂に使用し、その改訂版でCheckerを改訂し、Publisherを設計しました。制作に使ったスキルを、利用時の依存関係にはしていません。

Checkerは[Unflatten ProtocolのAdaptive Inquiry](https://github.com/kentaroid-bot/unflatten-protocol/tree/codex/adaptive-inquiry)を参考にしています。参照版と取り入れた考え方は付属資料に記録しています。

[既存のDialogue Essayリポジトリ](https://github.com/kentaroid-bot/dialogue-essay)は独立して残しています。このリポジトリは4つの現行版をまとめた配布先です。個々の手元のインストール先と自動同期する仕組みはありません。

同梱するEssayは、独立リポジトリのcommit `57673cac97872caa9991167ab2288e926723a7ea` の `skills/dialogue-essay/` を、付属資料・呼び出し設定ごと無改変で収録しています。ライセンスは [LICENSE-dialogue-essay](LICENSE-dialogue-essay) を参照してください。

CheckerとPublisherは、新しいPromptで「思考・適応」と「状態・記録・検証」を分けて再設計しました。人間の制作動機とエージェントの目的を別に伝え、実行条件は手続きとして明確にしています。[今回の設計とレビュー記録](docs/revisions/two-layer-redesign.md)に対応関係をまとめています。

## 検証の範囲

形式、ローカル参照、設定テンプレート、指示と目的の整合性を確認しています。付属の事例は検証材料であり、独立したモデル比較や性能向上を実証した結果ではありません。

比較用の旧版は原文のまま保存しています。旧版内の相対リンクは保存前の配置を前提とします。実行には各フォルダ直下のSKILL.mdを使用してください。
