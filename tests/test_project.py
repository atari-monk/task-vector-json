import pytest
from pydantic import ValidationError
from project.project import Project

def test_valid_repository_name():
    Project(
        id=1,
        name="Test",
        description="Test project",
        repository_name="valid-repo_123"
    )
    
def test_invalid_repository_name():
    with pytest.raises(ValidationError):
        Project(
            id=1,
            name="Test",
            description="Test project",
            repository_name="invalid repo"
        )
    
    with pytest.raises(ValidationError):
        Project(
            id=1,
            name="Test",
            description="Test project",
            repository_name="InvalidRepo"
        )