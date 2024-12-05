# app/schemas/financial_schema.py

from pydantic import BaseModel
from typing import List

class BudgetVarianceOut(BaseModel):
    project_id: int
    project_name: str
    assigned_budget: float
    actual_spending: float
    budget_variance: float

class SpendingRecord(BaseModel):
    date: str  # Format YYYY-MM-DD
    amount: float

class SpendingTrendOut(BaseModel):
    project_id: int
    project_name: str
    spending_over_time: List[SpendingRecord]

class ExpenseCategory(BaseModel):
    category: str
    total_spent: float

class ExpenseBreakdownOut(BaseModel):
    project_id: int
    project_name: str
    expenses: List[ExpenseCategory]
    total_expense: float
