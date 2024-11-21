# app/services/purchase_tool_bl.py
from app.repositories.purchase_tool_repository import (
    create_purchase_tool, get_purchase_tool_by_id, get_all_purchase_tools,
    update_purchase_tool, delete_purchase_tool
)
from app.schemas.purchase_tool_schema import PurchaseToolCreate, PurchaseToolOut

class PurchaseToolBL:

    @staticmethod
    def create_new_purchase_tool(tool_data: PurchaseToolCreate) -> PurchaseToolOut:
        return create_purchase_tool(tool_data)

    @staticmethod
    def get_purchase_tool(purchase_id: int) -> PurchaseToolOut:
        tool = get_purchase_tool_by_id(purchase_id)
        if not tool:
            raise ValueError("PurchaseTool not found")
        return tool

    @staticmethod
    def get_all_purchase_tools() -> list[PurchaseToolOut]:
        return get_all_purchase_tools()

    @staticmethod
    def update_existing_purchase_tool(purchase_id: int, tool_data: PurchaseToolCreate) -> PurchaseToolOut:
        tool = get_purchase_tool_by_id(purchase_id)
        if not tool:
            raise ValueError("PurchaseTool not found")
        return update_purchase_tool(purchase_id, tool_data)

    @staticmethod
    def delete_purchase_tool(purchase_id: int) -> None:
        tool = get_purchase_tool_by_id(purchase_id)
        if not tool:
            raise ValueError("PurchaseTool not found")
        delete_purchase_tool(purchase_id)
