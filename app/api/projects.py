# app/api/projects.py

from fastapi import APIRouter, Depends, HTTPException
from app.business_logic.project_bl import ProjectBL
from app.schemas.project_schema import (
    ProjectCompletionOut,
    ResourceUtilizationOut,
    ProjectOut
)
from app.api.auth import get_current_user
from app.schemas.user_schema import UserOut

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("/{project_id}/completion-percentage", response_model=ProjectCompletionOut)
def get_project_completion_percentage(
    project_id: int,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return ProjectBL.get_project_completion_percentage(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{project_id}/resource-utilization", response_model=ResourceUtilizationOut)
def get_resource_utilization(
    project_id: int,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return ProjectBL.get_resource_utilization(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[ProjectOut])
def get_all_projects(
    current_user: UserOut = Depends(get_current_user)
):
    return ProjectBL.get_all_projects()
