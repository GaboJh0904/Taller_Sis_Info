from fastapi import APIRouter, HTTPException
from app.schemas.store_schema import AlmacenCreate, AlmacenOut
from app.business_logic.store_bl import StoreBL

router = APIRouter()


@router.post("/store/", response_model=AlmacenOut)
def create_store(store_data: AlmacenCreate):
    try:
        return StoreBL.create_new_store(store_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/store/{store_id}", response_model=AlmacenOut)
def get_store(store_id: int):
    try:
        return StoreBL.get_store_by_id(store_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/store/", response_model=list[AlmacenOut])
def list_stores():
    return StoreBL.get_all_stores()


@router.put("/store/{store_id}", response_model=AlmacenOut)
def update_store(store_id: int, store_data: AlmacenCreate):
    try:
        return StoreBL.update_existing_store(store_id, store_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/store/{store_id}")
def delete_store(store_id: int):
    try:
        StoreBL.delete_store(store_id)
        return {"message": "El almacén fue eliminado exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
