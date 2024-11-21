# app/api/purchase_tools.py
from fastapi import APIRouter, HTTPException
from app.schemas.purchase_tool_schema import PurchaseToolCreate, PurchaseToolOut
from app.business_logic.purchase_tool_bl import PurchaseToolBL

router = APIRouter()

@router.post("/", response_model=PurchaseToolOut)
def create_new_purchase_tool(tool_data: PurchaseToolCreate):
    try:
        return PurchaseToolBL.create_new_purchase_tool(tool_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{purchase_id}", response_model=PurchaseToolOut)
def get_purchase_tool(purchase_id: int):
    try:
        return PurchaseToolBL.get_purchase_tool(purchase_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[PurchaseToolOut])
def list_all_purchase_tools():
    return PurchaseToolBL.get_all_purchase_tools()

@router.put("/{purchase_id}", response_model=PurchaseToolOut)
def update_existing_purchase_tool(purchase_id: int, tool_data: PurchaseToolCreate):
    try:
        return PurchaseToolBL.update_existing_purchase_tool(purchase_id, tool_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{purchase_id}")
def delete_existing_purchase_tool(purchase_id: int):
    try:
        PurchaseToolBL.delete_purchase_tool(purchase_id)
        return {"detail": "Purchase tool deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
