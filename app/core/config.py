# app/core/config.py

import os

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", 3306)
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "1590PPL")
    DB_NAME = os.getenv("DB_NAME", "planificacion_inventario")

    # Configuration for the connection pool
    POOL_SIZE = int(os.getenv("POOL_SIZE", 10))

settings = Settings()
