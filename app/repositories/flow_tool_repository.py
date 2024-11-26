# app/repositories/flow_tool_repository.py
from app.db.connection import get_db_connection
from app.schemas.flow_tool_schema import FlowToolOut, FlowToolCreate


def get_flow_tool_by_id(flow_tool_id: int) -> FlowToolOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
    SELECT 
        FH.*,
        A.UBICACION AS ALMACEN,
        H.NOMBRE AS HERRAMIENTA
    FROM 
        FLUJO_HERRAMIENTA FH
    JOIN 
        ALMACEN A ON FH.ALMACEN_ID = A.ID
    JOIN 
        HERRAMIENTA H ON FH.HERRAMIENTA_ID = H.ID
    WHERE ID = %s;
    ''', (flow_tool_id,))
    flow_tool = cursor.fetchone()
    conn.close()

    if flow_tool:
        return FlowToolOut(**flow_tool)
    return None


def get_all_flow_tools() -> list[FlowToolOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
    SELECT 
        FH.*,
        A.UBICACION AS ALMACEN,
        H.NOMBRE AS HERRAMIENTA
    FROM 
        FLUJO_HERRAMIENTA FH
    JOIN 
        ALMACEN A ON FH.ALMACEN_ID = A.ID
    JOIN 
        HERRAMIENTA H ON FH.HERRAMIENTA_ID = H.ID;

    ''')
    flow_tools = cursor.fetchall()
    conn.close()

    return [FlowToolOut(**flow_tool) for flow_tool in flow_tools]


def create_flow_tool(flow_tool_data: FlowToolCreate) -> FlowToolOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO FLUJO_HERRAMIENTA 
           (CANTIDAD, MOVIMIENTO, FECHA, ALMACEN_ID, HERRAMIENTA_ID)
           VALUES (%s, %s, %s, %s, %s)""",
        (
            flow_tool_data.CANTIDAD, flow_tool_data.MOVIMIENTO, flow_tool_data.FECHA,
            flow_tool_data.ALMACEN_ID, flow_tool_data.HERRAMIENTA_ID
        )
    )
    conn.commit()
    flow_tool_id = cursor.lastrowid  # Obtenemos el ID generado
    conn.close()

    return FlowToolOut(ID=flow_tool_id,HERRAMIENTA='',ALMACEN='', **flow_tool_data.dict())


def update_flow_tool(flow_tool_id: int, flow_tool_data: FlowToolCreate) -> FlowToolOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE FLUJO_HERRAMIENTA SET 
           CANTIDAD = %s, MOVIMIENTO = %s, FECHA = %s, ALMACEN_ID = %s, HERRAMIENTA_ID = %s 
           WHERE ID = %s""",
        (
            flow_tool_data.CANTIDAD, flow_tool_data.MOVIMIENTO, flow_tool_data.FECHA,
            flow_tool_data.ALMACEN_ID, flow_tool_data.HERRAMIENTA_ID,
            flow_tool_id
        )
    )
    conn.commit()
    conn.close()

    return FlowToolOut(ID=flow_tool_id, **flow_tool_data.dict())


def delete_flow_tool(flow_tool_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM FLUJO_HERRAMIENTA WHERE ID = %s", (flow_tool_id,))
    conn.commit()
    conn.close()


from datetime import date

class FlowToolRepository:
    @staticmethod
    def get_flows_by_tool_and_date_range(item_id: int, start_date: date, end_date: date):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = """
                SELECT * FROM FLUJO_HERRAMIENTA
                WHERE HERRAMIENTA_ID = %s AND FECHA BETWEEN %s AND %s
            """
            cursor.execute(sql, (item_id, start_date, end_date))
            rows = cursor.fetchall()
            return [FlowToolOut(**row) for row in rows] 