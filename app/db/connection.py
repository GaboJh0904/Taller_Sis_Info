# app/db/connection.py
import mysql.connector
from mysql.connector import pooling
from app.core.config import settings

# Crear un pool de conexiones con el tamaño configurable
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=settings.POOL_SIZE,  # Ahora el tamaño del pool puede configurarse
    pool_reset_session=True,
    host=settings.DB_HOST,
    database=settings.DB_NAME,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD
)

def get_db_connection():
    """Obtiene una conexión del pool"""
    return connection_pool.get_connection()
