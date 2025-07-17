from sqlmodel import Field
from datetime import datetime


class AuditModel:
    status: bool = Field(..., description="Estado activo/inactivo")
    userCreate: int = Field(..., description="ID del usuario que creó el registro")
    userUpdate: int = Field(..., description="ID del usuario que actualizó el registro")
    dateCreate: datetime = Field(..., description="Fecha de creación")
    dateUpdate: datetime = Field(..., description="Fecha de actualización")
