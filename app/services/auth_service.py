# app/services/auth_service.py
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.core.config import settings
from app.schemas.user_schema import TokenData
from app.repositories.user_repository import get_employee_id_by_user_id
from app.db.connection import get_db_connection
import logging


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


def get_user_role(user_id: int) -> str:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener el EMPLEADO_ID del usuario
    cursor.execute("SELECT EMPLEADO_ID FROM USUARIO WHERE ID = %s", (user_id,))
    employee_result = cursor.fetchone()
    if not employee_result:
        return "employee"

    employee_id = employee_result["EMPLEADO_ID"]

    # Verificar roles específicos
    cursor.execute("SELECT 1 FROM ENCARGADO_ALMACEN WHERE EMPLEADO_ID = %s", (employee_id,))
    if cursor.fetchone():
        return "almacen_manager"

    cursor.execute("SELECT 1 FROM GERENTE_INVENTARIO WHERE USUARIO_ID = %s", (user_id,))
    if cursor.fetchone():
        return "admin"

    cursor.execute("SELECT 1 FROM ENCARGADO_PROYECTO WHERE USUARIO_ID = %s", (user_id,))
    if cursor.fetchone():
        return "project_manager"

    cursor.execute("SELECT 1 FROM ENCARGADO_FINANZAS WHERE USUARIO_ID = %s", (user_id,))
    if cursor.fetchone():
        return "finance_manager"

    # Rol predeterminado
    return "employee"


logger = logging.getLogger("app")

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        logger.info("Payload del token: %s", payload)  # Registra el payload
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return payload  # Retorna el payload completo
    except JWTError:
        logger.error("Error al decodificar el token", exc_info=True)  # Registra errores
        raise credentials_exception
    

logging.basicConfig(
    level=logging.INFO,  # Nivel de log: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  # Muestra logs en la consola
    ]
)

logger = logging.getLogger("app")  # Puedes personalizar el nombre del logger
