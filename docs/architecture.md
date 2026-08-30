# Architecture

## Overview

アプリケーションは、ビルド時のデータ変換とブラウザ実行時の表示を分離する。

```text
source CSV
    |
    | scripts/build_data.py
    v
public JSON ----fetch----> browser state ----> DOM
                                      |
                                      +----> random selection
```

静的ホスティングは生成済みファイルを配信するだけで、検索、抽選、状態保持には関与しない。

## Proposed repository layout

```text
index.html
assets/
  main.js
  style.css
data/
  rubaiyat.json
misc/
  rubaiyat.csv
scripts/
  build_data.py
tests/
  test_build_data.py
docs/
```

## Responsibilities

### Source CSV

- 作品データの唯一の編集元とする。
- 人が差分を確認しやすい形式を保つ。
- 生成済みJSONを直接編集しない。

### Data builder

- Python標準ライブラリだけを使用する。
- CSVを検証し、ブラウザ向けの型へ変換する。
- 同じ入力から常に同じJSONを生成する。
- 表示ロジックやデプロイ処理を持たない。

Pythonは開発時の変換手段に限り、本番環境の依存ではない。

### Browser application

- JSONを一度読み込み、メモリ上に保持する。
- 候補集合から作品を選択する。
- DOM APIと `textContent` を使って安全に表示する。
- データの永続化や通信APIを持たない。

### Stylesheet

- レイアウト、タイポグラフィ、レスポンシブ表示、フォーカス表示だけを担当する。

### Static hosting

- リポジトリ内の公開ファイルをHTTPSで配信する。
- 初期案はGitHub Pagesのbranch deploymentとする。

## Data contract

初期JSONでは、移行元の情報を失わないため、次のフィールドを保持する。

```json
{
  "id": 1,
  "is_with_parentheses": false,
  "section": "解き得ぬ謎",
  "poem_body": "...",
  "poem_body_with_ruby": "...",
  "is_boozeism": false,
  "footnote": null
}
```

UIが初期リリースで使わないフィールドもあるが、データ移行時の情報欠落を避けるため保持する。新機能を先に実装する意図ではない。

## Runtime states

ブラウザ側の状態は次の4つに限定する。

- loading
- ready
- showing a poem
- error

状態管理ライブラリは使用しない。

## Trade-offs

### Full data download

データ全量はJSONで約90 KB、圧縮転送では約18 KBと小さい。ページ分割やAPI呼び出しを導入するより、初回に全件取得する方が単純で、選択時の待ち時間もない。

### Committed generated JSON

初期案では生成済みJSONをコミットする。branch deploymentで追加ビルドが不要になる一方、CSVとの同期確認が必要になる。この同期は変換スクリプトのcheckモードまたはテストで保証する。

### No offline support

通常のHTTPキャッシュは利用できるが、オフライン利用は保証しない。Service Workerの更新戦略と障害モードを持ち込まないためである。

## Security and privacy

- 作品本文に `innerHTML` を使用しない。
- 外部入力、Cookie、ユーザー追跡を持たない。
- 外部スクリプトとCDN依存を避ける。
- ランダム選択は娯楽用途であり、暗号学的乱数を必要としない。

