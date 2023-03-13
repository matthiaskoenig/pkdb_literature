"""pkdb_literature - Python utilities for literature."""
from pathlib import Path

__author__ = "Matthias Koenig"
__version__ = "0.0.1"


program_name: str = "pkdb_literature"
RESOURCES_DIR: Path = Path(__file__).parent / "resources"
RESULTS_DIR: Path = Path(__file__).parent.parent.parent / "results"

APIKEYS_DIR: Path = Path(__file__).parent.parent.parent / ".api_keys.txt"
