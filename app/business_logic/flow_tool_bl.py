# app/services/flow_tool_bl.py
from app.repositories.flow_tool_repository import (
    create_flow_tool, get_flow_tool_by_id, get_all_flow_tools, update_flow_tool, delete_flow_tool
)
from app.schemas.flow_tool_schema import FlowToolCreate, FlowToolOut

class FlowToolBL:

    @staticmethod
    def create_new_flow_tool(flow_tool_data: FlowToolCreate) -> FlowToolOut:
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
