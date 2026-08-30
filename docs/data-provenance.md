# Data Provenance

## Work

- 原題: `RUBA'IYAT`
- 邦題: 『ルバイヤート』
- 著者: オマル・ハイヤーム（1048–1131）
- 訳者: 小川亮作（1910–1951）

## Digital source

データは、青空文庫で公開されている小川亮作訳『ルバイヤート』をもとにしたデスクトップ版 [emguse/rubaiyat](https://github.com/emguse/rubaiyat) のCSVから移行する予定である。

- 青空文庫作品ページ: <https://www.aozora.gr.jp/cards/000288/card1760.html>
- 移行元リポジトリ: <https://github.com/emguse/rubaiyat>
- 入力: 土屋隆
- 校正: 高柳典子

## Migration record

作品データをこのリポジトリへ追加するとき、次をこの文書へ追記する。

- 取得日
- 移行元の完全なGitコミットID
- 移行したファイルのパス
- 原本ファイルのSHA-256
- 件数と分類件数
- 変換時に加えた正規化

現段階ではデータを取り込んでいないため、これらは未記入である。

## Transformation policy

- 本文、読み、章、脚注、改行を意図的に改変しない。
- CSVの `0` / `1` はJSONのbooleanへ変換する。
- 空の脚注はJSONの `null` へ変換する。
- 誤字修正や内容修正はデータ変換と別の変更として、根拠を記録する。

## Rights and notices

文学作品、翻訳、デジタル化データ、Webアプリケーションコードは、それぞれ権利関係が異なり得る。本リポジトリのコードライセンスだけで作品データの条件を説明したものとは扱わない。

公開前に、青空文庫の記載、移行元のREADMEとLICENSE、および新しいリポジトリのライセンス表記を確認する。

