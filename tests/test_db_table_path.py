from pathlib import Path
from json_db.db_path import DbPath
from json_db.db_table_path import DbTablePath


def test_dbtablepath_basic_path_and_file(tmp_path: Path):
    db_path = DbPath(tmp_path, "mydb")
    name_func = lambda: "tablename"
    table = DbTablePath(db_path, name_func)

    expected_path = tmp_path / "mydb" / "tablename.json"
    assert table.path == expected_path

    assert expected_path.exists()
    content = expected_path.read_text()
    assert content == "[]"


def test_dbtablepath_custom_extension_and_file(tmp_path: Path):
    db_path = DbPath(tmp_path, "mydb")
    name_func = lambda: "tablename"
    table = DbTablePath(db_path, name_func, ext="txt")

    expected_path = tmp_path / "mydb" / "tablename.txt"
    assert table.path == expected_path

    assert expected_path.exists()
    assert expected_path.read_text() == "[]"


def test_dbtablepath_dynamic_name_func_and_file(tmp_path: Path):
    db_path = DbPath(tmp_path, "mydb")

    prefix = "prefix"
    suffix = "suffix"

    def dynamic_name():
        return f"{prefix}_{suffix}"

    table = DbTablePath(db_path, dynamic_name)

    expected_path = tmp_path / "mydb" / f"{prefix}_{suffix}.json"
    assert table.path == expected_path

    assert expected_path.exists()
    assert expected_path.read_text() == "[]"
