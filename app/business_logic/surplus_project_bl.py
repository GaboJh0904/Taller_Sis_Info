# app/services/surplus_project_bl.py
from app.repositories.surplus_project_repository import (
    create_surplus_project, get_surplus_project_by_id, get_all_surplus_projects, update_surplus_project, delete_surplus_project
)
from app.repositories.material_allocation_repository import get_material_allocation_by_id
from app.schemas.surplus_project_schema import SurplusProjectCreate, SurplusProjectOut

class SurplusProjectBL:

    @staticmethod
    def create_new_surplus_project(surplus_project_data: SurplusProjectCreate) -> SurplusProjectOut:
        # 1. Obtener el material asociado al ASIGNACION_MATERIAL_ID
        material = get_material_allocation_by_id(surplus_project_data.ASIGNACION_MATERIAL_ID)
        if not material:
            raise ValueError("Material not found")

        # 2. Actualizar la cantidad de material según el tipo de movimiento
        if material.CANTIDAD < surplus_project_data.CANTIDAD:
            raise ValueError("Insufficient material quantity for the requested output")

        # 3. Crear el flujo de material en la tabla FLUJO_MATERIAL
        return create_surplus_project(surplus_project_data)


    @staticmethod
    def get_surplus_project(surplus_project_id: int) -> SurplusProjectOut:
        surplus_project = get_surplus_project_by_id(surplus_project_id)
        if not surplus_project:
            raise ValueError("Surplus material not found")
        return surplus_project

    @staticmethod
    def get_all_surplus_projects() -> list[SurplusProjectOut]:
        return get_all_surplus_projects()

    @staticmethod
    def update_existing_surplus_project(surplus_project_id: int, surplus_project_data: SurplusProjectCreate) -> SurplusProjectOut:
        surplus_project = get_surplus_project_by_id(surplus_project_id)
        if not surplus_project:
            raise ValueError("Surplus material not found")
        return update_surplus_project(surplus_project_id, surplus_project_data)

    @staticmethod
    def delete_surplus_project(surplus_project_id: int) -> None:
        surplus_project = get_surplus_project_by_id(surplus_project_id)
        if not surplus_project:
            raise ValueError("Surplus material not found")
        delete_surplus_project(surplus_project_id)
