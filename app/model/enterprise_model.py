from typing import Optional
from sqlmodel import SQLModel, Field

from app.model.audit_model import AuditModel


class EnterpriseModel(SQLModel, AuditModel, table=True):
    __tablename__ = "enterprise"

    enterprise_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    nit: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    url_icon: Optional[str] = None
    color: Optional[str] = None
    rep_name: Optional[str] = None
    rep_email: Optional[str] = None
    rep_cellphone: Optional[str] = None
