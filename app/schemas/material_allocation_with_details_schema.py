# app/schemas/material_allocation_with_details_schema.py

from pydantic import BaseModel
from datetime import datetime

class MaterialAllocationWithDetailsOut(BaseModel):
    id: int  # ID de ASIGNACION_MATERIAL
    nombre_material: str  # Nombre de MATERIAL
    descripcion_material: str  # Descripción de MATERIAL
    cantidad_asignada: int  # Cantidad de ASIGNACION_MATERIAL
    cantidad_disponible: int  # Cantidad de MATERIAL
    fecha_flujo: datetime  # Fecha de FLUJO_MATERIAL

    class Config:
        from_atributes = True
