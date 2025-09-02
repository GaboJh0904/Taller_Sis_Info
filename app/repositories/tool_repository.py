# app/repositories/tool_repository.py
from app.db.connection import get_db_connection
from app.schemas.tool_schema import ToolOut, ToolCreate


def get_tool_by_id(tool_id: int) -> ToolOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM HERRAMIENTA WHERE ID = %s", (tool_id,))
    tool = cursor.fetchone()
    conn.close()

    if tool:
        return ToolOut(**tool)
    return None


def update_tool_quantity(tool_id: int, new_quantity: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE HERRAMIENTA SET CANTIDAD = %s WHERE ID = %s", (new_quantity, tool_id))
    conn.commit()
    conn.close()


def get_all_tools() -> list[ToolOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM HERRAMIENTA")
    tools = cursor.fetchall()
    conn.close()

    return [ToolOut(**tool) for tool in tools]


def create_tool(tool_data: ToolCreate) -> ToolOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO HERRAMIENTA 
           (NOMBRE, DESCRIPCION, CANTIDAD, PRECIO_UNITARIO, CANTIDAD_MINIMA)
           VALUES (%s, %s, %s, %s, %s)""",
        (
            tool_data.NOMBRE, tool_data.DESCRIPCION, tool_data.CANTIDAD,
            tool_data.PRECIO_UNITARIO, tool_data.CANTIDAD_MINIMA
        )
    )
    conn.commit()
    tool_id = cursor.lastrowid  # Obtenemos el ID generado
    conn.close()

    return ToolOut(ID=tool_id, **tool_data.dict())


def update_tool(tool_id: int, tool_data: ToolCreate) -> ToolOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE HERRAMIENTA SET 
           NOMBRE = %s, DESCRIPCION = %s, CANTIDAD = %s, PRECIO_UNITARIO = %s, 
           CANTIDAD_MINIMA = %s 
           WHERE ID = %s""",
        (
            tool_data.NOMBRE, tool_data.DESCRIPCION, tool_data.CANTIDAD,
            tool_data.PRECIO_UNITARIO, tool_data.CANTIDAD_MINIMA,
            tool_id
        )
    )
    conn.commit()
    conn.close()

    return ToolOut(ID=tool_id, **tool_data.dict())


def delete_tool(tool_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM HERRAMIENTA WHERE ID = %s", (tool_id,))
    conn.commit()
    conn.close()


def get_low_stock_tools() -> list[ToolOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM HERRAMIENTA WHERE CANTIDAD <= CANTIDAD_MINIMA")
    tools = cursor.fetchall()
    conn.close()

    return [ToolOut(**tool) for tool in tools]
