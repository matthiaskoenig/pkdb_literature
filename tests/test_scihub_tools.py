from pkpdbib.scihub_tools import dois_from_csv, scihub_pdf_from_doi
from pkpdbib import BASE_PATH


def test_scihub_pdf_from_doi(tmp_path) -> None:
    doi = "https://doi.org/10.1145/3375633"
    pdf_path = tmp_path / "test.pdf"
    scihub_pdf_from_doi(doi=doi, pdf_path=pdf_path)
    assert pdf_path


def test_dois_from_csv(tmp_path) -> None:
    """Test getting dois from zotero csv."""
    dois = dois_from_csv(
        csv_path=BASE_PATH / "dois" / "aliskiren.csv",
    )
    assert dois is not None
    assert len(dois) == 61
