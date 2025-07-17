from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field

from app.model.audit_model import AuditModel


class SaleModel(SQLModel, AuditModel, table=True):
    __tablename__ = "sales"

    sale_id: Optional[int] = Field(default=None, primary_key=True)
    enterprise_id: int = Field(foreign_key="enterprise.enterprise_id")
    product_id: int = Field(foreign_key="product.product_id")  # Asumo que la tabla es "product"
    sale_date: Optional[date] = None
    quantity: int
