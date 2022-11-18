from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.sql import func

from db import Base


# model/table
class Product(Base):
    __tablename__ = "Product"

    # fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    brand = Column(String(20))
    price = Column(Float)
    quantity = Column(Integer)
    category = Column(String(30))


class Order(Base):
    __tablename__ = "Order"

    # fields
    order_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Product.id"))
    quantity = Column(Integer)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime(timezone=True), default=func.now())
    date_modified = Column(DateTime(timezone=True), default=func.now())
