# app/api/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.services.auth_service import create_access_token, verify_token
from app.repositories.user_repository import get_user_by_username
from app.schemas.user_schema import Token, TokenData, UserOut  # Added UserOut
from passlib.context import CryptContext
from jose import JWTError  # Added JWTError

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

@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.USER_NAME})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserOut:
    """
    Retrieve the current authenticated user based on the token.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Use verify_token to validate the token and extract user information
        token_data = verify_token(token, credentials_exception)
        user = get_user_by_username(token_data.USER_NAME)
        if user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user
