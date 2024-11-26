# app/schemas/provider_schema.py
from pydantic import BaseModel

class ProviderBase(BaseModel):
    NOMBRE: str
    DIRECCION: str
    TELEFONO: str

class ProviderCreate(ProviderBase):
    pass  # Creation uses the same fields as ProviderBase

class ProviderOut(ProviderBase):
    ID: int  # Include ID when returning a provider
