# app/api/tools.py
from fastapi import APIRouter, HTTPException
from app.schemas.tool_schema import ToolCreate, ToolOut
from app.business_logic.tool_bl import ToolBL

router = APIRouter()

@router.post("/", response_model=ToolOut)
def create_new_tool(tool_data: ToolCreate):
    try:
        return ToolBL.create_new_tool(tool_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{tool_id}", response_model=ToolOut)
def get_tool(tool_id: int):
    try:
        return ToolBL.get_tool(tool_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[ToolOut])
def list_all_tools():
    return ToolBL.get_all_tools()

@router.put("/{tool_id}", response_model=ToolOut)
def update_existing_tool(tool_id: int, tool_data: ToolCreate):
    try:
        return ToolBL.update_existing_tool(tool_id, tool_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{tool_id}")
def delete_existing_tool(tool_id: int):
    try:
        ToolBL.delete_tool(tool_id)
        return {"detail": "Tool deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/notifications/low-stock", response_model=list[ToolOut])
def get_low_stock_notifications():
    return ToolBL.get_low_stock_notifications()
