# app/api/flow_tools.py
from fastapi import APIRouter, HTTPException
from app.schemas.flow_tool_schema import FlowToolCreate, FlowToolOut
from app.business_logic.flow_tool_bl import FlowToolBL

router = APIRouter()

@router.post("/", response_model=FlowToolOut)
def create_new_flow_tool(flow_tool_data: FlowToolCreate):
    try:
        return FlowToolBL.create_new_flow_tool(flow_tool_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{flow_tool_id}", response_model=FlowToolOut)
def get_flow_tool(flow_tool_id: int):
    try:
        return FlowToolBL.get_flow_tool(flow_tool_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[FlowToolOut])
def list_all_flow_tools():
    return FlowToolBL.get_all_flow_tools()

@router.put("/{flow_tool_id}", response_model=FlowToolOut)
def update_existing_flow_tool(flow_tool_id: int, flow_tool_data: FlowToolCreate):
    try:
        return FlowToolBL.update_existing_flow_tool(flow_tool_id, flow_tool_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{flow_tool_id}")
def delete_existing_flow_tool(flow_tool_id: int):
    try:
        FlowToolBL.delete_flow_tool(flow_tool_id)
        return {"detail": "Flow tool deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
