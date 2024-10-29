# app/services/surplus_bl.py
from app.repositories.surplus_project_repository import (
    create_surplus, get_surplus_by_id, get_all_surpluses, update_surplus, delete_surplus, get_surplus_project_by_material_allocation
)
from app.repositories.material_allocation_repository import get_material_allocation_by_id
from app.repositories.used_material_repository import get_used_materials_by_asignacion_material_id
from app.schemas.surplus_project_schema import SurplusCreate, SurplusOut

class SurplusProjectBL:

    @staticmethod
    def create_new_surplus(surplus_data: SurplusCreate) -> SurplusOut:
        # 1. Obtener el material asociado al ASIGNACION_MATERIAL_ID
        material = get_material_allocation_by_id(surplus_data.ASIGNACION_MATERIAL_ID)
        if not material:
            raise ValueError("Material not found")
        
        # 2. Obtener todos los materiales usados asociados al ASIGNACION_MATERIAL_ID
        used_materials = get_used_materials_by_asignacion_material_id(surplus_data.ASIGNACION_MATERIAL_ID)

        # 3. Sumar la cantidad de materiales ya usados
        total_used_quantity = sum(used_material.CANTIDAD for used_material in used_materials) if used_materials else 0

        # 4. Registramos el sobrante de material en la tabla SOBRANTE_PROYECTO
        surplus_data.CANTIDAD = material.CANTIDAD - total_used_quantity
        
        # 5. Crear el sobrante de material en la tabla SOBRANTE_PROYECTO
        return create_surplus(surplus_data)

    @staticmethod
    def get_surplus(surplus_id: int) -> SurplusOut:
        surplus = get_surplus_by_id(surplus_id)
        if not surplus:
            raise ValueError("Surplus material not found")
        return surplus

    @staticmethod
    def get_all_surpluses() -> list[SurplusOut]:
        return get_all_surpluses()

    @staticmethod
    def update_existing_surplus(surplus_id: int, surplus_data: SurplusCreate) -> SurplusOut:
        surplus = get_surplus_by_id(surplus_id)
        if not surplus:
            raise ValueError("Surplus material not found")
        return update_surplus(surplus_id, surplus_data)

    @staticmethod
    def delete_surplus(surplus_id: int) -> None:
        surplus = get_surplus_by_id(surplus_id)
        if not surplus:
            raise ValueError("Surplus material not found")
        delete_surplus(surplus_id)

    @staticmethod
    def get_surplus_project_by_material_allocation_id(material_allocation_id: int) -> list[SurplusOut]:
        # Obtener las asignaciones de herramientas por proyecto
        allocations = get_surplus_project_by_material_allocation(material_allocation_id)
        if not allocations:
            raise ValueError("Used material not found")
        return allocations