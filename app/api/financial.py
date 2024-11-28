# app/api/financial.py

from fastapi import APIRouter, Depends, HTTPException
from app.business_logic.financial_bl import FinancialBL
from app.schemas.financial_schema import (
    BudgetVarianceOut,
    SpendingTrendOut,
    ExpenseBreakdownOut
)
from app.api.auth import get_current_user
from app.schemas.user_schema import UserOut

router = APIRouter(
    prefix="/financial",
    tags=["Financial"]
)

@router.get("/projects/{project_id}/budget-variance", response_model=BudgetVarianceOut)
def get_budget_variance(
    project_id: int,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return FinancialBL.get_budget_variance(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/projects/{project_id}/spending-trend", response_model=SpendingTrendOut)
def get_spending_trend(
    project_id: int,
    fase: str = None,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return FinancialBL.get_spending_trend(project_id, fase=fase)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/projects/{project_id}/material-spending", response_model=ExpenseBreakdownOut)
def material_spending(
    project_id: int,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return FinancialBL.get_material_spending(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/projects/{project_id}/tool-spending", response_model=ExpenseBreakdownOut)
def tool_spending(
    project_id: int,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return FinancialBL.get_tool_spending(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
