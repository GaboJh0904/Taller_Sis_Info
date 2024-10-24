# app/api/used_materials.py
from fastapi import APIRouter, HTTPException
from app.schemas.used_material_schema import UsedMaterialCreate, UsedMaterialOut
from app.business_logic.used_material_bl import UsedMaterialBL

router = APIRouter()

@router.post("/", response_model=UsedMaterialOut)
def create_new_used_material(used_material_data: UsedMaterialCreate):
    try:
        return UsedMaterialBL.create_new_used_material(used_material_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{used_material_id}", response_model=UsedMaterialOut)
def get_used_material(used_material_id: int):
    try:
        return UsedMaterialBL.get_used_material(used_material_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[UsedMaterialOut])
def list_all_used_materials():
    return UsedMaterialBL.get_all_used_materials()

@router.put("/{used_material_id}", response_model=UsedMaterialOut)
def update_existing_used_material(used_material_id: int, used_material_data: UsedMaterialCreate):
    try:
        return UsedMaterialBL.update_existing_used_material(used_material_id, used_material_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{used_material_id}")
def delete_existing_used_material(used_material_id: int):
    try:
        UsedMaterialBL.delete_used_material(used_material_id)
        return {"detail": "Used material deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
