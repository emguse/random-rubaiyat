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

- 取得日: 2026-08-30
- 移行元コミット: `a9091467fef84b1f8fe43e70b93486f51571f67b`
- 移行元ファイル: `misc/rubaiyat.csv`
- 保存先ファイル: `misc/rubaiyat.csv`
- 原本のSHA-256: `ca2773d0048f25f9eaca77a08338596556df1fdbcac69b06556f01d1e7a9b526`
- 全作品: 143件
- 酒に関係する作品: 71件
- 章: 8種類
- 脚注付き作品: 32件

## Transformation policy

- 本文、読み、章、脚注、改行を意図的に改変しない。
- CSVの `0` / `1` はJSONのbooleanへ変換する。
- 空の脚注はJSONの `null` へ変換する。
- JSONの配列は作品ID順に整列する。
- JSONはUTF-8、末尾改行あり、不要な空白なしで決定的に生成する。
- 誤字修正や内容修正はデータ変換と別の変更として、根拠を記録する。

## Rights and notices

文学作品、翻訳、デジタル化データ、Webアプリケーションコードは、それぞれ権利関係が異なり得る。本リポジトリのコードライセンスだけで作品データの条件を説明したものとは扱わない。

公開前に、青空文庫の記載、移行元のREADMEとLICENSE、および新しいリポジトリのライセンス表記を確認する。
