from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field

from app.model.audit_model import AuditModel


class UserPackModel(SQLModel, AuditModel, table=True):
    __tablename__ = "user_pack"

    user_pack_id: Optional[int] = Field(default=None, primary_key=True)
    package_id: int = Field(foreign_key="packages.package_id")
    user_id: int = Field(foreign_key="users.user_id")
    start_date: Optional[date] = None
    end_date: Optional[date] = None
