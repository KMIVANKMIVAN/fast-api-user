import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        db_url = os.getenv(
            'DATABASE_URL',
            f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        )
        connection = psycopg2.connect(db_url)
        return connection
    except psycopg2.Error as e:
        raise Exception(f"Error al conectar con PostgreSQL: {e}")

