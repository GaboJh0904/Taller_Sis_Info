# app/services/tool_allocation_bl.py
from app.repositories.tool_allocation_repository import (
    create_tool_allocation, get_tool_allocation_by_id, get_all_tool_allocations, update_tool_allocation, delete_tool_allocation
)
from app.repositories.tool_repository import get_tool_by_id
from app.schemas.tool_allocation_schema import ToolAllocationCreate, ToolAllocationOut
from app.schemas.flow_tool_schema import FlowToolCreate

class ToolAllocationBL:

    @staticmethod
    def create_new_tool_allocation(tool_allocation_data: ToolAllocationCreate, flow_tool_data: FlowToolCreate) -> ToolAllocationOut:
        # 1. Obtener la herramienta asociada al HERRAMIENTA_ID
        tool = get_tool_by_id(flow_tool_data.HERRAMIENTA_ID)
        if not tool:
            raise ValueError("Tool not found")

        # 2. Verifica si la cantidad no excede el existente
        if tool.CANTIDAD < tool_allocation_data.CANTIDAD:
            raise ValueError("Insufficient tool quantity for the requested output")

        # 3. Crear el flujo de herramienta en la tabla ASIGNACION_HERRAMIENTA
        return create_tool_allocation(tool_allocation_data)

    @staticmethod
    def get_tool_allocation(tool_allocation_id: int) -> ToolAllocationOut:
        tool_allocation = get_tool_allocation_by_id(tool_allocation_id)
        if not tool_allocation:
            raise ValueError("Allocation tool not found")
        return tool_allocation

    @staticmethod
    def get_all_tool_allocations() -> list[ToolAllocationOut]:
        return get_all_tool_allocations()

    @staticmethod
    def update_existing_tool_allocation(tool_allocation_id: int, tool_allocation_data: ToolAllocationCreate) -> ToolAllocationOut:
        tool_allocation = get_tool_allocation_by_id(tool_allocation_id)
        if not tool_allocation:
            raise ValueError("Allocation tool not found")
        return update_tool_allocation(tool_allocation_id, tool_allocation_data)

    @staticmethod
    def delete_tool_allocation(tool_allocation_id: int) -> None:
        tool_allocation = get_tool_allocation_by_id(tool_allocation_id)
        if not tool_allocation:
            raise ValueError("Allocation tool not found")
        delete_tool_allocation(tool_allocation_id)
