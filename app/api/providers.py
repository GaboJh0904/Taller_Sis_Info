# app/api/providers.py
from fastapi import APIRouter, HTTPException
from app.schemas.provider_schema import ProviderCreate, ProviderOut
from app.business_logic.provider_bl import ProviderBL

router = APIRouter()

@router.post("/", response_model=ProviderOut)
def create_provider(provider_data: ProviderCreate):
    try:
        return ProviderBL.create_new_provider(provider_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{provider_id}", response_model=ProviderOut)
def get_provider_by_id(provider_id: int):
    try:
        return ProviderBL.get_provider_by_id(provider_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[ProviderOut])
def list_all_providers():
    return ProviderBL.get_all_providers()

@router.put("/{provider_id}", response_model=ProviderOut)
def update_provider(provider_id: int, provider_data: ProviderCreate):
    try:
        return ProviderBL.update_existing_provider(provider_id, provider_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{provider_id}")
def delete_provider(provider_id: int):
    try:
        ProviderBL.delete_provider_by_id(provider_id)
        return {"detail": "Provider deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
