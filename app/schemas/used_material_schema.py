# app/schemas/used_material_schema.py
from pydantic import BaseModel
from datetime import date

class UsedMaterialBase(BaseModel):
    ASIGNACION_MATERIAL_ID: int
    CANTIDAD: int
    FECHA: date
    DETALLE: str

class UsedMaterialCreate(UsedMaterialBase):
    pass  # La creación usa los mismos campos que UsedMaterialBase

class UsedMaterialOut(UsedMaterialBase):
    ID: int  # Al devolver un uso de material, también incluimos el ID