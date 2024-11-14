# app/api/purchase_tool_details.py
from fastapi import APIRouter, HTTPException
from app.schemas.purchase_tool_detail_schema import PurchaseToolDetailCreate, PurchaseToolDetailOut
from app.business_logic.purchase_tool_detail_bl import PurchaseToolDetailBL

router = APIRouter()

@router.post("/", response_model=PurchaseToolDetailOut)
def create_new_purchase_tool_detail(detail_data: PurchaseToolDetailCreate):
    try:
        return PurchaseToolDetailBL.create_new_purchase_tool_detail(detail_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{detail_id}", response_model=PurchaseToolDetailOut)
def get_purchase_tool_detail(detail_id: int):
    try:
        return PurchaseToolDetailBL.get_purchase_tool_detail(detail_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[PurchaseToolDetailOut])
def list_all_purchase_tool_details():
    return PurchaseToolDetailBL.get_all_purchase_tool_details()

@router.put("/{detail_id}", response_model=PurchaseToolDetailOut)
def update_existing_purchase_tool_detail(detail_id: int, detail_data: PurchaseToolDetailCreate):
    try:
        return PurchaseToolDetailBL.update_existing_purchase_tool_detail(detail_id, detail_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{detail_id}")
def delete_existing_purchase_tool_detail(detail_id: int):
    try:
        PurchaseToolDetailBL.delete_purchase_tool_detail(detail_id)
        return {"detail": "Purchase tool detail deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
