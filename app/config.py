from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Configuración para Odoo
    ODOO_URL: str
    ODOO_DB: str
    ODOO_USERNAME: str
    ODOO_PASSWORD: str

    # Configuración para PostgreSQL
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    # Variables de encriptación
    EMAIL_FROM: str = Field(..., env="EMAIL_FROM")
    SENDGRID_API_KEY: str = Field(..., env="SENDGRID_API_KEY")
    LOG_LEVEL: str = Field(..., env="LOG_LEVEL")
    REDIS_URL: str = Field(..., env="REDIS_URL")

    model_config = {
        "extra": "ignore",
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }


settings = Settings()
