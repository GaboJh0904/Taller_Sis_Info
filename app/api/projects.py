# app/api/projects.py

from fastapi import APIRouter, HTTPException, Depends
from app.business_logic.project_bl import ProjectBL
from app.schemas.project_schema import (
    ProjectCreate,
    ProjectOut,
    ProjectCompletionOut,
    ResourceUtilizationOut
)
from app.api.auth import oauth2_scheme, get_current_user

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
    dependencies=[Depends(oauth2_scheme)]
)

@router.post("/", response_model=ProjectOut)
def create_new_project(project_data: ProjectCreate, token: str = Depends(oauth2_scheme)):
    try:
        current_user = get_current_user(token)
        return ProjectBL.create_new_project(project_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{project_id}", response_model=ProjectOut)
def get_project(project_id: int, token: str = Depends(oauth2_scheme)):
    try:
        current_user = get_current_user(token)
        return ProjectBL.get_project(project_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[ProjectOut])
def list_all_projects(token: str = Depends(oauth2_scheme)):
    current_user = get_current_user(token)
    return ProjectBL.get_all_projects()

@router.put("/{project_id}", response_model=ProjectOut)
def update_existing_project(project_id: int, project_data: ProjectCreate, token: str = Depends(oauth2_scheme)):
    try:
        current_user = get_current_user(token)
        return ProjectBL.update_existing_project(project_id, project_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{project_id}")
def delete_existing_project(project_id: int, token: str = Depends(oauth2_scheme)):
    try:
        current_user = get_current_user(token)
        ProjectBL.delete_project(project_id)
        return {"detail": "Project deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{project_id}/completion-percentage", response_model=ProjectCompletionOut)
def get_project_completion_percentage(project_id: int, token: str = Depends(oauth2_scheme)):
    try:
        current_user = get_current_user(token)
        return ProjectBL.get_project_completion_percentage(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{project_id}/resource-utilization", response_model=ResourceUtilizationOut)
def get_resource_utilization(project_id: int, token: str = Depends(oauth2_scheme)):
    try:
        current_user = get_current_user(token)
        return ProjectBL.get_resource_utilization(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
