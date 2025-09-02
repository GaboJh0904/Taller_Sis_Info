# app/schemas/purchase_tool_schema.py
from datetime import datetime

from pydantic import BaseModel

class PurchaseToolBase(BaseModel):
    COSTO_TOTAL: float
    FECHA: datetime
    PROVEEDOR_ID: int
    DETALLE: str

class PurchaseToolCreate(PurchaseToolBase):
    pass  # Creation uses the same fields as PurchaseToolBase

class PurchaseToolOut(PurchaseToolBase):
    ID: int  # Include ID when returning a purchase tool
    PROVEEDOR: str
