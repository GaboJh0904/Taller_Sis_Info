# app/schemas/tool_allocation_schema.py
from pydantic import BaseModel

class ToolAllocationBase(BaseModel):
    CANTIDAD: int
    FLUJO_HERRAMIENTA_ID: int
    PROYECTO_ID: int
    FASE: str

class ToolAllocationCreate(ToolAllocationBase):
    pass  # La creación usa los mismos campos que ToolAllocationBase

class ToolAllocationOut(ToolAllocationBase):
    ID: int  # Al devolver una asignación, también incluimos el ID