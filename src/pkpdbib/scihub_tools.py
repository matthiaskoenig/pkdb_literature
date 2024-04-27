"""Create DOI file from csv file."""

from pathlib import Path

import pandas as pd
from console import console


def dois_from_csv(csv_path: Path, doi_path: Path) -> None:
    """Create DOI file from csv file."""
    console.print(csv_path)
    df: pd.DataFrame = pd.read_csv(csv_path, sep=",")
    console.print(df.columns)
    console.print(df.head(10))

    df = df[["DOI"]]
    df[df.DOI == ""] = pd.NA
    df.dropna(inplace=True)

    # filter empty rows
    df.to_csv(doi_path, index=False, header=False)


if __name__ == "__main__":
    from pkdb_literature import BASE_PATH

    substance = "aliskiren"

    dois_from_csv(
        csv_path=BASE_PATH / "dois" / f"{substance}.csv",
        doi_path=BASE_PATH / "dois" / f"{substance}_dois.txt",
    )
