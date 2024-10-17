# app/schemas/surplus_project_schema.py
from pydantic import BaseModel

class SurplusBase(BaseModel):
    CANTIDAD: int
    ASIGNACION_MATERIAL_ID: int

class SurplusCreate(SurplusBase):
    pass  # La creación usa los mismos campos que SurplusBase

class SurplusOut(SurplusBase):
    ID: int  # Al devolver un sobrante, también incluimos el ID