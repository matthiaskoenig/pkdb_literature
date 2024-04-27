"""Programmatic access to zotero using pyzotero.

    **Documentation**
    https://pyzotero.readthedocs.org

    **api key**:
    https://www.zotero.org/settings/keys/new

    **group ids**:
    For group libraries, the ID can be found by opening the group’s page:
    https://www.zotero.org/groups, and hovering over the group settings link.
    The ID is the integer after /groups/

"""
from typing import Dict, List, Set

import pandas as pd
from pyzotero import zotero


from pkdb_literature.console import console



def create_zot_client(library_id: str, api_key: str, library_type: str = "group") -> zotero.Zotero:
    """Create zotero client for library."""
    return zotero.Zotero(library_id, library_type, api_key)



def get_items(zot: zotero.Zotero, show: bool = False, limit=None) -> List[Dict]:
    """List items for library."""

    '''
    A Zotero instance is bound to the library or group used to create it.
    Thus, if you create a Zotero instance with a library_id of 67 and a
    library_type of group, its item methods will only operate upon that group.
    '''
    if limit:
        items = zot.top(limit=limit)  # top level items
    else:
        items = zot.top()  # top level items

    if show:
        for k, item in enumerate(items):
            console.rule(title=f"Item {k+1}", align="left", style="white")
            #console.print(item['data'])
            #console.print()
            console.print(item)
    return items


def create_tag_table(items: List[Dict], tags_set: Set[str] = custom_tags, tag_prefixes: List[str] = custom_tag_prefixes) -> pd.DataFrame:
    """Creates a table with tag columns."""

    metadata: List[Dict] = []

    for k, item in enumerate(items):
        key = item["key"]
        data = item['data']

        md = {
            'key': key,
            'doi': data["DOI"],
            'pubmed': None,
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


if __name__ == "__main__":
    from pkdb_literature import RESULTS_DIR, APIKEYS_DIR

    # Your userID for use in API calls is 7851040
    # zot: zotero.Zotero = create_zot_client("pyzot")
    # get_items(zot, show=True, limit=1)
    # items = get_items(zot, show=False)
    # df = create_tag_table(items)
    # df.to_excel(RESULTS_DIR / "pyzot_tags.xlsx", sheet_name="tags")

    # do the same for glucose-risk-score library:
    # read api_key, FIXME: handle multiple api_keys in file
    with open(APIKEYS_DIR) as file:
        libraryinfo = file.readline()
        api_key = libraryinfo.split(":")[1]
    api_key = api_key.strip()

    zot: zotero.Zotero = create_zot_client(library="glucose-risk-score", api_key=api_key)
    eligible_items = zot.searches()
    console.print(eligible_items)


