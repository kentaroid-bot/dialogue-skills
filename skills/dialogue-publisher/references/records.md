# 利用者設定と作業記録

配布パッケージはこの白紙テンプレートのみを持つ。以下を、本人と決めた非公開の作業フォルダへコピーして使用する。nullと空配列は未設定であり、falseや「通知しない」と同義ではない。アカウントは公開プロフィールURL等で識別し、認証情報は保存しない。

## preferences.json

```json
{
  "schemaVersion": 1,
  "timezone": null,
  "destinations": [],
  "attribution": null,
  "confirmedAt": null,
  "confirmationSource": null
}
```

本人が確認した掲載先ごとに以下の形をdestinationsへ追加する。対象サービスに存在しない項目は省略してよい。

```json
{
  "destinationKey": null,
  "platform": null,
  "publicationUrl": null,
  "account": null,
  "languages": [],
  "delivery": null,
  "audience": null,
  "emailNotification": null,
  "appNotification": null,
  "promotionDestinations": [],
  "confirmedAt": null,
  "confirmationSource": null
}
```

deliveryはdraft / publish / schedule等を本人の希望に応じて記録する。記事更新という操作と配信形態は区別する。新しい指定で変更するときは確認根拠も更新する。設定は現在の希望を保存するものであり、投稿を自動実行するジョブではない。

## 記事台帳とイベント

記事ごとの台帳はMarkdown等でよい。articleKey、原稿の参照先・言語、採用した帰属表記、媒体ごとのURL・記事ID・状態を記録する。

操作ログは一依頼をrequestKey、各媒体の操作をeventKeyで区別し、次を記録する。

- schemaVersion、requestKey、eventKey、articleKey
- platform、account、action、今回認められた公開・通知範囲と根拠
- status：not_started / draft_saved / scheduled / verification_pending / published_verified / needs_action / interrupted
- requestedTime、performedTime、verifiedTime、recordedAt
- resultUrl、externalId、verification、issue、resolution、remainingWork

日時はvalueまたはstart/end、precision（exact / minute / date / range / unknown）、timezone、basisを持つ形で保存する。記録日時で過去の依頼時刻を埋めない。予約は予定時刻を別に記録する。

識別子は一度決めたら保持する。同一イベントの再取込に使えるようにし、訂正は訂正元を辿れる形にする。将来のConvex等への移行では、原記録を保持し、件数・URL・日時精度を照合する。保存先サービスの接続やデータ送信は別途依頼されたときに行う。
