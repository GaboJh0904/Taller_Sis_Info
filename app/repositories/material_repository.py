# app/repositories/material_repository.py
from app.db.connection import get_db_connection
from app.schemas.material_schema import MaterialOut, MaterialCreate


def get_material_by_id(material_id: int) -> MaterialOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MATERIAL WHERE ID = %s", (material_id,))
    material = cursor.fetchone()
    conn.close()

    if material:
        return MaterialOut(**material)
    return None


def get_all_materials() -> list[MaterialOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MATERIAL")
    materials = cursor.fetchall()
    conn.close()

    return [MaterialOut(**material) for material in materials]


def create_material(material_data: MaterialCreate) -> MaterialOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO MATERIAL 
           (NOMBRE, DESCRIPCION, CANTIDAD, PRECIO_UNITARIO, PROVEEDOR_ID, CANTIDAD_MINIMA)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (
            material_data.NOMBRE, material_data.DESCRIPCION, material_data.CANTIDAD,
            material_data.PRECIO_UNITARIO, material_data.PROVEEDOR_ID, material_data.CANTIDAD_MINIMA
        )
    )
    conn.commit()
    material_id = cursor.lastrowid  # Obtenemos el ID generado
    conn.close()

    return MaterialOut(ID=material_id, **material_data.dict())


def update_material(material_id: int, material_data: MaterialCreate) -> MaterialOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE MATERIAL SET 
           NOMBRE = %s, DESCRIPCION = %s, CANTIDAD = %s, PRECIO_UNITARIO = %s, 
           PROVEEDOR_ID = %s, CANTIDAD_MINIMA = %s 
           WHERE ID = %s""",
        (
            material_data.NOMBRE, material_data.DESCRIPCION, material_data.CANTIDAD,
            material_data.PRECIO_UNITARIO, material_data.PROVEEDOR_ID, material_data.CANTIDAD_MINIMA,
            material_id
        )
    )
    conn.commit()
    conn.close()

    return MaterialOut(ID=material_id, **material_data.dict())


def delete_material(material_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM MATERIAL WHERE ID = %s", (material_id,))
    conn.commit()
    conn.close()
