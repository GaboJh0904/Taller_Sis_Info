# app/repositories/project_repository.py
from app.db.connection import get_db_connection
from app.schemas.project_schema import ProjectOut, ProjectCreate


def get_project_by_id(project_id: int) -> ProjectOut | None:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PROYECTO WHERE ID = %s", (project_id,))
    project = cursor.fetchone()
    conn.close()

    if project:
        return ProjectOut(**project)
    return None


def get_all_projects() -> list[ProjectOut]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PROYECTO")
    projects = cursor.fetchall()
    conn.close()

    return [ProjectOut(**project) for project in projects]


def create_project(project_data: ProjectCreate) -> ProjectOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO PROYECTO 
           (NOMBRE, DESCRIPCION, CRONOGRAMA, PRESUPUESTO_ASIGNADO, METAS_FINANCIERAS, ESTADO, PRIORIDAD, 
           FECHA_INICIO, FECHA_FIN, ENCARGADO_PROYECTO_ID, GERENTE_INVENTARIO_ID, ENCARGADO_FINANZAS_ID)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (
            project_data.NOMBRE, project_data.DESCRIPCION, project_data.CRONOGRAMA,
            project_data.PRESUPUESTO_ASIGNADO, project_data.METAS_FINANCIERAS, project_data.ESTADO,
            project_data.PRIORIDAD, project_data.FECHA_INICIO, project_data.FECHA_FIN,
            project_data.ENCARGADO_PROYECTO_ID, project_data.GERENTE_INVENTARIO_ID,
            project_data.ENCARGADO_FINANZAS_ID
        )
    )
    conn.commit()
    project_id = cursor.lastrowid  # Obtenemos el ID generado
    conn.close()

    return ProjectOut(ID=project_id, **project_data.dict())


def update_project(project_id: int, project_data: ProjectCreate) -> ProjectOut:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE PROYECTO SET 
           NOMBRE = %s, DESCRIPCION = %s, CRONOGRAMA = %s, PRESUPUESTO_ASIGNADO = %s, 
           METAS_FINANCIERAS = %s, ESTADO = %s, PRIORIDAD = %s, FECHA_INICIO = %s, FECHA_FIN = %s, 
           ENCARGADO_PROYECTO_ID = %s, GERENTE_INVENTARIO_ID = %s, ENCARGADO_FINANZAS_ID = %s 
           WHERE ID = %s""",
        (
            project_data.NOMBRE, project_data.DESCRIPCION, project_data.CRONOGRAMA,
            project_data.PRESUPUESTO_ASIGNADO, project_data.METAS_FINANCIERAS, project_data.ESTADO,
            project_data.PRIORIDAD, project_data.FECHA_INICIO, project_data.FECHA_FIN,
            project_data.ENCARGADO_PROYECTO_ID, project_data.GERENTE_INVENTARIO_ID,
            project_data.ENCARGADO_FINANZAS_ID, project_id
        )
    )
    conn.commit()
    conn.close()

    return ProjectOut(ID=project_id, **project_data.dict())


def delete_project(project_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PROYECTO WHERE ID = %s", (project_id,))
    conn.commit()
    conn.close()
