# Random Rubaiyat

小川亮作訳『ルバイヤート』から一首をランダムに表示する、静的なWebサイトです。

このリポジトリは、Python、pywebview、SQLite、SQLModelで作られたデスクトップ版とは別のプロジェクトです。Web版はブラウザだけで動作し、静的ホスティングへ配置できることを目標とします。

## Status

内容とアクセシビリティのレビューまで完成しています。次は静的ホスティングへの公開段階です。

## Principles

- YAGNI: 現在必要な機能だけを実装する
- KISS: HTML、CSS、JavaScript、JSONで完結させる
- SRP: 原本、変換、表示、配信の責務を分離する
- Content fidelity: 本文、読み、脚注、改行を原本どおり保持する

## Initial scope

- 全作品から一首をランダムに表示する
- 酒に関係する作品から一首をランダムに表示する
- 作品番号、章、本文、脚注を表示する
- スマートフォンとデスクトップのブラウザで利用できる
- GitHub Pagesなどの静的ホスティングで配信できる

検索、タグ、お気に入り、履歴、ユーザーアカウント、PWAは初期スコープに含めません。

## Documentation

- [Requirements](docs/requirements.md)
- [Architecture](docs/architecture.md)
- [Implementation plan](docs/implementation-plan.md)
- [Data provenance](docs/data-provenance.md)
- [ADR 0001: Static browser application](docs/decisions/0001-static-browser-application.md)

## Data development

ブラウザ用JSONを再生成します。

```shell
python3 scripts/build_data.py
```

CSVと生成済みJSONが同期していることを確認します。

```shell
python3 scripts/build_data.py --check
python3 -m unittest discover -s tests
```

## Local preview

リポジトリルートで静的HTTPサーバーを起動します。

```shell
python3 -m http.server 8000
```

<http://localhost:8000> をブラウザで開きます。`file://` から直接開く方法は、JSON取得に対するブラウザ制約が異なるためサポートしません。

## Related project

デスクトップ版は [emguse/rubaiyat](https://github.com/emguse/rubaiyat) で継続します。このリポジトリへデスクトップ版の履歴や実行環境は持ち込みません。

## License

新しいWebアプリケーションコードのライセンスは未決定です。作品データの出典と権利関係は [Data provenance](docs/data-provenance.md) に分けて記録します。
