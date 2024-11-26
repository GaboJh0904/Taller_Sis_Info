# app/schemas/project_schema.py

from pydantic import BaseModel
from datetime import date
from typing import List

class ProjectCreate(BaseModel):
    NOMBRE: str
    DESCRIPCION: str
    CRONOGRAMA: str
    PRESUPUESTO_ASIGNADO: float
    METAS_FINANCIERAS: str
    ESTADO: str
    PRIORIDAD: str
    FECHA_INICIO: date
    FECHA_FIN: date
    ENCARGADO_PROYECTO_ID: int
    GERENTE_INVENTARIO_ID: int
    ENCARGADO_FINANZAS_ID: int

class ProjectOut(ProjectCreate):
    ID: int

class ProjectCompletionOut(BaseModel):
    project_id: int
    project_name: str
    completion_percentage: float  # value between 0 and 100
    start_date: date
    end_date: date
    current_date: date

class ResourceUtilizationEntry(BaseModel):
    resource_type: str
    utilization_rate: float

class ResourceUtilizationOut(BaseModel):
    project_id: int
    project_name: str
    resource_utilization: List[ResourceUtilizationEntry]
