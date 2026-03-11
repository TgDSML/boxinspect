from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
import uuid

router = APIRouter()

projects: Dict[str, Dict] = {}

class ProjectCreate(BaseModel):
    name: str

@router.post("/projects")
def create_project(project: ProjectCreate):
    project_id = str(uuid.uuid4())
    
    projects[project_id] = {
        "id": project_id,
        "name": project.name,
    }

    return projects[project_id]

@router.get("/projects")
def list_projects():
    return list(projects.values())