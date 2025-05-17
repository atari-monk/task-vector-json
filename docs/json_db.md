# Json Db

Data models to represent paths for json files database

## DbPath

- generates database path from repo_path and db_folder
- strict types
- Path type for paths
- generates folder

## DbTablePath

- generates db tables
- these are json files in db path with computed name
- writes `[]` to file

## DbInfo

- stores db path
- projects table (one table per db)
- tasks table (one table per project)
- records table (one table per project, year, month)