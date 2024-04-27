"""Programmatic access to zotero.

**Documentation**
https://pyzotero.readthedocs.org

**api key**:
https://www.zotero.org/settings/keys/new

**group ids**:
For group libraries, the ID can be found by opening the group’s page:
https://www.zotero.org/groups, and hovering over the group settings link.
The ID is the integer after /groups/
"""

from typing import Dict, List, Optional, Set

import pandas as pd
from pyzotero import zotero

from pkpdbib.console import console


def create_zot_client(
    api_key: str, library_id: int, library_type: str = "group"
) -> zotero.Zotero:
    """Create zotero client for library."""
    return zotero.Zotero(library_id, library_type, api_key)


def get_items(
    zot: zotero.Zotero, show: bool = False, limit: Optional[int] = None
) -> List[Dict]:
    """List items for library."""

    """
    A Zotero instance is bound to the library or group used to create it.
    Thus, if you create a Zotero instance with a library_id of 67 and a
    library_type of group, its item methods will only operate upon that group.
    """
    items: List[Dict]
    if limit:
        items = zot.top(limit=limit)  # top level items
    else:
        items = zot.top()  # top level items

    if show:
        for k, item in enumerate(items):
            console.rule(title=f"Item {k+1}", align="left", style="white")
            # console.print(item['data'])
            # console.print()
            console.print(item)
    return items


def create_tag_table(
    items: List[Dict],
    tags_set: Set[str],
    tag_prefixes: List[str],
) -> pd.DataFrame:
    """Create table with tags."""

    metadata: List[Dict] = []

    for _, item in enumerate(items):
        key = item["key"]
        data = item["data"]

        md = {
            "key": key,
            "doi": data["DOI"],
            "pubmed": None,
        }
        # 'extra': 'PMID: 27267043 \nPMCID: PMC4895977',

        item_tags = list()
        tags = [v["tag"] for v in data["tags"]]
        for tag in tags:
            if tag in tags_set:
                item_tags.append(tag)
                continue

            for prefix in tag_prefixes:
                if tag.startswith(prefix):
                    item_tags.append(tag)
                    continue

        for item_tag in item_tags:
            md[item_tag] = True

        metadata.append(md)

    df = pd.DataFrame(metadata)
    console.print(df.to_string())
    return df
