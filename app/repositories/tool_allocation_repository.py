from app.db.connection import get_db_connection
from app.schemas.tool_allocation_schema import ToolAllocationOut, ToolAllocationCreate

def get_tool_allocation_by_id(tool_allocation_id: int) -> ToolAllocationOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ASIGNACION_HERRAMIENTA WHERE ID = %s", (tool_allocation_id,))
    tool_allocation = cursor.fetchone()
    conn.close()

    if tool_allocation:
        return ToolAllocationOut(**tool_allocation)
    return None

def get_all_tool_allocations() -> list[ToolAllocationOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ASIGNACION_HERRAMIENTA")
    tool_allocations = cursor.fetchall()
    conn.close()

    return [ToolAllocationOut(**tool_allocation) for tool_allocation in tool_allocations]

def create_tool_allocation(tool_allocation_data: ToolAllocationCreate) -> ToolAllocationOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO ASIGNACION_HERRAMIENTA (CANTIDAD, FLUJO_HERRAMIENTA_ID, PROYECTO_ID, FASE) 
           VALUES (%s, %s, %s, %s)""",
        (tool_allocation_data.CANTIDAD, tool_allocation_data.FLUJO_HERRAMIENTA_ID, tool_allocation_data.PROYECTO_ID, tool_allocation_data.FASE)
    )
    conn.commit()
    tool_allocation_id = cursor.lastrowid
    conn.close()

    return ToolAllocationOut(ID=tool_allocation_id, **tool_allocation_data.dict())

def update_tool_allocation(tool_allocation_id: int, tool_allocation_data: ToolAllocationCreate) -> ToolAllocationOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE ASIGNACION_HERRAMIENTA SET 
           CANTIDAD = %s, FLUJO_HERRAMIENTA_ID = %s, PROYECTO_ID = %s, FASE = %s
           WHERE ID = %s""",
        (tool_allocation_data.CANTIDAD, tool_allocation_data.FLUJO_HERRAMIENTA_ID, tool_allocation_data.PROYECTO_ID, tool_allocation_data.FASE, tool_allocation_id)
    )
    conn.commit()
    conn.close()

    return ToolAllocationOut(ID=tool_allocation_id, **tool_allocation_data.dict())

def delete_tool_allocation(tool_allocation_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ASIGNACION_HERRAMIENTA WHERE ID = %s", (tool_allocation_id,))
    conn.commit()
    conn.close()

def get_tool_allocations_by_project(project_id: int, fase: str = None) -> list[ToolAllocationOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    print(f"Fetching allocations for project ID: {project_id}")

    if not fase:
        cursor.execute("SELECT * FROM ASIGNACION_HERRAMIENTA WHERE PROYECTO_ID = %s", (project_id, ))
    else:
        cursor.execute("SELECT * FROM ASIGNACION_HERRAMIENTA WHERE PROYECTO_ID = %s AND FASE = %s", (project_id, fase))
    allocations = cursor.fetchall()
    print(allocations)
    conn.close()

    return [ToolAllocationOut(**allocation) for allocation in allocations]