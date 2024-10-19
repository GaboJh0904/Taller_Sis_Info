from app.db.connection import get_db_connection
from app.schemas.material_allocation_schema import MaterialAllocationOut, MaterialAllocationCreate

def get_material_allocation_by_id(material_allocation_id: int) -> MaterialAllocationOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ASIGNACION_MATERIAL WHERE ID = %s", (material_allocation_id,))
    material_allocation = cursor.fetchone()
    conn.close()

    if material_allocation:
        return MaterialAllocationOut(**material_allocation)
    return None

def get_all_material_allocations() -> list[MaterialAllocationOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ASIGNACION_MATERIAL")
    material_allocations = cursor.fetchall()
    conn.close()

    return [MaterialAllocationOut(**material_allocation) for material_allocation in material_allocations]

def create_material_allocation(material_allocation_data: MaterialAllocationCreate) -> MaterialAllocationOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO ASIGNACION_MATERIAL (FLUJO_MATERIAL_ID, PROYECTO_ID, CANTIDAD) 
           VALUES (%s, %s, %s)""",
        (material_allocation_data.FLUJO_MATERIAL_ID, material_allocation_data.PROYECTO_ID, material_allocation_data.CANTIDAD)
    )
    conn.commit()
    material_allocation_id = cursor.lastrowid
    conn.close()

    return MaterialAllocationOut(ID=material_allocation_id, **material_allocation_data.dict())

def update_material_allocation(material_allocation_id: int, material_allocation_data: MaterialAllocationCreate) -> MaterialAllocationOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE ASIGNACION_MATERIAL SET 
           FLUJO_MATERIAL_ID = %s, PROYECTO_ID = %s, CANTIDAD = %s 
           WHERE ID = %s""",
        (material_allocation_data.FLUJO_MATERIAL_ID, material_allocation_data.PROYECTO_ID, material_allocation_data.CANTIDAD, material_allocation_id)
    )
    conn.commit()
    conn.close()

    return MaterialAllocationOut(ID=material_allocation_id, **material_allocation_data.dict())

def delete_material_allocation(material_allocation_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ASIGNACION_MATERIAL WHERE ID = %s", (material_allocation_id,))
    conn.commit()
    conn.close()
