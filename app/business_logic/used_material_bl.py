# app/services/used_material_bl.py
from app.repositories.used_material_repository import (
    create_used_material, get_used_material_by_id, get_all_used_materials, update_used_material, delete_used_material, get_used_material_by_material_allocation
)
from app.repositories.material_allocation_repository import get_material_allocation_by_id
from app.repositories.used_material_repository import get_used_materials_by_asignacion_material_id
from app.schemas.used_material_schema import UsedMaterialCreate, UsedMaterialOut

class UsedMaterialBL:

    @staticmethod
    def create_new_used_material(used_material_data: UsedMaterialCreate) -> UsedMaterialOut:
        # 1. Obtener el material asociado al ASIGNACION_MATERIAL_ID
        material = get_material_allocation_by_id(used_material_data.ASIGNACION_MATERIAL_ID)
        if not material:
            raise ValueError("Material not found")
        
        # 2. Obtener todos los materiales usados asociados al ASIGNACION_MATERIAL_ID
        used_materials = get_used_materials_by_asignacion_material_id(used_material_data.ASIGNACION_MATERIAL_ID)

        # 3. Sumar la cantidad de materiales ya usados
        total_used_quantity = sum(used_material.CANTIDAD for used_material in used_materials) if used_materials else 0

        # 4. Verificar si la cantidad sumada más la nueva cantidad excede el total disponible en MATERIAL_ALLOCATION
        if total_used_quantity + used_material_data.CANTIDAD > material.CANTIDAD:
            raise ValueError("Insufficient material quantity for the requested output")

        # 5. Si la validación pasa, proceder a crear el flujo de material en la tabla USO_MATERIAL
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

    @staticmethod
    def get_used_material_by_material_allocation_id(material_allocation_id: int) -> list[UsedMaterialOut]:
        # Obtener las asignaciones de herramientas por proyecto
        allocations = get_used_material_by_material_allocation(material_allocation_id)
        if not allocations:
            raise ValueError("Used material not found")
        return allocations

