from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field, Relationship

from app.model.audit_model import AuditModel


class PackageModel(SQLModel, AuditModel, table=True):
    __tablename__ = "packages"

    package_id: Optional[int] = Field(default=None, primary_key=True)
    enterprise_id: int = Field(foreign_key="enterprise.enterprise_id")
    total_credits: int
    used_credits: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None
