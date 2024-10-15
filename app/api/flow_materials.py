# app/api/flow_materials.py
from fastapi import APIRouter, HTTPException
from app.schemas.flow_material_schema import FlowMaterialCreate, FlowMaterialOut
from app.business_logic.flow_material_bl import FlowMaterialBL

router = APIRouter()

@router.post("/", response_model=FlowMaterialOut)
def create_new_flow_material(flow_material_data: FlowMaterialCreate):
    try:
        return FlowMaterialBL.create_new_flow_material(flow_material_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{flow_material_id}", response_model=FlowMaterialOut)
def get_flow_material(flow_material_id: int):
    try:
        return FlowMaterialBL.get_flow_material(flow_material_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[FlowMaterialOut])
def list_all_flow_materials():
    return FlowMaterialBL.get_all_flow_materials()

@router.put("/{flow_material_id}", response_model=FlowMaterialOut)
def update_existing_flow_material(flow_material_id: int, flow_material_data: FlowMaterialCreate):
    try:
        return FlowMaterialBL.update_existing_flow_material(flow_material_id, flow_material_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{flow_material_id}")
def delete_existing_flow_material(flow_material_id: int):
    try:
        FlowMaterialBL.delete_flow_material(flow_material_id)
        return {"detail": "Flow material deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
