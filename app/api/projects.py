# app/api/projects.py

from fastapi import APIRouter, Depends, HTTPException
from app.business_logic.project_bl import ProjectBL
from app.schemas.project_schema import (
    ProjectCompletionOut,
    ResourceUtilizationOut,
    ProjectOut,
    ProjectCreate
)
from app.api.auth import (get_current_user, get_admin_user, get_employee_user,
                           get_finance_manager_user, get_project_manager_user)
  
from app.schemas.user_schema import UserOut

router = APIRouter()

@router.get("/{project_id}/completion-percentage", response_model=ProjectCompletionOut)
def get_project_completion_percentage(
    project_id: int,
    current_user: UserOut = Depends(get_admin_user)
):
    try:
        return ProjectBL.get_project_completion_percentage(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{project_id}/resource-utilization", response_model=ResourceUtilizationOut)
def get_resource_utilization(
    project_id: int,
    current_user: UserOut = Depends(get_admin_user)
):
    try:
        return ProjectBL.get_resource_utilization(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

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
