"""Create DOI file from csv file."""

import argparse
from pathlib import Path
from typing import List, Optional, Union

import pandas as pd
from scidownl import scihub_download

from pkpdbib import BASE_PATH, RESULTS_DIR
from pkpdbib.console import console


def dois_from_csv(csv_path: Path) -> List[str]:
    """Create DOI file from csv file."""
    df: pd.DataFrame = pd.read_csv(csv_path, sep=",")
    df = df[["DOI"]]
    df[df.DOI == ""] = pd.NA
    df.dropna(inplace=True)
    dois: List[str] = df["DOI"].values
    return dois


def scihub_pdf_from_doi(
    doi: str, pdf_path: Path, scihub_url: Optional[str] = None
) -> None:
    """Download PDF from doi."""
    scihub_download(
        keyword=doi, paper_type="doi", out=str(pdf_path), scihub_url=scihub_url
    )


def scihub_pdfs_from_dois(
    dois: List[str], pdf_dir: Path, scihub_url: Optional[str] = None
) -> None:
    """Download PDFs from DOIS."""
    pdf_dir.mkdir(exist_ok=True, parents=True)
    console.rule("PDFs from dois", style="white")
    num_dois = len(dois)
    for k, doi in enumerate(dois):
        pdf_path = pdf_dir / f"{doi.replace('/', '__')}.pdf"
        console.print(f"[{k+1}/{num_dois}] {pdf_path}")
        if pdf_path.exists():
            continue
        scihub_pdf_from_doi(doi=doi, pdf_path=pdf_path, scihub_url=scihub_url)


def scihub_pdfs(zotero_tsv_path: Path, scihub_url: Optional[str] = None) -> None:
    """Download missing pdfs for substance."""
    console.print(zotero_tsv_path)
    dois = dois_from_csv(csv_path=zotero_tsv_path)
    scihub_pdfs_from_dois(
        dois=dois,
        pdf_dir=RESULTS_DIR / zotero_tsv_path.stem,
        scihub_url=scihub_url,
    )


def scihub_pdfs_command() -> None:
    """Download missing pdfs for substance."""
    parser = argparse.ArgumentParser(description="Retrieve PDFs for substance")
    parser.add_argument(
        "--zotero",
        "-z",
        help="zotero CSV path",
        dest="zotero_csv_path",
        type=str,
        required=True,
    )
    parser.set_defaults(func=scihub_pdfs)
    args: argparse.Namespace = parser.parse_args()
    zotero_csv_path = Path(args.zotero_csv_path)
    args.func(zotero_csv_path=zotero_csv_path)


if __name__ == "__main__":

    # scihub_pdfs(substance="aliskiren")
    scihub_pdfs_command()
    # scihub_pdfs -s aliskiren
    # scihub_pdfs_from_substance("aliskiren")
