from app.db.connection import get_db_connection
from app.schemas.surplus_project_schema import SobranteProyectoOut, SobranteProyectoCreate

def get_surplus_by_id(surplus_id: int) -> SobranteProyectoOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM SOBRANTE_PROYECTO WHERE ID = %s", (surplus_id,))
    surplus = cursor.fetchone()
    conn.close()

    if surplus:
        return SobranteProyectoOut(**surplus)
    return None

def get_all_surpluses() -> list[SobranteProyectoOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM SOBRANTE_PROYECTO")
    surpluses = cursor.fetchall()
    conn.close()

    return [SobranteProyectoOut(**surplus) for surplus in surpluses]

def create_surplus(surplus_data: SobranteProyectoCreate) -> SobranteProyectoOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO SOBRANTE_PROYECTO (CANTIDAD, ASIGNACION_MATERIAL_ID) 
           VALUES (%s, %s)""",
        (surplus_data.CANTIDAD, surplus_data.ASIGNACION_MATERIAL_ID)
    )
    conn.commit()
    surplus_id = cursor.lastrowid
    conn.close()

    return SobranteProyectoOut(ID=surplus_id, **surplus_data.dict())

def update_surplus(surplus_id: int, surplus_data: SobranteProyectoCreate) -> SobranteProyectoOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE SOBRANTE_PROYECTO SET 
           CANTIDAD = %s, ASIGNACION_MATERIAL_ID = %s 
           WHERE ID = %s""",
        (surplus_data.CANTIDAD, surplus_data.ASIGNACION_MATERIAL_ID, surplus_id)
    )
    conn.commit()
    conn.close()

    return SobranteProyectoOut(ID=surplus_id, **surplus_data.dict())

def delete_surplus(surplus_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SOBRANTE_PROYECTO WHERE ID = %s", (surplus_id,))
    conn.commit()
    conn.close()
