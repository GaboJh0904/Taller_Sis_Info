# app/schemas/material_schema.py
from pydantic import BaseModel

class MaterialBase(BaseModel):
    NOMBRE: str
    DESCRIPCION: str
    CANTIDAD: int
    PRECIO_UNITARIO: int
    CANTIDAD_MINIMA: int

class MaterialCreate(MaterialBase):
    pass  # La creación usa los mismos campos que MaterialBase

class MaterialOut(MaterialBase):
    ID: int  # Al devolver un material, también incluimos el ID
