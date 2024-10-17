# app/services/material_allocation_bl.py
from app.repositories.material_allocation_repository import (
    create_material_allocation, get_material_allocation_by_id, get_all_material_allocations, update_material_allocation, delete_material_allocation
)
from app.repositories.material_repository import get_material_by_id
from app.schemas.material_allocation_schema import MaterialAllocationCreate, MaterialAllocationOut

class MaterialAllocationBL:

    @staticmethod
    def create_new_material_allocation(material_allocation_data: MaterialAllocationCreate) -> MaterialAllocationOut:
        # 1. Obtener el material asociado al MATERIAL_ID
        material = get_material_by_id(material_allocation_data.MATERIAL_ID)
        if not material:
            raise ValueError("Material not found")

        # 2. Actualizar la cantidad de material según el tipo de movimiento
        if material.CANTIDAD < material_allocation_data.CANTIDAD:
            raise ValueError("Insufficient material quantity for the requested output")

        # 3. Crear el flujo de material en la tabla FLUJO_MATERIAL
        return create_material_allocation(material_allocation_data)


    @staticmethod
    def get_material_allocation(material_allocation_id: int) -> MaterialAllocationOut:
        material_allocation = get_material_allocation_by_id(material_allocation_id)
        if not material_allocation:
            raise ValueError("Allocation material not found")
        return material_allocation

    @staticmethod
    def get_all_material_allocations() -> list[MaterialAllocationOut]:
        return get_all_material_allocations()

    @staticmethod
    def update_existing_material_allocation(material_allocation_id: int, material_allocation_data: MaterialAllocationCreate) -> MaterialAllocationOut:
        material_allocation = get_material_allocation_by_id(material_allocation_id)
        if not material_allocation:
            raise ValueError("Allocation material not found")
        return update_material_allocation(material_allocation_id, material_allocation_data)

    @staticmethod
    def delete_material_allocation(material_allocation_id: int) -> None:
        material_allocation = get_material_allocation_by_id(material_allocation_id)
        if not material_allocation:
            raise ValueError("Allocation material not found")
        delete_material_allocation(material_allocation_id)
