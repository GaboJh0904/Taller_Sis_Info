# app/api/materials.py
from fastapi import APIRouter, HTTPException
from app.schemas.material_schema import MaterialCreate, MaterialOut
from app.business_logic.material_bl import MaterialBL

router = APIRouter()

@router.post("/", response_model=MaterialOut)
def create_new_material(material_data: MaterialCreate):
    try:
        return MaterialBL.create_new_material(material_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{material_id}", response_model=MaterialOut)
def get_material(material_id: int):
    try:
        return MaterialBL.get_material(material_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[MaterialOut])
def list_all_materials():
    return MaterialBL.get_all_materials()

@router.put("/{material_id}", response_model=MaterialOut)
def update_existing_material(material_id: int, material_data: MaterialCreate):
    try:
        return MaterialBL.update_existing_material(material_id, material_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{material_id}")
def delete_existing_material(material_id: int):
    try:
        MaterialBL.delete_material(material_id)
        return {"detail": "Material deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/notifications/low-stock", response_model=list[MaterialOut])
def get_low_stock_notifications():
    return MaterialBL.get_low_stock_notifications()
