# app/schemas/purchase_material_schema.py
from pydantic import BaseModel

class PurchaseMaterialBase(BaseModel):
    COSTO_TOTAL: float
    FECHA: int
    PROVEEDOR_ID: int
    DETALLE: str

class PurchaseMaterialCreate(PurchaseMaterialBase):
    pass  # Creation uses the same fields as PurchaseMaterialBase

class PurchaseMaterialOut(PurchaseMaterialBase):
    ID: int  # Include ID when returning a purchase material
