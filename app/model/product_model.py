from typing import Optional
from sqlmodel import SQLModel, Field

from app.model.audit_model import AuditModel


class ProductModel(SQLModel, AuditModel, table=True):
    __tablename__ = "product"

    product_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    description: Optional[str] = None
    characteristics: Optional[str] = None
