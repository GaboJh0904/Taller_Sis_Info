# app/schemas/tool_schema.py
from pydantic import BaseModel

class ToolBase(BaseModel):
    NOMBRE: str
    DESCRIPCION: str
    CANTIDAD: int
    PRECIO_UNITARIO: int
    CANTIDAD_MINIMA: int

class ToolCreate(ToolBase):
    pass  # La creación usa los mismos campos que ToolBase

class ToolOut(ToolBase):
    ID: int  # Al devolver una herramienta, también incluimos el ID
