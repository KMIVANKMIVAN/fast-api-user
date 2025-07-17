from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime
from app.schemas import BaseAuditSchema


class UserSchema(BaseAuditSchema):
    email: EmailStr
    name: str = Field(..., min_length=1)
    mobile: str = Field(..., min_length=7)
    password: str = Field(..., min_length=8, max_length=40)
    city: Optional[str] = ""
    country_id: Optional[int] = 0
    street: Optional[str] = ""
    website: Optional[str] = ""

    @field_validator("city", "street", "website", mode="before")
    @classmethod
    def none_to_empty_str(cls, v):
        return v or ""


class UserResponseSchema(BaseAuditSchema):
    id: int
    email: EmailStr
    name: str
    mobile: str
    city: Optional[str] = ""
    country_id: Optional[int] = 0
    street: Optional[str] = ""
    website: Optional[str] = ""


class UserCreateSchema(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1)
    mobile: str = Field(..., min_length=7)
    password: str = Field(..., min_length=8, max_length=40)
    city: Optional[str] = ""
    country_id: Optional[int] = 0
    street: Optional[str] = ""
    website: Optional[str] = ""

    @field_validator("city", "street", "website", mode="before")
    @classmethod
    def none_to_empty_str(cls, v):
        return v or ""


class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    mobile: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8, max_length=40)
    city: Optional[str] = None
    country_id: Optional[int] = None
    street: Optional[str] = None
    website: Optional[str] = None

    @field_validator("city", "street", "website", mode="before")
    @classmethod
    def none_to_empty_str(cls, v):
        return v or ""
