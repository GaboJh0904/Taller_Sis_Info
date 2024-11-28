from pydantic import BaseModel
from datetime import date

class AlmacenBase(BaseModel):
    ubicacion: str
    fecha_actualizacion: date
    encargado_almacen_id: int

class AlmacenCreate(AlmacenBase):
    pass

class AlmacenOut(AlmacenBase):
    id: int

    class Config:
        orm_mode = True