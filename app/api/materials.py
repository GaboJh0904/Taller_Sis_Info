from fastapi import APIRouter, HTTPException
from app.schemas.store_schema import AlmacenCreate, AlmacenOut
from app.business_logic.store_bl import StoreBL

router = APIRouter()

@router.post("/", response_model=AlmacenOut)
def create_new_store(store_data: AlmacenCreate): 
    """
    Crea un nuevo almacén.
    """
    try:
        return StoreBL.create_new_store(store_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{store_id}", response_model=AlmacenOut)
def get_store(store_id: int):
    """
    Obtiene un almacén por su ID.
    """
    try:
        return StoreBL.get_store_by_id(store_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[AlmacenOut])
def list_all_stores():
    """
    Obtiene todos los almacenes.
    """
    return StoreBL.get_all_stores()


@router.put("/{store_id}", response_model=AlmacenOut)
def update_existing_store(store_id: int, store_data: AlmacenCreate):
    """
    Actualiza un almacén existente.
    """
    try:
        return StoreBL.update_existing_store(store_id, store_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{store_id}")
def delete_existing_store(store_id: int):
    """
    Elimina un almacén existente.
    """
    try:
        StoreBL.delete_store(store_id)
        return {"detail": "Store deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
