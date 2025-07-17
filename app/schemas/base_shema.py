from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime  # <-- Corregido aquí


class BaseFilterShema(BaseModel):
    status: Optional[bool] = Field(None, description="Estado activo/inactivo")
    limit: Optional[int] = Field(
        10, ge=1, le=100, description="Cantidad de resultados por página"
    )
    page: Optional[int] = Field(1, ge=1, description="Número de página")
    userCreate: Optional[int] = Field(
        ..., description="ID del usuario que creó el registro"
    )
    userUpdate: Optional[int] = Field(
        ..., description="ID del usuario que actualizó el registro"
    )
    dateCreate: Optional[datetime] = Field(
        ..., description="Fecha en la que se creó el registro"
    )
    dateUpdate: Optional[datetime] = Field(
        ..., description="Fecha en la que se actualizó el registro"
    )
