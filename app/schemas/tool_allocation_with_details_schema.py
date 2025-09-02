# app/schemas/herramienta_allocation_with_details_schema.py

from pydantic import BaseModel
from datetime import datetime

class ToolAllocationWithDetailsOut(BaseModel):
    id: int  # ID de ASIGNACION_HERRAMIENTA
    nombre_herramienta: str  # Nombre de HERRAMIENTA
    descripcion_herramienta: str  # Descripción de HERRAMIENTA
    cantidad_asignada: int  # Cantidad de ASIGNACION_HERRAMIENTA
    cantidad_disponible: int  # Cantidad de HERRAMIENTA
    fecha_flujo: datetime  # Fecha de FLUJO_HERRAMIENTA

    class Config:
        from_atributes = True
