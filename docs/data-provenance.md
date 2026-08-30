# Data Provenance

## Work

- 原題: ``RUBA`IYAT``
- 邦題: 『ルバイヤート』
- 著者: オマル・ハイヤーム（1048–1131）
- 訳者: 小川亮作（1910–1951）

## Digital source

データは、青空文庫で公開されている小川亮作訳『ルバイヤート』をもとにしたデスクトップ版 [emguse/rubaiyat](https://github.com/emguse/rubaiyat) のCSVから移行した。

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

文学作品、翻訳、デジタル化データ、Webアプリケーションコードは、それぞれ権利関係が異なる。

本リポジトリ独自のソフトウェアとドキュメントにはMIT Licenseを適用する。詩文、翻訳、CSV、生成JSON、およびそれらから表示される作品本文にはMIT Licenseを適用しない。また、本リポジトリはこれらの作品データをCC0として提供するものではない。適用範囲と利用上の注意は [`DATA-NOTICE.md`](../DATA-NOTICE.md) に記載する。

青空文庫の図書カードは、小川亮作の没年を1951年としている。文化庁は、2018年の保護期間延長より前に保護が切れていた著作物の保護は復活しないと説明している。これらに基づき、本リポジトリでは小川亮作訳を日本国内でパブリックドメインとして扱う。これは一次資料に基づく本プロジェクトの判断であり、法的保証ではない。国外では保護状況が異なる可能性がある。

青空文庫の取り扱い規準は、著作権の切れた作品ファイルについて複製、再配布、共有、形式変換を認め、作品名、著者・訳者、底本、入力・校正者、作業履歴等を残すよう希望している。本リポジトリは、この文書と `DATA-NOTICE.md` にそれらの情報を保持する。

- 青空文庫収録ファイルの取り扱い規準: <https://www.aozora.gr.jp/guide/kijyunn.html>
- 文化庁「著作物等の保護期間の延長に関するQ&A」: <https://www.bunka.go.jp/seisaku/chosakuken/hokaisei/kantaiheiyo_chosakuken/1411890.html>
