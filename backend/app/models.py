
from sqlalchemy import Column, Integer, String, Float, DateTime, func
from app.database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=func.now())