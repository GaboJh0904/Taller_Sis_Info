# app/schemas/flow_material_schema.py
from pydantic import BaseModel
from datetime import date
from enum import Enum

# Definimos un enum para los tipos de movimiento
class MovimientoEnum(str, Enum):
    entrada = 'entrada'
    salida = 'salida'

class FlowMaterialBase(BaseModel):
    MATERIAL_ID: int
    ALMACEN_ID: int
    CANTIDAD: int
    MOVIMIENTO: MovimientoEnum
    FECHA: date

class FlowMaterialCreate(FlowMaterialBase):
    pass  # La creación usa los mismos campos que FlowMaterialBase

class FlowMaterialOut(FlowMaterialBase):
    ID: int  # Al devolver un flujo de material, incluimos el ID
