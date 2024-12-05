# app/services/tool_allocation_bl.py
from app.repositories.tool_allocation_repository import (
    create_tool_allocation, get_tool_allocation_by_id, get_all_tool_allocations, update_tool_allocation, delete_tool_allocation
)
from app.repositories.tool_allocation_repository import get_tool_allocations_by_project
from app.repositories.tool_repository import get_tool_by_id
from app.repositories.flow_tool_repository import get_flow_tool_by_id
from app.schemas.tool_allocation_schema import ToolAllocationCreate, ToolAllocationOut
from app.schemas.flow_tool_schema import FlowToolCreate
from app.schemas.tool_allocation_with_details_schema import ToolAllocationWithDetailsOut

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
        
    @staticmethod
    def get_tool_allocations_with_details_by_project(project_id: int, fase: str) -> list[ToolAllocationWithDetailsOut]:
        # Obtener las asignaciones de herramientas por proyecto
        allocations = get_tool_allocations_by_project(project_id, fase)
        # print(allocations)
        results = []

        # Iterar sobre cada asignación y buscar el flujo de herramientas y la herramienta asociado
        for allocation in allocations:
            flow_tool = get_flow_tool_by_id(allocation.FLUJO_HERRAMIENTA_ID)
            if not flow_tool:
                raise ValueError(f"Flow tool not found for ID {allocation.FLUJO_HERRAMIENTA_ID}")

            tool = get_tool_by_id(flow_tool.HERRAMIENTA_ID)
            if not tool:
                raise ValueError(f"Tool not found for ID {flow_tool.HERRAMIENTA_ID}")

            # Combinar los datos en un nuevo objeto ToolAllocationWithDetailsOut
            details = ToolAllocationWithDetailsOut(
                id=allocation.ID,
                nombre_herramienta=tool.NOMBRE,
                descripcion_herramienta=tool.DESCRIPCION,
                cantidad_asignada=allocation.CANTIDAD,
                cantidad_disponible=tool.CANTIDAD,
                fecha_flujo=flow_tool.FECHA
            )
            results.append(details)
        return results

