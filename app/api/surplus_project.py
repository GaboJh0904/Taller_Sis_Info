# app/api/surpluss.py
from fastapi import APIRouter, HTTPException
from app.schemas.surplus_project_schema import SurplusCreate, SurplusOut
from app.business_logic.surplus_project_bl import SurplusProjectBL

router = APIRouter()

@router.post("/", response_model=SurplusOut)
def create_new_surplus(surplus_data: SurplusCreate):
    try:
        return SurplusProjectBL.create_new_surplus(surplus_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{surplus_id}", response_model=SurplusOut)
def get_surplus(surplus_id: int):
    try:
        return SurplusProjectBL.get_surplus(surplus_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[SurplusOut])
def list_all_surpluses():
    return SurplusProjectBL.get_all_surpluses()

@router.put("/{surplus_id}", response_model=SurplusOut)
def update_existing_surplus(surplus_id: int, surplus_data: SurplusCreate):
    try:
        return SurplusProjectBL.update_existing_surplus(surplus_id, surplus_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{surplus_id}")
def delete_existing_surplus(surplus_id: int):
    try:
        SurplusProjectBL.delete_surplus(surplus_id)
        return {"detail": "Surplus material deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
