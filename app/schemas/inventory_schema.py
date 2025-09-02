# app/schemas/inventory_schema.py

from pydantic import BaseModel
from datetime import date


class StockLevelOut(BaseModel):
    item_id: int
    item_name: str
    current_stock: int
    minimum_stock: int
    stock_difference: int
    alert: bool


class InventoryTurnoverOut(BaseModel):
    item_id: int
    item_name: str
    turnover_ratio: float
    total_sold: int
    average_inventory: float
    start_date: date
    end_date: date


class ReplenishmentTimeOut(BaseModel):
    item_id: int
    item_name: str
    average_replenishment_time: float  # in days

    number_of_replenishments: int

class StockoutRateOut(BaseModel):
    item_id: int
    item_name: str

    stockout_rate: float  # percentage

    stockout_days: int
    total_days: int
    start_date: date
    end_date: date

