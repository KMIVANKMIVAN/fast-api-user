from pydantic import BaseModel, Field
from datetime import datetime  # <-- Corregido aquí

class BaseAuditSchema(BaseModel):
    status: bool = Field(..., description="Estado activo/inactivo")
    userCreate: int = Field(..., description="ID del usuario que creó el registro")
    userUpdate: int = Field(..., description="ID del usuario que actualizó el registro")
    dateCreate: datetime = Field(..., description="Fecha en la que se creó el registro")
    dateUpdate: datetime = Field(..., description="Fecha en la que se actualizó el registro")
