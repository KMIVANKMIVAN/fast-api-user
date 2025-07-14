import psycopg2
from app.config import settings  # importa tu instancia de configuración


def get_db_connection():
    try:
        db_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        connection = psycopg2.connect(db_url)
        return connection
    except psycopg2.Error as e:
        raise Exception(f"Error al conectar con PostgreSQL: {e}")
