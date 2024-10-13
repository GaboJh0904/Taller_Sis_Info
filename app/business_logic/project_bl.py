# app/services/project_bl.py
from app.repositories.project_repository import (
    create_project, get_project_by_id, get_all_projects, update_project, delete_project
)
from app.schemas.project_schema import ProjectCreate, ProjectOut

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
