from mysql.connector import IntegrityError, Error
from app.db.connection import get_db_connection
import traceback

def assign_role(usuario_id: int, role_type: str, assign: bool = True):
    """
    Asigna o desasigna un rol específico a un usuario.
    Si assign es True, asigna el rol. Si es False, desasigna el rol.
    
    Parámetros:
        usuario_id (int): ID del usuario.
        role_type (str): Tipo de rol. Valores válidos: 
                         "encargado_proyecto", "encargado_finanzas", "gerente_inventario", "encargado_almacen".
        assign (bool): True para asignar, False para desasignar. Por defecto es True.
    
    Returns:
        dict: Resultado de la operación, con mensajes de éxito o error.
    """
    valid_roles = {"encargado_proyecto", "encargado_finanzas", "gerente_inventario", "encargado_almacen"}
    mensaje_error = None

    if role_type not in valid_roles:
        return {"success": False, "error": "Tipo de rol no válido."}

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                if assign:
                    if role_type == "encargado_proyecto":
                        cursor.execute(
                            "SELECT 1 FROM ENCARGADO_PROYECTO WHERE USUARIO_ID = %s LIMIT 1",
                            (usuario_id,)
                        )
                        if cursor.fetchone():
                            return {"success": True, "message": "El rol fue actualizado exitosamente."}
                        cursor.execute(
                            "INSERT INTO ENCARGADO_PROYECTO (USUARIO_ID) VALUES (%s)",
                            (usuario_id,)
                        )
                    elif role_type == "encargado_finanzas":
                        cursor.execute(
                            "SELECT 1 FROM ENCARGADO_FINANZAS WHERE USUARIO_ID = %s LIMIT 1",
                            (usuario_id,)
                        )
                        if cursor.fetchone():
                            return {"success": True, "message": "El rol fue actualizado exitosamente."}
                        cursor.execute(
                            "INSERT INTO ENCARGADO_FINANZAS (USUARIO_ID) VALUES (%s)",
                            (usuario_id,)
                        )
                    elif role_type == "gerente_inventario":
                        cursor.execute(
                            "SELECT 1 FROM GERENTE_INVENTARIO WHERE USUARIO_ID = %s LIMIT 1",
                            (usuario_id,)
                        )
                        if cursor.fetchone():
                            return {"success": True, "message": "El rol fue actualizado exitosamente."}
                        cursor.execute(
                            "INSERT INTO GERENTE_INVENTARIO (NOTIFICACIONES_ACTIVAS, USUARIO_ID, NIVEL_ACCESO) VALUES (%s, %s, %s)",
                            (True, usuario_id, '')
                        )
                    elif role_type == "encargado_almacen":
                        cursor.execute(
                            "SELECT 1 FROM ENCARGADO_ALMACEN WHERE USUARIO_ID = %s LIMIT 1",
                            (usuario_id,)
                        )
                        if cursor.fetchone():
                            return {"success": True, "message": "El rol fue actualizado exitosamente."}
                        cursor.execute(
                            "INSERT INTO ENCARGADO_ALMACEN (NOTIFICACIONES_ACTIVAS, NIVEL_ACCESO, USUARIO_ID) VALUES (%s, %s, %s)",
                            (True, "", usuario_id)
                        )
                else:
                    if role_type == "encargado_proyecto":
                        cursor.execute(
                            '''SELECT DISTINCT P.NOMBRE, P.ID FROM PROYECTO P, ENCARGADO_PROYECTO E WHERE P.ENCARGADO_PROYECTO_ID = E.ID 
                                AND E.USUARIO_ID = %s''',
                            (usuario_id,)
                        )
                        proyectos_en_curso = cursor.fetchall()
                        if proyectos_en_curso:
                            mensaje_error = "No se puede eliminar el rol de encargado de proyecto. El empleado está asignado a los siguientes proyectos: " + \
                                            ", ".join([f"{p[0]} (ID: {p[1]})" for p in proyectos_en_curso])
                        else:
                            cursor.execute(
                                "DELETE FROM ENCARGADO_PROYECTO WHERE USUARIO_ID = %s",
                                (usuario_id,)
                            )
                    elif role_type == "encargado_finanzas":
                        cursor.execute(
                            '''SELECT DISTINCT P.NOMBRE, P.ID FROM PROYECTO P, ENCARGADO_FINANZAS E WHERE P.ENCARGADO_FINANZAS_ID = E.ID 
                                AND E.USUARIO_ID = %s''',
                            (usuario_id,)
                        )
                        proyectos_en_curso = cursor.fetchall()
                        if proyectos_en_curso:
                            mensaje_error = "No se puede eliminar el rol de encargado de finanzas. El empleado está asignado a los siguientes proyectos: " + \
                                            ", ".join([f"{p[0]} (ID: {p[1]})" for p in proyectos_en_curso])
                        else:
                            cursor.execute(
                                "DELETE FROM ENCARGADO_FINANZAS WHERE USUARIO_ID = %s",
                                (usuario_id,)
                            )
                    elif role_type == "gerente_inventario":
                        cursor.execute(
                            '''SELECT DISTINCT P.NOMBRE, P.ID FROM PROYECTO P, GERENTE_INVENTARIO E WHERE P.GERENTE_INVENTARIO_ID = E.ID 
                                AND E.USUARIO_ID = %s''',
                            (usuario_id,)
                        )
                        proyectos_en_curso = cursor.fetchall()
                        if proyectos_en_curso:
                            mensaje_error = "No se puede eliminar el rol de gerente de inventario. El empleado está asignado a los siguientes proyectos: " + \
                                            ", ".join([f"{p[0]} (ID: {p[1]})" for p in proyectos_en_curso])
                        else:
                            cursor.execute(
                                "DELETE FROM GERENTE_INVENTARIO WHERE USUARIO_ID = %s",
                                (usuario_id,)
                            )
                    elif role_type == "encargado_almacen":
                        cursor.execute(
                            '''SELECT DISTINCT P.UBICACION, P.ID FROM ALMACEN P, ENCARGADO_ALMACEN E WHERE P.ENCARGADO_ALMACEN_ID = E.ID 
                                AND E.USUARIO_ID = %s''',
                            (usuario_id,)
                        )
                        proyectos_en_curso = cursor.fetchall()
                        if proyectos_en_curso:
                            mensaje_error = "No se puede eliminar el rol de encargado de almacén. El empleado está asignado a los siguientes almacenes: " + \
                                            ", ".join([f"{p[0]} (ID: {p[1]})" for p in proyectos_en_curso])
                        else:
                            cursor.execute(
                                "DELETE FROM ENCARGADO_ALMACEN WHERE USUARIO_ID = %s",
                                (usuario_id,)
                            )
            conn.commit()
    except IntegrityError:
        return {"success": False, "error": "Error de integridad en la base de datos."}
    except Exception as e:
        traceback.print_exc()
        return {"success": False, "error": f"Error inesperado: {str(e)}"}

    if mensaje_error:
        return {"success": False, "error": mensaje_error}

    return {"success": True, "message": "El rol fue actualizado exitosamente."}

def create_team(nombre: str, estado: str, ubicacion: str, proyecto_id: int):
    """
    Crea un nuevo equipo asociado a un proyecto. Si el equipo ya existe, ignora la solicitud.
    
    Parámetros:
        nombre (str): Nombre del equipo.
        estado (str): Estado del equipo.
        ubicacion (str): Ubicación del equipo.
        proyecto_id (int): ID del proyecto asociado.
    
    Returns:
        int: ID del equipo creado o existente.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT IGNORE INTO EQUIPO (NOMRE, FECHA_CREACION, ESTADO, UBICACION, PROYECTO_ID) "
                    "VALUES (%s, NOW(), %s, %s, %s)",
                    (nombre, estado, ubicacion, proyecto_id)
                )
                equipo_id = cursor.lastrowid
                if equipo_id == 0:
                    cursor.execute(
                        "SELECT ID FROM EQUIPO WHERE NOMRE = %s AND PROYECTO_ID = %s",
                        (nombre, proyecto_id)
                    )
                    result = cursor.fetchone()
                    equipo_id = result[0] if result else None
            conn.commit()
        return equipo_id
    except Exception:
        return None  # Ignora errores y retorna None

def assign_employee_to_team(usuario_id: int, equipo_id: int):
    """
    Asigna un usuario a un equipo. Si la asignación ya existe, ignora la solicitud.
    
    Parámetros:
        usuario_id (int): ID del usuario.
        equipo_id (int): ID del equipo.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT IGNORE INTO EMPLEADO_EQUIPO (EQUIPO_ID, USUARIO_ID) VALUES (%s, %s)",
                    (equipo_id, usuario_id)
                )
            conn.commit()
    except Exception:
        pass  # Ignora errores para comportamiento flexible

def get_employee_details_with_roles(usuario_id: int):
    """
    Obtiene los detalles de un usuario junto con sus roles asignados.
    
    Parámetros:
        usuario_id (int): ID del usuario.
    
    Returns:
        dict: Diccionario con los detalles del usuario y sus roles, o None si el usuario no existe.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True, buffered=True) as cursor:
                # Mapea usuario_id a empleado_id
                cursor.execute("SELECT EMPLEADO_ID FROM USUARIO WHERE ID = %s LIMIT 1", (usuario_id,))
                result = cursor.fetchone()
                if not result:
                    return None  # Usuario no existe
                empleado_id = result["EMPLEADO_ID"]

                # Obtiene detalles del empleado
                cursor.execute("SELECT * FROM EMPLEADO WHERE ID = %s LIMIT 1", (empleado_id,))
                empleado = cursor.fetchone()

                if not empleado:
                    return None  # Empleado no existe

                # Obtiene los roles asignados al usuario
                roles = {}
                role_queries = {
                    "encargado_proyecto": "SELECT 1 FROM ENCARGADO_PROYECTO WHERE USUARIO_ID = %s LIMIT 1",
                    "encargado_finanzas": "SELECT 1 FROM ENCARGADO_FINANZAS WHERE USUARIO_ID = %s LIMIT 1",
                    "gerente_inventario": "SELECT 1 FROM GERENTE_INVENTARIO WHERE USUARIO_ID = %s LIMIT 1",
                    "encargado_almacen": "SELECT 1 FROM ENCARGADO_ALMACEN WHERE USUARIO_ID = %s LIMIT 1",
                }

                for role, query in role_queries.items():
                    cursor.execute(query, (usuario_id,))
                    roles[role] = bool(cursor.fetchone())

                return {
                    "empleado": empleado,
                    "roles": roles
                }
    except Exception:
        return None  # Ignora errores y retorna None

def get_all_employees():
    """
    Obtiene una lista de todos los empleados, enmascarando sus IDs con sus IDs de usuario.
    
    Returns:
        list: Lista de diccionarios con los detalles de cada empleado.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                # Obtiene usuarios y sus IDs de empleados asociados
                cursor.execute("SELECT ID AS USUARIO_ID, EMPLEADO_ID FROM USUARIO")
                usuarios = cursor.fetchall()

                employees = []
                for usuario in usuarios:
                    usuario_id = usuario["USUARIO_ID"]
                    empleado_id = usuario["EMPLEADO_ID"]

                    # Obtiene detalles del empleado
                    cursor.execute("SELECT NOMBRE, ROL, TELFONO, FECHA_REGISTRO FROM EMPLEADO WHERE ID = %s", (empleado_id,))
                    empleado = cursor.fetchone()
                    if empleado:
                        empleado["ID"]=usuario_id
                        employees.append({
                            **empleado
                        })
        return employees
    except Exception:
        return []  # Retorna lista vacía en caso de error
    

from app.db.connection import get_db_connection

def get_employees_by_encargado_almacen():
    """
    Obtiene todos los empleados con el rol de Encargado de Almacén.
    Realiza una unión con la tabla USUARIO para fusionar los datos personales.
    """
    query = """
    SELECT 
        ENCARGADO_ALMACEN.ID,
        ENCARGADO_ALMACEN.NIVEL_ACCESO,
        ENCARGADO_ALMACEN.NOTIFICACIONES_ACTIVAS,
        ENCARGADO_ALMACEN.USUARIO_ID,
        USUARIO.USER_NAME,
        USUARIO.EMAIL,
        USUARIO.EMPLEADO_ID
    FROM ENCARGADO_ALMACEN
    JOIN USUARIO ON ENCARGADO_ALMACEN.USUARIO_ID = USUARIO.ID
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        raise RuntimeError(f"Error al obtener encargados de almacén: {e}")


def get_employees_by_encargado_finanzas():
    """
    Obtiene todos los empleados con el rol de Encargado de Finanzas.
    Realiza una unión con la tabla USUARIO para fusionar los datos personales.
    """
    query = """
    SELECT 
        ENCARGADO_FINANZAS.ID,
        ENCARGADO_FINANZAS.USUARIO_ID,
        USUARIO.USER_NAME,
        USUARIO.EMAIL,
        USUARIO.EMPLEADO_ID
    FROM ENCARGADO_FINANZAS
    JOIN USUARIO ON ENCARGADO_FINANZAS.USUARIO_ID = USUARIO.ID
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        raise RuntimeError(f"Error al obtener encargados de finanzas: {e}")


def get_employees_by_encargado_proyecto():
    """
    Obtiene todos los empleados con el rol de Encargado de Proyecto.
    Realiza una unión con la tabla USUARIO para fusionar los datos personales.
    """
    query = """
    SELECT 
        ENCARGADO_PROYECTO.ID,
        ENCARGADO_PROYECTO.USUARIO_ID,
        USUARIO.USER_NAME,
        USUARIO.EMAIL,
        USUARIO.EMPLEADO_ID
    FROM ENCARGADO_PROYECTO
    JOIN USUARIO ON ENCARGADO_PROYECTO.USUARIO_ID = USUARIO.ID
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        raise RuntimeError(f"Error al obtener encargados de proyecto: {e}")


def get_employees_by_gerente_inventario():
    """
    Obtiene todos los empleados con el rol de Gerente de Inventario.
    Realiza una unión con la tabla USUARIO para fusionar los datos personales.
    """
    query = """
    SELECT 
        GERENTE_INVENTARIO.ID,
        GERENTE_INVENTARIO.NIVEL_ACCESO,
        GERENTE_INVENTARIO.ENCARGADO_PEDIDOS,
        GERENTE_INVENTARIO.NOTIFICACIONES_ACTIVAS,
        GERENTE_INVENTARIO.USUARIO_ID,
        USUARIO.USER_NAME,
        USUARIO.EMAIL,
        USUARIO.EMPLEADO_ID
    FROM GERENTE_INVENTARIO
    JOIN USUARIO ON GERENTE_INVENTARIO.USUARIO_ID = USUARIO.ID
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        raise RuntimeError(f"Error al obtener gerentes de inventario: {e}")
