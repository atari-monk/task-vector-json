from pathlib import Path
from typing import List, Optional
import json
from pydantic import ValidationError
from project.project import Project

class ProjectCRUD:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        if not self.file_path.exists():
            self.file_path.write_text("[]")

    def _read_projects(self) -> List[Project]:
        try:
            data = json.loads(self.file_path.read_text())
            return [Project.model_validate(item) for item in data]
        except (json.JSONDecodeError, ValidationError) as e:
            raise ValueError(f"Invalid data in storage file: {e}")

    def _write_projects(self, projects: List[Project]) -> None:
        self.file_path.write_text(json.dumps([project.model_dump() for project in projects], indent=2))

    def create(self, project: Project) -> Project:
        projects = self._read_projects()
        if any(p.id == project.id for p in projects):
            raise ValueError(f"Project with ID {project.id} already exists")
        projects.append(project)
        self._write_projects(projects)
        return project

    def read_all(self) -> List[Project]:
        return self._read_projects()

    def read(self, project_id: int) -> Optional[Project]:
        projects = self._read_projects()
        return next((p for p in projects if p.id == project_id), None)

    def update(self, project_id: int, project_data: Project) -> Project:
        projects = self._read_projects()
        index = next((i for i, p in enumerate(projects) if p.id == project_id), None)
        if index is None:
            raise ValueError(f"Project with ID {project_id} not found")
        if project_id != project_data.id:
            if any(p.id == project_data.id for p in projects):
                raise ValueError(f"Project with ID {project_data.id} already exists")
        projects[index] = project_data
        self._write_projects(projects)
        return project_data

    def delete(self, project_id: int) -> None:
        projects = self._read_projects()
        index = next((i for i, p in enumerate(projects) if p.id == project_id), None)
        if index is None:
            raise ValueError(f"Project with ID {project_id} not found")
        del projects[index]
        self._write_projects(projects)