# JSON DB

Data models for managing paths in a JSON-based database.

## `DbPath`

* Constructs the root database path using `repo_path` and `db_folder`.
* Uses strict typing.
* Paths are `Path` objects (from `pathlib`).
* Creates the necessary folders automatically.

## `DbTablePath`

* Generates paths to specific database tables.
* Tables are stored as JSON files inside the database path.
* Automatically names and initializes each file with `[]`.

## `DbInfo`

* Stores the base database path.
* Contains references to:

  * A **projects** table (one per database).
  * A **tasks** table (one per project).
  * A **records** table (one per project, year, and month).
