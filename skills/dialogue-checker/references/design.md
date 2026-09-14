# 設計の由来

人間の問題提起：別セッションでレビューするたびに修正提案が増え、元の意図や作品の特徴が失われることへの懸念。修正点を作ることより、今回の目的を満たしたかの判断を求めた。

CodexはUnflatten ProtocolのAdaptive Inquiryを読み、次の考え方をレビュー用途へ具体化した。

- 問いと動機の由来を辿り、記録と推測を区別する。
- 判断を変え得る次の一手を選び、発見なしの完了を認める。
- 評価軸の変更を明示し、過去の結果を上書きしない。
- 差異を平均化せず、推奨と実行権限を分ける。

参照版：Adaptive 0.3.2、commit `2fbe1cc62457c939fe04ca57f306217000edd365`。

- [Protocol](https://github.com/kentaroid-bot/unflatten-protocol/blob/2fbe1cc62457c939fe04ca57f306217000edd365/protocols/adaptive/protocol.md)
- [Decision](https://github.com/kentaroid-bot/unflatten-protocol/blob/2fbe1cc62457c939fe04ca57f306217000edd365/protocols/adaptive/modes/decision.md)
- [Evaluation](https://github.com/kentaroid-bot/unflatten-protocol/blob/2fbe1cc62457c939fe04ca57f306217000edd365/protocols/adaptive/evaluation.md)

本スキルは上記の考え方を参考にCodexが新規執筆した独立したレビュー手順。SDK、役割サイクル、記録スキーマの導入や、元リポジトリの変更は行っていない。原文の指示を全文転用していない。

必要修正・確認不足・任意拡張の区分、MVPの完了判定、再レビューの範囲は、今回の目的に合わせたCodexの設計判断。形式検証は実行精度を保証しない。事例による独立したモデル評価は未実施。
