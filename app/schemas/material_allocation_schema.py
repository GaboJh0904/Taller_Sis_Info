# app/schemas/material_allocation_schema.py
from pydantic import BaseModel

class MaterialAllocationBase(BaseModel):
    FLUJO_MATERIAL_ID: int
    PROYECTO_ID: int
    CANTIDAD: int
    FASE: str

class MaterialAllocationCreate(MaterialAllocationBase):
    pass  # La creación usa los mismos campos que MaterialAllocationBase

class MaterialAllocationOut(MaterialAllocationBase):
    ID: int  # Al devolver una asignación, también incluimos el ID