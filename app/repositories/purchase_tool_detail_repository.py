# app/repositories/purchase_tool_detail_repository.py
from app.db.connection import get_db_connection
from app.schemas.purchase_tool_detail_schema import PurchaseToolDetailOut, PurchaseToolDetailCreate

def get_purchase_tool_detail_by_id(detail_id: int) -> PurchaseToolDetailOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM DETALLE_COMPRA_HERRAMIENTA WHERE ID = %s", (detail_id,))
    purchase_tool_detail = cursor.fetchone()
    conn.close()

    if purchase_tool_detail:
        return PurchaseToolDetailOut(**purchase_tool_detail)
    return None

def get_all_purchase_tool_details() -> list[PurchaseToolDetailOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM DETALLE_COMPRA_HERRAMIENTA")
    purchase_tool_details = cursor.fetchall()
    conn.close()

    return [PurchaseToolDetailOut(**detail) for detail in purchase_tool_details]

def create_purchase_tool_detail(detail_data: PurchaseToolDetailCreate) -> PurchaseToolDetailOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO DETALLE_COMPRA_HERRAMIENTA 
           (COSTO, CANTIDAD, HERRAMIENTA_ID, COMPRA_HERRAMIENTA_ID)
           VALUES (%s, %s, %s, %s)""",
        (
            detail_data.COSTO, detail_data.CANTIDAD, detail_data.HERRAMIENTA_ID,
            detail_data.COMPRA_HERRAMIENTA_ID
        )
    )
    conn.commit()
    detail_id = cursor.lastrowid  # Get the generated ID
    conn.close()

    return PurchaseToolDetailOut(ID=detail_id, **detail_data.dict())

def update_purchase_tool_detail(detail_id: int, detail_data: PurchaseToolDetailCreate) -> PurchaseToolDetailOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE DETALLE_COMPRA_HERRAMIENTA SET 
           COSTO = %s, CANTIDAD = %s, HERRAMIENTA_ID = %s, COMPRA_HERRAMIENTA_ID = %s
           WHERE ID = %s""",
        (
            detail_data.COSTO, detail_data.CANTIDAD, detail_data.HERRAMIENTA_ID,
            detail_data.COMPRA_HERRAMIENTA_ID, detail_id
        )
    )
    conn.commit()
    conn.close()

    return PurchaseToolDetailOut(ID=detail_id, **detail_data.dict())

def delete_purchase_tool_detail(detail_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM DETALLE_COMPRA_HERRAMIENTA WHERE ID = %s", (detail_id,))
    conn.commit()
    conn.close()
