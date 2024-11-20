# app/services/purchase_tool_detail_bl.py
from app.repositories.purchase_tool_detail_repository import (
    create_purchase_tool_detail, get_purchase_tool_detail_by_id, get_all_purchase_tool_details,
    update_purchase_tool_detail, delete_purchase_tool_detail, fetch_tool_details_by_purchase_id
)
from app.schemas.purchase_tool_detail_schema import PurchaseToolDetailCreate, PurchaseToolDetailOut

class PurchaseToolDetailBL:

    @staticmethod
    def create_new_purchase_tool_detail(detail_data: PurchaseToolDetailCreate) -> PurchaseToolDetailOut:
        return create_purchase_tool_detail(detail_data)

    @staticmethod
    def get_purchase_tool_detail(detail_id: int) -> PurchaseToolDetailOut:
        detail = get_purchase_tool_detail_by_id(detail_id)
        if not detail:
            raise ValueError("PurchaseToolDetail not found")
        return detail

    @staticmethod
    def get_all_purchase_tool_details() -> list[PurchaseToolDetailOut]:
        return get_all_purchase_tool_details()

    @staticmethod
    def update_existing_purchase_tool_detail(detail_id: int, detail_data: PurchaseToolDetailCreate) -> PurchaseToolDetailOut:
        detail = get_purchase_tool_detail_by_id(detail_id)
        if not detail:
            raise ValueError("PurchaseToolDetail not found")
        return update_purchase_tool_detail(detail_id, detail_data)

    @staticmethod
    def delete_purchase_tool_detail(detail_id: int) -> None:
        detail = get_purchase_tool_detail_by_id(detail_id)
        if not detail:
            raise ValueError("PurchaseToolDetail not found")
        delete_purchase_tool_detail(detail_id)

    @staticmethod
    def retrieve_tool_details_by_purchase_id(compra_herramienta_id: int) -> list[PurchaseToolDetailOut]:
        return fetch_tool_details_by_purchase_id(compra_herramienta_id)
