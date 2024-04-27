"""Create DOI file from csv file."""
import tempfile
from pathlib import Path
from typing import List

import pandas as pd
from pkpdbib.console import console
from scidownl import scihub_download


def scihub_pdf_from_doi(doi: str, pdf_path: Path) -> None:
    """Download PDF from doi."""
    scihub_download(doi, paper_type="doi", out=str(pdf_path))

def scihub_pdf_from_pmid(pmid: str, pdf_path: Path) -> None:
    """Download PDF from pmid."""
    scihub_download(pmid, paper_type="pmid", out=str(pdf_path))


def dois_from_csv(csv_path: Path) -> List[str]:
    """Create DOI file from csv file."""
    df: pd.DataFrame = pd.read_csv(csv_path, sep=",")
    df = df[["DOI"]]
    df[df.DOI == ""] = pd.NA
    df.dropna(inplace=True)
    dois: List[str] = df["DOI"].values
    return dois


def scihub_pdfs_from_dois(dois: List[str], pdf_dir: Path):
    pass


if __name__ == "__main__":
    from pkpdbib import BASE_PATH

    console.rule("PDF from doi", style="white")
    scihub_pdf_from_doi(doi="https://doi.org/10.1145/3375633", pdf_path="doi.pdf")

    console.rule("PDFs from dois", style="white")
    # doi creation
    substance: str = "aliskiren"
    console.print(substance)
    dois = dois_from_csv(
        csv_path=BASE_PATH / "dois" / f"{substance}.csv",
    )

    # scihub_pdfs_from_dois(
    #     dois=dois,
    #
    # )
