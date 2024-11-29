# app/api/inventory.py

from fastapi import APIRouter, Depends, HTTPException
from app.business_logic.inventory_bl import InventoryBL
from app.schemas.inventory_schema import (
    StockLevelOut,
    InventoryTurnoverOut,
    ReplenishmentTimeOut,
    StockoutRateOut
)
from app.api.auth import get_current_user  # Import get_current_user
from app.schemas.user_schema import UserOut
from datetime import date

router = APIRouter()

@router.get("/stock-levels", response_model=StockLevelOut)
def get_stock_levels(
    item_id: int,
    item_type: str,
    current_user: UserOut = Depends(get_current_user)  # Require authentication
):
    try:
        return InventoryBL.get_stock_levels(item_id, item_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/turnover-ratio", response_model=InventoryTurnoverOut)
def get_inventory_turnover_ratio(
    item_id: int,
    item_type: str,
    start_date: date,
    end_date: date,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return InventoryBL.get_inventory_turnover_ratio(item_id, item_type, start_date, end_date)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/replenishment-time", response_model=ReplenishmentTimeOut)
def get_average_replenishment_time(
    item_id: int,
    item_type: str,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return InventoryBL.get_average_replenishment_time(item_id, item_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/stockout-rate", response_model=StockoutRateOut)
def get_stockout_rate(
    item_id: int,
    item_type: str,
    start_date: date,
    end_date: date,
    current_user: UserOut = Depends(get_current_user)
):
    try:
        return InventoryBL.get_stockout_rate(item_id, item_type, start_date, end_date)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
