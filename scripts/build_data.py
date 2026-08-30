from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = PROJECT_ROOT / "misc" / "rubaiyat.csv"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "rubaiyat.json"

FIELDS = (
    "id",
    "is_with_parentheses",
    "section",
    "poem_body",
    "poem_body_with_ruby",
    "is_boozeism",
    "footnote",
)

EXPECTED_POEMS = 143
EXPECTED_BOOZEISM_POEMS = 71
EXPECTED_SECTIONS = 8
EXPECTED_FOOTNOTES = 32


class DataValidationError(ValueError):
    """Raised when the source data does not satisfy the public data contract."""


def parse_boolean(value: str, *, row_number: int, field: str) -> bool:
    if value not in {"0", "1"}:
        raise DataValidationError(
            f"row {row_number}: {field} must be 0 or 1, got {value!r}"
        )
    return value == "1"


def load_poems(source: Path) -> list[dict[str, Any]]:
    with source.open(encoding="utf-8", newline="") as source_file:
        reader = csv.DictReader(source_file)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise DataValidationError(
                f"unexpected CSV columns: expected {FIELDS!r}, got {reader.fieldnames!r}"
            )

        poems: list[dict[str, Any]] = []
        for row_number, row in enumerate(reader, start=2):
            if None in row:
                raise DataValidationError(f"row {row_number}: unexpected extra columns")

            try:
                poem_id = int(row["id"])
            except ValueError as error:
                raise DataValidationError(
                    f"row {row_number}: id must be an integer, got {row['id']!r}"
                ) from error

            section = row["section"]
            poem_body = row["poem_body"]
            poem_body_with_ruby = row["poem_body_with_ruby"]
            if not section or not poem_body or not poem_body_with_ruby:
                raise DataValidationError(
                    f"row {row_number}: section and poem bodies must not be empty"
                )

            poems.append(
                {
                    "id": poem_id,
                    "is_with_parentheses": parse_boolean(
                        row["is_with_parentheses"],
                        row_number=row_number,
                        field="is_with_parentheses",
                    ),
                    "section": section,
                    "poem_body": poem_body,
                    "poem_body_with_ruby": poem_body_with_ruby,
                    "is_boozeism": parse_boolean(
                        row["is_boozeism"],
                        row_number=row_number,
                        field="is_boozeism",
                    ),
                    "footnote": row["footnote"] or None,
                }
            )

    validate_collection(poems)
    return sorted(poems, key=lambda poem: poem["id"])


def validate_collection(poems: list[dict[str, Any]]) -> None:
    if len(poems) != EXPECTED_POEMS:
        raise DataValidationError(
            f"expected {EXPECTED_POEMS} poems, got {len(poems)}"
        )

    poem_ids = [poem["id"] for poem in poems]
    if len(set(poem_ids)) != len(poem_ids):
        raise DataValidationError("poem ids must be unique")
    if set(poem_ids) != set(range(1, EXPECTED_POEMS + 1)):
        raise DataValidationError(f"poem ids must cover 1 through {EXPECTED_POEMS}")

    boozeism_count = sum(poem["is_boozeism"] for poem in poems)
    if boozeism_count != EXPECTED_BOOZEISM_POEMS:
        raise DataValidationError(
            f"expected {EXPECTED_BOOZEISM_POEMS} booze-ism poems, got {boozeism_count}"
        )

    section_count = len({poem["section"] for poem in poems})
    if section_count != EXPECTED_SECTIONS:
        raise DataValidationError(
            f"expected {EXPECTED_SECTIONS} sections, got {section_count}"
        )

    footnote_count = sum(poem["footnote"] is not None for poem in poems)
    if footnote_count != EXPECTED_FOOTNOTES:
        raise DataValidationError(
            f"expected {EXPECTED_FOOTNOTES} footnotes, got {footnote_count}"
        )


def encode_poems(poems: list[dict[str, Any]]) -> bytes:
    document = json.dumps(poems, ensure_ascii=False, separators=(",", ":")) + "\n"
    return document.encode("utf-8")


def build(source: Path, output: Path, *, check: bool) -> None:
    expected = encode_poems(load_poems(source))

    if check:
        if not output.exists():
            raise DataValidationError(f"generated data is missing: {output}")
        if output.read_bytes() != expected:
            raise DataValidationError(
                f"generated data is stale: run {Path(__file__).name}"
            )
        return

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(expected)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the canonical Rubaiyat CSV and generate browser JSON."
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if the generated JSON is missing or stale",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        build(args.source, args.output, check=args.check)
    except (DataValidationError, OSError) as error:
        raise SystemExit(f"error: {error}") from error
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
