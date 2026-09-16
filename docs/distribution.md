# 導入・更新・配布

## GitHubから導入する

配布の正本は `kentaroid-bot/dialogue-skills` の `main`。プラグインの名前は `dialogue-skills`、GitHub由来のマーケットプレイス名も `dialogue-skills` である。

```sh
codex plugin marketplace add kentaroid-bot/dialogue-skills --ref main
codex plugin add dialogue-skills@dialogue-skills
```

登録後は、デスクトップのPluginsで「Dialogue Skills · GitHub」を選んで導入する方法もある。新しいタスクで利用し、表示が更新されない場合はアプリを再読み込みする。

カタログのプラグイン参照先もGitHubにしているため、ローカルの作業フォルダにある未追跡ファイルや個人設定を配布元として読み込まない。

## インストール済みの版を更新する

```sh
codex plugin marketplace upgrade dialogue-skills
codex plugin add dialogue-skills@dialogue-skills
codex plugin list --marketplace dialogue-skills --json
```

マーケットプレイスの更新とインストールされたプラグインの確認を一組にする。`version` が配布版と一致し、`installed` と `enabled` がともに `true` であることを確認する。新しいタスクから更新版を使う。

以前の `dialogue-skills@personal` や単独配置の `dialogue-*` がある場合は、独自変更を比較し、バックアップした上で通常の読み込み対象から外す。GitHub版での確認が済む前に旧版を取り除かない。作業用の原本は、インストール済みコピーとは別に保管する。

## 改善して配布する

1. スキルを改訂し、変更に必要なテストとレビューを行う。
2. Essayを変えた場合は独立リポジトリにも反映し、READMEの同梱元コミットを更新する。フォルダ全体が一致することを確認する。
3. ルートと `.codex-plugin/` の両マニフェストの版番号を揃え、変更記録を残す。開発中の更新には `plugin-creator` のバージョン更新用ヘルパーを使える。
4. `python3 scripts/release.py` と各スキル・プラグインの形式検証を実行する。
5. 対象ファイルを明示してコミットし、GitHubへ反映する。個人設定、会話ログ、検証中の未追跡ファイルは含めない。
6. `python3 scripts/release.py --build` でコミット済みHEADから配布ファイルを作る。
7. 利用環境で更新を取り込み、配布版の内容とインストールされた内容を照合する。

配布ファイルは `.local/releases/<version>/` に作られる。4スキルをまとめたプラグインZIP、各スキルのZIP、コミット・版番号・本文とアーカイブのSHA-256を記した `release.json` が含まれる。作業中のファイルは取り込まず、Gitにコミットされたファイルだけを使う。

## Web側で利用する

ローカルのマーケットプレイス登録だけでは、Web側のスキルやプラグインを更新したことにはならない。

ワークスペース管理者として「管理 → プラグイン → マーケットプレイスをインポート」を利用できる場合は、このリポジトリのURLと `main` を指定する。カタログはルートに配置しているため、パス欄は空欄にする。同期結果と実際に使う版を確認する。

個人アカウントでこの取り込み機能がない場合は、利用できるアップロード画面に合わせてプラグインZIPまたは各スキルZIPを取り込む。既存のスキルを更新できる画面なら、重複した新規登録より更新を優先する。Web側の機能が受け付ける形式を確かめ、導入できたものだけを完了として記録する。

Web側の取込版も `release.json` と対応させる。GitHub更新だけで、別途取り込んだWeb版が自動更新されるとは扱わない。

公式資料：[パッケージとマーケットプレイス](https://developers.openai.com/plugins/build/plugins)、[ワークスペースでのGitHub同期](https://learn.chatgpt.com/docs/enterprise/plugin-management)。
