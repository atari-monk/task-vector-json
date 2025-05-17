from datetime import datetime
from pathlib import Path
from json_db.db_path import DbPath
from json_db.db_table_path import DbTablePath


class DbInfo:
    def __init__(self):
        self.db_path = DbPath(
            Path(r"C:\atari-monk\code\apps-data-store"), "task_vector_json_db"
        )
        self.proj_table = DbTablePath(self.db_path, name_func=lambda: "projects")

    def get_task_table(self, project_name: str) -> DbTablePath:
        return DbTablePath(self.db_path, lambda: f"{project_name}_tasks")

    def get_record_table(self, project_name: str) -> DbTablePath:
        today = datetime.today()
        return DbTablePath(
            self.db_path,
            lambda: f"{project_name}_records_{today.year}_{today.month:02d}",
        )
