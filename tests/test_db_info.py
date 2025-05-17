from pathlib import Path
from datetime import datetime
from json_db.db_info import DbInfo
from json_db.db_path import DbPath


def test_proj_table_full_path(tmp_path: Path):
    dbinfo = DbInfo()
    dbinfo.db_path = DbPath(tmp_path, "task_log")
    dbinfo.proj_table = dbinfo.proj_table.__class__(dbinfo.db_path, lambda: "projects")

    expected_path = tmp_path / "task_log" / "projects.json"
    assert dbinfo.proj_table.path == expected_path


def test_task_table_full_path(tmp_path: Path):
    dbinfo = DbInfo()
    dbinfo.db_path = DbPath(tmp_path, "task_log")

    project_name = "myproject"
    table = dbinfo.get_task_table(project_name)
    expected_path = tmp_path / "task_log" / f"{project_name}_tasks.json"
    assert table.path == expected_path


def test_record_table_full_path(tmp_path: Path):
    dbinfo = DbInfo()
    dbinfo.db_path = DbPath(tmp_path, "task_log")

    project_name = "myproject"
    table = dbinfo.get_record_table(project_name)

    today = datetime.today()
    expected_name = f"{project_name}_records_{today.year}_{today.month:02d}.json"
    expected_path = tmp_path / "task_log" / expected_name

    assert table.path == expected_path
