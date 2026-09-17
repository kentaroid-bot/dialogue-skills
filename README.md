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

### 公式ディレクトリから使う

[ChatGPTのプラグイン一覧でDialogue Skillsを開く](https://chatgpt.com/plugins/plugins_6aaa1a44c0b481919f378cff2ce211fe)

対話から論考を作るEssay、指示を整えるPrompt、成果物をレビューするChecker、掲載を進めるPublisherを収録しています。必要なスキルだけ、単独で使えます。

### GitHubからCodexに導入する

このリポジトリ全体が、4つのスキルを収録した `dialogue-skills` プラグインです。

```text
dialogue-skills/
├── plugin.json                 # Agent Plugins形式の識別情報
├── .codex-plugin/plugin.json   # OpenAI向け表示情報と互換用マニフェスト
└── skills/
    ├── dialogue-essay/
    ├── dialogue-prompt/
    ├── dialogue-checker/
    └── dialogue-publisher/
```

GitHubから4スキルをまとめて導入できます。

```sh
codex plugin marketplace add kentaroid-bot/dialogue-skills --ref main
codex plugin add dialogue-skills@dialogue-skills
```

この方法で導入した場合、デスクトップのPluginsでは「Dialogue Skills · GitHub」が導入元です。新しいタスクで使い、表示が更新されない場合はアプリを再読み込みしてください。

更新時はカタログを更新し、プラグインを再取得して、インストール済みの版を確認します。

```sh
codex plugin marketplace upgrade dialogue-skills
codex plugin add dialogue-skills@dialogue-skills
codex plugin list --marketplace dialogue-skills --json
```

[導入・更新・配布の手順](docs/distribution.md)に、旧ローカル版からの移行、配布ZIPの作成、Web側への取り込み方法をまとめています。Web側で別に導入したコピーは、ローカルの更新だけでは更新されません。

このプラグインはスキルと参照資料を収録します。MCPサーバーや外部アプリの接続設定は含みません。Publisherが掲載に使う接続は、利用環境にあるツールを使います。

### スキルを個別に配置する

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

同梱するEssayは、独立リポジトリのcommit `98109281b6d6edc5be32d8e08961d3bc5117cc99` の `skills/dialogue-essay/` を、付属資料・呼び出し設定ごと無改変で収録しています。ライセンスは [LICENSE-dialogue-essay](LICENSE-dialogue-essay) を参照してください。

CheckerとPublisherは、新しいPromptで「思考・適応」と「状態・記録・検証」を分けて再設計しました。人間の制作動機とエージェントの目的を別に伝え、実行条件は手続きとして明確にしています。[今回の設計とレビュー記録](docs/revisions/two-layer-redesign.md)に対応関係をまとめています。

## 検証の範囲

形式、ローカル参照、設定テンプレート、指示と目的の整合性を確認しています。付属の事例は検証材料であり、独立したモデル比較や性能向上を実証した結果ではありません。

比較用の旧版は原文のまま保存しています。旧版内の相対リンクは保存前の配置を前提とします。実行には各フォルダ直下のSKILL.mdを使用してください。

[読者へ案内する資料の範囲の改訂記録](docs/revisions/reader-reference-scope.md)には、EssayとCheckerの変更理由、原稿作成1件とレビュー5件の実行結果をまとめています。リンク・添付を含む成果物の適切さを確認し、問題のある参照先の指摘と、適切な原稿の完了判断を両方確かめました。

[会話の参加者への配慮を加えた改訂記録](docs/revisions/participant-reference-scope.md)では、読者への有用性と、無関係な発言まで紹介されることの参加者にとっての適切さを分けています。追加版6実行と現行版2実行を比較し、適切な抜粋・全文リンクを維持できることも確認しました。
