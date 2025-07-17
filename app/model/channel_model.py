from typing import Optional
from sqlmodel import SQLModel, Field

from app.model.audit_model import AuditModel


class ChannelModel(SQLModel, AuditModel, table=True):
    __tablename__ = "channels"

    channel_id: Optional[int] = Field(default=None, primary_key=True)
    category_id: int = Field(foreign_key="categories.category_id")
    name: str
    logo_url: Optional[str] = None
