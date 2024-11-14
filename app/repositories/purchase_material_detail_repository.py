# app/repositories/purchase_material_detail_repository.py
from app.db.connection import get_db_connection
from app.schemas.purchase_material_detail_schema import PurchaseDetailOut, PurchaseDetailCreate

def get_purchase_detail_by_id(detail_id: int) -> PurchaseDetailOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM DETALLE_COMPRA_MATERIAL WHERE ID = %s", (detail_id,))
    purchase_detail = cursor.fetchone()
    conn.close()

    if purchase_detail:
        return PurchaseDetailOut(**purchase_detail)
    return None

def get_all_purchase_details() -> list[PurchaseDetailOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM DETALLE_COMPRA_MATERIAL")
    purchase_details = cursor.fetchall()
    conn.close()

    return [PurchaseDetailOut(**detail) for detail in purchase_details]

def create_purchase_detail(detail_data: PurchaseDetailCreate) -> PurchaseDetailOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO DETALLE_COMPRA_MATERIAL 
           (COSTO, CANTIDAD, MATERIAL_ID, COMPRA_MATERIAL_ID)
           VALUES (%s, %s, %s, %s)""",
        (
            detail_data.COSTO, detail_data.CANTIDAD, detail_data.MATERIAL_ID,
            detail_data.COMPRA_MATERIAL_ID
        )
    )
    conn.commit()
    detail_id = cursor.lastrowid  # Get the generated ID
    conn.close()

    return PurchaseDetailOut(ID=detail_id, **detail_data.dict())

def update_purchase_detail(detail_id: int, detail_data: PurchaseDetailCreate) -> PurchaseDetailOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE DETALLE_COMPRA_MATERIAL SET 
           COSTO = %s, CANTIDAD = %s, MATERIAL_ID = %s, COMPRA_MATERIAL_ID = %s
           WHERE ID = %s""",
        (
            detail_data.COSTO, detail_data.CANTIDAD, detail_data.MATERIAL_ID,
            detail_data.COMPRA_MATERIAL_ID, detail_id
        )
    )
    conn.commit()
    conn.close()

    return PurchaseDetailOut(ID=detail_id, **detail_data.dict())

def delete_purchase_detail(detail_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM DETALLE_COMPRA_MATERIAL WHERE ID = %s", (detail_id,))
    conn.commit()
    conn.close()
