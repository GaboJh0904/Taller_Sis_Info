# app/api/purchase_material_details.py
from fastapi import APIRouter, HTTPException
from app.schemas.purchase_material_detail_schema import PurchaseDetailCreate, PurchaseDetailOut
from app.business_logic.purchase_material_detail_bl import PurchaseDetailBL

router = APIRouter()

@router.post("/", response_model=PurchaseDetailOut)
def create_new_purchase_detail(detail_data: PurchaseDetailCreate):
    try:
        return PurchaseDetailBL.create_new_purchase_detail(detail_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{detail_id}", response_model=PurchaseDetailOut)
def get_purchase_detail(detail_id: int):
    try:
        return PurchaseDetailBL.get_purchase_detail(detail_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[PurchaseDetailOut])
def list_all_purchase_details():
    return PurchaseDetailBL.get_all_purchase_details()

@router.put("/{detail_id}", response_model=PurchaseDetailOut)
def update_existing_purchase_detail(detail_id: int, detail_data: PurchaseDetailCreate):
    try:
        return PurchaseDetailBL.update_existing_purchase_detail(detail_id, detail_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{detail_id}")
def delete_existing_purchase_detail(detail_id: int):
    try:
        PurchaseDetailBL.delete_purchase_detail(detail_id)
        return {"detail": "Purchase detail deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/by_purchase/{compra_material_id}", response_model=list[PurchaseDetailOut])
def get_details_by_material_purchase_id(compra_material_id: int):
    try:
        return PurchaseDetailBL.retrieve_details_by_material_purchase_id(compra_material_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))