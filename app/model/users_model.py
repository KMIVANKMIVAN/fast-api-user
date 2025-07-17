from typing import Optional
from sqlmodel import SQLModel, Field

from app.model.audit_model import AuditModel


class UserModel(SQLModel, AuditModel, table=True):
    __tablename__ = "users"

    user_id: Optional[int] = Field(default=None, primary_key=True)
    enterprise_id: int = Field(foreign_key="enterprise.enterprise_id")
    name: str
    email: str
    ci: str
