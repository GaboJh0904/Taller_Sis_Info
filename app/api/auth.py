# app/api/auth.py
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.config import settings
from app.services.auth_service import create_access_token, verify_token
from app.repositories.user_repository import get_user_by_username
from app.schemas.user_schema import Token, TokenData, UserOut  # Added UserOut
from passlib.context import CryptContext
from jose import JWTError, jwt # Added JWTError


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(USER_NAME=username)
    except JWTError:
        raise credentials_exception
    return token_data

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.services.auth_service import create_access_token, verify_token, get_user_role
from app.repositories.user_repository import get_user_by_username
from app.schemas.user_schema import Token
from passlib.context import CryptContext

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # Kept the original tokenUrl
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user:
        return False
    if not verify_password(password, user.PASSWOR_HASH):
        return False
    return user


def get_current_user(required_role: str = None, token: str = Depends(oauth2_scheme)):
    payload = verify_token(token, credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
    ))
    role = payload.get("role")
    if required_role and required_role != '' and role != required_role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have enough permissions",
        )
    return get_user_by_username(payload.get("sub"))



from functools import partial

get_admin_user = partial(get_current_user, required_role="admin")
get_project_manager_user = partial(get_current_user, required_role="project_manager")
get_finance_manager_user = partial(get_current_user, required_role="finance_manager")
get_employee_user = partial(get_current_user, required_role="employee")



@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Obtener el rol del usuario
    role = get_user_role(user.ID)

    # Crear el token con el rol
    access_token = create_access_token(data={"sub": user.USER_NAME, "role": role})
    return {"access_token": access_token, "token_type": "bearer"}
