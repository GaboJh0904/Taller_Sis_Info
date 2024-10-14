# app/services/material_bl.py
from app.repositories.material_repository import (
    create_material, get_material_by_id, get_all_materials, update_material, delete_material
)
from app.schemas.material_schema import MaterialCreate, MaterialOut

class MaterialBL:

    @staticmethod
    def create_new_material(material_data: MaterialCreate) -> MaterialOut:
        return create_material(material_data)

    @staticmethod
    def get_material(material_id: int) -> MaterialOut:
        material = get_material_by_id(material_id)
        if not material:
            raise ValueError("Material not found")
        return material

    @staticmethod
    def get_all_materials() -> list[MaterialOut]:
        return get_all_materials()

    @staticmethod
    def update_existing_material(material_id: int, material_data: MaterialCreate) -> MaterialOut:
        material = get_material_by_id(material_id)
        if not material:
            raise ValueError("Material not found")
        return update_material(material_id, material_data)

    @staticmethod
    def delete_material(material_id: int) -> None:
        material = get_material_by_id(material_id)
        if not material:
            raise ValueError("Material not found")
        delete_material(material_id)
