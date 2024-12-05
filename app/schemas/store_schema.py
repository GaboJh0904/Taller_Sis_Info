from pydantic import BaseModel
from datetime import date

class AlmacenBase(BaseModel):
    UBICACION: str
    FECHA_ACTUALIZACION: date
    ENCARGADO_ALMACEN_ID: int

class AlmacenCreate(AlmacenBase):
    pass

class AlmacenOut(AlmacenBase):
    ID: int

    class Config:
        from_atributes = True