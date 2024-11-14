# app/schemas/purchase_material_detail_schema.py
from pydantic import BaseModel

class PurchaseDetailBase(BaseModel):
    COSTO: float
    CANTIDAD: int
    MATERIAL_ID: int
    COMPRA_MATERIAL_ID: int

class PurchaseDetailCreate(PurchaseDetailBase):
    pass  # Creation uses the same fields as PurchaseDetailBase

class PurchaseDetailOut(PurchaseDetailBase):
    ID: int  # Include ID when returning a purchase detail
