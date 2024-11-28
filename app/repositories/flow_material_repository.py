# app/repositories/flow_material_repository.py
from app.db.connection import get_db_connection
from app.schemas.flow_material_schema import FlowMaterialOut, FlowMaterialCreate


def get_flow_material_by_id(flow_material_id: int) -> FlowMaterialOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
    SELECT 
    FM.*,
    A.UBICACION AS ALMACEN,
    M.NOMBRE AS MATERIAL
    FROM 
        FLUJO_MATERIAL FM
    JOIN 
        ALMACEN A ON FM.ALMACEN_ID = A.ID
    JOIN 
        MATERIAL M ON FM.MATERIAL_ID = M.ID 
    WHERE FM.ID = %s;
    ''', (flow_material_id,))
    flow_material = cursor.fetchone()
    conn.close()

    if flow_material:
        return FlowMaterialOut(**flow_material)
    return None


def get_all_flow_materials() -> list[FlowMaterialOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
    SELECT 
    FM.*,
    A.UBICACION AS ALMACEN,
    M.NOMBRE AS MATERIAL
    FROM 
        FLUJO_MATERIAL FM
    JOIN 
        ALMACEN A ON FM.ALMACEN_ID = A.ID
    JOIN 
        MATERIAL M ON FM.MATERIAL_ID = M.ID;
    ''')
    flow_materials = cursor.fetchall()
    conn.close()

    return [FlowMaterialOut(**flow_material) for flow_material in flow_materials]


def create_flow_material(flow_material_data: FlowMaterialCreate) -> FlowMaterialOut:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO FLUJO_MATERIAL 
           (MATERIAL_ID, ALMACEN_ID, CANTIDAD, MOVIMIENTO, FECHA)
           VALUES (%s, %s, %s, %s, %s)""",
        (
            flow_material_data.MATERIAL_ID, flow_material_data.ALMACEN_ID, flow_material_data.CANTIDAD,
            str(flow_material_data.MOVIMIENTO.value), flow_material_data.FECHA
        )
    )
    conn.commit()
    flow_material_id = cursor.lastrowid  # Obtenemos el ID generado
    conn.close()

    return FlowMaterialOut(ID=flow_material_id,MATERIAL='',ALMACEN='', **flow_material_data.dict())


def update_flow_material(flow_material_id: int, flow_material_data: FlowMaterialCreate) -> FlowMaterialOut:
    conn = get_db_connection()
    cursor = conn.cursor()

    
    cursor.execute(
        """UPDATE FLUJO_MATERIAL SET 
           MATERIAL_ID = %s, ALMACEN_ID = %s, CANTIDAD = %s, MOVIMIENTO = %s, FECHA = %s 
           WHERE ID = %s""",
        (
            flow_material_data.MATERIAL_ID, flow_material_data.ALMACEN_ID, flow_material_data.CANTIDAD,
            str(flow_material_data.MOVIMIENTO.value), flow_material_data.FECHA,
            flow_material_id
        )
    )
    conn.commit()
    conn.close()

    return FlowMaterialOut(ID=flow_material_id, **flow_material_data.dict())


def delete_flow_material(flow_material_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM FLUJO_MATERIAL WHERE ID = %s", (flow_material_id,))
    conn.commit()
    conn.close()

def get_encargado_almacen(almacen_id: int) -> dict:
    """
    Obtiene el correo y nombre del encargado del almacén asociado a un ALMACEN_ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
    SELECT
        U.USER_NAME AS NOMBRE,
        U.EMAIL AS CORREO
    FROM
        USUARIO U
    JOIN
        EMPLEADO E ON U.EMPLEADO_ID = E.ID
    JOIN
        ENCARGADO_ALMACEN EA ON EA.EMPLEADO_ID = E.ID
    JOIN
        ALMACEN A ON EA.ID = A.ENCARGADO_ALMACEN_ID
    WHERE
        A.ID = %s;
    ''', (almacen_id,))
    encargado = cursor.fetchone()
    conn.close()
    if not encargado:
        raise ValueError(f"Encargado del almacén no encontrado para ALMACEN_ID: {almacen_id}.")
    return encargado

from app.schemas.flow_material_schema import FlowMaterialOut
from datetime import date

class FlowMaterialRepository:
    @staticmethod
    def get_flows_by_item_and_date_range(item_id: int, start_date: date, end_date: date):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = """
                SELECT * FROM FLUJO_MATERIAL
                WHERE MATERIAL_ID = %s AND FECHA BETWEEN %s AND %s
            """
            cursor.execute(sql, (item_id, start_date, end_date))
            rows = cursor.fetchall()
            return [FlowMaterialOut(**row) for row in rows] 