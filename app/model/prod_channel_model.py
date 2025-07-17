from typing import Optional
from sqlmodel import SQLModel, Field

from app.model.audit_model import AuditModel

class ProdChannelModel(SQLModel, table=True):
    __tablename__ = "prod_channel"

    product_id: int = Field(foreign_key="product.product_id", primary_key=True)
    channel_id: int = Field(foreign_key="channels.channel_id", primary_key=True)
