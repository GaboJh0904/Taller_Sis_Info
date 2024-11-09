# app/api/tool_allocations.py
from fastapi import APIRouter, HTTPException
from app.schemas.tool_allocation_schema import ToolAllocationCreate, ToolAllocationOut
from app.business_logic.tool_allocation_bl import ToolAllocationBL
from app.schemas.flow_tool_schema import FlowToolCreate
from app.business_logic.flow_tool_bl import FlowToolBL
from app.schemas.tool_allocation_with_details_schema import ToolAllocationWithDetailsOut

router = APIRouter()

@router.post("/", response_model=ToolAllocationOut)
def create_new_tool_allocation(tool_allocation_data: ToolAllocationCreate, flow_tool_data: FlowToolCreate):
    try:
        # 1. Crear un nuevo flujo de herramienta primero
        flow_tool = FlowToolBL.create_new_flow_tool(flow_tool_data)
        
        # 2. Usar el ID del flujo de herramienta recién creado para la asignación
        tool_allocation_data.FLUJO_HERRAMIENTA_ID = flow_tool.ID
        
        # 3. Crear la asignación de herramienta
        return ToolAllocationBL.create_new_tool_allocation(tool_allocation_data, flow_tool_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{tool_allocation_id}", response_model=ToolAllocationOut)
def get_tool_allocation(tool_allocation_id: int):
    try:
        return ToolAllocationBL.get_tool_allocation(tool_allocation_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[ToolAllocationOut])
def list_all_tool_allocations():
    return ToolAllocationBL.get_all_tool_allocations()

@router.put("/{tool_allocation_id}", response_model=ToolAllocationOut)
def update_existing_tool_allocation(tool_allocation_id: int, tool_allocation_data: ToolAllocationCreate):
    try:
        return ToolAllocationBL.update_existing_tool_allocation(tool_allocation_id, tool_allocation_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{tool_allocation_id}")
def delete_existing_tool_allocation(tool_allocation_id: int):
    try:
        ToolAllocationBL.delete_tool_allocation(tool_allocation_id)
        return {"detail": "Flow tool deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/project/{project_id}/tools/{fase}", response_model=list[ToolAllocationWithDetailsOut])
def get_tool_allocations_with_details_by_project(project_id: int, fase: str):
    try:
        return ToolAllocationBL.get_tool_allocations_with_details_by_project(project_id, fase)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))