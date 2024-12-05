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

    # Configuración para el correo
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME", "pruebacorreos0904@gmail.com")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "tbew ydau ugqx caby")
    EMAIL_FROM = os.getenv("EMAIL_FROM", "pruebacorreos@gmail.com")


settings = Settings()
