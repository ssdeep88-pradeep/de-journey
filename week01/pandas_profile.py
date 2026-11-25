"""pandas_profile.py - profile a CSV file using pandas."""
import sys
from pathlib import Path

import pandas as pd


def profile(path):
    df = pd.read_csv(path)

    print(f"File:    {path}")
    print(f"Rows:    {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Duplicate rows: {df.duplicated().sum()}\n")

    summary = pd.DataFrame(
        {
            "type": df.dtypes.astype(str),
            "nulls": df.isna().sum(),
            "unique": df.nunique(),
            "min": df.min(numeric_only=True),
            "max": df.max(numeric_only=True),
        },
        index=df.columns,
    )
    print(summary.to_string(na_rep=""))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python pandas_profile.py <file.csv>")
    file = Path(sys.argv[1])
    if not file.exists():
        sys.exit(f"File not found: {file}")
    profile(file)
