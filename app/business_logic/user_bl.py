# app/services/user_bl.py
from app.repositories.user_repository import (
    create_user, get_user_by_username, get_user_by_id, get_all_users, update_user, delete_user
)
from app.schemas.user_schema import UserCreate, UserOut
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserBL:

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verifica si la contraseña en texto plano coincide con el hash almacenado."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def hash_password(password: str) -> str:
        """Genera el hash de una contraseña."""
        return pwd_context.hash(password)

    @staticmethod
    def create_new_user(user_data: UserCreate) -> UserOut:
        # Verificar si ya existe el usuario
        existing_user = get_user_by_username(user_data.USER_NAME)
        if existing_user:
            raise ValueError("Username already registered")

        # Hashear la contraseña antes de crear el usuario
        hashed_password = UserBL.hash_password(user_data.PASSWOR_HASH)
        user_data.PASSWOR_HASH = hashed_password

        # Crear el nuevo usuario
        return create_user(user_data)

    @staticmethod
    def get_user(user_id: int) -> UserOut:
        user = get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def get_all_users() -> list[UserOut]:
        return get_all_users()

    @staticmethod
    def update_existing_user(user_id: int, user_data: UserCreate) -> UserOut:
        user = get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        # Hashear la nueva contraseña antes de actualizar el usuario
        hashed_password = UserBL.hash_password(user_data.PASSWOR_HASH)
        user_data.PASSWOR_HASH = hashed_password

        return update_user(user_id, user_data)

    @staticmethod
    def delete_user(user_id: int) -> None:
        user = get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        delete_user(user_id)
