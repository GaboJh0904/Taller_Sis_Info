# app/api/material_allocations.py
from fastapi import APIRouter, HTTPException
from app.schemas.material_allocation_schema import MaterialAllocationCreate, MaterialAllocationOut
from app.business_logic.material_allocation_bl import MaterialAllocationBL
from app.schemas.flow_material_schema import FlowMaterialCreate
from app.business_logic.flow_material_bl import FlowMaterialBL

router = APIRouter()

@router.post("/", response_model=MaterialAllocationOut)
def create_new_material_allocation(material_allocation_data: MaterialAllocationCreate, flow_material_data: FlowMaterialCreate):
    try:
        # 1. Crear un nuevo flujo de material primero
        flow_material = FlowMaterialBL.create_new_flow_material(flow_material_data)
        
        # 2. Usar el ID del flujo de material recién creado para la asignación
        material_allocation_data.FLUJO_MATERIAL_ID = flow_material.ID
        
        # 3. Crear la asignación de material
        return MaterialAllocationBL.create_new_material_allocation(material_allocation_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{material_allocation_id}", response_model=MaterialAllocationOut)
def get_material_allocation(material_allocation_id: int):
    try:
        return MaterialAllocationBL.get_material_allocation(material_allocation_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[MaterialAllocationOut])
def list_all_material_allocations():
    return MaterialAllocationBL.get_all_material_allocations()

@router.put("/{material_allocation_id}", response_model=MaterialAllocationOut)
def update_existing_material_allocation(material_allocation_id: int, material_allocation_data: MaterialAllocationCreate):
    try:
        return MaterialAllocationBL.update_existing_material_allocation(material_allocation_id, material_allocation_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{material_allocation_id}")
def delete_existing_material_allocation(material_allocation_id: int):
    try:
        MaterialAllocationBL.delete_material_allocation(material_allocation_id)
        return {"detail": "Allocation material deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
