# app/services/used_material_bl.py
from app.repositories.used_material_repository import (
    create_used_material, get_used_material_by_id, get_all_used_materials, update_used_material, delete_used_material
)
from app.repositories.material_allocation_repository import get_material_allocation_by_id
from app.schemas.used_material_schema import UsedMaterialCreate, UsedMaterialOut

class UsedMaterialBL:

    @staticmethod
    def create_new_used_material(used_material_data: UsedMaterialCreate) -> UsedMaterialOut:
        # 1. Obtener el material asociado al ASIGNACION_MATERIAL_ID
        material = get_material_allocation_by_id(used_material_data.ASIGNACION_MATERIAL_ID)
        if not material:
            raise ValueError("Material not found")

        # 2. Actualizar la cantidad de material según el tipo de movimiento
        if material.CANTIDAD < used_material_data.CANTIDAD:
            raise ValueError("Insufficient material quantity for the requested output")

        # 3. Crear el flujo de material en la tabla FLUJO_MATERIAL
        return create_used_material(used_material_data)


    @staticmethod
    def get_used_material(used_material_id: int) -> UsedMaterialOut:
        used_material = get_used_material_by_id(used_material_id)
        if not used_material:
            raise ValueError("Used material not found")
        return used_material

    @staticmethod
    def get_all_used_materials() -> list[UsedMaterialOut]:
        return get_all_used_materials()

    @staticmethod
    def update_existing_used_material(used_material_id: int, used_material_data: UsedMaterialCreate) -> UsedMaterialOut:
        used_material = get_used_material_by_id(used_material_id)
        if not used_material:
            raise ValueError("Used material not found")
        return update_used_material(used_material_id, used_material_data)

    @staticmethod
    def delete_used_material(used_material_id: int) -> None:
        used_material = get_used_material_by_id(used_material_id)
        if not used_material:
            raise ValueError("Used material not found")
        delete_used_material(used_material_id)
