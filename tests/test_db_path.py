import shutil
from pathlib import Path
from json_db.db_path import DbPath


def test_path_property_returns_correct_path(tmp_path: Path):
    folder_name = "mydb"
    dp = DbPath(tmp_path, folder_name)
    assert dp.path == tmp_path / folder_name


def test_directory_created_on_init(tmp_path: Path):
    folder_name = "db_folder"
    target = tmp_path / folder_name
    assert not target.exists()
    DbPath(tmp_path, folder_name)
    assert target.exists()
    assert target.is_dir()


def test_accepts_string_repo_path(tmp_path: Path):
    folder_name = "db"
    repo_str = str(tmp_path)
    dp = DbPath(repo_str, folder_name)
    assert isinstance(dp.repo_path, Path)
    assert dp.repo_path == tmp_path
    assert (tmp_path / folder_name).exists()


def test_existing_directory_is_preserved(tmp_path: Path):
    folder_name = "existing"
    existing = tmp_path / folder_name
    existing.mkdir()
    dp = DbPath(tmp_path, folder_name)
    assert dp.path == existing
    assert existing.exists()


def test_nested_folder_creation(tmp_path: Path):
    nested = "a/b/c"
    dp = DbPath(tmp_path, nested)
    expected = tmp_path / "a" / "b" / "c"
    assert dp.path == expected
    assert expected.exists()
    assert expected.is_dir()


def test_cleanup(tmp_path: Path):
    folder_name = "to_remove"
    DbPath(tmp_path, folder_name)
    assert (tmp_path / folder_name).exists()
    shutil.rmtree(tmp_path / folder_name)
    assert not (tmp_path / folder_name).exists()
