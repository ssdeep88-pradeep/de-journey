"""csv_profile.py - print a quick profile of a CSV file."""
import csv
import sys
from pathlib import Path


def infer_type(values):
    """Guess a column's type from its non-empty values."""
    def all_match(cast):
        try:
            for v in values:
                cast(v)
            return True
        except ValueError:
            return False

    if not values:
        return "empty"
    if all_match(int):
        return "int"
    if all_match(float):
        return "float"
    return "string"


def profile(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        columns = reader.fieldnames or []

    print(f"File:    {path}")
    print(f"Rows:    {len(rows)}")
    print(f"Columns: {len(columns)}\n")
    print(f"{'column':<20}{'type':<8}{'nulls':>6}{'unique':>8}  min / max")
    print("-" * 60)

    for col in columns:
        raw = [(r.get(col) or "").strip() for r in rows]
        values = [v for v in raw if v]
        nulls = len(raw) - len(values)
        col_type = infer_type(values)
        if col_type in ("int", "float"):
            nums = [float(v) for v in values]
            rng = f"{min(nums):g} / {max(nums):g}"
        else:
            rng = ""
        print(f"{col:<20}{col_type:<8}{nulls:>6}{len(set(values)):>8}  {rng}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python csv_profile.py <file.csv>")
    file = Path(sys.argv[1])
    if not file.exists():
        sys.exit(f"File not found: {file}")
    profile(file)
