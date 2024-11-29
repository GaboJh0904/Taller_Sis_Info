# app/repositories/almacen_repository.py
from app.db.connection import get_db_connection
from app.schemas.store_schema import AlmacenOut, AlmacenCreate


def get_almacen_by_id(almacen_id: int) -> AlmacenOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ALMACEN WHERE ID = %s", (almacen_id,))
    almacen = cursor.fetchone()
    conn.close()

    if almacen:
        return AlmacenOut(**almacen)
    return None


def get_all_almacenes() -> list[AlmacenOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ALMACEN")
    almacenes = cursor.fetchall()
    conn.close()

    print([almacen for almacen in almacenes])
    return [AlmacenOut(**almacen) for almacen in almacenes]


def create_almacen(almacen_data: AlmacenCreate) -> AlmacenOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO ALMACEN (UBICACION, FECHA_ACTUALIZACION, ENCARGADO_ALMACEN_ID) 
           VALUES (%s, %s, %s)""",
        (
            almacen_data.UBICACION,
            almacen_data.FECHA_ACTUALIZACION,
            almacen_data.ENCARGADO_ALMACEN_ID
        )
    )
    conn.commit()
    almacen_id = cursor.lastrowid  
    conn.close()
    return AlmacenOut(ID=almacen_id, **almacen_data.dict())


def update_almacen(almacen_id: int, almacen_data: AlmacenCreate) -> AlmacenOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE ALMACEN SET 
           UBICACION = %s, FECHA_ACTUALIZACION = %s, ENCARGADO_ALMACEN_ID = %s 
           WHERE ID = %s""",
        (
            almacen_data.UBICACION,
            almacen_data.FECHA_ACTUALIZACION,
            almacen_data.ENCARGADO_ALMACEN_ID,
            almacen_id
        )
    )
    conn.commit()
    conn.close()

    return AlmacenOut(ID=almacen_id, **almacen_data.dict())


def delete_almacen(almacen_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ALMACEN WHERE ID = %s", (almacen_id,))
    conn.commit()
    conn.close()
