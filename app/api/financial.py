# app/api/financial.py

from fastapi import APIRouter, HTTPException, Depends
from app.business_logic.financial_bl import FinancialBL
from app.schemas.financial_schema import BudgetVarianceOut, SpendingTrendOut, ExpenseBreakdownOut
from app.api.auth import oauth2_scheme, get_current_user
4
router = APIRouter()

@router.get("/projects/{project_id}/budget-variance", response_model=BudgetVarianceOut)
def get_budget_variance(
    project_id: int,
    token: str = Depends(oauth2_scheme)
):
    try:
        current_user = get_current_user(token)
        return FinancialBL.get_budget_variance(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/projects/{project_id}/spending-trend", response_model=SpendingTrendOut)
def get_spending_trend(
    project_id: int,
    token: str = Depends(oauth2_scheme)
):
    try:
        current_user = get_current_user(token)
        return FinancialBL.get_spending_trend(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/projects/{project_id}/expense-breakdown", response_model=ExpenseBreakdownOut)
def get_expense_breakdown(
    project_id: int,
    token: str = Depends(oauth2_scheme)
):
    try:
        current_user = get_current_user(token)
        return FinancialBL.get_expense_breakdown(project_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))