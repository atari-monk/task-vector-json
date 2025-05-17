from pydantic import BaseModel, Field, field_validator

class Project(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    description: str = Field(..., max_length=300)
    repository_name: str = Field(
        default="",
        max_length=50,
        pattern=r"^[a-z0-9_-]*$"
    )

    @field_validator('repository_name')
    @classmethod
    def validate_repo_name(cls, v: str) -> str:
        if ' ' in v:
            raise ValueError('No spaces allowed')
        return v.lower()