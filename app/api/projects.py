# app/api/projects.py
from fastapi import APIRouter, HTTPException
from app.schemas.project_schema import ProjectCreate, ProjectOut
from app.business_logic.project_bl import ProjectBL

router = APIRouter()

@router.post("/", response_model=ProjectOut)
def create_new_project(project_data: ProjectCreate):
    try:
        return ProjectBL.create_new_project(project_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{project_id}", response_model=ProjectOut)
def get_project(project_id: int):
    try:
        return ProjectBL.get_project(project_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[ProjectOut])
def list_all_projects():
    return ProjectBL.get_all_projects()

@router.put("/{project_id}", response_model=ProjectOut)
def update_existing_project(project_id: int, project_data: ProjectCreate):
    try:
        return ProjectBL.update_existing_project(project_id, project_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{project_id}")
def delete_existing_project(project_id: int):
    try:
        ProjectBL.delete_project(project_id)
        return {"detail": "Project deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
