# app/repositories/purchase_material_repository.py
from app.db.connection import get_db_connection
from app.schemas.purchase_material_schema import PurchaseMaterialOut, PurchaseMaterialCreate

def get_purchase_material_by_id(purchase_id: int) -> PurchaseMaterialOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM COMPRA_MATERIAL WHERE ID = %s", (purchase_id,))
    purchase_material = cursor.fetchone()
    conn.close()

    if purchase_material:
        return PurchaseMaterialOut(**purchase_material)
    return None

def get_all_purchase_materials() -> list[PurchaseMaterialOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM COMPRA_MATERIAL")
    purchase_materials = cursor.fetchall()
    conn.close()

    return [PurchaseMaterialOut(**purchase) for purchase in purchase_materials]

def create_purchase_material(purchase_data: PurchaseMaterialCreate) -> PurchaseMaterialOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO COMPRA_MATERIAL 
           (COSTO_TOTAL, FECHA, PROVEEDOR_ID, DETALLE)
           VALUES (%s, %s, %s, %s)""",
        (
            purchase_data.COSTO_TOTAL, purchase_data.FECHA, purchase_data.PROVEEDOR_ID,
            purchase_data.DETALLE
        )
    )
    conn.commit()
    purchase_id = cursor.lastrowid  # Get the generated ID
    conn.close()

    return PurchaseMaterialOut(ID=purchase_id, **purchase_data.dict())

def update_purchase_material(purchase_id: int, purchase_data: PurchaseMaterialCreate) -> PurchaseMaterialOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE COMPRA_MATERIAL SET 
           COSTO_TOTAL = %s, FECHA = %s, PROVEEDOR_ID = %s, DETALLE = %s
           WHERE ID = %s""",
        (
            purchase_data.COSTO_TOTAL, purchase_data.FECHA, purchase_data.PROVEEDOR_ID,
            purchase_data.DETALLE, purchase_id
        )
    )
    conn.commit()
    conn.close()

    return PurchaseMaterialOut(ID=purchase_id, **purchase_data.dict())

def delete_purchase_material(purchase_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM COMPRA_MATERIAL WHERE ID = %s", (purchase_id,))
    conn.commit()
    conn.close()
