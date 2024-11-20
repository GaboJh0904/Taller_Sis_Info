# app/services/purchase_material_detail_bl.py
from app.repositories.purchase_material_detail_repository import (
    create_purchase_detail, get_purchase_detail_by_id, get_all_purchase_details,
    update_purchase_detail, delete_purchase_detail, fetch_purchase_details_by_material_purchase_id
)
from app.schemas.purchase_material_detail_schema import PurchaseDetailCreate, PurchaseDetailOut

class PurchaseDetailBL:

    @staticmethod
    def create_new_purchase_detail(detail_data: PurchaseDetailCreate) -> PurchaseDetailOut:
        return create_purchase_detail(detail_data)

    @staticmethod
    def get_purchase_detail(detail_id: int) -> PurchaseDetailOut:
        detail = get_purchase_detail_by_id(detail_id)
        if not detail:
            raise ValueError("PurchaseDetail not found")
        return detail

    @staticmethod
    def get_all_purchase_details() -> list[PurchaseDetailOut]:
        return get_all_purchase_details()

    @staticmethod
    def update_existing_purchase_detail(detail_id: int, detail_data: PurchaseDetailCreate) -> PurchaseDetailOut:
        detail = get_purchase_detail_by_id(detail_id)
        if not detail:
            raise ValueError("PurchaseDetail not found")
        return update_purchase_detail(detail_id, detail_data)

    @staticmethod
    def delete_purchase_detail(detail_id: int) -> None:
        detail = get_purchase_detail_by_id(detail_id)
        if not detail:
            raise ValueError("PurchaseDetail not found")
        delete_purchase_detail(detail_id)

    @staticmethod
    def retrieve_details_by_material_purchase_id(compra_material_id: int) -> list[PurchaseDetailOut]:
        return fetch_purchase_details_by_material_purchase_id(compra_material_id)

