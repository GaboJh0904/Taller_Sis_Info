# app/services/purchase_material_bl.py
from app.repositories.purchase_material_repository import (
    create_purchase_material, get_purchase_material_by_id, get_all_purchase_materials,
    update_purchase_material, delete_purchase_material
)
from app.schemas.purchase_material_schema import PurchaseMaterialCreate, PurchaseMaterialOut

class PurchaseMaterialBL:

    @staticmethod
    def create_new_purchase_material(purchase_data: PurchaseMaterialCreate) -> PurchaseMaterialOut:
        return create_purchase_material(purchase_data)

    @staticmethod
    def get_purchase_material(purchase_id: int) -> PurchaseMaterialOut:
        purchase = get_purchase_material_by_id(purchase_id)
        if not purchase:
            raise ValueError("PurchaseMaterial not found")
        return purchase

    @staticmethod
    def get_all_purchase_materials() -> list[PurchaseMaterialOut]:
        return get_all_purchase_materials()

    @staticmethod
    def update_existing_purchase_material(purchase_id: int, purchase_data: PurchaseMaterialCreate) -> PurchaseMaterialOut:
        purchase = get_purchase_material_by_id(purchase_id)
        if not purchase:
            raise ValueError("PurchaseMaterial not found")
        return update_purchase_material(purchase_id, purchase_data)

    @staticmethod
    def delete_purchase_material(purchase_id: int) -> None:
        purchase = get_purchase_material_by_id(purchase_id)
        if not purchase:
            raise ValueError("PurchaseMaterial not found")
        delete_purchase_material(purchase_id)
