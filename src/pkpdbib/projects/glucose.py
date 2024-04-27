"""Example for glucose library."""

from typing import Dict, List, Set

from pyzotero import zotero

from pkpdbib.console import console
from pkpdbib.zotero_tools import create_zot_client


custom_tags: Set[str] = {
    "has_simulation",
    "pkdb",
}
custom_tag_prefixes: List[str] = [
    "data:",
    "group:",
    "species:",
    "timecourse:",
]


if __name__ == "__main__":
    # zot: zotero.Zotero = create_zot_client("pyzot")
    # get_items(zot, show=True, limit=1)
    # items = get_items(zot, show=False)
    # df = create_tag_table(items)
    # df.to_excel(RESULTS_DIR / "pyzot_tags.xlsx", sheet_name="tags")

    api_key: str = "5w2kDQMA7YfRbnyUxPdjBEgW"
    library_id: int = 4979949
    zot: zotero.Zotero = create_zot_client(
        api_key=api_key, library_id=library_id, library_type="group"
    )
    items = zot.searches()
    console.print(items)
