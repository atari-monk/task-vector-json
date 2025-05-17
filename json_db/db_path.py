from pathlib import Path
from typing import Union

class DbPath:
    def __init__(self, db_repository_path: Union[str, Path], subdir: str):
        self.repo_path = Path(db_repository_path)
        self.path = self.repo_path / subdir
        self.path.mkdir(parents=True, exist_ok=True)
