# Implementation Plan

## Phase 0: Documentation baseline

Status: Complete

### Deliverables

- プロジェクトの目的とスコープ
- 機能要件と受け入れ条件
- 静的アーキテクチャの決定
- データの出典と移行ルール

### Exit criteria

- 未決事項と対象外機能が文書から判別できる。
- アプリケーションコードを追加せずに構成をレビューできる。

## Phase 1: Data pipeline

Status: Complete

### Work

1. デスクトップ版からCSVを明示的に取り込む。
2. データの出典と取得時点のコミットを記録する。
3. 標準ライブラリだけの変換スクリプトを作る。
4. 型、件数、ID、必須値を検証する。
5. 決定的なJSONを生成する。
6. 変換結果を自動テストする。

### Exit criteria

- 既知の143件を欠落なくJSONへ変換できる。
- 不正な入力で変換が失敗する。
- JSONを手編集せず再生成できる。

## Phase 2: Minimum browser application

Status: Next

### Work

1. セマンティックな `index.html` を作る。
2. JSONの読み込み状態とエラー状態を実装する。
3. 全作品からのランダム選択を実装する。
4. 酒に関係する作品からのランダム選択を実装する。
5. 本文、章、番号、脚注をDOMへ描画する。
6. モバイル優先の最小スタイルを作る。

### Exit criteria

- 要件FR-1からFR-4をローカルHTTPサーバーで確認できる。
- 表示中にコンソールエラーがない。
- データ取得後の選択に追加通信がない。

## Phase 3: Content and accessibility review

### Work

1. 全件について変換前後の文字列一致を機械的に検証する。
2. 長い本文、脚注、括弧付き作品を目視確認する。
3. キーボード操作、フォーカス、読み上げ用状態通知を確認する。
4. 小さい画面と広い画面でレイアウトを確認する。
5. 出典表示を実装する。

### Exit criteria

- 機能要件と非機能要件の受け入れ条件を満たす。
- 作品データの欠落または意図しないHTML解釈がない。

## Phase 4: Static deployment

### Work

1. 新しいGitHubリポジトリへremoteを設定する。
2. GitHub Pagesを `main` branchのrootから配信する。
3. 公開URLで相対パス、HTTPS、モバイル表示を確認する。
4. READMEへ公開URLとローカル確認方法を追記する。

### Exit criteria

- 公開URLから2種類のランダム表示を利用できる。
- 本番環境にPython、SQLite、シークレットがない。

## Deferred backlog

利用者から具体的な必要性が確認できた場合だけ検討する。

- 直前に表示した作品との重複回避
- 読み付き本文の表示切り替え
- URLによる特定作品へのリンク
- お気に入り
- オフライン対応
- 独自ドメイン

## Change strategy

- 各Phaseを独立した小さな変更としてレビューする。
- 機能追加とデザイン刷新を同じ変更に混ぜない。
- 新しい依存を追加する場合は、標準機能では解決できない理由を記録する。
