# app/services/flow_material_bl.py
from app.repositories.flow_material_repository import (
    create_flow_material, get_flow_material_by_id, get_all_flow_materials, update_flow_material, delete_flow_material
)
from app.repositories.material_repository import get_material_by_id, update_material_quantity
from app.schemas.flow_material_schema import FlowMaterialCreate, FlowMaterialOut

class FlowMaterialBL:

    @staticmethod
    def create_new_flow_material(flow_material_data: FlowMaterialCreate) -> FlowMaterialOut:
        # 1. Obtener el material asociado al MATERIAL_ID
        material = get_material_by_id(flow_material_data.MATERIAL_ID)
        if not material:
            raise ValueError("Material not found")

        # 2. Actualizar la cantidad de material según el tipo de movimiento
        if flow_material_data.MOVIMIENTO == "entrada":
            new_quantity = material.CANTIDAD + flow_material_data.CANTIDAD
        elif flow_material_data.MOVIMIENTO == "salida":
            if material.CANTIDAD < flow_material_data.CANTIDAD:
                raise ValueError("Insufficient material quantity for the requested output")
            new_quantity = material.CANTIDAD - flow_material_data.CANTIDAD
        else:
            raise ValueError("Invalid movement type")

        # 3. Actualizar la cantidad en la tabla MATERIAL
        update_material_quantity(flow_material_data.MATERIAL_ID, new_quantity)

        # 4. Crear el flujo de material en la tabla FLUJO_MATERIAL
        return create_flow_material(flow_material_data)


    @staticmethod
    def get_flow_material(flow_material_id: int) -> FlowMaterialOut:
        flow_material = get_flow_material_by_id(flow_material_id)
        if not flow_material:
            raise ValueError("Flow material not found")
        return flow_material

    @staticmethod
    def get_all_flow_materials() -> list[FlowMaterialOut]:
        return get_all_flow_materials()

    @staticmethod
    def update_existing_flow_material(flow_material_id: int, flow_material_data: FlowMaterialCreate) -> FlowMaterialOut:
        flow_material = get_flow_material_by_id(flow_material_id)
        if not flow_material:
            raise ValueError("Flow material not found")
        return update_flow_material(flow_material_id, flow_material_data)

    @staticmethod
    def delete_flow_material(flow_material_id: int) -> None:
        flow_material = get_flow_material_by_id(flow_material_id)
        if not flow_material:
            raise ValueError("Flow material not found")
        delete_flow_material(flow_material_id)
