from fastapi import APIRouter, HTTPException
from app.repositories.management_repository import (
    assign_role,
    create_team,
    assign_employee_to_team,
    get_all_employees,
    get_employee_details_with_roles,
    get_employees_by_encargado_almacen,
    get_employees_by_encargado_finanzas,
    get_employees_by_encargado_proyecto,
    get_employees_by_gerente_inventario,
)
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Modelos para requests
class RoleAssignmentRequest(BaseModel):
    empleado_id: int
    role_type: str
    assign: Optional[bool] = None


class TeamCreationRequest(BaseModel):
    nombre: str
    estado: str
    ubicacion: str
    proyecto_id: int


class EmployeeTeamAssignmentRequest(BaseModel):
    empleado_id: int


@router.post("/roles")
def create_role(role_request: RoleAssignmentRequest):
    """
    Assign or remove a role from an employee.
    """
    valid_roles = ["encargado_proyecto", "encargado_finanzas", "gerente_inventario", "encargado_almacen"]
    if role_request.role_type not in valid_roles:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid role type. Valid types: {', '.join(valid_roles)}",
        )

    # Call the function and capture the response
    response = assign_role(
        role_request.empleado_id, role_request.role_type, getattr(role_request, "assign", True)
    )

    # Handle failure responses
    if not response["success"]:
        raise HTTPException(status_code=400, detail=response["error"])

    return {"message": response["message"]}


@router.post("/equipos")
def create_new_team(team_request: TeamCreationRequest):
    """
    Create a new team associated with a project.
    """
    try:
        team_id = create_team(
            team_request.nombre,
            team_request.estado,
            team_request.ubicacion,
            team_request.proyecto_id,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Team created successfully", "team_id": team_id}


@router.post("/equipos/{equipo_id}/empleados")
def assign_employee_to_team_route(
    equipo_id: int, team_assignment_request: EmployeeTeamAssignmentRequest
):
    """
    Assign an employee to a team.
    """
    try:
        assign_employee_to_team(team_assignment_request.empleado_id, equipo_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "message": f"Empleado {team_assignment_request.empleado_id} assigned to team {equipo_id}"
    }


@router.get("/empleados")
def get_all_employees_route():
    """
    Get a list of all employees.
    """
    employees = get_all_employees()
    return employees


@router.get("/empleados/{usuario_id}")
def get_employee_details_route(usuario_id: int):
    """
    Get details of an employee, including their roles.
    """
    employee_details = get_employee_details_with_roles(usuario_id)
    if not employee_details:
        raise HTTPException(status_code=404, detail="Empleado not found")

    return employee_details


# Nuevos Endpoints para roles
@router.get("/roles/almacen")
def get_encargados_almacen_route():
    """
    Get all employees with the 'Encargado de Almacén' role.
    """
    try:
        empleados = get_employees_by_encargado_almacen()
        return empleados
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/roles/finanzas")
def get_encargados_finanzas_route():
    """
    Get all employees with the 'Encargado de Finanzas' role.
    """
    try:
        empleados = get_employees_by_encargado_finanzas()
        return empleados
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/roles/proyecto")
def get_encargados_proyecto_route():
    """
    Get all employees with the 'Encargado de Proyecto' role.
    """
    try:
        empleados = get_employees_by_encargado_proyecto()
        return empleados
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/roles/inventario")
def get_gerentes_inventario_route():
    """
    Get all employees with the 'Gerente de Inventario' role.
    """
    try:
        empleados = get_employees_by_gerente_inventario()
        return empleados
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
