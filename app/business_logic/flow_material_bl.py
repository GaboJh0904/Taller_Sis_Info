# app/services/flow_material_bl.py
from app.repositories.flow_material_repository import (
    create_flow_material, get_flow_material_by_id, get_all_flow_materials, update_flow_material, delete_flow_material
)
from app.schemas.flow_material_schema import FlowMaterialCreate, FlowMaterialOut

class FlowMaterialBL:

    @staticmethod
    def create_new_flow_material(flow_material_data: FlowMaterialCreate) -> FlowMaterialOut:
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
