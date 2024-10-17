from app.db.connection import get_db_connection
from app.schemas.used_material_schema import UsoMaterialOut, UsoMaterialCreate

def get_used_material_by_id(used_material_id: int) -> UsoMaterialOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USO_MATERIAL WHERE ID = %s", (used_material_id,))
    used_material = cursor.fetchone()
    conn.close()

    if used_material:
        return UsoMaterialOut(**used_material)
    return None

def get_all_used_materials() -> list[UsoMaterialOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USO_MATERIAL")
    used_materials = cursor.fetchall()
    conn.close()

    return [UsoMaterialOut(**used_material) for used_material in used_materials]

def create_used_material(used_material_data: UsoMaterialCreate) -> UsoMaterialOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO USO_MATERIAL (ASIGNACION_MATERIAL_ID, CANTIDAD, FECHA, DETALLE) 
           VALUES (%s, %s, %s, %s)""",
        (used_material_data.ASIGNACION_MATERIAL_ID, used_material_data.CANTIDAD, used_material_data.FECHA, used_material_data.DETALLE)
    )
    conn.commit()
    used_material_id = cursor.lastrowid
    conn.close()

    return UsoMaterialOut(ID=used_material_id, **used_material_data.dict())

def update_used_material(used_material_id: int, used_material_data: UsoMaterialCreate) -> UsoMaterialOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE USO_MATERIAL SET 
           ASIGNACION_MATERIAL_ID = %s, CANTIDAD = %s, FECHA = %s, DETALLE = %s 
           WHERE ID = %s""",
        (used_material_data.ASIGNACION_MATERIAL_ID, used_material_data.CANTIDAD, used_material_data.FECHA, used_material_data.DETALLE, used_material_id)
    )
    conn.commit()
    conn.close()

    return UsoMaterialOut(ID=used_material_id, **used_material_data.dict())

def delete_used_material(used_material_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USO_MATERIAL WHERE ID = %s", (used_material_id,))
    conn.commit()
    conn.close()
