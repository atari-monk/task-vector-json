from typing import Optional
import typer
from json_db.db_info import DbInfo
from project.project import Project
from project.project_crud import ProjectCRUD

app = typer.Typer()
crud = ProjectCRUD(DbInfo().proj_table.path)

@app.command()
def create(
    id: int,
    name: str,
    description: str,
    repository_name: str = ""
):
    project = Project(
        id=id,
        name=name,
        description=description,
        repository_name=repository_name
    )
    try:
        created = crud.create(project)
        typer.echo(f"Created project: {created}")
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

@app.command()
def list():
    projects = crud.read_all()
    for project in projects:
        typer.echo(project)

@app.command()
def get(id: int):
    project = crud.read(id)
    if project:
        typer.echo(project)
    else:
        typer.echo(f"Project with ID {id} not found", err=True)
        raise typer.Exit(1)

@app.command()
def update(
    id: int,
    name: Optional[str] = None,
    description: Optional[str] = None,
    repository_name: Optional[str] = None
):
    project = crud.read(id)
    if not project:
        typer.echo(f"Project with ID {id} not found", err=True)
        raise typer.Exit(1)
    
    update_data = {
        "name": name if name is not None else project.name,
        "description": description if description is not None else project.description,
        "repository_name": repository_name if repository_name is not None else project.repository_name
    }
    
    updated_project = Project(
        id=id,
        **update_data
    )
    
    try:
        result = crud.update(id, updated_project)
        typer.echo(f"Updated project: {result}")
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

@app.command()
def delete(id: int):
    try:
        crud.delete(id)
        typer.echo(f"Deleted project with ID {id}")
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

def main():
    app()

if __name__ == "__main__":
    main()