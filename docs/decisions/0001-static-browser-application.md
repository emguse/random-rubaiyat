# ADR 0001: Use a static browser application

- Status: Accepted
- Date: 2026-08-30

## Context

移行元はpywebview、SQLite、SQLModelを利用するローカルデスクトップアプリケーションである。公開したい機能は、143件の固定データから条件に応じて一首を選び、表示することに限られる。

データ全量はブラウザへ一度に配信できる大きさであり、ユーザー入力の保存、認証、同時編集、サーバー側検索を必要としない。

## Decision

Web版をHTML、CSS、JavaScript、JSONからなる静的ブラウザアプリケーションとして構築する。

- 作品データは初回に全量取得する。
- 抽選と表示はブラウザ内で行う。
- データベース、APIサーバー、JavaScriptフレームワークを使用しない。
- データ変換用のPythonは開発時だけ使用できる。
- デスクトップ版は別リポジトリに残し、Web版へ履歴を移植しない。

## Consequences

### Positive

- 静的ホスティングだけで公開できる。
- サーバー運用、データベース移行、実行時シークレットが不要になる。
- 配信後の作品選択がネットワーク遅延を受けない。
- 構成要素と障害点が少ない。

### Negative

- 配信したデータは利用者が全件取得できる。
- サーバーを介した利用状況の保存や同期はできない。
- データ更新時は静的ファイルを再生成し、再配信する必要がある。

これらは公開作品の小規模な閲覧サイトでは許容できる。

## Rejected alternatives

### Keep SQLite behind an API

固定された143件の読み取りに、サーバーとデータベースの運用責任を持ち込むため採用しない。

### Run SQLite in WebAssembly

現在必要な抽選と絞り込みは配列操作で十分であり、依存、転送量、初期化処理が増えるため採用しない。

### Adopt a JavaScript framework

画面と状態が小さく、DOM APIで明瞭に実装できるため採用しない。

### Add offline support initially

Service Workerのキャッシュ更新戦略とテスト範囲が必要になる。公開URLからの利用を先に成立させ、要求が確認されるまで延期する。
