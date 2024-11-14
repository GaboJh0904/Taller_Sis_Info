# app/repositories/purchase_tool_repository.py
from app.db.connection import get_db_connection
from app.schemas.purchase_tool_schema import PurchaseToolOut, PurchaseToolCreate

def get_purchase_tool_by_id(purchase_id: int) -> PurchaseToolOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM COMPRA_HERRAMIENTA WHERE ID = %s", (purchase_id,))
    purchase_tool = cursor.fetchone()
    conn.close()

    if purchase_tool:
        return PurchaseToolOut(**purchase_tool)
    return None

def get_all_purchase_tools() -> list[PurchaseToolOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM COMPRA_HERRAMIENTA")
    purchase_tools = cursor.fetchall()
    conn.close()

    return [PurchaseToolOut(**tool) for tool in purchase_tools]

def create_purchase_tool(tool_data: PurchaseToolCreate) -> PurchaseToolOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO COMPRA_HERRAMIENTA 
           (COSTO_TOTAL, FECHA, PROVEEDOR_ID, DETALLE)
           VALUES (%s, %s, %s, %s)""",
        (
            tool_data.COSTO_TOTAL, tool_data.FECHA, tool_data.PROVEEDOR_ID,
            tool_data.DETALLE
        )
    )
    conn.commit()
    purchase_id = cursor.lastrowid  # Get the generated ID
    conn.close()

    return PurchaseToolOut(ID=purchase_id, **tool_data.dict())

def update_purchase_tool(purchase_id: int, tool_data: PurchaseToolCreate) -> PurchaseToolOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE COMPRA_HERRAMIENTA SET 
           COSTO_TOTAL = %s, FECHA = %s, PROVEEDOR_ID = %s, DETALLE = %s
           WHERE ID = %s""",
        (
            tool_data.COSTO_TOTAL, tool_data.FECHA, tool_data.PROVEEDOR_ID,
            tool_data.DETALLE, purchase_id
        )
    )
    conn.commit()
    conn.close()

    return PurchaseToolOut(ID=purchase_id, **tool_data.dict())

def delete_purchase_tool(purchase_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM COMPRA_HERRAMIENTA WHERE ID = %s", (purchase_id,))
    conn.commit()
    conn.close()
