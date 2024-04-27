"""pkdbbib - Python utilities for PK/DB literature and bibliography."""

from pathlib import Path

__author__ = "Matthias König"
__version__ = "0.1.0"


program_name: str = "pkdb_literature"
RESOURCES_DIR: Path = Path(__file__).parent / "resources"

BASE_PATH = Path(__file__).parent.parent.parent
RESULTS_DIR: Path = BASE_PATH / "results"
RESULTS_DIR.mkdir(exist_ok=True)
