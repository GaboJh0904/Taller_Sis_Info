# app/schemas/purchase_tool_detail_schema.py
from pydantic import BaseModel

class PurchaseToolDetailBase(BaseModel):
    COSTO: float
    CANTIDAD: int
    HERRAMIENTA_ID: int
    COMPRA_HERRAMIENTA_ID: int

class PurchaseToolDetailCreate(PurchaseToolDetailBase):
    pass  # Creation uses the same fields as PurchaseToolDetailBase

class PurchaseToolDetailOut(PurchaseToolDetailBase):
    ID: int  # Include ID when returning a purchase tool detail
    HERRAMIENTA: str
