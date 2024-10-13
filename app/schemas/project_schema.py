# app/schemas/project_schema.py
from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class ProjectBase(BaseModel):
    NOMBRE: str
    DESCRIPCION: str
    CRONOGRAMA: str
    PRESUPUESTO_ASIGNADO: Decimal
    METAS_FINANCIERAS: Decimal
    ESTADO: str
    PRIORIDAD: str
    FECHA_INICIO: date
    FECHA_FIN: date
    ENCARGADO_PROYECTO_ID: int
    GERENTE_INVENTARIO_ID: int
    ENCARGADO_FINANZAS_ID: int

class ProjectCreate(ProjectBase):
    pass  # La creación usa los mismos campos que ProjectBase

class ProjectOut(ProjectBase):
    ID: int  # Al devolver un proyecto, también incluimos el ID
