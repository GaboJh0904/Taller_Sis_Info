# app/repositories/provider_repository.py
from app.db.connection import get_db_connection
from app.schemas.provider_schema import ProviderOut, ProviderCreate

def fetch_provider_by_id(provider_id: int) -> ProviderOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PROVEEDOR WHERE ID = %s", (provider_id,))
    provider = cursor.fetchone()
    conn.close()

    if provider:
        return ProviderOut(**provider)
    return None

def fetch_all_providers() -> list[ProviderOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PROVEEDOR")
    providers = cursor.fetchall()
    conn.close()

    return [ProviderOut(**provider) for provider in providers]

def insert_provider(provider_data: ProviderCreate) -> ProviderOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO PROVEEDOR 
           (NOMBRE, DIRECCION, TELEFONO)
           VALUES (%s, %s, %s)""",
        (provider_data.NOMBRE, provider_data.DIRECCION, provider_data.TELEFONO)
    )
    conn.commit()
    provider_id = cursor.lastrowid  # Get the generated ID
    conn.close()

    return ProviderOut(ID=provider_id, **provider_data.dict())

def update_provider(provider_id: int, provider_data: ProviderCreate) -> ProviderOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE PROVEEDOR SET 
           NOMBRE = %s, DIRECCION = %s, TELEFONO = %s
           WHERE ID = %s""",
        (provider_data.NOMBRE, provider_data.DIRECCION, provider_data.TELEFONO, provider_id)
    )
    conn.commit()
    conn.close()

    return ProviderOut(ID=provider_id, **provider_data.dict())

def delete_provider(provider_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PROVEEDOR WHERE ID = %s", (provider_id,))
    conn.commit()
    conn.close()
