"""Clean the Superstore dataset.

Usage:
    python scripts/clean_data.py
Reads  data/Sample - Superstore.csv
Writes data/superstore_cleaned.csv
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "Sample - Superstore.csv"
OUT = ROOT / "data" / "superstore_cleaned.csv"


def cap_outliers_iqr(s: pd.Series) -> pd.Series:
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    return s.clip(lower=q1 - 1.5 * iqr, upper=q3 + 1.5 * iqr)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates().copy()

    # data types
    for c in ["Order Date", "Ship Date"]:
        df[c] = pd.to_datetime(df[c], errors="coerce")
    for c in ["Ship Mode", "Segment", "Region", "Category", "Sub-Category"]:
        df[c] = df[c].astype("category")

    # missing values
    num = df.select_dtypes("number").columns
    df[num] = df[num].fillna(df[num].median())
    for c in df.select_dtypes(["object", "category"]).columns:
        if df[c].isna().any():
            df[c] = df[c].fillna(df[c].mode()[0])
    df = df.dropna(subset=["Order Date"])

    # outliers (IQR capping) on key numeric columns
    for c in ["Sales", "Profit"]:
        df[c + "_capped"] = cap_outliers_iqr(df[c])
    return df


if __name__ == "__main__":
    raw = pd.read_csv(RAW, encoding="latin-1")
    cleaned = clean(raw)
    cleaned.to_csv(OUT, index=False)
    print(f"Raw: {raw.shape} -> Cleaned: {cleaned.shape}\nSaved to {OUT}")
