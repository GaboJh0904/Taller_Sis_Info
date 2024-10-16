# app/services/flow_tool_bl.py
from app.repositories.flow_tool_repository import (
    create_flow_tool, get_flow_tool_by_id, get_all_flow_tools, update_flow_tool, delete_flow_tool
)
from app.repositories.tool_repository import get_tool_by_id, update_tool_quantity
from app.schemas.flow_tool_schema import FlowToolCreate, FlowToolOut

class FlowToolBL:

    @staticmethod
    def create_new_flow_tool(flow_tool_data: FlowToolCreate) -> FlowToolOut:
        # 1. Obtener la herramienta asociada al HERRAMIENTA_ID
        tool = get_tool_by_id(flow_tool_data.HERRAMIENTA_ID)
        if not tool:
            raise ValueError("Tool not found")

        # 2. Actualizar la cantidad de herramienta según el tipo de movimiento
        if flow_tool_data.MOVIMIENTO == "entrada":
            new_quantity = tool.CANTIDAD + flow_tool_data.CANTIDAD
        elif flow_tool_data.MOVIMIENTO == "salida":
            if tool.CANTIDAD < flow_tool_data.CANTIDAD:
                raise ValueError("Insufficient tool quantity for the requested output")
            new_quantity = tool.CANTIDAD - flow_tool_data.CANTIDAD
        else:
            raise ValueError("Invalid movement type")

        # 3. Actualizar la cantidad en la tabla HERRAMIENTA
        update_tool_quantity(flow_tool_data.HERRAMIENTA_ID, new_quantity)

        # 4. Crear el flujo de herramienta en la tabla FLUJO_HERRAMIENTA
        return create_flow_tool(flow_tool_data)

    @staticmethod
    def get_flow_tool(flow_tool_id: int) -> FlowToolOut:
        flow_tool = get_flow_tool_by_id(flow_tool_id)
        if not flow_tool:
            raise ValueError("Flow tool not found")
        return flow_tool

    @staticmethod
    def get_all_flow_tools() -> list[FlowToolOut]:
        return get_all_flow_tools()

    @staticmethod
    def update_existing_flow_tool(flow_tool_id: int, flow_tool_data: FlowToolCreate) -> FlowToolOut:
        flow_tool = get_flow_tool_by_id(flow_tool_id)
        if not flow_tool:
            raise ValueError("Flow tool not found")
        return update_flow_tool(flow_tool_id, flow_tool_data)

    @staticmethod
    def delete_flow_tool(flow_tool_id: int) -> None:
        flow_tool = get_flow_tool_by_id(flow_tool_id)
        if not flow_tool:
            raise ValueError("Flow tool not found")
        delete_flow_tool(flow_tool_id)
