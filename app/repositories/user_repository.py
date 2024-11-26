# app/repositories/user_repository.py
from app.db.connection import get_db_connection
from app.schemas.user_schema import UserOut, UserCreate


def get_user_by_username(username: str) -> UserOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USUARIO WHERE USER_NAME = %s", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return UserOut(**user)
    return None


def get_user_by_id(user_id: int) -> UserOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USUARIO WHERE ID = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return UserOut(**user)
    return None


def get_all_users() -> list[UserOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USUARIO")
    users = cursor.fetchall()
    conn.close()

    return [UserOut(**user) for user in users]


def create_user(user_data: UserCreate) -> UserOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO USUARIO (USER_NAME, EMAIL, PASSWOR_HASH, EMPLEADO_ID) VALUES (%s, %s, %s, %s)",
        (user_data.USER_NAME, user_data.EMAIL, user_data.PASSWOR_HASH, user_data.EMPLEADO_ID)
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    return UserOut(
        ID=user_id,
        USER_NAME=user_data.USER_NAME,
        EMAIL=user_data.EMAIL,
        EMPLEADO_ID=user_data.EMPLEADO_ID
    )


def update_user(user_id: int, user_data: UserCreate) -> UserOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE USUARIO SET USER_NAME = %s, EMAIL = %s, PASSWOR_HASH = %s, EMPLEADO_ID = %s WHERE ID = %s",
        (user_data.USER_NAME, user_data.EMAIL, user_data.PASSWOR_HASH, user_data.EMPLEADO_ID, user_id)
    )
    conn.commit()
    conn.close()

    return UserOut(
        ID=user_id,
        USER_NAME=user_data.USER_NAME,
        EMAIL=user_data.EMAIL,
        EMPLEADO_ID=user_data.EMPLEADO_ID
    )


def delete_user(user_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USUARIO WHERE ID = %s", (user_id,))
    conn.commit()
    conn.close()


def get_employee_id_by_user_id(user_id: int) -> int | None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT EMPLEADO_ID FROM USUARIO WHERE ID = %s", (user_id,))
    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None
