from app.db.connection import get_db_connection
from app.schemas.surplus_project_schema import SurplusOut, SurplusCreate

def get_surplus_by_id(surplus_id: int) -> SurplusOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM SOBRANTE_PROYECTO WHERE ID = %s", (surplus_id,))
    surplus = cursor.fetchone()
    conn.close()

    if surplus:
        return SurplusOut(**surplus)
    return None

def get_all_surpluses() -> list[SurplusOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM SOBRANTE_PROYECTO")
    surpluses = cursor.fetchall()
    conn.close()

    return [SurplusOut(**surplus) for surplus in surpluses]

def create_surplus(surplus_data: SurplusCreate) -> SurplusOut:
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

    return SurplusOut(ID=surplus_id, **surplus_data.dict())

def update_surplus(surplus_id: int, surplus_data: SurplusCreate) -> SurplusOut:
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

    return SurplusOut(ID=surplus_id, **surplus_data.dict())

def delete_surplus(surplus_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SOBRANTE_PROYECTO WHERE ID = %s", (surplus_id,))
    conn.commit()
    conn.close()

def get_surplus_project_by_material_allocation(material_allocation_id: int) -> list[SurplusOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # print(f"Fetching allocations for project ID: {material_allocation_id}")
    cursor.execute("SELECT * FROM SOBRANTE_PROYECTO WHERE ASIGNACION_MATERIAL_ID = %s", (material_allocation_id,))
    allocations = cursor.fetchall()
    # print(allocations)
    conn.close()

    return [SurplusOut(**allocation) for allocation in allocations]