from __future__ import annotations

import csv
import json
import tempfile
import unittest
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from scripts.build_data import (
    DEFAULT_OUTPUT,
    DEFAULT_SOURCE,
    DataValidationError,
    encode_poems,
    load_poems,
)


class BuildDataTest(unittest.TestCase):
    def test_bundled_source_satisfies_the_data_contract(self) -> None:
        poems = load_poems(DEFAULT_SOURCE)

        self.assertEqual(len(poems), 143)
        self.assertEqual(sum(poem["is_boozeism"] for poem in poems), 71)
        self.assertEqual(len({poem["section"] for poem in poems}), 8)
        self.assertEqual(sum(poem["footnote"] is not None for poem in poems), 32)
        self.assertEqual([poem["id"] for poem in poems], list(range(1, 144)))

    def test_generated_json_is_current_and_valid(self) -> None:
        poems = load_poems(DEFAULT_SOURCE)

        self.assertEqual(DEFAULT_OUTPUT.read_bytes(), encode_poems(poems))
        self.assertEqual(json.loads(DEFAULT_OUTPUT.read_text(encoding="utf-8")), poems)

    def test_invalid_boolean_is_rejected(self) -> None:
        rows, fieldnames = self.read_source_rows()
        rows[0]["is_boozeism"] = "yes"

        with self.temporary_csv(rows, fieldnames) as source:
            with self.assertRaisesRegex(DataValidationError, "must be 0 or 1"):
                load_poems(source)

    def test_duplicate_id_is_rejected(self) -> None:
        rows, fieldnames = self.read_source_rows()
        rows[1]["id"] = rows[0]["id"]

        with self.temporary_csv(rows, fieldnames) as source:
            with self.assertRaisesRegex(DataValidationError, "ids must be unique"):
                load_poems(source)

    @staticmethod
    def read_source_rows() -> tuple[list[dict[str, str]], list[str]]:
        with DEFAULT_SOURCE.open(encoding="utf-8", newline="") as source_file:
            reader = csv.DictReader(source_file)
            return list(reader), list(reader.fieldnames or ())

    @contextmanager
    def temporary_csv(
        self, rows: list[dict[str, str]], fieldnames: list[str]
    ) -> Iterator[Path]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rubaiyat.csv"
            with path.open("w", encoding="utf-8", newline="") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            yield path


if __name__ == "__main__":
    unittest.main()
