# app/api/purchases_material.py
from fastapi import APIRouter, HTTPException
from app.schemas.purchase_material_schema import PurchaseMaterialCreate, PurchaseMaterialOut
from app.business_logic.purchase_material_bl import PurchaseMaterialBL

router = APIRouter()

@router.post("/", response_model=PurchaseMaterialOut)
def create_new_purchase_material(purchase_data: PurchaseMaterialCreate):
    try:
        return PurchaseMaterialBL.create_new_purchase_material(purchase_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{purchase_id}", response_model=PurchaseMaterialOut)
def get_purchase_material(purchase_id: int):
    try:
        return PurchaseMaterialBL.get_purchase_material(purchase_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[PurchaseMaterialOut])
def list_all_purchase_materials():
    return PurchaseMaterialBL.get_all_purchase_materials()

@router.put("/{purchase_id}", response_model=PurchaseMaterialOut)
def update_existing_purchase_material(purchase_id: int, purchase_data: PurchaseMaterialCreate):
    try:
        return PurchaseMaterialBL.update_existing_purchase_material(purchase_id, purchase_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{purchase_id}")
def delete_existing_purchase_material(purchase_id: int):
    try:
        PurchaseMaterialBL.delete_purchase_material(purchase_id)
        return {"detail": "Purchase material deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
