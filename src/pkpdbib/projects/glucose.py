from typing import Dict, Set, List
from pkdb_literature

libraries: Dict[str, Dict] = {
    "pyzot": {'gid': 4979949, 'api_key': "5w2kDQMA7YfRbnyUxPdjBEgW"},
    "glucose-risk-score": {'gid': 4535898, 'api_key': None}
}

custom_tags: Set[str] = {
    'has_simulation',
    'pkdb',
}
custom_tag_prefixes: List[str] = [
    "data:",
    "group:",
    "species:",
    "timecourse:",
]


library_id = libraries[library]["gid"]
