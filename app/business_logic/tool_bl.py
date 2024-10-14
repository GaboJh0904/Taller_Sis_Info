# app/services/tool_bl.py
from app.repositories.tool_repository import (
    create_tool, get_tool_by_id, get_all_tools, update_tool, delete_tool
)
from app.schemas.tool_schema import ToolCreate, ToolOut

class ToolBL:

    @staticmethod
    def create_new_tool(tool_data: ToolCreate) -> ToolOut:
        return create_tool(tool_data)

    @staticmethod
    def get_tool(tool_id: int) -> ToolOut:
        tool = get_tool_by_id(tool_id)
        if not tool:
            raise ValueError("Tool not found")
        return tool

    @staticmethod
    def get_all_tools() -> list[ToolOut]:
        return get_all_tools()

    @staticmethod
    def update_existing_tool(tool_id: int, tool_data: ToolCreate) -> ToolOut:
        tool = get_tool_by_id(tool_id)
        if not tool:
            raise ValueError("Tool not found")
        return update_tool(tool_id, tool_data)

    @staticmethod
    def delete_tool(tool_id: int) -> None:
        tool = get_tool_by_id(tool_id)
        if not tool:
            raise ValueError("Tool not found")
        delete_tool(tool_id)
