from pathlib import Path
from typing import Callable
from json_db.db_path import DbPath


class DbTablePath:
    def __init__(
        self, db_path: DbPath, name_func: Callable[[], str], ext: str = "json"
    ):
        self.db_path = db_path
        self.name_func = name_func
        self.ext = ext
        self._path = self._compute_path()
        self._initialize_file()

    def _compute_path(self) -> Path:
        return self.db_path.path / f"{self.name_func()}.{self.ext}"

    @property
    def path(self) -> Path:
        return self._path

    def _initialize_file(self):
        if not self._path.exists():
            self._path.write_text("[]")
