# app/api/users.py
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserOut
from app.business_logic.user_bl import UserBL

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_new_user(user_data: UserCreate):
    try:
        return UserBL.create_new_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    try:
        return UserBL.get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[UserOut])
def list_all_users():
    return UserBL.get_all_users()

@router.put("/{user_id}", response_model=UserOut)
def update_existing_user(user_id: int, user_data: UserCreate):
    try:
        return UserBL.update_existing_user(user_id, user_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{user_id}")
def delete_existing_user(user_id: int):
    try:
        UserBL.delete_user(user_id)
        return {"detail": "User deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
