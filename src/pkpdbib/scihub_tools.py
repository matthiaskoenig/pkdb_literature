"""Create DOI file from csv file."""
from pathlib import Path
from typing import List
import argparse
import pandas as pd
from pkpdbib.console import console
from scidownl import scihub_download
from pkpdbib import BASE_PATH, RESULTS_DIR


def dois_from_csv(csv_path: Path) -> List[str]:
    """Create DOI file from csv file."""
    df: pd.DataFrame = pd.read_csv(csv_path, sep=",")
    df = df[["DOI"]]
    df[df.DOI == ""] = pd.NA
    df.dropna(inplace=True)
    dois: List[str] = df["DOI"].values
    return dois


def scihub_pdf_from_doi(doi: str, pdf_path: Path, scihub_url: str = None) -> None:
    """Download PDF from doi."""
    scihub_download(
        keyword=doi,
        paper_type="doi",
        out=str(pdf_path),
        scihub_url=scihub_url
    )


def scihub_pdfs_from_dois(dois: List[str], pdf_dir: Path, scihub_url: str = None) -> None:
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


def scihub_pdfs(substance: str, scihub_url: str = None) -> None:
    """Download missing pdfs for substance."""
    console.print(substance)
    dois = dois_from_csv(csv_path=BASE_PATH / "dois" / f"{substance}.csv")
    scihub_pdfs_from_dois(
        dois=dois,
        pdf_dir=RESULTS_DIR / substance,
        scihub_url=scihub_url,
    )


def scihub_pdfs_command() -> None:
    """Download missing pdfs for substance."""
    parser = argparse.ArgumentParser(description="Retrieve PDFs for substance")
    parser.add_argument(
        "--substance",
        "-s",
        help="substance name",
        dest="substance",
        type=str,
        required=True,
    )
    parser.set_defaults(func=scihub_pdfs)
    args: argparse.Namespace = parser.parse_args()
    args.func(substance=args.substance)


if __name__ == "__main__":

    # scihub_pdfs(substance="aliskiren")
    scihub_pdfs_command()
    # scihub_pdfs -s aliskiren
    # scihub_pdfs_from_substance("aliskiren")

