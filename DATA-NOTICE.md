# Data Notice

## Scope

The MIT License in [`LICENSE`](LICENSE) applies to the original software and documentation in this repository. It does not apply to the literary work, its Japanese translation, or the poem data contained in the following files:

- `misc/rubaiyat.csv`
- `data/rubaiyat.json`
- poem text rendered from those files

These materials are not offered under the MIT License or dedicated under CC0 by this repository.

## Work and attribution

- Title: 『ルバイヤート』
- Original title: ``RUBA`IYAT``
- Author: オマル・ハイヤーム（1048–1131）
- Translator: 小川亮作（1910–1951）
- Source edition: 岩波文庫、岩波書店
- First edition: 1949（昭和24）年1月15日
- Edition used for input: 1997（平成9）年7月7日、第52刷
- Revision noted by Aozora Bunko: 1979（昭和54）年9月17日、第23刷改版
- Digital input: 土屋隆
- Proofreading: 高柳典子
- Aozora Bunko work page: <https://www.aozora.gr.jp/cards/000288/card1760.html>

The data in this repository was migrated from the CSV in [emguse/rubaiyat](https://github.com/emguse/rubaiyat), which was prepared from the Aozora Bunko text. Complete migration provenance is recorded in [`docs/data-provenance.md`](docs/data-provenance.md).

## Copyright status and use

The translator died in 1951. Based on the Japanese Agency for Cultural Affairs' explanation that copyright terms which had already expired before the 2018 term extension were not revived, this repository treats the translation as being in the public domain in Japan.

Aozora Bunko's handling rules state that files of works whose copyright has expired may be freely copied, redistributed, shared, and converted to other formats. They also ask that information about the work, author, translator, source edition, digital input, proofreading, and file history be retained when the files are reused.

- Aozora Bunko handling rules: <https://www.aozora.gr.jp/guide/kijyunn.html>
- Agency for Cultural Affairs Q&A: <https://www.bunka.go.jp/seisaku/chosakuken/hokaisei/kantaiheiyo_chosakuken/1411890.html>

Copyright status and permitted use may differ outside Japan. Users are responsible for confirming the law that applies in their jurisdiction. This notice provides provenance and project policy; it is not legal advice or a warranty of legal status.

Use of the name “Aozora Bunko” indicates the source of the digitized text. It does not imply involvement, endorsement, or approval by Aozora Bunko.

## Transformations in this repository

The source CSV is retained byte-for-byte from the recorded upstream commit. The browser JSON is generated deterministically with only the following structural transformations:

- integer IDs are represented as JSON numbers;
- CSV `0` and `1` values are represented as JSON booleans;
- empty footnotes are represented as JSON `null`;
- records are ordered by poem ID;
- JSON is encoded as UTF-8.

The poem text, readings, sections, footnotes, and line breaks are not intentionally altered by this conversion.
