# app/db/connection.py
import mysql.connector
from mysql.connector import pooling
from app.core.config import settings
import aiomysql
from contextlib import asynccontextmanager

# Crear un pool de conexiones
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=settings.POOL_SIZE,
    pool_reset_session=True,
    host=settings.DB_HOST,
    database=settings.DB_NAME,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD
)

def get_db_connection():
    """Obtiene una conexión del pool"""
    return connection_pool.get_connection()





DATABASE_CONFIG = {
    "host": settings.DB_HOST,
    "port": 3306,
    "user": settings.DB_USER,
    "password": settings.DB_PASSWORD,
    "db": settings.DB_NAME
}

@asynccontextmanager
async def get_connection():
    conn = await aiomysql.connect(**DATABASE_CONFIG)
    try:
        yield conn
    finally:
        conn.close()
