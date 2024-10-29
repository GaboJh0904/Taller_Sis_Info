# app/schemas/flow_tool_schema.py
from pydantic import BaseModel
from datetime import date
from enum import Enum

# Definimos un enum para los tipos de movimiento
class MovimientoEnum(str, Enum):
    entrada = 'entrada'
    salida = 'salida'

class FlowToolBase(BaseModel):
    CANTIDAD: int
    MOVIMIENTO: MovimientoEnum
    FECHA: date
    ALMACEN_ID: int
    HERRAMIENTA_ID: int

class FlowToolCreate(FlowToolBase):
    pass  # La creación usa los mismos campos que FlowToolBase

class FlowToolOut(FlowToolBase):
    ID: int  # Al devolver un flujo de herramienta, incluimos el ID
    ALMACEN: str
    HERRAMIENTA: str
