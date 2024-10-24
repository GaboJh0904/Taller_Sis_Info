# app/schemas/user_schema.py
from pydantic import BaseModel

class UserBase(BaseModel):
    USER_NAME: str
    EMAIL: str
    EMPLEADO_ID: int

class UserCreate(UserBase):
    PASSWOR_HASH: str

class UserOut(UserBase):
    ID: int
    PASSWOR_HASH: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    USER_NAME: str | None = None
