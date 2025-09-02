# app/services/material_allocation_bl.py
from app.repositories.material_allocation_repository import (
    create_material_allocation, get_material_allocation_by_id, get_all_material_allocations, update_material_allocation, delete_material_allocation
)
from app.repositories.material_allocation_repository import get_material_allocations_by_project
from app.repositories.material_repository import get_material_by_id
from app.repositories.flow_material_repository import get_flow_material_by_id
from app.schemas.material_allocation_schema import MaterialAllocationCreate, MaterialAllocationOut
from app.schemas.flow_material_schema import FlowMaterialCreate
from app.schemas.material_allocation_with_details_schema import MaterialAllocationWithDetailsOut

class MaterialAllocationBL:

    @staticmethod
    def create_new_material_allocation(material_allocation_data: MaterialAllocationCreate, flow_material_data: FlowMaterialCreate) -> MaterialAllocationOut:
        # 1. Obtener el material asociado al MATERIAL_ID
        material = get_material_by_id(flow_material_data.MATERIAL_ID)
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
        
    @staticmethod
    def get_material_allocations_with_details_by_project(project_id: int, fase: str) -> list[MaterialAllocationWithDetailsOut]:
        # Obtener las asignaciones de material por proyecto
        allocations = get_material_allocations_by_project(project_id, fase)
        
        results = []

        # Iterar sobre cada asignación y buscar el flujo de material y el material asociado
        for allocation in allocations:
            flow_material = get_flow_material_by_id(allocation.FLUJO_MATERIAL_ID)
            if not flow_material:
                raise ValueError(f"Flow material not found for ID {allocation.FLUJO_MATERIAL_ID}")

            material = get_material_by_id(flow_material.MATERIAL_ID)
            if not material:
                raise ValueError(f"Material not found for ID {flow_material.MATERIAL_ID}")

            # Combinar los datos en un nuevo objeto MaterialAllocationWithDetailsOut
            details = MaterialAllocationWithDetailsOut(
                id=allocation.ID,
                nombre_material=material.NOMBRE,
                descripcion_material=material.DESCRIPCION,
                cantidad_asignada=allocation.CANTIDAD,
                cantidad_disponible=material.CANTIDAD,
                fecha_flujo=flow_material.FECHA
            )
            results.append(details)
        return results
