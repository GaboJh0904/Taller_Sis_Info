# app/business_logic/project_bl.py

from app.repositories.project_repository import (
    create_project,
    get_project_by_id,
    get_all_projects,
    update_project,
    delete_project
)
from app.repositories.material_allocation_repository import get_material_allocations_by_project
from app.repositories.tool_allocation_repository import get_tool_allocations_by_project
from app.repositories.used_material_repository import get_used_material_by_material_allocation
from app.schemas.project_schema import ProjectCreate, ProjectOut
from datetime import date

class ProjectBL:

    @staticmethod
    def create_new_project(project_data: ProjectCreate) -> ProjectOut:
        return create_project(project_data)

    @staticmethod
    def get_project(project_id: int) -> ProjectOut:
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        return project

    @staticmethod
    def get_all_projects() -> list[ProjectOut]:
        return get_all_projects()

    @staticmethod
    def update_existing_project(project_id: int, project_data: ProjectCreate) -> ProjectOut:
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        return update_project(project_id, project_data)

    @staticmethod
    def delete_project(project_id: int) -> None:
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        delete_project(project_id)

    @staticmethod
    def get_project_completion_percentage(project_id: int):
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

        start_date = project.FECHA_INICIO
        end_date = project.FECHA_FIN
        current_date = date.today()

        if current_date >= end_date:
            completion_percentage = 100.0
        elif current_date <= start_date:
            completion_percentage = 0.0
        else:
            total_duration = (end_date - start_date).days
            elapsed_duration = (current_date - start_date).days
            completion_percentage = (elapsed_duration / total_duration) * 100

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "completion_percentage": completion_percentage,
            "start_date": start_date,
            "end_date": end_date,
            "current_date": current_date
        }

    @staticmethod
    def get_resource_utilization(project_id: int):
        project = get_project_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")

        # For Materials
        material_allocations = get_material_allocations_by_project(project_id)
        total_allocated_materials = sum(allocation.CANTIDAD for allocation in material_allocations)

        total_used_materials = 0
        for allocation in material_allocations:
            used_materials = get_used_material_by_material_allocation(allocation.ID)
            if used_materials:
                total_used_materials += sum(used_material.CANTIDAD for used_material in used_materials)

        if total_allocated_materials == 0:
            material_utilization_rate = 0.0
        else:
            material_utilization_rate = (total_used_materials / total_allocated_materials) * 100

        # For Tools (assuming full utilization)
        tool_allocations = get_tool_allocations_by_project(project_id)
        total_allocated_tools = sum(allocation.CANTIDAD for allocation in tool_allocations)
        tool_utilization_rate = 100.0 if total_allocated_tools > 0 else 0.0  # Since we lack usage data for tools

        resource_utilization = [
            {"resource_type": "Materials", "utilization_rate": material_utilization_rate},
            {"resource_type": "Tools", "utilization_rate": tool_utilization_rate}
        ]

        return {
            "project_id": project.ID,
            "project_name": project.NOMBRE,
            "resource_utilization": resource_utilization
        }
