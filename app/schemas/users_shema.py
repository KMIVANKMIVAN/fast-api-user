from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime

from app.schemas import (
    BaseAuditSchema,
)


class User(BaseAuditSchema):  # Hereda de audit.schema
    email: EmailStr
    name: str = Field(..., min_length=1)
    mobile: str = Field(..., min_length=7)
    password: str = Field(..., min_length=8, max_length=40)
    city: Optional[str] = ""
    country_id: Optional[int] = 0
    street: Optional[str] = ""
    website: Optional[str] = ""

    @field_validator("city", "street", "website", mode="before")
    def none_to_empty_str(cls, v):
        return v or ""


class UserResponse(BaseAuditSchema):
    id: int
    email: EmailStr
    name: str
    mobile: str
    city: Optional[str] = ""
    country_id: Optional[int] = 0
    street: Optional[str] = ""
    website: Optional[str] = ""
