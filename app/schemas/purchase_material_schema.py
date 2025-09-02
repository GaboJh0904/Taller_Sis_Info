# app/schemas/purchase_material_schema.py
from datetime import date
from datetime import datetime
from pydantic import BaseModel

class PurchaseMaterialBase(BaseModel):
    COSTO_TOTAL: float
    FECHA: datetime
    PROVEEDOR_ID: int
    DETALLE: str

class PurchaseMaterialCreate(PurchaseMaterialBase):
    pass  # Creation uses the same fields as PurchaseMaterialBase

class PurchaseMaterialOut(PurchaseMaterialBase):
    ID: int  # Include ID when returning a purchase material
    PROVEEDOR: str
